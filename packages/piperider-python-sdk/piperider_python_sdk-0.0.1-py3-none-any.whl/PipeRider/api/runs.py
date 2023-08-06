from typing import List, Dict


class Run(object):

    def __init__(self, data: dict):
        self.raw = data
        fields = ['uid', 'name', 'config', 'params', 'metrics', 'user', 'created_at', 'logs']
        self.uid: str = None
        self.name: str = None
        self.config: dict = None
        self.params: dict = None
        self.metrics: dict = None
        self.logs: List[Dict] = None

        self.user: str = None
        self.created_at: int = None

        for field_name in fields:
            setattr(self, field_name, data.get(field_name))

    def __repr__(self) -> str:
        return f'Run[uid: {self.uid}, name: {self.name}, created_at: {self.created_at}]'


class Runs(object):

    def __init__(self, project):
        self.project = project
        self.uri = f'projects/{self.project.uid}/runs'

    def list(self) -> List[Run]:
        return [Run(x) for x in self.project.client.get(self.uri)]

    def create(self, run_data: dict):
        response = self.project.client.post(self.uri, run_data)
        if 'uid' in response:
            return response['uid']

    def get(self, run_uid: str):
        return Run(self.project.client.get(f'{self.uri}/{run_uid}'))

    def delete(self, run_uid: str):
        return self.project.client.delete(f'{self.uri}/{run_uid}')

    def update(self, run_uid: str, run_data: dict):
        return self.project.client.put(f'{self.uri}/{run_uid}', run_data)

    def mark_as_winner(self, run_uid: str):
        return self.project.client.post_without_response(f'{self.uri}/{run_uid}/win', {})
