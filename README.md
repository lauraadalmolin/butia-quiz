## Instalação
----------

Primeiramente você precisa seguir o tutorial de cloud da google disponível [aqui](https://cloud.google.com/speech-to-text/docs/quickstart-client-libraries).

**Importante:** toda vez que abrir um novo terminal você precisará rodar o seguinte comando: 

`export GOOGLE_APPLICATION_CREDENTIALS="caminho_para_suas_credenciais"`

Antes de executar a primeira vez, execute o seguinte código: 

~~~
sudo apt install ffmpeg
pip3 install pydub
pip3 install nltk
pip3 install wolframalpha
pip3 install python-Levenshtein

~~~

## Execução
----------
Para executar o sistema, basta instalar todos os requirements e rodar:

~~~
python3 quiz.py -f 'nomedoarquivo'
~~~

Em 'nomedoarquivo', você deve informar o path para o arquivo de áudio (.mp3 ou .wav).
Na sua tela aparecerão a pergunta, extraída do áudio, e a resposta.

# Alguns problemas frequentes
---------
Talvez você precise executar os seguintes comandos:

~~~
nltk.download('stopwords')
nltk.download('punkt')
~~~

Essas duas linhas estão comentadas no arquivo pseudo_nlp.py. Se você encontrar algum erro relacionado aos termos 'stopwords' e 'punkt', experimente descomentá-las e rodar novamente.


