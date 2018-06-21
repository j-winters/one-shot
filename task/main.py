#!flask/bin/python

import sys
import logging

from flask import Flask, render_template, request, redirect, Response, url_for
import random, json

import gspread
from oauth2client.service_account import ServiceAccountCredentials

app = Flask(__name__)

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('Oneshot-0b481afa3ab2.json',scope)
client = gspread.authorize(creds)


@app.route('/')
def signUp():
	return render_template('consent.html')

@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/finish.html')
def finish():
    return render_template('finish.html')

@app.route('/postmethod', methods = ['POST'])
def get_post_javascript_data():
	jsdata = request.form['javascript_data']
	data = client.open('Oneshotdata')
	row = json.loads(jsdata)
	#print row
	#row = ["IP","NEW!"]
	data.worksheet("output").append_row(row)
	#row = json.loads(jsdata)
	#data.worksheet("output").append_row(row)

#@app.route('/postmethod', methods = ['POST'])
#def get_post_javascript_data():
#	jsdata = request.form['javascript_data']
#	user = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
	#print jsdata
	#return jsdata
	#Need to get rid of this replace stuff if you're just having raw data
	#jsdata = jsdata.replace('Age%', 'Age:')
	#jsdata = jsdata.replace('3A', ' ')
	#jsdata = jsdata.replace('%3', ';')
	#jsdata = jsdata.replace('BLanguage%', 'Language:')
	#print jsdata

#	data = client.open('Oneshotdata')
	#row = json.loads(jsdata)
#	row = ["IP","WHAT!"]
#	data.worksheet("output").append_row(row)

	#content = open("test.txt", 'a')
	#content.write('IP: '+user+';'+jsdata+'\n')
	#content.write(jsdata+'\n')
	#content.close()
    
