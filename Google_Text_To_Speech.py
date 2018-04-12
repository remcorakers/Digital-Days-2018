from google.cloud import texttospeech
import os
import io
import playsound

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "creds.json"
language = 'nl-NL'

client = texttospeech.TextToSpeechClient()

# [START tts_synthesize_text]
def synthesize_text(text):
    """Synthesizes speech from the input string of text."""
    from google.cloud import texttospeech
    client = texttospeech.TextToSpeechClient()

    input_text = texttospeech.types.SynthesisInput(text=text)

    # Note: the voice can also be specified by name.
    # Names of voices can be retrieved with client.list_voices().
    voice = texttospeech.types.VoiceSelectionParams(
        language_code=language)

    audio_config = texttospeech.types.AudioConfig(
        audio_encoding=texttospeech.enums.AudioEncoding.MP3,
    speaking_rate=0.75)

    response = client.synthesize_speech(input_text, voice, audio_config)

    # The response's audio_content is binary.
    file_path = 'output.mp3'
    with io.open(file_path, 'wb+') as out:
        out.write(response.audio_content)
        print('Audio content written to file "output.mp3"')
    playsound.playsound(file_path, True)
    os.remove(file_path)


# [START tts_synthesize_ssml]
def synthesize_ssml(ssml):
    """Synthesizes speech from the input string of ssml.
    Note: ssml must be well-formed according to:
        https://www.w3.org/TR/speech-synthesis/
    Example: <speak>Hello there.</speak>
    """
    from google.cloud import texttospeech
    client = texttospeech.TextToSpeechClient()

    input_text = texttospeech.types.SynthesisInput(ssml=ssml)

    # Note: the voice can also be specified by name.
    # Names of voices can be retrieved with client.list_voices().
    voice = texttospeech.types.VoiceSelectionParams(
        language_code=language)

    audio_config = texttospeech.types.AudioConfig(
        audio_encoding=texttospeech.enums.AudioEncoding.MP3,
    speaking_rate=0.75)


    response = client.synthesize_speech(input_text, voice, audio_config)

    # The response's audio_content is binary.
    file_path = 'output.mp3'
    with io.open(file_path, 'wb+') as out:
        out.write(response.audio_content)
        print('Audio content written to file "output.mp3"')
    playsound.playsound(response, True)
    os.remove(file_path)

text="Hoi, ik ben Alice"
ssml_text="<speak>Hoi Bob<break time='200ms' />" \
          "Met mij gaat het erg goed.</speak>"

synthesize_text(text)
