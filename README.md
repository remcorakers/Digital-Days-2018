# Digital Days 2018 Hackathon

Welcome to the documentation for the Digital Days 2018 Hackathon. As you all heard the goal for this hackathon is to prototype a new use-case for the Alice project. This Github repository will provide documentation and code examples to help you get started.

# Introduction

During the Alice hackathon your team will come up with solution to the problem statement. During the hackathon all teams will try to build a first prototype of the solution. To help you get started with this, this repository contains documentation on how to get started with Artificial Intelligence.

# Services to use

Every team is free to use any kind of service, online platform and AI-technique in every (commonly used) programming language. However, the examples in this repository are in Python. We used the Google Cloud platform to do Text-To-Speech, Speech-To-Text and Image Recognition. At the start of the hackathon credentials to the Google Cloud platform will be provided. If you want to use other services during the Hackathon you can contact Joost Naaijen, Egemen Uzunali or Youri van der Zee. For other platforms you will have to create an account yourself.

# Code Examples

To help you get started with developing artificial intelligence, some code examples are provided. Most of the Google examples are inspired by this repository: https://github.com/GoogleCloudPlatform/python-docs-samples. The following examples are provided:

File  | Explanation
------------- | -------------
Google_Text_To_Speech.py  | Code to make an API request to the Text-To-Speech service.
Google_Speech_To_Text.py  | Code to make an API request to the Speech Recognition service. The example records for X seconds and sends that to the cloud.
Google_Vision_API.py | Code to make an API request to the Vision API. The API can be used to classify images.
Google_Streaming_SST.py | Code to stream audio to google for speech recognition. Currently only English works.
IBM_Watson_Assistant.py | Code to implement an IBM Watson Assistant workspace in Python.
Alice Robot/Alice.py | If you are using one of the robots, this folder is available with some example code. See Alice.py for more explanation.

The folder Chatbot_Example contains a very simple chatbot example made in Dialogflow. The example is used to help engineers understand how a chatbot retrieves context from a chat and how entities can be retrieved.

# Starting the ZORA Robots

Two ZORA robots will be available at the hackathon for teams to use. In order to use the robots, we first need to start to the robot. To start the robot, press the big button in the center until it lights up. After that we can connect to the robots network. This can be done with an Ethernet cable or through Wi-Fi. Using an Ethernet cable is recommended since you can connect to Wi-Fi/4G simultaneously. 

The ZORA robot needs some time to boot (approximately 10 minutes) before it can be used. You will know that the robot is ready for use when it starts saying "Hi, my name is Alice. My internet address is X.X.X.X". Depending on the volume settings, it could be quite silent. If everything is connected you can now go to this address and you will see a portal.

In this portal you can start some pre-installed programs and try-out some of the robots functionalities like changing posture, text-to-speech and speech recognition.

# Developing for ZORA

SDKs are available in for Python, C++, Java and JavaScript. Since the development team for Alice uses Python, code examples in the repository will be in Python. An overview of all SDKs can be found here: [http://doc.aldebaran.com/2-5/dev/programming_index.html](url). 

Since nobody likes to create user accounts, the folder "Library" contains an installer for the Python library.

**Note about Python versions: Make sure you use Python 2.7 - 32 bits. During development we had trouble with different versions.**

# Api keys
To get the api key for Google Cloud ask the slack bot @digital_days_bot in the Deloitte Digital slack team [ddnl.slack.com](ddnl.slack.com)
# Questions?

You can reach out to Laurens Schumacher, Bob van den Berg, Youri van der Zee and Joost Naaijen for technical questions regarding the Zora Robots, Google Cloud platform, IBM Watson or Dialogflow.
