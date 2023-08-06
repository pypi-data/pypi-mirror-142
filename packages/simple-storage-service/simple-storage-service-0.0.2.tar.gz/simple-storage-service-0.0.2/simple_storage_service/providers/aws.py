import io

import boto3
from botocore.exceptions import ClientError

from .base_provider import BaseProvider

from botocore.client import Config


class AWSProvider(BaseProvider):
    REQUIRED_PARAMS = [
        'bucket_name',
        'region_name',
        'aws_access_key_id',
        'aws_secret_access_key',
    ]

    def __init__(self, bucket_name, region_name, aws_access_key_id, aws_secret_access_key):
        self.bucket_name = bucket_name
        self.region_name = region_name
        self.aws_access_key_id = aws_access_key_id
        self.aws_secret_access_key = aws_secret_access_key

    def get_resource_config(self):
        return {
            'region_name': self.region_name,
            'aws_access_key_id': self.aws_access_key_id,
            'aws_secret_access_key': self.aws_secret_access_key,
        }


    def get_object_to_stream(self, key):
        s3 = boto3.resource('s3', **self.get_resource_config())
        bucket = self.bucket_name
        data = io.BytesIO()

        try:
            s3.Bucket(bucket).download_fileobj(key, data)
        except ClientError:
            return None

        data.seek(0)
        return data.read()

    def get_object_to_path(self, key, path):
        s3 = boto3.resource('s3', **self.get_resource_config())
        s3.Bucket(self.bucket_name).download_file(key, path)

    def upload_object_from_path(self, key, path):
        s3 = boto3.resource('s3', **self.get_resource_config())
        body = open(path, 'rb')
        s3.Bucket(self.bucket_name).put_object(Key=key, Body=body)

    def upload_object_from_stream(self, key, stream):
        s3 = boto3.client('s3',**self.get_resource_config())
        with open('filename', 'rb') as stream:
            s3.upload_fileobj(stream, self.bucket_name, key)

    def get_presigned_url(self, key, expiration=3600, method='get_object'):
        s3 = boto3.client(
            's3',
            **self.get_resource_config(),
            config=Config(signature_version='s3v4')
        )
        response = s3.generate_presigned_url(
            method,
            Params={
                'Bucket': self.bucket_name,
                'Key': key
            },
            ExpiresIn=expiration
        )
        return response
