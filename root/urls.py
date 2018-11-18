from flask import Blueprint
from .views import *

root = Blueprint("root", __name__)

root.add_url_rule('/', 'index', index)
root.add_url_rule('/login', 'login', login, methods=['POST', 'GET'])
root.add_url_rule('/register', 'register', register, methods=['POST', 'GET'])
root.add_url_rule('/upload', 'upload', upload, methods=['POST'])
root.add_url_rule('/logout', 'logout', logout)
root.add_url_rule('/search', 'search', search)
root.add_url_rule('/upload_search', 'upload_search', upload_search, methods=['POST'])
root.add_url_rule('/result', 'result', result)
