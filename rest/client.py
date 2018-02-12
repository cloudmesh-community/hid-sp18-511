import requests 
import json 

def get_computer_info(): 
	response = requests.get("http://127.0.0.1:5000/computer") 
	print(json.dumps(response.json(), indent=4, sort_keys=True)) 
	
	response = requests.get("http://127.0.0.1:5000/computer/processor") 
	print(json.dumps(response.json(), indent=4, sort_keys=True))
	
	response = requests.get("http://127.0.0.1:5000/computer/disk") 
	print(json.dumps(response.json(), indent=4, sort_keys=True))
	
	response = requests.get("http://127.0.0.1:5000/computer/memory") 
	print(json.dumps(response.json(), indent=4, sort_keys=True))
	
	response = requests.get("http://127.0.0.1:5000/computer/cpu") 
	print(json.dumps(response.json(), indent=4, sort_keys=True))
		
get_computer_info()