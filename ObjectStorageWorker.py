import os

from requests import get, put, post


class ObjectStorageWorker:
    STORAGE_URL = "https://storage.yandexcloud.net/"

    def __init__(self, bucket_id):
        self.bucket_id = bucket_id

    def get_object_text(self, object_key):
        response = get(self.STORAGE_URL + self.bucket_id + '/' + object_key)
        if response.status_code != 200:
            raise Exception
        return response.text

    def load_object_text(self, object_key, text):
        response = put(self.STORAGE_URL + self.bucket_id + '/' + object_key, text)
        if response.status_code != 200:
            raise Exception


if __name__ == '__main__':
    ObjectStorageWorker(os.environ.get("OBJECT_STORAGE_BUCKET")).load_object_text("1", "lol")
