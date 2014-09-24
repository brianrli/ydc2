from flask import Flask, request, render_template
from app import app
from config import si  
from models import image

@app.route('/')
@app.route('/index',methods=['GET'])
def index():
	# request.form['title']
	request_args = request.args.to_dict()
	if(request_args):
		Images = si.query(**request_args).execute(constructor=image)
	else:
		Images = si.query(publishDate="1801").execute(constructor=image)
	return render_template('search.html',Images=Images)

# # search page
# @app.route('/search',methods=['GET','POST'])
# def search():
# 	# request.form['title']
# 	request_args = request.args.to_dict()
# 	if(request_args):
# 		Images = si.query(**request_args).execute(constructor=image)
# 	else:
# 		Images = si.query(publishDate="1801").execute(constructor=image)
# 	return render_template('search.html',Images=Images)

# @app.route('/add', methods=['GET'])
# def add(): 
# 	print("add");
# 	if request.method == 'GET':
# 		d = {"publishDate",request.form['year']} 
# 		Images = si.query(**d).execute(constructor=image)
# 	return render_template('search.html',Images=Images)