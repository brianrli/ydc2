from flask import Flask 
from config import si

app = Flask(__name__)
#print si.schema.fields.keys()
for result in si.query({'recordtype':"lido"}).execute():
	print result

from app import views
