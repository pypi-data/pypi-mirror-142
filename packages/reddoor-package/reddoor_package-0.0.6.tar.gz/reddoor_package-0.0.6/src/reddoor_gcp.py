# -*- coding: utf-8 -*-
import os
import arrow
import base64
import calendar
import csv
import pydash as py_
import pymysql
import time
from datetime import date, datetime, timedelta
from decimal import Decimal
from tempfile import NamedTemporaryFile
from google.cloud import storage
from google.cloud import bigquery


class GoogleCloudService:

    def __init__(self, jsonkey, mysql_config):
        self.storage_client = storage.Client.from_service_account_json(jsonkey)
        self.bigquery_client = bigquery.Client.from_service_account_json(jsonkey)
        self.mysql_config = mysql_config

    def _mysql_execute(self, sql):
        conn = pymysql.connect(**self.mysql_config, local_infile=True)
        conn.set_charset('utf8mb4')

        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(sql)
        conn.commit()

        cursor.close()
        conn.close()

    def _bq_to_mysql_schema_converter(self, otype):
        otype = otype.upper()
        if otype == 'INT64':
            return 'INT(11)'
        elif otype == 'NUMERIC':
            return 'DECIMAL(11)'
        elif otype == 'TIMESTAMP' or otype == 'DATETIME':
            return 'DATETIME'
        elif otype == 'DATE':
            return 'DATE'
        elif otype == 'STRING':
            return 'VARCHAR(200)'
        elif otype == 'BYTES':
            return 'BLOB(200)'
        elif otype == 'BOOLEAN':
            return 'TINYINT(11)'

    def mysql_to_csv(self, sql, sql_config, is_delete=False, complate_func=None):
        """mysql匯出csv

        Args:
            sql (str)): sql 語法
            sql_config (str): 連線字串
            is_delete (bool, optional): 做完刪除
            complate_func (function, optional): 刪除前要做的事

        Returns:
            [type]: [description]
        """
        # 建立mysql連線
        conn = pymysql.connect(**sql_config)
        conn.set_charset('utf8')
        cursor = conn.cursor()

        # 建立臨時檔案
        tmp_file_handle = NamedTemporaryFile(delete=is_delete, mode='w')

        try:
            # 查詢
            cursor.execute(sql)

            # 取得表頭欄位名稱並寫入第一行
            header = list(map(lambda schema_tuple: schema_tuple[0], cursor.description))
            csv_writer = csv.writer(tmp_file_handle, delimiter='\t')
            csv_writer.writerow(header)

            # 轉換csv文檔可呈現的格式
            def convert_type(value, schema_type):
                if isinstance(value, (datetime, date)):
                    return calendar.timegm(value.timetuple())
                if isinstance(value, timedelta):
                    return value.total_seconds()
                if isinstance(value, Decimal):
                    return float(value)
                if schema_type == "BYTES":
                    col_val = base64.standard_b64encode(value)
                    col_val = col_val.decode('ascii')
                    return col_val
                return value

            # Mysql欄位轉換為Bigquery欄位
            def field_to_bigquery(field):
                type_map = {
                    pymysql.FIELD_TYPE.BIT: 'INTEGER',
                    pymysql.FIELD_TYPE.DATETIME: 'TIMESTAMP',
                    pymysql.FIELD_TYPE.DATE: 'TIMESTAMP',
                    pymysql.FIELD_TYPE.DECIMAL: 'FLOAT',
                    pymysql.FIELD_TYPE.NEWDECIMAL: 'FLOAT',
                    pymysql.FIELD_TYPE.DOUBLE: 'FLOAT',
                    pymysql.FIELD_TYPE.FLOAT: 'FLOAT',
                    pymysql.FIELD_TYPE.INT24: 'INTEGER',
                    pymysql.FIELD_TYPE.LONG: 'INTEGER',
                    pymysql.FIELD_TYPE.LONGLONG: 'INTEGER',
                    pymysql.FIELD_TYPE.SHORT: 'INTEGER',
                    pymysql.FIELD_TYPE.TIME: 'TIME',
                    pymysql.FIELD_TYPE.TIMESTAMP: 'TIMESTAMP',
                    pymysql.FIELD_TYPE.TINY: 'INTEGER',
                    pymysql.FIELD_TYPE.YEAR: 'INTEGER',
                }
                field_type = type_map.get(field[1], "STRING")
                field_mode = "NULLABLE" if field[6] or field_type == "TIMESTAMP" else "REQUIRED"
                return {
                    'name': field[0],
                    'type': field_type,
                    'mode': field_mode,
                }

            # 取得對應Bigquery的schema
            schema = [field_to_bigquery(field) for field in cursor.description]
            # 取得轉換csv的欄位屬性對照
            col_type_dict = { col['name']: col['type'] for col in schema }

            # 開始遞迴寫入每筆內容
            for row in cursor:
                row = [
                    convert_type(value, col_type_dict.get(name))
                    for name, value in zip(header, row)
                ]
                csv_writer.writerow(row)

            # 要先釋放暫存才會真正寫入
            tmp_file_handle.flush()
            # 回傳資訊
            data = {
                'file': None if is_delete else tmp_file_handle,
                'schema': schema,
                'func_result': None
            }

            if complate_func:
                # 自訂回傳結果
                data['func_result'] = complate_func(tmp_file_handle)

            result = 'ok', data

        except Exception as ex:
            result = 'fail', ex

        finally:
            # 關閉檔案與連線
            tmp_file_handle.close()
            cursor.close()
            conn.close()
            return result

    def local_to_gcs(self, file_name, bucket_name, bucket_file, content_type=None):

        try:
            # 上傳至GCS
            bucket = self.storage_client.get_bucket(bucket_name)
            blob = bucket.blob(blob_name=bucket_file)
            blob.upload_from_filename(filename=file_name, content_type=content_type)
            result = 'ok', None

        except Exception as ex:
            result = 'fail', ex

        finally:
            return result

    def gcs_to_local(self, bucket_name, bucket_file, file_name):

        try:
            # GCS下載至本地
            bucket = self.storage_client.get_bucket(bucket_name)
            blob = bucket.blob(bucket_file)
            blob.download_to_filename(file_name)
            result = 'ok', None

        except Exception as ex:
            result = 'fail', ex

        finally:
            return result

    def bq_to_gcs(self, bucket, dataset_id, table_id, destination_format='CSV', field_delimiter=',', print_header=True):

        try:
            job_config = bigquery.ExtractJobConfig()
            job_config.field_delimiter = field_delimiter
            job_config.destination_format = destination_format
            job_config.print_header = print_header

            dataset_ref = self.bigquery_client.dataset(dataset_id)
            table_ref = dataset_ref.table(table_id)

            # 上傳到level1_table
            extrace_job = self.bigquery_client.extract_table(
                source=table_ref, 
                destination_uris=bucket,
                timeout=1800,
                job_config=job_config
            )  # Make an API request.
            extrace_job.result()  # Waits for the job to complete.
            result = 'ok', None

        except Exception as ex:
            result = 'fail', ex

        finally:
            return result

    def mysql_to_gcs(self, sql, sql_config, bucket_name, bucket_file):

        # 轉換csv完成後, 上傳gcs
        def complate_func(file):
            return self.local_to_gcs(file.name, bucket_name, bucket_file, 'text/csv')

        result = self.mysql_to_csv(sql, sql_config, is_delete=True, complate_func=complate_func)

        if result[0] == 'ok' and result[1]['func_result'][0] == 'ok':
            return 'ok', result[1]
        elif result[0] == 'ok':
            return 'fail', '上傳GCS發生錯誤'
        else:
            return 'fail', 'MYSQL轉CSV發生錯誤'

    def gcs_to_bq(self, bucket, source_objects, destination_project_dataset_table, 
        schema_fields=None, source_format='CSV', create_disposition='CREATE_IF_NEEDED', 
        skip_leading_rows=0, write_disposition='WRITE_EMPTY', field_delimiter='\t', 
        allow_quoted_newlines=False, allow_jagged_rows=False, time_partitioning=None):

        job_config = bigquery.LoadJobConfig()
        job_config.schema = schema_fields
        job_config.source_format = source_format
        job_config.create_disposition = create_disposition
        job_config.skip_leading_rows = skip_leading_rows
        job_config.write_disposition = write_disposition
        job_config.field_delimiter = field_delimiter
        job_config.allow_quoted_newlines = allow_quoted_newlines
        job_config.allow_jagged_rows = allow_jagged_rows
        job_config.time_partitioning = time_partitioning

        # 上傳到level1_table
        load_job = self.bigquery_client.load_table_from_uri(
            f'gs://{bucket}/{source_objects}', destination_project_dataset_table, job_config=job_config
        )  # Make an API request.
        load_job.result()  # Waits for the job to complete.

        destination_table = self.bigquery_client.get_table(destination_project_dataset_table)  # Make an API request.
        print("Loaded {} rows.".format(destination_table.num_rows))

    def bq_to_mysql(self, sql, bucket_name, bucket_file, mysql_table, field_delimiter='\t'):
        try:
            job_config = bigquery.QueryJobConfig()
            job_config.use_legacy_sql = False
            bq_result = self.bigquery_client.query(sql, job_config=job_config)
            bq_result.result()

            # 等待bq查詢完畢
            while bq_result.done() is False or bq_result._properties['status']['state'] != 'DONE':
                time.sleep(1)

            # get bq table schema
            bq_schema = [{i['name']: i['type']} for i in bq_result._query_results._properties['schema']['fields']]
            mysql_schema = []
            mysql_load_set_str = []
            mysql_load_key_str = []

            for dic in bq_schema:
                mysql_schema.append(''.join([f'{k} {self._bq_to_mysql_schema_converter(v)}' for k, v in dic.items()]))
                mysql_load_set_str.append(''.join([f"{k} = NULLIF(@v{k}, '')" for k, v in dic.items()]))
                mysql_load_key_str.append(''.join([f"@v{k}" for k, v in dic.items()]))


            # create mysql table
            self._mysql_execute(f'DROP TABLE IF EXISTS {mysql_table};')

            mysql_schema_str = ", \n".join(mysql_schema)
            mysql_load_set = ', \n'.join(mysql_load_set_str)
            mysql_load_key = ', '.join(mysql_load_key_str)

            self._mysql_execute(f'''
                CREATE TABLE {mysql_table} (
                    {mysql_schema_str}
                );
            ''')

            # bq to gcs
            dataset_id = py_.get(bq_result._properties, 'configuration.query.destinationTable.datasetId')
            table_id = py_.get(bq_result._properties, 'configuration.query.destinationTable.tableId')
            file_name = f'{table_id[:6]}_{arrow.now("Asia/Taipei").timestamp}.csv'
            file_url = f'{bucket_file}/{file_name}'
            self.bq_to_gcs(f'gs://{bucket_name}/{file_url}', dataset_id, table_id, field_delimiter=field_delimiter)

            # gcs to local
            self.gcs_to_local(bucket_name, file_url, f'{os.path.abspath(".")}/{file_name}')

            # local to mysql
            self._mysql_execute(f"""
                LOAD DATA LOCAL INFILE '{os.path.abspath(".")}/{file_name}' REPLACE INTO TABLE {mysql_table} 
                FIELDS TERMINATED BY {field_delimiter} ESCAPED BY '\\' IGNORE 1 LINES 
                ({mysql_load_key})
                SET
                    {mysql_load_set}
            """)

            return 'ok', None

        except Exception as ex:
            print(ex)
            return 'fail', ex

        finally:
            if os.path.isfile(f'{os.path.abspath(".")}/{file_name}'):
                os.remove(f'{os.path.abspath(".")}/{file_name}')
