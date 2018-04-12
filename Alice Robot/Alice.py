"""
Use example code if you want to use the Zora robot

1 - You will need to install Python 2.7 - 32 bits (be sure that it is the 32 bits version)
    You can find the installer here: https://www.python.org/downloads/release/python-2714/
2 - After installing Python, install the naoqi executable also in Library: pynaoqi-python-2.7-naoqi-x.x-win32.exe
3 - Everything should work if you run Alice.py.
"""

import time
import json
from Zora import Zora


class Alice:
    def __init__(self):
        self.answers = []

        # This depends on what Zora robot you have. Make sure the robot is connected (through UTP-cable).
        self.ZORA_IP = "169.254.58.192"
        # self.ZORA_IP = "169.254.132.185"   # Other Zora robot (of the two) IP. So if you can't connect, uncomment this

        print("Starting Program for Alice")
        # Connect to Zora
        self.zora = Zora(self)

        self.run()

    def run(self):
        self.zora.talk("Hey, I can talk.")
        self.conversation()
        self.stand()

    def conversation(self):
        self.zora.talk("I will ask a question. You can answer me by responding with yes or no. Are you ready?")
        self.recognizedWord = ""
        self.zora.recognize()
        self.answers = self.recognizedWord
        print(self.recognizedWord)
        if self.answers == "yes":
            self.zora.talk("You said yes")
        elif self.answers == "no":
            self.zora.talk("You said no")
        else:
            self.zora.talk("I didn't hear you say anything.")

    def stand(self):
        # Find more at: http://doc.aldebaran.com/2-1/naoqi/motion/alrobotposture.html
        self.zora.goToPosture("Stand", 1.0)


Alice()
