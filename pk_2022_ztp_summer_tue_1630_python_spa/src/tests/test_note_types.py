import uuid

from tests import constants
from tests import urls
from .fixtures import client


class TestNoteType:

    def add_note_type(self, client, _id, name):
        data = {'name': name}
        client.post(urls.ADD_NOTE_TYPE_URL, json=data)
        data['id'] = _id
        return data

    def test_get_note_types(self, client):
        print("TEST: '{}' path".format(urls.GET_NOTE_TYPES_URL))

        name_1 = 'name_1{}'.format(uuid.uuid4())
        name_2 = 'name_2{}'.format(uuid.uuid4())
        data_1 = self.add_note_type(client, 1, name_1)
        data_2 = self.add_note_type(client, 2, name_2)

        rv = client.get(urls.GET_NOTE_TYPES_URL)
        assert rv.status_code == 200, constants.MSG_HTTP_CODE

        expected = [data_1, data_2]
        assert rv.get_json() == [data_1, data_2], constants.MSG_DATA.format(expected)

    def test_add_note_type(self, client):
        print("TEST: '{}' path".format(urls.ADD_NOTE_TYPE_URL))

        expected_name = 'name_{}'.format(uuid.uuid4())
        data = {'name': expected_name}
        rv = client.post(urls.ADD_NOTE_TYPE_URL, json=data)

        assert rv.status_code == 200, constants.MSG_HTTP_CODE
        assert 'success' in rv.get_json(), constants.MSG_EXPECTED_KEY.format('success')

        rv = client.get(urls.GET_NOTE_TYPES_URL)
        result = rv.get_json()
        assert len(result) == 1, constants.MSG_SINGLE_RECORD
        item = result[0]
        assert item['name'] == expected_name, constants.MSG_NOTE_TYPE_RECORD

    def test_remove_note_type(self, client):
        print("TEST: '{}' path".format(urls.REMOVE_NOTE_TYPE_URL))

        name = 'name_{}'.format(uuid.uuid4())
        _id = 1
        self.add_note_type(client, _id, name)
        rv = client.delete(urls.REMOVE_NOTE_TYPE_URL.format(_id))

        assert rv.status_code == 200, constants.MSG_HTTP_CODE
        assert 'success' in rv.get_json(), constants.MSG_EXPECTED_KEY.format('success')

        rv = client.get(urls.GET_NOTE_TYPES_URL)
        result = rv.get_json()
        assert len(result) == 0, constants.MSG_NO_RECORDS
