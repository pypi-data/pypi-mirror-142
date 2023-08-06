import boto3
import io

from botocore.exceptions import ClientError
from .base_provider import BaseProvider


class AWSProvider(BaseProvider):
    REQUIRED_PARAMS = [
        'bucket_name',
        'region_name',
        'aws_access_key_id',
        'aws_secret_access_key',
    ]

    def __init__(self, bucket_name):
        self.bucket_name = bucket_name

    def get_object(self, key):
        s3 = boto3.resource('s3')
        bucket = self.bucket_name
        data = io.BytesIO()

        try:
            s3.Bucket(bucket).download_fileobj(key, data)
        except ClientError:
            return None

        data.seek(0)
        return data.read()
