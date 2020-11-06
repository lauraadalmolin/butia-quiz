from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk
import string
# nltk.download('stopwords')
# nltk.download('punkt')


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

    return merge_question_array(filtered_sentence)


def merge_question_array(question_array):
    question = ''
    for word in question_array:
        question = question + word
    return question