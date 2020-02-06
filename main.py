import helper
from flask import Flask, request, jsonify, Response

import json

app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello World!'

@app.route('/tasks/new', methods=['PUT'])
def add_task():
	# global idCount
	# idCount = idCount + 1 
	# get item from the POST body, request module used to parse request and get HTTP body data. response is used to return response to the client, of type JSON
	req_data = request.get_json()
	task = req_data['task']
	# add task to the list
	res_data = helper.add_to_incomplete(task)

	# return error if task cant be added
	if res_data is None:
		response = Response("{'error': 'Task not added - " + task + "'}", mimetype='application/json')
		return response;
	response = Response(json.dumps(res_data), mimetype='application/json')
	return response 

@app.route('/tasks/all', methods = ["GET"])
def get_all_items():
	res_data = helper.get_all_completes(), helper.get_all_incompletes()
	response = Response(json.dumps(res_data), mimetype='application/json')
	return response

@app.route('/tasks/complete', methods = ["POST"])
def complete_task():
	req_data = request.get_json()
	inputId = req_data['id']
	res_data = helper.add_to_complete(inputId)
	# find matching task to input id
	return "completed task" + inputId

@app.route('/tasks/incomplete', methods = ["PATCH"])
def uncomplete_task():
	req_data = request.get_json()
	inputId = req_data['id']
	res_data = helper.uncomplete(inputId)
	# find matching task to input id
	return "un-completed task" + inputId

@app.route('/tasks/remove', methods = ["DELETE"])
def delete():
	req_data = request.get_json()
	inputId = req_data['id']
	res_data = helper.delete_task(inputId)
	if res_data is None:
		response = Response("{'error': 'Error deleting task - '" + task +  "}", status=400 , mimetype='application/json')
	return "deleted task id" + " " + inputId 

@app.route('/tasks/empty', methods = ["EMPTY"])
def delete_all():
	helper.empty()
	return "you deleted everything"

