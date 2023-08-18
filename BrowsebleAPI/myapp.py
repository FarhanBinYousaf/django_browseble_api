import requests
import json


URL = "http://127.0.0.1:8000/studentapi/"			# This URL is used when 'studenapi' URL is direct used in Django main urls.py file 



# URL = "http://127.0.0.1:8000"						# This is used when 'studentapi' URL is used in 'api' app' urls.py file 

def get_data(id = None):
	data = {}
	if id is not None:
		data = {'id':id}
	headers = {'content-Type':'application/json'}
	json_data = json.dumps(data)
	r = requests.get(url = URL, headers=headers, data  = json_data)
	data = r.json()
	print(data)

# get_data(1)
get_data()

def post_data():
	data = {
		'name':'Farhan',
		'roll' : 160,
		'city': 'Lahore'
	}

	headers = {'content-Type':'application/json'}

	json_data = json.dumps(data)
	r = requests.post(url = URL, headers=headers, data  = json_data)
	data = r.json()
	print(data)

# post_data()


def update_data():
	data = {
		'id':3,
		'name':'Yousaf',
		'roll':12,
		'city': 'Karachi'
	}
	headers = {'content-Type':'application/json'}

	json_data = json.dumps(data)
	r = requests.put(url = URL, headers=headers ,data  = json_data)
	data = r.json()
	print(data)

# update_data()



def delete_data():
	data = {'id':3}
	headers = {'content-Type':'application/json'}

	json_data = json.dumps(data)
	r = requests.delete(url = URL, headers=headers ,data  = json_data)
	data = r.json()
	print(data)

# delete_data()