import time
from naoqi import ALProxy
from naoqi import ALModule

ZORA_IP = "169.254.58.192"
check = 0

# Creates a proxy on the speech-recognition module
asr = ALProxy("ALSpeechRecognition", ZORA_IP, 9559)
mem = ALProxy("ALMemory", ZORA_IP, 9559)


class myModule(ALModule):
    def pythondatachanged(self, strVarName, value):
        """callback when data change"""
        print "datachanged", strVarName, " ", value
        global check
        check = 1

    def _pythonPrivateMethod(self, param1, param2, param3):
        global check


asr.setLanguage("English")
vocabulary = ["yes", "no"]
asr.setVocabulary(vocabulary, False)

# Start the speech recognition engine with user Test_ASR
asr.subscribe("Test_ASR")
print 'Speech recognition engine started'
for i in range(0, 100):
    print(mem.getData("WordRecognized"))
    time.sleep(0.2)

asr.unsubscribe("Test_ASR")
