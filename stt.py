from os import path, environ
from pydub import AudioSegment
from pseudo_nlp import find_question

def transcribe_file(speech_file):
    from google.cloud import speech
    import io

    if ".mp3" in speech_file:
        sound = AudioSegment.from_mp3(speech_file)
        sound = sound.set_channels(1)
        sound.export(speech_file[:-4] + ".wav", format="wav")
        speech_file = speech_file[:-4] + ".wav"

    client = speech.SpeechClient()

    with io.open(speech_file, "rb") as audio_file:
        content = audio_file.read()


    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        language_code="en-US"
    )

    response = client.recognize(config=config, audio=audio)
    
    response_string = ""
    for result in response.results:
       response_string += result.alternatives[0].transcript

    # print(response_string)

    # question_obj = find_question(response_string)
    # if question_obj != None:
    #     response_string = question_obj['question']

    return response_string