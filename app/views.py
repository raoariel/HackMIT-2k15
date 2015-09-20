"""
Definition of views.
"""
import sys
import json
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpRequest
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.template.loader import render_to_string
from datetime import datetime
from django.http import HttpResponse
from pymongo import *
import pyqrcode
import png

sys.path.insert(0, 'app/nlp/')
from FeedContent import *

mongo = MongoClient('localhost', 27017)
db = mongo.cache

# def parseCharityList():
# 	with open('app/data/charities.json') as data_file:    
# 		charities_obj = json.load(data_file)
# 	return charities_obj

# def getContentFromQuery(query):
# 	articles = FeedContent(query)
# 	articles.processContent()
# 	content = articles.getContent()
# 	queryDoc = {'query' : query}
# 	document = dict(content.items() + queryDoc.items())
# 	db.myCache.update_one(queryDoc, {'$set' : {'articles' : content['articles']}}, True)
# 	return content

def home(request):
	"""Renders the home page."""
	assert isinstance(request, HttpRequest)
	# charities = []
	# for key in parseCharityList():
	# 	charities.append(key);
	# context = {'charityList': charities}
	context = RequestContext(request, {'request': request, 'user': request.user})
	return render(request, 'app/index.html', context)


def qr(request):
	"""Renders the home page."""
	assert isinstance(request, HttpRequest)
	# charities = []
	# for key in parseCharityList():
	# 	charities.append(key);
	# context = {'charityList': charities}
	context = RequestContext(request, {'request': request, 'user': request.user})
	return render(request, 'app/qr.html', context)


def qrcode(request):
	"""Renders the home page."""
	qr = pyqrcode.create("hello world")
	qr.png('hackmitqr.png', scale=6)
	console.log('pass')
	return HttpRequest("pass")
