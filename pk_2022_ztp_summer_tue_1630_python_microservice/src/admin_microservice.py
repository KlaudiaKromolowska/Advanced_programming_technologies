
import json
from flask import Flask, request
import sqlite3
import db
app = Flask(__name__)


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


db = sqlite3.connect(':memory:', check_same_thread=False)
db.row_factory = dict_factory

with open('../db/admin.sql', 'r') as f:
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
        current_cell.execute('INSERT INTO tbl_users (username) values (?)', (user,))
        db.commit()
        last_row_id = current_cell.lastrowid
        return app.response_class(response=json.dumps({'uuid': last_row_id, 'username': user}),
                                  status=200,
                                  mimetype='application/json')


    @app.route('/users/<id>', methods=['GET', 'DELETE'])
    def get_delete_user(id):
        cur = db.cursor()
        # requested id can be wrong
        if id is None or not id.isdigit():
            return app.response_class(status=400)

        user = cur.execute(
            "SELECT * FROM tbl_users WHERE uuid = ?", (id,)).fetchone()

        # user don't exist
        if user is None:
            return app.response_class(status=404)

        if request.method == 'GET':
            print("hell")
            return app.response_class(response=json.dumps(user), status=200, mimetype='application/json')

        if request.method == 'DELETE':
            rentals = requests.get(f'http://127.0.0.1:5001/users/{id}')

            # if rentals exists user cannot be deleted
            if rentals is not None:
                return app.response_class(status=403)
            cur.execute("DELETE FROM tbl_users WHERE uuid = ?", (id, ))
            db.commit()
            return app.response_class(status=200)


if __name__ == '__main__':
    app.run(port=5001, debug=True)
