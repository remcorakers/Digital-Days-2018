# Creates a proxy on the text-to-speech module
import time
from naoqi import ALProxy

ZORA_IP = "169.254.58.192"
tts = ALProxy("ALTextToSpeech", ZORA_IP, 9559)
print(tts.getAvailableVoices())


# Example: Sends a string to the text-to-speech module
tts.setVoice("Kenny22Enhanced")

tts.say("Hello!")
# time.sleep(1)
# tts.say("Hallo!")
# tts.setVoice("Julia22Enhanced")
# time.sleep(1)
# tts.say("Hallo!")
# tts.setVoice("Lulu22Enhanced")
# time.sleep(1)
# tts.say("Hallo!")
# tts.setVoice("Sanna22Enhanced")
# time.sleep(1)
# tts.say("Hallo!")
# tts.setVoice("maki_n16")
# time.sleep(1)
# tts.say("Hallo!")
# tts.setVoice("naoenu")