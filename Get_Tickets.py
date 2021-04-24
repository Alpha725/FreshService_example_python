import multiprocessing
from multiprocessing import Manager
import requests
from requests.auth import HTTPBasicAuth
import json

## Please update the below before running ;)
instances = {
    'Shared Instance': 'https://example.freshservice.com'
}
APIKey = {
    'example Instance': 'kljashf435098sdfnjkfh'
}
NOC = {
    'example Instance': '923783'
}

TicketListFinal = []

## explaination on the below:
## FreshService does not allow you to pull number of total tickets.
## there for you look for the max number that a page can have recursively until it isnt the max value.

class Getbot:
    def Tickets(instance, TicketListFinal):
        x = 1
        y = 30
        while y == 30:
            url = instances[instance]+"/helpdesk/tickets"+Tickets[instance]
            auth = HTTPBasicAuth(APIKey[instance], 'x')
            req = requests.get(url+"?format=json&page="+str(x), auth=auth)
            TicketList = json.loads(req.text)
            y = len(TicketList)
            print(y)
            for Ticket in TicketList:
                payload = {'subject': str(Ticket['subject']), 'id': str(Ticket['display_id']), 'instance': instance, 'description': Ticket['description']}
                TicketListFinal.append(payload)
            x += 1
    def Filter_Tickets(TicketListFinal):
        for Ticket in TicketListFinal:
            Getbot.Print_Tickets(Ticket)
    def Print_Tickets(Ticket):
        ticket_url = instances[Ticket['instance']]+'/helpdesk/tickets/'+Ticket['id']
        ticket_subject = Ticket['subject']
        print(ticket_subject+'\n'+ticket_url+'\n')

## Below is to accomplish multiprocessing to decrease request times for mutpile instances, if dont need consider removing

if __name__ == '__main__':
    with Manager() as manager:
        TicketListFinal = manager.list()
        jobs = []
        for instance in instances:
            webagent = multiprocessing.Process(target=Getbot.Tickets, args=(instance, TicketListFinal))
            webagent.start()
            jobs.append(webagent)
        for job in jobs:
            job.join()
        for Ticket in TicketListFinal:
            Getbot.Print_Tickets(Ticket)
