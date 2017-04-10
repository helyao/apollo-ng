from . import main
from flask import make_response

@main.route('/')
def index():
    return "Hello World"

@main.route('/angular')
def angular():
    return make_response(open('../front/dist/index.html').read())