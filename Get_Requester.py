import multiprocessing
from multiprocessing import Manager
import requests
from requests.auth import HTTPBasicAuth
import json

## Make sure to update the below with your own details:
instances = {
    'Shared Instance': 'https://example.freshservice.com'
}
APIKey = {
    'example Instance': 'kljashf435098sdfnjkfh'
}

RequestersListFinal = []

## Below looks for users recursively across different FreshService instances 
## Asks for the user name

class Getbot:
    def Requesters(instance, RequestersListFinal):
        x = 1
        y = 50
        while y == 50:
            url = instances[instance]+"/itil/requesters?format=json&page="
            auth = HTTPBasicAuth(APIKey[instance], 'x')
            req = requests.get(url+str(x), auth=auth)
            RequestersList = json.loads(req.text)
            y = len(RequestersList)
            print(instance+'.'*x)
            for Requesters in RequestersList:
                payload = {'name': Requesters['user']['name'], 'id': str(Requesters['user']['id']), 'instance': instance, 'email': Requesters['user']['email']}
                RequestersListFinal.append(payload)
            x += 1
    def Filter_Requesters(RequestersListFinal):
        for Requesters in RequestersListFinal:
            Getbot.Print_Requesters(Requesters)
    def Print_Requesters(Requesters):
        Requesters_url = Requesters['name']
        Requesters_subject = Requesters['email']
        print(Requesters_subject+'\n'+Requesters_url+'\n')

## Multi threaded goodness, still takes ages with big instances
## optimisations are to make the tech select the instance, but also multi-thread with a range in function
## rework required....

if __name__ == '__main__':
    with Manager() as manager:
        RequestersListFinal = manager.list()
        jobs = []
        search = input('\n \nWhat user are you looking for?')
        for instance in instances:
            webagent = multiprocessing.Process(target=Getbot.Requesters, args=(instance, RequestersListFinal))
            webagent.start()
            jobs.append(webagent)
        for job in jobs:
            job.join()
        for Requesters in RequestersListFinal:
            if search in Requesters['name']:
                Getbot.Print_Requesters(Requesters)
