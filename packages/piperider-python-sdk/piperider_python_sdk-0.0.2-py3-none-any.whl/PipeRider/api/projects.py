from PipeRider.api.datasets import Datasets
from PipeRider.api.http_client import Client, get_default_client
from PipeRider.api.runs import Runs
from PipeRider.api.models import Models
from PipeRider.api.events import Events


def get_account_info():
    return get_default_client().get('me')


class Projects(object):

    def __init__(self):
        self.client = get_default_client()

    def list(self):
        project_data = self.client.get('projects')

        def as_project(p):
            project = Project(p['uid'])
            project.name = p['name']
            return project

        return [as_project(x) for x in project_data]

    def create(self, name):
        response = self.client.post('projects', dict(name=name))
        # name of the create-response is project-uid
        if 'uid' in response:
            return Project(response['uid'])

    def delete(self, project):
        if isinstance(project, Project):
            project = project.uid
        return self.client.delete(f'projects/{project}')

    def get(self, project):
        if isinstance(project, Project):
            project = project.uid
        response = self.client.get(f'projects/{project}')
        # name of a get-response is project name
        if 'name' in response:
            p = Project(project)
            p.name = response['name']
            return p

    def update(self, project, name):
        if isinstance(project, Project):
            project = project.uid
        return self.client.put(f'projects/{project}', dict(name=name))


class Project(object):

    def __init__(self, uid: str):
        self.uid = uid
        self.name = None
        self.client: Client = get_default_client()
        self.runs: Runs = Runs(self)
        self.models: Models = Models(self)
        self.events: Events = Events(self)
        self.datasets: Datasets = Datasets(self)

        self.users: ProjectUsers = ProjectUsers(self)
        self._data = None

        self._load()

    def __repr__(self):
        return f'Project[uid: {self.uid}, name: {self.name}]'

    def _load(self):
        self._data = self.client.get(f'/projects/{self.uid}')
        for k, v in self._data.items():
            setattr(self, k, v)

    def __str__(self) -> str:
        return f'Project[uid: {self.uid}, name: {self.name}]'


class ProjectUsers(object):

    def __init__(self, project: Project):
        self.project = project
        self.client = project.client
        self.uri = f'projects/{self.project.uid}/users'

    def list(self):
        response = self.client.get(self.uri)
        return response

    def add(self, user_uid):
        return self.client.post_without_response(self.uri, dict(user_uid=user_uid))

    def delete(self, user_uid):
        return self.client.delete_with_payload(self.uri, dict(user_uid=user_uid))
