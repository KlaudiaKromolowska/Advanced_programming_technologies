import uuid
from tests import urls
from .fixtures import app
from .utils import captured_templates


class TestRemove():

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

    def test_remove_user(self, client):
        print("TEST: '{}' path".format(urls.REGISTER_URL))
        user_login = 'user{}'.format(uuid.uuid4())
        with captured_templates(app):
            data = {
                'login': user_login,
                'password': 'password'
            }
            client.post(urls.REGISTER_URL, data=data)
        user_id = self.show_users(user_login, client)
        assert user_id is not None, \
            "Oczekiwano że zostanie stworzonu użytkownik do usunięcia"
        client.get(urls.REMOVE_URL.format(user_id))
        user_id = self.show_users(user_login, client)
        assert user_id is None, \
            "Oczekiwano że użytkownik zostanie usunięty"
