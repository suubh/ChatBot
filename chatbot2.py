from chatterbot import ChatBot 
from chatterbot.trainers import ListTrainer

bot_project=ChatBot('IEEE Bot')
trainer=ListTrainer(bot_project)
trainer.train(["Hi there!",
    "Hello",
    "How are you?",
    "I am good.",
    "That is good to hear.",
    "Thank you",
    "You are welcome.",
    "What is your name?",
    "My name is Bot_IEEE, I am created by Shubham",
    "Who are you?",
    "I am an Artificial Intelligence ,running on algorithms",
    "Which language you work on?",
    "I work on Python language",
    "Where do you live?",
    "I live in computers RAM",
    
   ])


print("Welcome to Project1 Bot")
while True:
    ask_bot=input()
    if ask_bot=='Bye':
        break
    answer=bot_project.get_response(ask_bot)
    print("Bot:",answer)
