from tests.common import client

def test_empty_api(client):
    rv = client.get('/api/')
    assert b'hitagi' in rv.data

def test_git(client):
    rv = client.get('/api/')
    assert b'hitagi' in rv.data