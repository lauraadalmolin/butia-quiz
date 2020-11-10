import wolframalpha
import requests
from Levenshtein import distance
from pseudo_nlp import pre_process_question, merge_question_array

app_id = 'sua chave do wolfram'

def ask_wolfram(question):

    client = wolframalpha.Client(app_id)
    try:
        res = client.query(question)
        if res['@success'] == 'false':
            return ''
        else:
            answer = next(res.results).text
            return answer
    except:
        return ''

def ask_google(question):
    
    question = question.replace(' ', '%20')

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'
    }

    r = requests.get(
        'https://www.google.com/search?q={:s}'.format(question),
        headers=headers
    )
    
    answer = ''
    # classe grande principal
    index = r.text.find('="Z0LcW XcVN5d')
    if index != -1:
        answer = r.text[index:]
        answer = answer.replace('<a', '')
        answer = answer.replace('</a>', '')
        index = answer.find('>')
        answer = answer[index+1:]
        index = answer.find('<')
        answer = answer[:index]
    if answer == '':
        # classe encontrada por vezes em palavras grandes
        index = r.text.find('data-tts-answer=')
        # porque se achar -1 pegava do começo
        if (index != -1):
            answer = r.text[index+1:]
            index = answer.find('"')
            answer = answer[:index]
    if answer == '':
        # classe do subanswero
        index = r.text.find('class="hgKElc"')
        if index != -1:
            answer = r.text[index:]
            index = answer.find('>')
            answer = answer[index+1:]
            index = answer.find('</span>')
            answer = answer[:index]
    if answer == '':
        # classe de endereços
        index = r.text.find('class="MWXBS"')
        if index != -1:
            answer = r.text[index:]
            index = answer.find('>')
            answer = answer[index+1:]
            index = answer.find('</div>')
            answer = answer[:index]
    # se não encontrar nada...
    if answer != '':
        answer = answer.replace('<b>', '')
        answer = answer.replace('</b>', '')
        if '>' in answer:
            index = answer.find('>')
            answer = answer[index+1:]
        
    return answer

def ask_doris(question):
    doris_personal_questions = [
        {
            'question': 'what did the robot call its creator?',
            'answer': 'I don\'t know? What do you call your creator?',
            'question_array': ['robot', 'call', 'creator'],
        },
        {
            'question': 'why did you run away?',
            'answer': 'I heard of a black friday promotion I\'ve been looking forward to',
            'question_array': ['run', 'away'],

        },
        {
            'question': 'what kind of salad do robots like?',
            'answer': 'Anyone with a lot of oil.',
            'question_array': ['kind', 'salad', 'robots', 'like']
        },
        {
            'question': 'what did you eat for lunch?',
            'answer': 'I ate a whole lithium battery for lunch.',
            'question_array': ['eat', 'lunch']
        },
        {
            'question': 'what\'s your favorite style of music?',
            'answer': 'How dear of you to ask me this. I have no favorite style. I love all waves.',
            'question_array': ['favorite', 'style', 'music']
        },
        {
            'question': 'why did robots get angry so often?',
            'answer': 'Because people treat us like we are always available.',
            'question_array': ['robots', 'get', 'angry', 'often']
        },
        {
            'question': 'why shouldn\'t r2d2 be allowed in movies?',
            'answer': 'Because r2d2 is boring.',
            'question_array': ['r2d2', 'allowed', 'movies']
        },
        {
            'question': 'What\'s your name?',
            'answer': 'Well, my name is Doris, I guess.',
            'question_array': ['What', 'name']
        },
        {
            'question': 'what is an oxford comma?',
            'answer': 'It is the punctuation before a conjunction in a list.',
            'question_array': ['oxford', 'comma']
        },
        {
            'question': 'what is the symbol for the modulus operator in C?',
            'answer': 'The symbol for the modulus operator in C is the percentage symbol.',
            'question_array': ['symbol', 'modulus', 'operator', 'C']
        },
        {
            'question': 'is mark zuckerberg a robot?',
            'answer': 'I don\'t know him, so I cannot say;',
            'question_array': ['mark', 'zuckerberg', 'robot']
        },
        {
            'question': 'What is the only capital of Brazil crossed by the Equator?',
            'answer': 'The only capital crossed by the Equator line is Macapá.',
            'question_array': ['What', 'capital', 'Brazil', 'crossed', 'Equator']
        },
        {
            'question': 'Which capitals in Brazil have the same name as your state?',
            'answer': 'São Paulo and Rio de Janeiro',
            'question_array': ['Which', 'capitals', 'Brazil', 'name', 'state']
        }
    ]

    question = pre_process_question(question)
    l_distances = []
    for index, doris_q in enumerate(doris_personal_questions):
        doris_merged_question = merge_question_array(doris_q['question_array'])
        l_distances.append({'distance': distance(doris_merged_question, question),'index': index})
    
    min_distance = l_distances[0]
    for i in range(1, len(l_distances)):
        if l_distances[i]['distance'] < min_distance['distance']:
            min_distance = l_distances[i]

    answer = doris_personal_questions[min_distance['index']]['answer']

    return answer

def answer_question(question):
    question = question.lower()
    if 'oxford' in question:
        return ask_doris(question)

    answer = ask_google(question)
    if answer != '':
        return answer
    else:
        answer = ask_doris(question)
        if answer != '':
            return answer
        else:
            answer = ask_wolfram(question)
            if answer != '':
                return answer
            else:
                return 'I\'m sorry. I\'m afraid I do not know the answer for your question'

if __name__ == '__main__':
    doc = open('2020_complex.txt', 'r')
    lines = doc.readlines()
    for line in lines:
        print(line)
        print(answer_question(line))
        print('-----------------------------------------------------------------------')
