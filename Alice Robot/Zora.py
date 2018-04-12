import time
from naoqi import ALProxy
import qi


class Zora:

    def __init__(self, alice):
        self.alice = alice

        self.SENSITIVTY = 0.85      # The sensitivity of the microphone sensor.
        self.IP = alice.ZORA_IP
        self.session = qi.Session()
        self.session.connect(alice.ZORA_IP + ":9559")

        self.sr_service = self.session.service("ALSpeechRecognition")
        vocabulary = ["yes", "no"]
        self.sr_service.setVocabulary(vocabulary, False)

        self.tts_service = self.session.service("ALTextToSpeech")

        self.posture_service = self.session.service("ALRobotPosture")
        self.memory = self.session.service("ALMemory")
        self.ttsProxy = ALProxy("ALTextToSpeech", self.IP, 9559)
        self.postureProxy = ALProxy("ALRobotPosture", self.IP, 9559)
        self.sound_detect_service = self.session.service("ALSoundDetection")
        self.sound_detect_service.setParameter("Sensitivity", self.SENSITIVTY)

    def detectSound(self):
        print("DETECTING")
        self.sound_detect_service.subscribe("TEST_SOUND")
        subscriber = self.memory.subscriber("SoundDetected")
        subscriber.signal.connect(self.alice.onSoundDetected)
        time.sleep(3)
        self.sound_detect_service.unsubscribe("TEST_SOUND")
        print("STOPPING")

    def talk(self, sentence):
        self.tts_service.say(sentence)

    def goToPosture(self, posture):
        self.posture_service.goToPosture(posture, 1.0)

    def getPosture(self):
        print self.posture_service.getPostureFamily()
        return self.posture_service.getPostureFamily()

    def recognize(self):
        self.sr_service.subscribe("TEST_ASR")
        subscriber = self.memory.subscriber("WordRecognized")
        subscriber.signal.connect(self.alice.onReceivedWord)
        # SLEEP IS NEEDED, DUNNO WHY YET (because else it'll overwrite previous actions?)
        time.sleep(5)
        self.sr_service.unsubscribe("TEST_ASR")