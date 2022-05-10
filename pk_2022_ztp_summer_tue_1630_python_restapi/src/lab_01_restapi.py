from flask import Flask
from flask import request
import json
import sqlite3

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

with open('../doc/create_library_db.sql', 'r') as f:
    db.executescript(f.read())
    db.commit()


    @app.route('/users', methods=['GET'])
    def users_get():
        current_cell = db.cursor()
        user = current_cell.execute("SELECT * FROM tbl_users").fetchall()
        return app.response_class(response=json.dumps(user),
                                  status=200,
                                  mimetype='application/json')


    @app.route('/users', methods=['POST'])
    def users_post():
        current_cell = db.cursor()
        user = request.json.get('username')
        current_cell.execute('INSERT INTO tbl_users (name) values (?)', (user,))
        db.commit()
        last_row_id = current_cell.lastrowid
        return app.response_class(response=json.dumps({'id': last_row_id, 'name': user}),
                                  status=200,
                                  mimetype='application/json')


    @app.route('/users/<id_user>', methods=['GET', 'DELETE'])
    def user_get_delete(id_user):
        current_cell = db.cursor()
        if id_user is None or not id_user.isdigit():
            return app.response_class(status=400)

        user = current_cell.execute(
            "SELECT * FROM tbl_users WHERE id = ?", (id_user,)).fetchone()

        if user is None:
            return app.response_class(status=404)

        if request.method == 'GET':
            return app.response_class(response=json.dumps(user),
                                      status=200,
                                      mimetype='application/json')

        if request.method == 'DELETE':
            current_cell.execute("DELETE FROM tbl_users WHERE id = ?", (id_user,))
            db.commit()
            return app.response_class(status=200)


    @app.route('/books', methods=['GET'])
    def books_get():
        current_cell = db.cursor()
        books = current_cell.execute("SELECT * FROM tbl_books").fetchall()
        return app.response_class(response=json.dumps(books),
                                  status=200,
                                  mimetype='application/json')


    @app.route('/books/<book_id>', methods=['GET'])
    def book_with_id(id_book):
        current_cell = db.cursor()
        if request.method == 'GET':
            books = 'SELECT * from tbl_books where id = ?'
            book = current_cell.execute(books, (id_book,)).fetchone()

            rentals = 'SELECT * from tbl_rentals where bookid_fk = ?'
            books_rentals = current_cell.execute(rentals, (id_book,)).fetchall()
            book['rental_list'] = books_rentals
            return app.response_class(response=json.dumps(book),
                                      status=200,
                                      mimetype='application/json')


    @app.route('/books/rent/<book_id>', methods=['PATCH'])
    def rent_id_book(id_book):
        current_cell = db.cursor()
        book = current_cell.execute('SELECT * FROM tbl_books where id = ?', (id_book,)).fetchone()
        if book is None:
            return app.response_class(status=400)
        if book.get('quantity') == 0:
            return app.response_class(status=409)

        user_id = request.headers.get('user')
        user = current_cell.execute('SELECT * FROM tbl_users where id = ?', (user_id,)).fetchone()
        if user is None:
            return app.response_class(status=401)

        current_cell.execute("UPDATE tbl_books SET quantity = ? WHERE id = ?", (book.get('quantity') - 1, id_book))
        current_cell.execute("INSERT INTO tbl_rentals (userid_fk, bookid_fk, rental_date) VALUES (?,?,Date('now'))",
                             (user_id, id_book))

        rent_a_book = current_cell.execute("SELECT rental_date from tbl_rentals where id = ?",
                                           (current_cell.lastrowid,)) \
            .fetchone()

        db.commit()

        return app.response_class(response=json.dumps(rent_a_book), status=200, mimetype='application/json')


    @app.route('/books/return/<book_id>', methods=['PATCH'])
    def return_id_book(id_book):
        current_cell = db.cursor()
        book = current_cell.execute(
            'SELECT * FROM tbl_books where id = ?', (id_book,)).fetchone()
        if book is None:
            return app.response_class(status=400)

        user_id = request.headers.get('user')
        user = current_cell.execute('SELECT * FROM tbl_users where id = ?', (user_id,)).fetchone()
        if user is None:
            return app.response_class(status=401)

        rentals = current_cell.execute("SELECT * FROM tbl_rentals WHERE userid_fk = ? and bookid_fk = ?",
                                       (user_id, id_book))
        if rentals is None:
            return app.response_class(status=409)

        current_cell.execute("UPDATE tbl_books SET quantity = ? WHERE id = ?",
                             (book.get('quantity') + 1, id_book))
        current_cell.execute(
            "UPDATE tbl_rentals SET return_date = Date('now') WHERE userid_fk = ? and bookid_fk = ?",
            (user_id, id_book))

        rental = current_cell.execute("SELECT rental_date from tbl_rentals where id = ?",
                                      (current_cell.lastrowid,)).fetchone()
        db.commit()

        return app.response_class(response=json.dumps(rental), status=200, mimetype='application/json')

if __name__ == '__main__':
    app.run(debug=True)
