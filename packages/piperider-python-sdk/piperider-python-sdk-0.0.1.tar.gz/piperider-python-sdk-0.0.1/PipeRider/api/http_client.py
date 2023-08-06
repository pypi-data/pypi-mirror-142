import os
import requests
from typing import Dict

from PipeRider.api.logger import logger


class Client(object):

    def __init__(self, **kwargs):
        self.api_key = kwargs.get('api_key') or os.environ.get('PIPERIDER_API_KEY')
        if not self.api_key:
            logger.warning('PIPERIDER_API_KEY not found')

        self.base_url = 'https://api.piperider.io/v1'
        logger.info(f'create http-client: {self.base_url}')

    @property
    def headers(self):
        return {'Authorization': f'Bearer {self.api_key}'}

    def get(self, path: str, query_string=None):
        if not query_string:
            url = f'{self.base_url}/{path}'
        else:
            url = f'{self.base_url}/{path}?{query_string}'

        logger.debug(f'url: {url}')
        response = requests.get(url, headers=self.headers)
        content = self.as_json(response)
        logger.debug(f'response: {content}')

        if 'results' in content:
            return content['results']
        return content

    def as_json(self, response):
        status_code = response.status_code
        try:
            return response.json()
        except:
            raise ValueError(dict(status_code=status_code, text=response.text))

    def post_without_response(self, path: str, data: Dict):
        url = f'{self.base_url}/{path}'
        logger.debug(f'url: {url}, payload: {data}')
        response = requests.post(url, headers=self.headers, json=data)
        return response.status_code == 204

    def post(self, path: str, data: Dict):
        url = f'{self.base_url}/{path}'
        logger.debug(f'url: {url}, payload: {data}')
        response = requests.post(url, headers=self.headers, json=data)
        content = self.as_json(response)
        logger.debug(f'response: {content}')
        # TODO handle error
        return content

    def put(self, path: str, data: Dict):
        url = f'{self.base_url}/{path}'
        logger.debug(f'url: {url}, payload: {data}')
        response = requests.put(url, headers=self.headers, json=data)
        return response.status_code == 204

    def delete(self, path: str):
        url = f'{self.base_url}/{path}'
        logger.debug(f'url: {url}')
        response = requests.delete(url, headers=self.headers)
        return response.status_code == 204

    def delete_with_payload(self, path: str, data: dict):
        url = f'{self.base_url}/{path}'
        logger.debug(f'url: {url}')
        response = requests.delete(url, headers=self.headers, json=data)
        return response.status_code == 204


default_client = Client()


def get_default_client():
    global default_client
    return default_client


def set_api_key(api_key: str):
    default_client.api_key = api_key
