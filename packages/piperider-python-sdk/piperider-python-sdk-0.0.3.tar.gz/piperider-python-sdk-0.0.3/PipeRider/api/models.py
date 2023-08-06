from typing import List


class Model(object):

    def __init__(self, data: dict):
        self.raw = data
        fields = ['uid', 'name', 'config', 'params', 'metrics', 'user', 'created_at', 'marked_at', 'marked_by']
        self.uid: str = None
        self.name: str = None
        self.config: dict = None
        self.params: dict = None
        self.metrics: dict = None

        self.user: str = None
        self.marked_by: str = None
        self.created_at: int = None
        self.marked_at: int = None

        for field_name in fields:
            setattr(self, field_name, data.get(field_name))

    def __repr__(self) -> str:
        return f'Model[uid: {self.uid}, name: {self.name}, marked_at: {self.marked_at}, marked_by: {self.marked_by}]'


class Models(object):

    def __init__(self, project):
        self.project = project
        self.uri = f'projects/{self.project.uid}/models'

    def list(self) -> List[Model]:
        return [Model(x) for x in self.project.client.get(self.uri)]

    def get(self, model_uid: str):
        return Model(self.project.client.get(f'{self.uri}/{model_uid}'))

    def delete(self, model_uid: str):
        return self.project.client.delete(f'{self.uri}/{model_uid}')
