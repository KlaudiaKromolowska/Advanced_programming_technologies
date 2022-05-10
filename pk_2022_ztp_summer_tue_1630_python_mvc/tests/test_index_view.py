from tests import constants
from tests import urls
from .fixtures import app
from .utils import captured_templates


class TestIndexView():

    def test_status_code_expect_200(self, client):
        print("TEST: '{}' path".format(urls.INDEX_URL))
        assert 200 == client.get(urls.INDEX_URL).status_code,\
            constants.MSG_HTTP_CODE

    def test_check_render_template(self, client):
        print("TEST: '{}' path".format(urls.INDEX_URL))
        with captured_templates(app) as templates:
            rv = client.get(urls.INDEX_URL)
            assert rv.status_code == 200, \
                constants.MSG_HTTP_CODE
            assert len(templates) == 1
            template = templates[0][0]
            assert template.name == constants.INDEX, \
                constants.MSG_TEMP_RENDER.format(
                    constants.INDEX)
