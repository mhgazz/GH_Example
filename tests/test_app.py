def test_hello_world():
    from app import app
    with app.test_client() as c:
        rv = c.get('/')
        assert rv.data == b'Hello, World!'
