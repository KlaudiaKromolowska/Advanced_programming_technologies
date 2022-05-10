import uuid
from tests import constants

from tests import urls
from .fixtures import app
from .utils import captured_templates


class TestGenerateBook():

    def show_users(self, user_login, client):
        user_id = None
        with captured_templates(app) as templates:
            client.get(urls.SHOW_USERS_URL)
            users = templates[0][1]['users']
            for user in users:
                if user.login == user_login:
                    user_id = user.id
                    break
        return user_id

    def test_generate_book(self, client):
        print("TEST: '{}' path".format(urls.BOOKS_URL))
        user_login = 'user{}'.format(uuid.uuid4())
        with captured_templates(app) as templates:
            data = {
                'login': user_login,
                'password': 'password'
            }
            client.post(urls.REGISTER_URL, data=data)
        user_id = self.show_users(user_login, client)
        assert user_id is not None
        client.get(urls.GENERATE_BOOK_URL.format(user_id))
        with captured_templates(app) as templates:
            data = {
                'user_id': user_id,
                'column_name': 'title',
                'order_by': '',
            }
            rv = client.post(urls.BOOKS_URL, data=data)
            assert rv.status_code == 200, \
                constants.MSG_HTTP_CODE
            assert len(templates) == 1
            template, context = templates[0]
            books = context['books']
            gen_book_user_id = [user.id for user in context['users']
                                if user.id == books[0].user_id]
            assert len(gen_book_user_id) == 1
            assert template.name == constants.SHOW_BOOKS, \
                constants.MSG_TEMP_RENDER.format(
                    constants.SHOW_BOOKS)
