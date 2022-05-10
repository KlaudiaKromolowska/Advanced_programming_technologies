from flask import jsonify
from app import app


@app.errorhandler(Exception)
def handle_exception(e):
    errors = [err for err in str(e).split(',')]
    return jsonify(jsonify({'errors': errors}))
