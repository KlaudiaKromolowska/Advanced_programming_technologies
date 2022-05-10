import os
import pytest
import app

db = app.db
app = app.app

src_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
db_file = os.path.join(src_dir, 'test.db')


@pytest.fixture
def client():
    if os.path.exists(db_file):
        os.remove(db_file)

    with app.test_client() as client:
        db.create_all()
        yield client
