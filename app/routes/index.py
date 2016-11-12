from app import app
from flask import jsonify, request

@app.route('/', methods=['GET', 'POST'])
def index_page():

    return "inde page"

@app.route('/echo', methods=['GET', 'POST'])
def echo():
    print("echo", request.json)
    return jsonify(request.json)