from PipeRider.api.http_client import get_default_client


class Users(object):

    def __init__(self):
        self.client = get_default_client()

    def me(self):
        data = self.client.get('me')
        return UserData(data['uid'], data['info'])

    def update(self, info: dict):
        return self.client.put('me', info)

    def create_token(self, key_name):
        response = self.client.post('my/token', dict(key_name=key_name))
        if 'key' in response:
            return TokenData(key_name, response['key'])

    def delete_token(self, key):
        return self.client.delete_with_payload('my/token', dict(key=key))

    def list_token(self):
        return [TokenData(x['key_name'], x['uid']) for x in self.client.get('my/token')]


class UserData(object):

    def __init__(self, uid, info):
        self.uid = uid
        self.info = info


class TokenData(object):

    def __init__(self, key_name, key):
        self.key_name = key_name
        self.key = key
