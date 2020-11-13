from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from Levenshtein import distance
import nltk
import string
import json
# nltk.download('stopwords')
# nltk.download('punkt')

with open('questions/all_questions.json') as json_file:
    all_questions = json.load(json_file)["questions"]

def pre_process_question(question):
    # removes punctuation
    question = question.replace('\'s', ' is')
    question = question.replace('n\'t', ' not')
    question = question.replace('\'ll', ' will')
    question = question.replace('\'ve', ' have')

    question = ' '.join(word.strip(string.punctuation)
                        for word in question.split())

    stop_words = set(stopwords.words('english'))

    word_tokens = word_tokenize(question)

    filtered_sentence = [w for w in word_tokens if not w in stop_words]

    return merge_question_array(filtered_sentence), filtered_sentence

def merge_question_array(question_array):
    question = ''
    for word in question_array:
        question = question + word
    return question

def find_question(question, questions=all_questions):

    question, _ = pre_process_question(question)
    question = question.lower()
    l_distances = []
    for index, file_question in enumerate(questions):
        merged_file_question = merge_question_array(file_question['question_array']).lower()
        l_distances.append({'distance': distance(merged_file_question, question),'index': index})
    
    min_distance = l_distances[0]

    for i in range(1, len(l_distances)):
        if l_distances[i]['distance'] < min_distance['distance']:
            min_distance = l_distances[i]
    
    if min_distance['distance'] > 5:
        return {'question': '', 'question_array': []}

    question_obj = questions[min_distance['index']]

    return question_obj
    
def generate_questions_json(files, output_file):
    data = {}
    data['questions'] = []
    for doc in files:
        handler = open(doc, 'r')
        lines = handler.readlines()
        for line in lines:
            _, filtered_sentence = pre_process_question(line)
            data['questions'].append({
                'question': line,
                'question_array': filtered_sentence
            })

    with open(output_file, 'w') as outfile:
        json.dump(data, outfile)
        

if __name__ == '__main__':
    import json
    
    generate_questions_json([
        'questions/2020_complex.txt',
        'questions/2020_simple.txt'
    ], 'questions/all_questions.json')

