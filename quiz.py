import wolframalpha

app_id = 'V3897X-4ELHA6XU53'

def answer_question(question):

    client = wolframalpha.Client(app_id)
    try:
        res = client.query(question)
        if res['@success'] == 'false':
            #search wikipedia
            
        else:
            answer = next(res.results).text
            return answer


question = input('Question: ')
