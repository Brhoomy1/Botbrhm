import telebot
from telebot import types 

private = "6806056786:AAHaiz8hqzcikvbx-Ry-i2iEotEcwV4rfAw"
bot = telebot.TeleBot(private)
is_bot_active = True #التشغيل 

bot.set_my_commands([telebot.types.BotCommand("/start", "🤖 Start Bot")]) 

@bot.message_handler(commands=['start'])
def start(message):
        bot.reply_to(message, "• 👋 مرحبا بك عزيزي في بوت الايدي ارسل 〈 /ID 〉 للحصول علا الايدي") 

@bot.message_handler(func=lambda message: True)
def id(message):
    bot.reply_to(message, "• 𝗬𝗼𝘂𝗿 𝗜𝗗 : " + str(message.chat.id))

print("running") 
bot.polling(True)
#لبوت لغرض تعليم مقدم من @termuxpp
#قناة @termuxpp 