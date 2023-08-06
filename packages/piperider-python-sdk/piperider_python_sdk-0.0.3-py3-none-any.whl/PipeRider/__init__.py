from PipeRider.api.projects import Projects, Project
from PipeRider.api.runs import Run

projects = Projects()


class PipeRiderException(BaseException):
    pass


class RunModel(object):

    def __init__(self, project_api: Project):
        self.project_api = project_api
        self.current_run_uid: str = None
        self.current_run: Run = None

    def create(self, name: str, **kwargs):
        self.current_run_uid = self.project_api.runs.create({**dict(name=name), **kwargs})
        self.current_run = self.project_api.runs.get(self.current_run_uid)
        return self

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def close(self):
        self.current_run = None
        self.current_run_uid = None

    def log(self, data: dict):
        self._validate_run()

        if 'logs' not in self.current_run.raw:
            self.current_run.raw['logs'] = []

        self.current_run.raw['logs'].append(data)
        self.project_api.runs.update(self.current_run_uid, self.current_run.raw)

    def add_dataset(self, dataset):
        self._validate_run()

        selected = [x for x in self.project_api.datasets.list() if x.uid == dataset or x.name == dataset]
        # TODO raise error when more than one selected
        if not selected:
            raise ValueError(f'cannot find a dataset [{dataset}]')

        d = selected[0]
        if 'datasets' not in self.current_run.raw:
            self.current_run.raw['datasets'] = []

        if d.uid not in self.current_run.raw['datasets']:
            self.current_run.raw['datasets'].append(d.uid)

    @property
    def params(self):
        self._validate_run()
        return self.current_run.get('params', {})

    @params.setter
    def params(self, data: dict):
        self._validate_run()
        self.current_run.raw['params'] = data
        self.project_api.runs.update(self.current_run_uid, self.current_run.raw)

    @property
    def metrics(self):
        self._validate_run()
        return self.current_run.get('metrics', {})

    @metrics.setter
    def metrics(self, data: dict):
        self._validate_run()
        self.current_run.raw['metrics'] = data
        self.project_api.runs.update(self.current_run_uid, self.current_run.raw)

    def _validate_run(self):
        if self.current_run_uid is None or self.current_run is None:
            raise ValueError('The run has been closed')

    def win(self):
        self._validate_run()
        self.project_api.runs.mark_as_winner(self.current_run_uid)


class ProjectModel(object):

    def __init__(self, project_api: Project):
        self.project_api = project_api
        self.current_run = None

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
