from flask import Flask, request, render_template
from app import app
from config import si
from models import image
import urllib2

@app.route('/')
@app.route('/index')
def index():
	return "Hello, World!"

#search page
@app.route('/search',methods=['GET'])
def search():
	#get GET request
	request_args = request.args.to_dict()
	
	#forward them on to apache solr server
	Images = si.query(**request_args).execute(constructor=image)

	return render_template('search.html',Images=Images)