from typing import List


class AwsS3Watcher(object):

    def __init__(self, data: dict):
        fields = ['aws_account_id', 'bucket', 'created_at', 'isConfirmed', 'name', 'region', 'subscription_arn',
                  'topic_arn', 'url']
        self.aws_account_id: int = None
        self.bucket: str = None
        self.created_at: str = None
        self.isConfirmed: bool = None
        self.name: str = None
        self.region: str = None
        self.subscription_arn: str = None
        self.topic_arn: str = None
        self.url: str = None

        for field_name in fields:
            setattr(self, field_name, data.get(field_name))


class Dataset(object):

    def __init__(self, data: dict):
        self.raw = data
        fields = ['uid', 's3_url', 'description', 'filetype', 'name', 'type']
        fields += ['created_at', 'updated_at']
        self.uid: str = None
        self.aws_s3_watcher: AwsS3Watcher = None
        self.s3_url: str = None
        self.description: str = None
        self.filetype: str = None
        self.name: str = None
        self.type: str = None

        self.created_at: int = None
        self.updated_at: int = None

        for field_name in fields:
            setattr(self, field_name, data.get(field_name))

        if data.get('aws_s3_watcher') is not None:
            self.aws_s3_watcher = AwsS3Watcher(data.get('aws_s3_watcher'))

    def __repr__(self) -> str:
        return f'Dataset[uid: {self.uid}, name: {self.name}, created_at: {self.created_at}]'


class Datasets(object):

    def __init__(self, project):
        self.project = project
        self.uri = f'projects/{self.project.uid}/datasets'

    def list(self) -> List[Dataset]:
        return [Dataset(x) for x in self.project.client.get(self.uri)]

    def create(self, data: dict) -> str:
        response = self.project.client.post(self.uri, data)
        if 'uid' in response:
            return response['uid']

    def get(self, dataset_uid: str) -> Dataset:
        return Dataset(self.project.client.get(f'{self.uri}/{dataset_uid}'))

    def delete(self, dataset_uid: str) -> bool:
        return self.project.client.delete(f'{self.uri}/{dataset_uid}')

    def delete_s3_watcher(self, dataset_uid: str) -> bool:
        return self.project.client.delete(f'{self.uri}/{dataset_uid}/s3')

    def create_s3_watcher(self, dataset_uid: str, aws_account_id: int, s3_region: str, s3_url: str) -> bool:
        data = dict(aws_account_id=aws_account_id, s3_bucket_region=s3_region, s3_url=s3_url)
        response = self.project.client.post(f'{self.uri}/{dataset_uid}/s3', data)
        return response
