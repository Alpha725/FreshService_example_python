import requests
from requests.auth import HTTPBasicAuth
import json
## update the below with your own details: 
instances = {
    'Shared Instance': 'https://example.freshservice.com'
}
APIKey = {
    'example Instance': 'kljashf435098sdfnjkfh'
}

## Work in progress, in response to having more than one instance and needing information quickly
## At the moment it only pulls all of the catagories, but a little work will allow it to pull artilces recursively

class Knowledgebot:
	def Get_details():
		search = 'test'## input('\n \nWhat are you looking for?')
		for instance in instances:
			Knowledgebot.Build_request(instance, search)
	def Build_request(instance, search):
		url = instances[instance]+"/solution/categories.json"
		auth = HTTPBasicAuth(APIKey[instance], 'x')
		Knowledgebot.Request(instance, url, auth, search)
	def Request(instance, url, auth, search):
		req = requests.get(url, auth=auth)
		catagories = json.loads(req.text)
		for catagory in catagories:
			print(instance+' - '+catagory['category']['name'])

Knowledgebot.Get_details()
