# this module will exclude from release, and it is only used for testing
import configparser
import os

from PipeRider.api.http_client import get_default_client

"""
[tests]
# we execute all tests by the user
runner_user_uid =
runner_user_token =

# we add this user to a project
runner_added_uid =

# s3 datatype
aws_account_id =
s3_url =
"""

SKIP_REASON = 'Give up regression tests, caused by ~/.piperider-tests.ini not found or invalid'


class TestConfig(object):

    def __init__(self):
        # api base url
        self.base_url: str = None

        # the user executes all tests
        self.runner_user_uid: str = None
        self.runner_user_token: str = None

        # the user is added to a project
        self.runner_added_uid: str = None

        self.aws_account_id: int = None
        self.s3_bucket: str = None
        self.s3_region: str = None

    def validate(self):
        how_many_miss_values = len([x for x in self.__dict__.values() if not x])
        # TODO validate aws api could put data to the bucket
        return how_many_miss_values == 0

    def load_by_parser(self, parser: configparser.ConfigParser):
        section = 'tests'
        self.base_url = parser[section].get('base_url')
        if not self.base_url:
            self.base_url = 'https://api.piperider.io/v1'

        self.runner_user_uid = parser[section].get('runner_user_uid')
        self.runner_user_token = parser[section].get('runner_user_token')
        self.runner_added_uid = parser[section].get('runner_added_uid')

        _aws_account_id = parser[section].get('aws_account_id')
        if _aws_account_id:
            try:
                self.aws_account_id = int(_aws_account_id)
            except BaseException:
                pass
        self.s3_bucket = parser[section].get('s3_bucket')
        self.s3_region = parser[section].get('s3_region')


_test_config: TestConfig = None


def piperider_test_config_path():
    cfg_path = os.getenv('PIPERIDER_TEST_CONFIG_PATH')
    if cfg_path and os.path.exists(cfg_path):
        return cfg_path

    cfg_path = os.path.expanduser('~/.piperider-tests.ini')
    if cfg_path and os.path.exists(cfg_path):
        return cfg_path

    return None


def get_piperider_test_settings():
    global _test_config
    return _test_config


def init_piperider_test_settings():
    global _test_config

    # return values
    skip_test = True
    dont_skip_test = not skip_test

    # only load config once
    if _test_config:
        return dont_skip_test

    # section name
    section = 'tests'

    cfg_path = piperider_test_config_path()
    if not cfg_path:
        return skip_test

    parser = configparser.ConfigParser()
    parser.read(cfg_path)

    if not parser.has_section(section):
        print('Cannot find "tests" section in the PIPERIDER_TEST_CONFIG_PATH')
        return skip_test

    config = TestConfig()
    config.load_by_parser(parser)

    if not config.validate():
        print(f'cannot pass validator, caused by missing values {config.__dict__}')
        return skip_test

    _test_config = config
    return dont_skip_test


def reset_api_key_for_test():
    get_default_client().api_key = get_piperider_test_settings().runner_user_token
    get_default_client().base_url = get_piperider_test_settings().base_url


if __name__ == '__main__':
    init_piperider_test_settings()
