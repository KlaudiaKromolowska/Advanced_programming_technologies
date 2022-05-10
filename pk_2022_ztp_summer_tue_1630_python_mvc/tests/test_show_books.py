from tests import urls
import models
from tests import constants
from .fixtures import app, db
from .utils import captured_templates

_NUMBER_OF_BOOKS = 10

_EXPECTED_ASC_TITLES = [f"Title {i}"
                        for i in range(_NUMBER_OF_BOOKS)]


class TestShowBooks():

    def gen_users_books(self):
        user = models.User(login='login', password='password')
        books = [models.Book(title=f"Title {i}", user_id=1)
                 for i in range(_NUMBER_OF_BOOKS)]
        db.session.add(user)
        for book in books:
            db.session.add(book)
        db.session.commit()

    def test_sort_asc(self, client):
        print("TEST: '{}' path".format(urls.BOOKS_URL))
        self.gen_users_books()
        with captured_templates(app) as templates:
            data = {
                'user_id': 1,
                'column_name': 'title',
                'order_by': '',
            }
            rv = client.post(urls.BOOKS_URL, data=data)
            assert rv.status_code == 200, \
                constants.MSG_HTTP_CODE
            assert len(templates) == 1
            template, context = templates[0]
            books = context['books']
            users = context['users']
            assert len(books) == _NUMBER_OF_BOOKS, \
                f"Oczekiwano że będzie {_NUMBER_OF_BOOKS} książek"
            assert len(users) == 1, \
                "Oczekiwano że książki będą posortowane " \
                "dla jednego użytkownika"
            result_titles = [book.title for book in books]
            assert result_titles == _EXPECTED_ASC_TITLES

    def test_sort_dsc(self, client):
        print("TEST: '{}' path".format(urls.BOOKS_URL))
        self.gen_users_books()
        with captured_templates(app) as templates:
            data = {
                'user_id': 1,
                'column_name': 'title',
                'order_by': 'desc',
            }
            rv = client.post(urls.BOOKS_URL, data=data)
            assert rv.status_code == 200, \
                constants.MSG_HTTP_CODE
            assert len(templates) == 1
            template, context = templates[0]
            books = context['books']
            users = context['users']
            assert len(books) == _NUMBER_OF_BOOKS, \
                f"Oczekiwano że będzie {_NUMBER_OF_BOOKS} książek"
            assert len(users) == 1, \
                "Oczekiwano że książki będą posortowane " \
                "dla jednego użytkownika"
            result_titles = [book.title for book in books]
            assert result_titles == sorted(
                _EXPECTED_ASC_TITLES, reverse=True)
