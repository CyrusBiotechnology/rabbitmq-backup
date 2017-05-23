import requests

from os import getenv

from requests.auth import HTTPBasicAuth

TRANSPORT = getenv('RABBITMQ_API_URL', 'http://localhost:15672')
USERNAME = getenv('RABBITMQ_API_USER', 'guest')
PASSWORD = getenv('RABBITMQ_API_PASSWORD', 'guest')

while TRANSPORT.endswith('/'):
    TRANSPORT = TRANSPORT[:-1]


def export_definitions(api_url, user, pass_):
    r = requests.get(api_url + '/api/definitions', auth=HTTPBasicAuth(user, pass_))
    assert r.status_code == 200, f'Error when exporting definitions: {r}'
    return r.json()


def import_definitions(api_url, user, pass_, definitions):
    r = requests.post(
        api_url + '/api/definitions',
        json=definitions,
        auth=HTTPBasicAuth(user, pass_)
    )
    assert r.status_code == 201, f'Error when importing definitions: {r}'


if __name__ == '__main__':
    d = export_definitions(TRANSPORT, USERNAME, PASSWORD)
    import_definitions(TRANSPORT, USERNAME, PASSWORD, d)
