'''

Use example code if you want to use the Zora robot

1 - You will need to install Python 2.7 - 32 bits (be sure that it is the 32 bits version)
    You can find the installer here: https://www.python.org/downloads/release/python-2714/
2 - After installing Python, install the naoqi executable also in Library: pynaoqi-python-2.7-naoqi-x.x-win32.exe

'''

import time
import json
from APIConnector import APIConnector
from Zora import Zora


class Alice:
    def __init__(self):
        self.answers = []

        # This depends on what Zora robot you have. Make sure the robot is connected (through UTP-cable).
        ALICE_NUMBER = "alice1"
        self.ZORA_IP = "169.254.58.192"

        # ALICE_NUMBER = "alice2"
        # self.ZORA_IP = "169.254.58.192"

        print("Starting Program for Alice 1")

        # Stored credentials
        self.creds = json.load(open('information.json'))
        # Connect to the API with the given credentials
        self.api = APIConnector(username=self.creds[ALICE_NUMBER]['username'],
                                password=self.creds[ALICE_NUMBER]['password'])
        # Connect to Zora
        self.zora = Zora(self)

        self.run()

    def run(self):
        self.zora.talk("Hey, I can talk.")
        self.onboarding()

    def onboarding(self):
        self.zora.talk("Now I will ask a question. You can react to this question by responding with yes or no.")
        for i, item in enumerate(self.creds["onboarding"]):
            self.recognizedWord = ""
            self.zora.recognize()
            self.answers = self.recognizedWord
            print(self.recognizedWord)

Alice()