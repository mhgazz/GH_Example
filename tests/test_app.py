import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def test_hello_world():
    from app import app
    with app.test_client() as c:
        rv = c.get('/')
        assert rv.data == b'Hello, World!'
