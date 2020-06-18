from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import logging
from flask import Flask, render_template, request


'''
This is an example showing how to train a chat bot using the
ChatterBot Corpus of conversation dialog.
'''

# Enable info level logging
logging.basicConfig(level=logging.INFO)

chatbot = ChatBot('Example Bot')

# Start by training our bot with the ChatterBot corpus data
trainer = ChatterBotCorpusTrainer(chatbot)

trainer.train(
    'chatterbot.corpus.english'
)
app = Flask(__name__)
# Now let's get a response to a greeting
response = chatbot.get_response('How are you doing today?')
print(response)
@app.route("/")
def home():    
    return render_template("home.html") 
@app.route("/get")
def get_bot_response():    
    userText = request.args.get('msg')    
    return str(chatbot.get_response(userText)) 
if __name__ == "__main__":    
    app.run(debug=True)