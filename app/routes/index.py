from app import app
from flask import jsonify

@app.route('/', methods=['GET', 'POST'])
def index_page():

    return "inde page"

@app.route('/echo')
def echo():
    ex_dict = {}
    ex_dict['pang'] = 'aldf'
    ex_dict['elh'] = 'dfadf'
    return jsonify(ex_dict)