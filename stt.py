from os import path, environ
from pydub import AudioSegment

def transcribe_file(speech_file):
    from google.cloud import speech
    import io

    if ".mp3" in speech_file:
        sound = AudioSegment.from_mp3(speech_file)
        sound.export(speech_file[:-4] + ".wav", format="wav")

    client = speech.SpeechClient()

    with io.open(speech_file, "rb") as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        language_code="en-US",
    )

    response = client.recognize(config=config, audio=audio)

    response_string = ""
    for result in response.results:
       response_string += result.alternatives[0].transcript

    return response_string

print(transcribe_file('resources/0703.wav'))
