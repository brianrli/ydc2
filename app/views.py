from flask import Flask, request, render_template
from app import app
from config import si
from models import image

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

#search page
@app.route('/search',methods=['GET'])
def search():
	#get GET request
	request_args = request.args.to_dict()

	if(request_args):
		Images = si.query(**request_args).execute(constructor=image)
	else:
		Images = None

	return render_template('search.html',Images=Images)