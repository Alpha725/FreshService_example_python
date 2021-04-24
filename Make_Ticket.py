import requests
from requests.auth import HTTPBasicAuth
import json
## make sure to update all of the below with your details: 
instances = {
    'Shared Instance': 'https://example.freshservice.com'
}
APIKey = {
    'example Instance': 'kljashf435098sdfnjkfh'
}
## Use this as a command line tool, it will ask for what instance to make the ticket, subject and description
## It will also return the ticket URL once completed for ease.

class Putbot:
    def Get_details():
        for instance in instances:
            print(instance)
        ticket_instance = input('\n \nEnter which client:')
        subject = input('\n \nEnter subject:')
        description = input('\n \nEnter description:')
        if(ticket_instance in instances):
            print('You have chosen '+ticket_instance)
            Putbot.MakeTicket(ticket_instance, subject, description)
        else:
            print('Please enter exactly which client from the below list:')
            Putbot.Get_details()
    def MakeTicket(instance, subject, description):
        url = instances[instance]+"/helpdesk/tickets.json"
        header = {"content-type": "application/json"}
        auth = HTTPBasicAuth(APIKey[instance], 'x')
        data = {
            'helpdesk_ticket': {
                'description': description,
                'subject': subject,
                'email': 'example@example.com',
                'priority': 2,
                'status': 2,
                'ticket_type': 'Incident',
            },
            'cc_emails': ''
        }
        Putbot.Post(instance, url, header, auth, data)
    def Post(instance, url, header, auth, data):
        req = requests.post(url, auth=auth, headers=header, json=data)
        posted_ticket = json_data = json.loads(req.text)
        print(instances[instance]+'/helpdesk/tickets/'+str(posted_ticket["item"]["helpdesk_ticket"]["display_id"]))

Putbot.Get_details()
