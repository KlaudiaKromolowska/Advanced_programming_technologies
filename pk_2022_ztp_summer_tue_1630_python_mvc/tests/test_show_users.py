import uuid
from tests import constants
from tests import urls
from .fixtures import app
from .utils import captured_templates


class TestShowUsers():

    def test_status_code_expect_200(self, client):
        print("TEST: '{}' path".format(urls.SHOW_USERS_URL))
        assert 200 == client.get(urls.SHOW_USERS_URL).status_code, \
            constants.MSG_HTTP_CODE

    def test_check_render_template(self, client):
        print("TEST: '{}' path".format(urls.SHOW_USERS_URL))
        with captured_templates(app) as templates:
            rv = client.get(urls.SHOW_USERS_URL)
            assert rv.status_code == 200, \
                constants.MSG_HTTP_CODE
            assert len(templates) == 1, \
                constants.MSG_ONE_TEMP
            template, context = templates[0]
            assert template.name == constants.SHOW_USERS, \
                constants.MSG_TEMP_RENDER.format(
                    constants.SHOW_USERS)
            users = context.get('users', None)
            assert users is not None, \
                constants.MSG_USERS_IN_TEMP
            assert len(users) >= 0, \
                constants.MSG_USERS_IN_TEMP
            assert context.get('number_of_users', -1) >= 0, \
                "Oczekiwano przekazanie do templatki " \
                "zmiennej 'number_of_users'"

    def test_check_show_users_user_count(self, client):
        print("TEST: '{}' path".format(urls.SHOW_USERS_URL))
        data = {
            'login': 'user{}'.format(uuid.uuid4()),
            'password': 'password'
        }
        client.post(urls.REGISTER_URL, data=data)
        with captured_templates(app) as templates:
            rv = client.get(urls.SHOW_USERS_URL)
            assert rv.status_code == 200, \
                constants.MSG_HTTP_CODE
            assert len(templates) == 1, \
                constants.MSG_ONE_TEMP
            template, context = templates[0]
            assert template.name == constants.SHOW_USERS, \
                constants.MSG_TEMP_RENDER.format(
                    constants.SHOW_USERS)
            users = context.get('users', None)
            assert users is not None, \
                constants.MSG_USERS_IN_TEMP
            assert len(users) == 1, \
                "Oczekiwano że bedzie jeden użytkownik na stronie"
            assert context.get('number_of_users', None) == 1, \
                "Oczekiwano że bedzie jeden użytkownik na stronie"
