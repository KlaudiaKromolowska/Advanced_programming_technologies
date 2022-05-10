from tests import constants
import uuid
from tests import urls
from .fixtures import app
from .utils import captured_templates


class TestRegister():

    def test_status_code_expect_200(self, client):
        print("TEST: '{}' path".format(urls.REGISTER_URL))
        assert 200 == client.get(urls.REGISTER_URL).status_code, \
            constants.MSG_HTTP_CODE

    def test_check_render_template(self, client):
        print("TEST: '{}' path".format(urls.REGISTER_URL))
        with captured_templates(app) as templates:
            rv = client.get(urls.REGISTER_URL)
            assert rv.status_code == 200, \
                constants.MSG_HTTP_CODE
            assert len(templates) == 1, \
                constants.MSG_TEMP_RENDER
            template, context = templates[0]
            assert template.name == constants.REGISTER, \
                constants.MSG_TEMP_RENDER.format(constants.REGISTER)

    def test_register_user(self, client):
        print("TEST: '{}' path".format(urls.REGISTER_URL))
        with captured_templates(app) as templates:
            data = {
                'login': 'user{}'.format(uuid.uuid4()),
                'password': 'password'
            }
            rv = client.post(urls.REGISTER_URL, data=data)
            assert rv.status_code == 200, \
                constants.MSG_HTTP_CODE
            assert len(templates) == 1
            template, context = templates[0]
            assert template.name == constants.REGISTER, \
                constants.MSG_TEMP_RENDER.format(constants.REGISTER)

    def test_register_existing_user(self, client):
        print("TEST: '{}' path".format(urls.REGISTER_URL))
        data = {
            'login': 'duplicate_user{}'.format(uuid.uuid4()),
            'password': 'password'
        }
        with captured_templates(app) as templates:
            rv = client.post(urls.REGISTER_URL, data=data)
            assert rv.status_code == 200, \
                constants.MSG_HTTP_CODE
            assert len(templates) == 1
            template, context = templates[0]
            assert template.name == constants.REGISTER, \
                constants.MSG_TEMP_RENDER.format(constants.REGISTER)

        rv = client.post(urls.REGISTER_URL, data=data)
        assert rv.status_code == 302, \
            "Oczekiwano że nie można będzie dodać użytkownika " \
            "o tym samym loginie"

    def test_register_user_no_login(self, client):
        print("TEST: '{}' path".format(urls.REGISTER_URL))
        data = {
            'login': '',
            'password': 'password'
        }
        rv = client.post(urls.REGISTER_URL, data=data)
        assert rv.status_code == 302, \
            "Oczekiwano że jeśli nie będzie podany 'login' " \
            "żądanie się nie powiedzie"

    def test_register_user_no_password(self, client):
        print("TEST: '{}' path".format(urls.REGISTER_URL))
        data = {
            'login': 'login',
            'password': ''
        }
        rv = client.post(urls.REGISTER_URL, data=data)
        assert rv.status_code == 302, \
            "Oczekiwano że jeśli nie będzie podany 'password' " \
            "żądanie się nie powiedzie"
