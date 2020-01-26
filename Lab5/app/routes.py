from app import app
from flask import request

@app.route('/')
@app.route('/index')
def index():
    name = request.args.get('name')
    if not name:
        return "No argument passed. "
    else:
        return "Hello "+name