# Digital Days 2018 Hackathon

Welcome to the documentation for the Digital Days 2018 Hackathon. As you all heard the goal for this hackathon is to develop a new use-case for the Alice project. This Github repository will provide you with documentation and code examples to get you started.


# Services to use

TBA

# Code Examples

To help you get started with developing artificial intelligence, some code examples are provided. The following examples are provided:

File  | Explanation
------------- | -------------
Google_Text_To_Speech.py  | Code to make an API request to the Text-To-Speech service.
Google_Speech_To_Text.py  | Code to make an API request to the Speech Recognition service. The example records for X seconds and sends that to the cloud.
Google_Vision_API.py | Code to make an API request to the Vision API. The API can be used to recognied images.
IBM_Watson_Assistant.py | Code to implement a IBM Watson Assistant workspace in Python.
Dialogflow.py | Code to implement a DialogFlow agent in Python.

Alice Robot/Alice.py | If you are using one of the robots, this folder is available with some example code. See Alice.py for more explanation.

# Starting the ZORA Robots

Two ZORA robots will be available at the hackathon for teams to use. In order to use the robots, we first need to start to the robot. To start the robot, press the big button in the center until it lights up. After that we can connect to the robots network. This can be done with an Ethernet cable or through Wi-Fi. Using an Ethernet cable is recommended since you can connect to Wi-Fi/4G simultaneously. 

The ZORA robot needs some time to boot (approximately 10 minutes) before it can be used. You will know that the robot is ready for use when it starts saying "Hi, my name is Alice. My internet adress is X.X.X.X". Depending on the volume settings, it could be quite silent. If everything is connected you can now go to this adress and you wil see a portal.

In this portal you can start some pre-installed programs and try-out some of the robots functionalities like changing posture, text-to-speech and speech recognition.

# Developing for ZORA

SDKs are available in for Python, C++, Java and JavaScript. Since the development team for Alice uses Python, code examples in the repository will be in Python. An overview of all SDKs can be found here: [http://doc.aldebaran.com/2-5/dev/programming_index.html](url). 

Since nobody likes to create user accounts, the folder "Library" contains an installer for the Python library.

**Note about Python versions: Make sure you use Python 2.7 - 32 bits. During development we had trouble with different versions.**

# Questions?

You can reach out to Laurens Schumacher, Bob van den Berg and Youri van der Zee for technical questions regarding the Zora Robots, Raspberry Pi and cloud.
