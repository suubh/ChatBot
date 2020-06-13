from chatterbot import ChatBot 
#from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

bot = ChatBot('Project1')

trainer = ChatterBotCorpusTrainer(bot)
#response=['How are you?','My name is Bot,I am created by Shubham.','I speak in Binary.',
#    'I live in a Memory.','I am fine.','In which city do you live ?.','What is your name?.',
#    'Nice to meet you.','Sorry I cant understand.','How can I help?.','hey, good to see you.', 'How may i assist you today?.',
#    'I am good.','Let us know about each other.','Yea sure, so what you wanna talk.','Whats your favourite food?.',
#    'That is good to hear.','What are your Hobbies?.','Nice.',
#    'Thank you.',
#    'You are welcome.','Bye.']

trainer.train(
    "chatterbot.corpus.english.conversations"
)
   
trainer.export_for_training('./my_export.json')



print("Welcome to Project1 Bot")
while True:
    ask_bot=input()
    if ask_bot=='Bye':
        break
    answer=bot.get_response(ask_bot)
    print("Bot:",answer)

   

