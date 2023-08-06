import boto3
from boto3.s3.transfer import TransferConfig
from .config import Config


def get_s3_client(endpoint_url, aws_access_key, aws_secret_key):
    session = boto3.session.Session(
        aws_access_key_id=aws_access_key,
        aws_secret_access_key=aws_secret_key
    )

    client = session.client(
        service_name='s3',
        endpoint_url=endpoint_url
    )

    return client


class S3Helper:
    def __init__(self, access_key, secret_key, bucket):
        self.access_key = access_key
        self.secret_key = secret_key

        self.s3 = get_s3_client(
            'https://storage.yandexcloud.net',
            aws_access_key=self.access_key,
            aws_secret_key=self.secret_key
        )
        self.bucket = bucket

    def upload_file(self, file_full_path, key_path, file_name=None):
        config = TransferConfig(multipart_threshold=1024 * 25, max_concurrency=10,
                                multipart_chunksize=1024 * 25, use_threads=True)
        s3_file_name = file_full_path.split("/")[-1] if file_name is None else file_name
        key = key_path + "/" + s3_file_name
        self.s3.upload_file(file_full_path, self.bucket, key, ExtraArgs={'ACL': 'public-read'}, Config=config)

    def get_object(self, path):
        get_object_response = self.s3.get_object(Bucket=self.bucket, Key=path)
        return get_object_response['Body'].read()


def upload_file_to_project_s3(source_code_path, s3_access_key, s3_secret_key, project_id_last_part):
    helper = S3Helper(s3_access_key, s3_secret_key, Config.NIRVANA_PROJECTS_BUCKET_NAME)
    helper.upload_file(source_code_path, project_id_last_part)

