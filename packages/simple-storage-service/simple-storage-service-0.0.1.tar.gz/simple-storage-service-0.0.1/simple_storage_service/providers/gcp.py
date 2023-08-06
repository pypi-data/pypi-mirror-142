from google.cloud import storage
from google.api_core.exceptions import NotFound as GCPNotFound

import io

from .base_provider import BaseProvider


class GCPProvider(BaseProvider):
    REQUIRED_PARAMS = ['bucket_name']

    def __init__(self, bucket_name) -> None:
        self.bucket_name = bucket_name

    def get_object(self, key):
        client = storage.Client()
        bucket = client.get_bucket(self.bucket_name)
        blob = storage.Blob(key, bucket)
        data = io.BytesIO()
        try:
            client.download_blob_to_file(blob, data)
        except GCPNotFound:
            return None
        data.seek(0)
        return data.read()
