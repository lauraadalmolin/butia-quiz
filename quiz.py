import argparse
from search import answer_question
from stt import transcribe_file

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--files', nargs='+',
                    help='Please inform the name of the audio files separated by a space', required=True)

audio_files = vars(parser.parse_args())["files"]

for audio_file in audio_files:
    print('+------------------------------------------------------------------------------+')
    print('| Processing audio file...                                                     |')
    question = transcribe_file(audio_file)
    print('| ---------------------------------------------------------------------------- |')
    print('| Your question was:                                                           |')
    print('| {:s}'.format(question))
    print('| ---------------------------------------------------------------------------- |')
    print('| Let me think...                                                              |')
    answer = answer_question(question)
    print('|                                                                              |')
    print('| -> {:s}'.format(answer))
    print('+------------------------------------------------------------------------------+')