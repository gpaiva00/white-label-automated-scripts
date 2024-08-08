import boto3
import os
from config import S3_BUCKET_NAME, LOCAL_TEMP_DIR

s3 = boto3.client('s3')

def download_from_s3(s3_path, local_path):
    s3.download_file(S3_BUCKET_NAME, s3_path, local_path)
    print(f"Downloaded {s3_path} to {local_path}")

def upload_to_s3(local_path, s3_path):
    s3.upload_file(local_path, S3_BUCKET_NAME, s3_path)
    print(f"Uploaded {local_path} to {s3_path}")
