import argparse
from search import answer_question
from stt import transcribe_file
import os

def answer(question):
    print('| ---------------------------------------------------------------------------- |')
    print('| Your question was:                                                           |')
    print('| {:s}'.format(question))
    print('| ---------------------------------------------------------------------------- |')
    print('| Let me think...                                                              |')
    answer = answer_question(question)
    print('|                                                                              |')
    print('| -> {:s}'.format(answer))
    print('+------------------------------------------------------------------------------+')

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--files', nargs='+',
                    help='Please inform the name of the audio files separated by a space', required=False)

audio_files = vars(parser.parse_args())["files"]

if audio_files != None:
    for audio_file in audio_files:
        print('+------------------------------------------------------------------------------+')
        print('| Processing audio file...                                                     |')
        question = transcribe_file(audio_file)
        print('| Let me think...                                                              |')
        answer = answer_question(question)
        print('|                                                                              |')
        print('| -> {:s}'.format(answer))
        print('+------------------------------------------------------------------------------+')
else:
    exit = False
    print('+------------------------------------------------------------------------------+')
    print('| Hello and welcome to Doris Assistant...                                      |')
    print('| Remember that I only undestand non-abstract questions:                       |')
    print('+------------------------------------------------------------------------------+')
    while exit == False:
        print('+------------------------------------------------------------------------------+')
        print('| Please choose your option:                                                   |')
        print('| 1) Input your question as string                                             |')
        print('| 2) Input a path to your question as an .mp3 file                                  |')
        print('| 3) Exit                                                                      |')
        option = input('| -> ').strip()
        if option == '2':
            path = input('! Path: ').strip().lower()
            if os.path.exists(path):
                question = transcribe_file(path)
                answer(question)
            else:
                print('| -> Please inform a valid path                                                   |')
                print('+------------------------------------------------------------------------------+')
        elif option == '1':
            question = input('! Question: ').strip().lower()
            answer(question)
        elif option == '3':
            exit = True
            print('| Well, then... Goodbye! Thank you for stopping by :D                          |')
            print('+------------------------------------------------------------------------------+')
        else: 
            print('| Please inform a valid option                                                 |')
            print('+------------------------------------------------------------------------------+')
        
