print('__file__={0:<35} | __name__={1:<20} | __package__={2:<20}'.format(__file__,__name__,str(__package__)))

import os
import tempfile

import pytest

import hitagi

@pytest.fixture
def client():
    app = hitagi.create_app()
    app.config['TESTING'] = True

    with app.test_client() as client:
        yield client