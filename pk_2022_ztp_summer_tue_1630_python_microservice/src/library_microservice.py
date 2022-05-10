from flask import Flask
from flask import request
import json
import sqlite3

from pip._vendor import requests

app = Flask(__name__)


# @app.route('/api')
# def api():
#     return "RestApi Bilioteka 2022"


def database(x, y):
    d = {}
    for idx, col in enumerate(x.description):
        d[col[0]] = y[idx]
    return d


db = sqlite3.connect(':memory:', check_same_thread=False)
db.row_factory = database

with open('../db/library.sql', 'r') as f:
    db.executescript(f.read())
    db.commit()

    @app.route('/users', methods=['GET'])
    def get_users():
        user = requests.get(f'http://127.0.0.1:5001/users')
        return app.response_class(response=user,
                                  status=200,
                                  mimetype='application/json')


    @app.route('/users/<id>', methods=['GET'])
    def get_user(id):
        cur = db.cursor()
        # requested id can be wrong
        if id is None or not id.isdigit():
            return app.response_class(status=400)

        user = requests.get(f'http://127.0.0.1:5001/users/{id}')
        if user.status_code ==404:
            return app.response_class(status=404)
        elif user.status_code ==400:
            return app.response_class(status=400)
        elif user.status_code == 200:
            return app.response_class(response=user, status=200, mimetype='application/json')


    @app.route('/books', methods=['GET'])
    def books_get():
        current_cell = db.cursor()
        books = current_cell.execute("SELECT * FROM tbl_books").fetchall()
        return app.response_class(response=json.dumps(books),
                                  status=200,
                                  mimetype='application/json')


    @app.route('/books/<id>', methods=['GET'])
    def book_with_id(id):
        current_cell = db.cursor()
        if request.method == 'GET':
            books = 'SELECT * from tbl_books where id = ?'
            book = current_cell.execute(books, (id,)).fetchone()

            rentals = 'SELECT * from tbl_rentals where book_id = ?'
            books_rentals = current_cell.execute(rentals, (id,)).fetchall()
            book['rental_list'] = books_rentals
            return app.response_class(response=json.dumps(book),
                                      status=200,
                                      mimetype='application/json')


    @app.route('/books/rent/<id>', methods=['PATCH'])
    def rent_id_book(id):
        current_cell = db.cursor()
        book = current_cell.execute('SELECT * FROM tbl_books where id = ?', (id,)).fetchone()
        if book is None:
            return app.response_class(status=409)
        if book.get('quantity') == 0:
            return app.response_class(status=409)

        user_id = (request.headers.get('user'))
        # user = current_cell.execute('SELECT * FROM tbl_users where uuid = ?', (user_id,)).fetchone()
        user = requests.get(f'http://127.0.0.1:5001/users/{user_id}')
        # user = user.json() if user.status_code == 200 else None
        if user.status_code == 400 or user is None:
            return app.response_class(status=401)

        current_cell.execute("UPDATE tbl_books SET quantity = ? WHERE id = ?", (book.get('quantity') - 1, id))
        current_cell.execute("INSERT INTO tbl_rentals (user_id, book_id, rental_date) VALUES (?,?,Date('now'))",
                             (user_id, id))

        rent_a_book = current_cell.execute("SELECT rental_date from tbl_rentals where id = ?",
                                           (current_cell.lastrowid,)) \
            .fetchone()

        db.commit()

        return app.response_class(response=json.dumps(rent_a_book), status=200, mimetype='application/json')



    @app.route('/books/return/<id>', methods=['PATCH'])
    def return_id_book(id):
        current_cell = db.cursor()
        book = current_cell.execute(
            'SELECT * FROM tbl_books where id = ?', (id,)).fetchone()
        if book is None:
            return app.response_class(status=400)

        user_id = request.headers.get('user')
        user = requests.get(f'http://127.0.0.1:5001/users/{user_id}')
        if  user.status_code == 400:
            return app.response_class(status=400)
        if  user.status_code == 401:
            return app.response_class(status=401)
        if user is None:
            return app.response_class(status=401)

        rentals = current_cell.execute("SELECT * FROM tbl_rentals WHERE user_id = ? and book_id = ?",
                                       (user_id, id))
        if rentals is None:
            return app.response_class(status=409)

        current_cell.execute("UPDATE tbl_books SET quantity = ? WHERE id = ?",
                             (book.get('quantity') + 1, id))
        current_cell.execute(
            "UPDATE tbl_rentals SET return_date = Date('now') WHERE user_id = ? and book_id = ?",
            (user_id, id))

        rental = current_cell.execute("SELECT rental_date from tbl_rentals where id = ?",
                                      (current_cell.lastrowid,)).fetchone()
        db.commit()

        return app.response_class(response=json.dumps(rental), status=200, mimetype='application/json')


    @app.route('/users/<id>/books', methods=['GET'])
    def get_user_books(id):
        cur = db.cursor()
        # requested id can be wrong
        if id is None or not id.isdigit():
            return app.response_class(status=400)

        user = requests.get(f'http://127.0.0.1:5001/users/{id}')

        if user is None:
            return app.response_class(status=404)

        # if request.method == 'GET':
        #     return app.response_class(response=json.dumps(user), status=200, mimetype='application/json')
        rentals = cur.execute(
            "SELECT * from tbl_rentals WHERE user_id= ? AND return_date IS NULL", (id,)).fetchall()

        return app.response_class(response=json.dumps(rentals), status=200, mimetype='application/json')

if __name__ == '__main__':
    app.run(port=5000, debug=True)
