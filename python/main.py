import telebot 
from decouple import config 
BOT_TOKEN = config('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)
greetings = ["hi", "hello", "hey", "greetings","سلام عليكم","أهلا"]
@bot.message_handler(commands=["start","help"])
def welcom(message):
    bot.send_message(message.chat.id,"welcome to hichem bot")
def  ismag(message):
      return True 
@bot.message_handler(func=ismag)
def reply(message):
    words = message.text.split()
    
    if words[0].lower() in greetings :
        return  bot.reply_to(message,"welcome,مرحبا بك")
    else:
        return  bot.reply_to(message,"that 's not a command of mine !")
    
    
bot.polling()
