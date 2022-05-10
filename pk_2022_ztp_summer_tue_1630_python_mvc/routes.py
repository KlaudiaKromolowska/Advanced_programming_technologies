from app import app
from app import db
from flask import render_template, Response
from flask import request
from flask import redirect
from flask import url_for
from flask import flash
from models import User
from models import Book
from sqlalchemy import desc
from sqlalchemy import asc
import requests


@app.route('/', methods=['GET'])
def index():
    return render_template('base.html')


@app.route('/users', methods=['GET'])
def show_users():
    users = User.query.all()
    return render_template(
        'show_users.html',
        users=users,
        number_of_users=len(users))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        login = request.form['login']
        password = request.form['password']
        error = None
        if not login or not password:
            error = 'Missing login or password'
        elif User.query.filter_by(login=login).first():
            error = 'User already exist'

        if error:
            flash(error)
            return Response(status=302, mimetype='application/json')

        user = User(login=login, password=password)
        db.session.add(user)
        db.session.commit()

        flash('User successfully added')
    return render_template('register.html')


@app.route('/remove/<int:user_id>', methods=['GET'])
def remove(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()

    flash('User successfully deleted')
    return render_template('show_users.html')


@app.route('/generate_book/<int:user_id>', methods=['GET'])
def generate_book(user_id):
    user = User.query.get_or_404(user_id)
    book_data = requests.get('https://fakerapi.it/api/v1/books?_quantity=1')
    book_data = book_data.json()
    title = book_data['data'][0]['title']
    book = Book(title=title, user_id=user.id)
    db.session.add(book)
    db.session.commit()

    flash('New book successfully added')
    return redirect(url_for('show_users'))


@app.route('/books', methods=['GET', 'POST'])
def show_books():
    users = User.query.all()

    if request.method == 'POST':
        user_id = request.form['user_id']
        column_name = request.form['column_name']
        order_by = request.form['order_by']

        if order_by == 'desc':
            books = Book.query.filter_by(
                user_id=user_id).order_by(desc(
                    column_name)).all()
        else:
            books = Book.query.filter_by(
                user_id=user_id).order_by(asc(
                    column_name)).all()
        return render_template(
            'show_books.html',
            users=users,
            books=books)
    return render_template(
        'show_books.html',
        users=users)
