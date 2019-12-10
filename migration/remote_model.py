import requests
import urllib.parse

from settings import ENTITY_BASE_URL_MAP


class RemoteModel:

    def __init__(self, request, entity, version):
        self.request = request
        self.entity = entity
        self.version = version
        self.url = f'{ENTITY_BASE_URL_MAP.get(entity)}/api/{version}/{entity}'

    def _headers(self, override_headers=None):
        base_headers = {'content-type': 'application/json'}
        override_headers = override_headers or {}
        return {
            **request.META,
            **base_headers,
            **override_headers,
        }

    def _cookies(self, override_cookies=None):
        override_cookies = override_cookies or {}
        return {
            **self.request.COOKIES,
            **override_cookies,
        }


    def get(self, entity_id):
        return requests.get(
            f'{self.url}/{entity_id}', 
            headers=self._headers(),
            cookies=self._cookies())

    def filter(self, **conditions):
        params = f'?{urllib.parse.urlencode(conditions)}' if conditions else ''
        return requests.get(
            f'{self.url}/{params}',
            headers=self._headers(),
            cookies=self._cookies())

    def delete(self, entity_id):
        return requests.delete(
            f'{self.url}/{entity_id}',
            headers=self._headers(),
            cookies=self._cookies())

    def create(self, entity_id, entity_data):
        return requests.put(
            f'{self.url}/', 
            data=json.dumps(entity_data), 
            headers=self._headers(),
            cookies=self._cookies())

    def update(self, entity_id, entity_data):
        return requests.post(
            f'{self.url}/{entity_id}'
            data=json.dumps(entity_data),
            headers=self._headers(),
            cookies=self._cookies())
