from flask import Flask, render_template, url_for, request, redirect
import json
import helper

app =Flask(__name__)

@app.route('/')
def home():
	mylist = helper.from_stored_json('hang.json')
	return render_template('index.html', mylist = json.dumps(mylist) )
	
if __name__ == '__main__':
	app.run(host='0.0.0.0', debug =True)
