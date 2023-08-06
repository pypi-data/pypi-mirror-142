from PipeRider.api.projects import Projects, Project
from PipeRider.api.runs import Run

projects = Projects()


class PipeRiderException(BaseException):
    pass


class RunModel(object):

    def __init__(self, project_api: Project):
        self.project_api = project_api
        self.raw: dict = None
        self.invoke_win: bool = None

        self.run_uid: str = None

    def get_by_uid(self, run_uid: str):
        run = self.project_api.runs.get(run_uid)
        self.run_uid = run.uid
        self.raw = run.raw

    def create(self, name: str, **kwargs):
        self.run_uid = None
        self.raw = {**dict(name=name), **kwargs}
        return self

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.save()

    def reload(self):
        if not self.run_uid:
            return
        self.get_by_uid(self.run_uid)

    def save(self):
        # convert dataset to the right format
        if 'datasets' in self.raw:
            mapped_datasets = []
            datasets = self.raw['datasets']
            for x in self.project_api.datasets.list():
                for d in datasets:
                    if d == x.uid:
                        mapped_datasets.append(d)
                    if d == x.name:
                        mapped_datasets.append(x.uid)

            self.raw['datasets'] = mapped_datasets

        # create the run or update it
        if not self.run_uid:
            self.run_uid = self.project_api.runs.create(self.raw)
        else:
            self.project_api.runs.update(self.run_uid, self.raw)

        if self.invoke_win:
            self.project_api.runs.mark_as_winner(self.run_uid)
            self.invoke_win = None

    def log(self, data: dict):
        self._validate_run()

        if 'logs' not in self.raw:
            self.raw['logs'] = []

        self.raw['logs'].append(data)

    def add_dataset(self, dataset):
        self._validate_run()

        if 'datasets' not in self.raw:
            self.raw['datasets'] = []

        # will replace the dataset to uid later
        self.raw['datasets'].append(dataset)

    @property
    def config(self):
        self._validate_run()
        return self.raw.get('config', {})

    @config.setter
    def config(self, data: dict):
        self._validate_run()
        self.raw['config'] = data

    @property
    def params(self):
        self._validate_run()
        return self.raw.get('params', {})

    @params.setter
    def params(self, data: dict):
        self._validate_run()
        self.raw['params'] = data

    @property
    def metrics(self):
        self._validate_run()
        return self.raw.get('metrics', {})

    @metrics.setter
    def metrics(self, data: dict):
        self._validate_run()
        self.raw['metrics'] = data

    def _validate_run(self):
        if self.raw is None:
            raise ValueError('The run has been closed')

    def win(self):
        # TODO handle a run not created
        self._validate_run()
        self.invoke_win = True


class ProjectModel(object):

    def __init__(self, project_api: Project):
        self.project_api = project_api
        self.current_run = None

    def __repr__(self):
        return self.project_api.__repr__()

    @property
    def name(self):
        return self.project_api.name

    @property
    def uid(self):
        return self.project_api.uid

    @property
    def runs(self):
        if self.current_run is not None:
            return self.current_run

        self.current_run = RunModel(self.project_api)
        return self.current_run

    def comment(self, comment):
        """
        write comment to the project

        :param comment:
        :return:
        """
        self.project_api.events.add('comment', 'add_comment', {}, comment)

    def add_event(self, name: str, event_type: str, metadata: dict, comment: str):
        """
        add custom event to the project

        :param name:
        :param event_type: type name for a custom event
        :param metadata:  data payload for the event
        :param comment: additional comments for the event
        :return:
        """
        self.project_api.events.add(name, event_type, metadata, comment)


def project_by_uid(uid: str):
    """

    Get an existing project by uid

    :param uid: the uid of a project
    :return: a project
    """
    projects_list = projects.list()
    existing = [p for p in projects_list if p.uid == uid]
    if existing:
        return ProjectModel(existing[0])

    raise PipeRiderException(f'Cannot find a project with uid={uid}')


def project(name: str, **kwargs):
    """

    Get an existing project by name

    :param name: name or uid of a project
    :param kwargs:
    :return: a project
    """
    projects_list = projects.list()
    existing = [p for p in projects_list if p.name == name]

    if len(existing) > 1:
        raise PipeRiderException(
            f'Found more than one project named "{name}", please get project with "project_by_uid" function')

    if existing:
        return ProjectModel(existing[0])


def create_project(name: str):
    return ProjectModel(projects.create(name))


def set_api_key(api_key: str):
    from PipeRider.api.http_client import set_api_key as _set_api_key
    _set_api_key(api_key)
