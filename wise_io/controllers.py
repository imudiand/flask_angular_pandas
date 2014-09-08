import os
from flask import make_response, jsonify
from wise_io import app

@app.route('/query')
def query():
	results = app.config['df'].query(app.config['query'])
	ret = {
		'rows': len(results.index),
		'index_first': results.index[0],
		'index_last': results.index[len(results.index)-1],
	}
	return jsonify(**ret)

@app.route('/')
def basic_pages(**kwargs):
	return make_response(open('wise_io/templates/index.html').read())
