import uuid

from tests import constants
from tests import urls
from .fixtures import client


class TestNote:

    def add_note_type(self, client):
        data = {'name': 'name_{}'.format(uuid.uuid4())}
        client.post(urls.ADD_NOTE_TYPE_URL, json=data)

    def get_note_data(self, note_type_id=1):
        return {
            'title': 'title_{}'.format(uuid.uuid4()),
            'content': 'content_{}'.format(uuid.uuid4()),
            'note_type_id': note_type_id,
            'important': True,
            'is_task': False
        }

    def compare_note_data(self, item, expected_data, _id=1):
        assert 'created_at' in item, constants.MSG_EXPECTED_KEY.format('created_at')
        # adjust data to fit database model
        item.pop('created_at')
        expected_data['id'] = _id
        expected_data['note_type'] = expected_data.pop('note_type_id')
        assert item == expected_data, constants.MSG_DATA.format(expected_data)

    def test_add_note(self, client):
        print("TEST: '{}' path".format(urls.ADD_NOTE_URL))
        self.add_note_type(client)

        expected_data = self.get_note_data()
        rv = client.post(urls.ADD_NOTE_URL, json=expected_data)

        assert rv.status_code == 200, constants.MSG_HTTP_CODE
        assert 'success' in rv.get_json(), constants.MSG_EXPECTED_KEY.format('success')

        rv = client.get(urls.LIST_URL)
        result = rv.get_json()
        assert len(result) == 1, constants.MSG_SINGLE_RECORD

        item = result[0]
        self.compare_note_data(item, expected_data)

    def test_get_note(self, client):
        print("TEST: '{}' path".format(urls.GET_NOTE_URL))
        self.add_note_type(client)

        expected_data = self.get_note_data()
        client.post(urls.ADD_NOTE_URL, json=expected_data)

        rv = client.get(urls.GET_NOTE_URL.format(1))

        assert rv.status_code == 200, constants.MSG_HTTP_CODE

        item = rv.get_json()
        self.compare_note_data(item, expected_data)

    def test_edit_note(self, client):
        print("TEST: '{}' path".format(urls.EDIT_NOTE_URL))
        self.add_note_type(client)
        self.add_note_type(client)

        data = self.get_note_data()
        client.post(urls.ADD_NOTE_URL, json=data)

        new_data = self.get_note_data(note_type_id=2)
        new_data['is_task'] = True
        new_data['note_type'] = 2
        rv = client.put(urls.EDIT_NOTE_URL.format(1), json=new_data)

        assert rv.status_code == 200, constants.MSG_HTTP_CODE
        assert 'success' in rv.get_json(), constants.MSG_EXPECTED_KEY.format('success')

        rv = client.get(urls.LIST_URL)
        result = rv.get_json()
        assert len(result) == 1, constants.MSG_SINGLE_RECORD

        item = result[0]
        self.compare_note_data(item, new_data)

    def test_remove_note(self, client):
        print("TEST: '{}' path".format(urls.REMOVE_NOTE_URL))
        self.add_note_type(client)

        expected_data = self.get_note_data()
        client.post(urls.ADD_NOTE_URL, json=expected_data)

        rv = client.delete(urls.REMOVE_NOTE_URL.format(1))

        assert rv.status_code == 200, constants.MSG_HTTP_CODE
        assert 'success' in rv.get_json(), constants.MSG_EXPECTED_KEY.format('success')

        rv = client.get(urls.LIST_URL)
        result = rv.get_json()
        assert len(result) == 0, constants.MSG_NO_RECORDS

    def test_list(self, client):
        print("TEST: '{}' path".format(urls.LIST_URL))
        self.add_note_type(client)
        self.add_note_type(client)
        self.add_note_type(client)

        data_1 = self.get_note_data()
        data_2 = self.get_note_data(note_type_id=2)
        data_2['is_task'] = True
        data_3 = self.get_note_data(note_type_id=3)
        data_3['important'] = False
        client.post(urls.ADD_NOTE_URL, json=data_1)
        client.post(urls.ADD_NOTE_URL, json=data_2)
        client.post(urls.ADD_NOTE_URL, json=data_3)

        rv = client.get(urls.LIST_URL)
        assert rv.status_code == 200, constants.MSG_HTTP_CODE

        result = rv.get_json()
        assert len(result) == 3

        item_1, item_2, item_3 = result
        self.compare_note_data(item_1, data_1, 1)
        self.compare_note_data(item_2, data_2, 2)
        self.compare_note_data(item_3, data_3, 3)

    def test_list_sort(self, client):
        print("TEST: '{}' path".format(urls.LIST_SORT_URL))
        self.add_note_type(client)

        data_1 = self.get_note_data()
        data_1['title'] = 'hhh'
        data_2 = self.get_note_data()
        data_2['title'] = 'yyy'
        data_3 = self.get_note_data()
        data_3['title'] = 'aaa'
        client.post(urls.ADD_NOTE_URL, json=data_1)
        client.post(urls.ADD_NOTE_URL, json=data_2)
        client.post(urls.ADD_NOTE_URL, json=data_3)

        rv = client.get(urls.LIST_SORT_URL.format('title'))
        assert rv.status_code == 200, constants.MSG_HTTP_CODE

        result = rv.get_json()
        assert len(result) == 3

        item_1, item_2, item_3 = result
        self.compare_note_data(item_1, data_3, 3)
        self.compare_note_data(item_2, data_1, 1)
        self.compare_note_data(item_3, data_2, 2)

    def test_list_filter(self, client):
        print("TEST: '{}' path".format(urls.LIST_FILTER_URL))
        self.add_note_type(client)

        data_1 = self.get_note_data()
        data_1['title'] = 'hhh'
        data_2 = self.get_note_data()
        data_2['title'] = 'yyy'
        data_3 = self.get_note_data()
        data_3['title'] = 'hhh'
        client.post(urls.ADD_NOTE_URL, json=data_1)
        client.post(urls.ADD_NOTE_URL, json=data_2)
        client.post(urls.ADD_NOTE_URL, json=data_3)

        rv = client.get(urls.LIST_FILTER_URL.format('title', 'hhh'))
        assert rv.status_code == 200, constants.MSG_HTTP_CODE

        result = rv.get_json()
        assert len(result) == 2

        item_1, item_2 = result
        self.compare_note_data(item_1, data_1, 1)
        self.compare_note_data(item_2, data_3, 3)

    def test_list_filter_sort(self, client):
        print("TEST: '{}' path".format(urls.LIST_FILTER_SORT_URL))
        self.add_note_type(client)

        data_1 = self.get_note_data()
        data_1['title'] = 'last'
        data_1['content'] = 'hhh'
        data_2 = self.get_note_data()
        data_2['title'] = 'yyy'
        data_2['content'] = 'yyy'
        data_3 = self.get_note_data()
        data_3['title'] = 'first'
        data_3['content'] = 'hhh'
        client.post(urls.ADD_NOTE_URL, json=data_1)
        client.post(urls.ADD_NOTE_URL, json=data_2)
        client.post(urls.ADD_NOTE_URL, json=data_3)

        rv = client.get(urls.LIST_FILTER_SORT_URL.format('content', 'hhh', 'title'))
        assert rv.status_code == 200, constants.MSG_HTTP_CODE

        result = rv.get_json()
        assert len(result) == 2

        item_1, item_2 = result
        self.compare_note_data(item_1, data_3, 3)
        self.compare_note_data(item_2, data_1, 1)
        