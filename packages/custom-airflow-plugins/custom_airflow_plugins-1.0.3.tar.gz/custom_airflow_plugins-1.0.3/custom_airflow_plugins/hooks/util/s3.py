from io import BytesIO

import pandas as pd
import numpy as np
from airflow.hooks.S3_hook import S3Hook


def df_2_s3(
        s3_conn_id: str,
        dataframe: pd.DataFrame,
        bucket: str,
        key: str,
        filetype: str = 'parquet',
        force_str: bool = False):
    dest = S3Hook(s3_conn_id)
    if dataframe.empty:
        # se estiver vazio, entao simplesmente apaga o arquivo existente
        dest.delete_objects(bucket=bucket, keys=key + '.' + filetype)
        return
    dataframe.fillna(value='', inplace=True)
    dataframe = dataframe.replace(r'^\s*$', np.NaN, regex=True)
    # for c in dataframe:
    #     if str(dataframe[c].dtype) in ('object', 'string_', 'unicode_'):
    #         dataframe[c].fillna(value=np.NaN, inplace=True)

    if filetype.lower() == 'json':
        json_str = dataframe.to_json(path_or_buf=None, orient='records', date_format='iso', index=False)
        # Load Into S3
        dest.load_string(
            string_data=json_str,
            key=key + '.json',
            bucket_name=bucket,
            replace=True
        )
    elif filetype.lower() == 'parquet':
        out_buffer = BytesIO()
        dataframe.to_parquet(
            out_buffer,
            compression='snappy',
            engine='pyarrow',
            index=False,
            allow_truncated_timestamps=True,
            use_deprecated_int96_timestamps=True
        )
        out_buffer.seek(0)
        # Load Into S3
        dest.load_bytes(
            bytes_data=out_buffer.read(),
            key=key + '.parquet',
            bucket_name=bucket,
            replace=True
        )


def clear_s3(s3_conn_id: str, bucket: str, key: str):
    dest = S3Hook(s3_conn_id)
    # delete keys
    keys_delete = dest.list_keys(bucket_name=bucket, prefix=key)
    if keys_delete:
        dest.delete_objects(bucket=bucket, keys=keys_delete)
