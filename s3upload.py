import boto3
from dotenv import load_dotenv
load_dotenv()
import os

s3 = boto3.client('s3', aws_access_key_id=os.getenv('access_key'), aws_secret_access_key=os.getenv('secret_key'))

for file in ['products.csv', 'customers.csv', 'sales.csv']:
    subfolder = file.split('.')[0]
    s3_key = f"raw/{subfolder}/{file}"
    s3.upload_file(file, 'practice-buck11', s3_key)
    print(f"Uploaded {file} to S3 at {s3_key}")

    