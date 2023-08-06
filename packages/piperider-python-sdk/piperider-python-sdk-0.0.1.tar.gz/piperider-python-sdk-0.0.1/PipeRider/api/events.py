from typing import List


class Relationship(object):

    def __init__(self, data: dict):
        self.raw = data
        self.dataset = []

        if 'dataset' in data:
            for k, v in data['dataset'].items():
                v['uid'] = k
                self.dataset.append(v)


class Event(object):

    def __init__(self, data: dict):
        fields = ['uid', 'user', 'item_name', 'type', 'metadata', 'created_at']
        self.raw = data
        self.uid: str = None
        self.item_name: str = None
        self.type: str = None
        self.metadata: dict = None

        self.user: str = None
        self.created_at: int = None

        for field_name in fields:
            setattr(self, field_name, data.get(field_name))

        if 'relationship' in data and data['relationship']:
            self.relationship = Relationship(data['relationship'])

    def __repr__(self) -> str:
        return f'Event[{self.raw}]'


class Events(object):

    def __init__(self, project):
        self.project = project
        self.uri = f'projects/{self.project.uid}/events'

    def list(self, **kwargs) -> List[Event]:
        params = ['user_uid', 'dataset_uid', 'run_uid']

        query_string_list = []
        for param_name in params:
            if param_name not in kwargs:
                continue
            value = kwargs[param_name]
            if isinstance(value, list):
                query_string_list.append(f'{param_name}={",".join(value)}')
            else:
                query_string_list.append(f'{param_name}={value}')

        qs = "&".join(query_string_list)

        return [Event(x) for x in self.project.client.get(self.uri, qs)]

    def add(self, item_name: str, type: str, metadata: dict, comment: str):
        data = dict(item_name=item_name, type=type, metadata=metadata, comment=comment)
        response = self.project.client.post(self.uri, data)
        if 'uid' in response:
            return response['uid']
