from flask import Flask, request
from app import app
from config import si
from models import image

@app.route('/')
@app.route('/index')
def index():
	return "Hello, World!"

#search page
@app.route('/search',methods=['GET'])
def search():
	#get GET request
	request_args = request.args.to_dict()
	print(request_args)

	#forward them on to apache solr server
	for result in si.query(**request_args).execute(constructor=image):
		print result

	return "Okay...."