import time
import requests
import json

class APIConnector():
    #Initialize object
    def __init__(self, username, password):
        self.session = ""
        self.payload = {'username': username, 'password': password}
        self.url = 'https://alice-api.azurewebsites.net'

    #Register bot
    def register(self):
        r = requests.post(self.url + '/auth/register')
        print(r.text)

    #Login bot
    def login(self):
        r = requests.post(self.url + '/auth/login', data=self.payload)
        print(r)
        self.session = json.loads(r.text)['session_id']
        print("LOGGED IN")


    #Check for matching bot
    def pollForMatch(self):
        print("POLLING FOR MATCH")
        poll_response = requests.get(self.url + '/bot/match/', headers={"X-Session-Token": self.session})
        response_json = json.loads(poll_response.text)
        if(response_json['talking_id'] == self.payload['username']):
            print("This Alice is currently in TALKING mode")
            return True
        else:
            print("This Alice is currently in LISTENING mode")
            return False

    #Send message
    def sendMessage(self, message_id):
        print('Start sending')
        send_message_url = requests.post(self.url + '/bot/send/', data={"text_id": message_id}, headers={"X-Session-Token": self.session})
        print(send_message_url.text)
        print("Message sent:" + str(message_id))
        time.sleep(1)
        # Sleep for a short time, to avoid "no match found" as the other bot is processing the message

    #Obtain message from other bot
    def receiveMessage(self):
        poll_response = requests.get(self.url + '/bot/receive/', headers={"X-Session-Token": self.session})
        print(poll_response.text)
        # Check if we have a new message
        message = poll_response.text
        if (message=="[]"):
            print("No message yet")
            time.sleep(0.5)
            return 0
        else:
            print("Got message:")
            message_json = json.loads(message)
            print("Message: " + str(message_json[0]['text_id']))
            return message_json[0]['text_id']

    #End current conversation
    def endConversation(self):
        response = requests.delete(self.url + '/bot/match', headers={"X-Session-Token": self.session})
        print(response.text)