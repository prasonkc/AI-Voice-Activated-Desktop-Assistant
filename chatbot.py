from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

with open("./Linux/human_text.txt", "r") as chat:
    data = chat.read().splitlines()

chatbot = ChatBot(
    'Doggo',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.sqlite3'
)

trainer = ListTrainer(chatbot)
trainer.train(data)


def respond(query):
    return str(chatbot.get_response(query))
