import telebot
from telebot import types
BASKET=[]
bot_key = open("telebot.key","r").readline()
print("token:",bot_key)

bot = telebot.TeleBot(bot_key[:-1])

@bot.message_handler(commands=["start"])
def start(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=2)
    button1 = types.KeyboardButton("Хочу Завтрак")
    button2 = types.KeyboardButton("Хочу Обед") 
    

    keyboard.add (button1,button2)

    bot.send_message(message.chat.id ,"Добро пожаловать в таверну ВУ! Здесь ты можешь заказать поесть! \n Введите /deserts - и я пришлю каталог десертов.\n Введите /food - и я пришлю каталог еды. ",reply_markup=keyboard)

@bot.message_handler(commands=['deserts'])
def giveMenu(message):
    f = open('deserts.pdf','rb')
    bot.send_document(message.chat.id, f)


@bot.message_handler(commands=['food'])
def giveMenu(message):
    f = open('food.pdf','rb')
    bot.send_document(message.chat.id, f)

@bot.message_handler(func=lambda message: message.text=="Хочу Завтрак")
def answerBREAKFEST(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=2)
    button1 = types.KeyboardButton("Яичница")
    button2 = types.KeyboardButton("Овсянка") 
    button3 = types.KeyboardButton("Мюсли с молоком") 
    button4 = types.KeyboardButton("Фритата")
    button5 = types.KeyboardButton("КОРЗИНА")

    keyboard.add (button1,button2,button3,button4,button5)
    bot.send_message(message.chat.id ,"Выберайте!",reply_markup=keyboard)

# @bot.message_handler(func=lambda message: message.text== )
# def answerSTR(message):
#     keyboard = types.ReplyKeyboardMarkup(row_width=2)
#     button1 = types.KeyboardButton("Яичница")
#     button2 = types.KeyboardButton("Овсянка") 
#     button3 = types.KeyboardButton("Мюсли с молоком") 
#     button4 = types.KeyboardButton("Фритата")
#     button5 = types.KeyboardButton("КОРЗИНА")

#     global BASKET
#     BASKET.append(message.text)

#     keyboard.add (button1,button2,button3,button4,button5)
#     bot.send_message(message.chat.id ,"Ещё что-то?",reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text=="Яичница" or message.text=="Овсянка" or message.text=="Мюсли с молоком" or message.text=="Фритата")
def answerBREAKFESTIN(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=2)
    button1 = types.KeyboardButton("Яичница")
    button2 = types.KeyboardButton("Овсянка") 
    button3 = types.KeyboardButton("Мюсли с молоком") 
    button4 = types.KeyboardButton("Фритата")
    button5 = types.KeyboardButton("КОРЗИНА")
    button6 = types.KeyboardButton("НАЗАД")
    global BASKET
    BASKET.append(message.text)

    keyboard.add (button1,button2,button3,button4,button5,button6)
    bot.send_message(message.chat.id,"Ещё что-то?", reply_markup=keyboard)   

@bot.message_handler(func=lambda message: message.text=="КОРЗИНА")
def answerBASKETBREAKFEST(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=2)
    button1 = types.KeyboardButton("Яичница")
    button2 = types.KeyboardButton("Овсянка") 
    button3 = types.KeyboardButton("Мюсли с молоком") 
    button4 = types.KeyboardButton("Фритата")
    button5 = types.KeyboardButton("КОРЗИНА")
    button6 = types.KeyboardButton("НАЗАД")

    keyboard.add (button1,button2,button3,button4,button5,button6)
    bot.send_message(message.chat.id, f"{BASKET}",reply_markup=keyboard) 

@bot.message_handler(func=lambda message: message.text=="НАЗАД")
def start(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=2)
    button1 = types.KeyboardButton("Хочу Завтрак")
    button2 = types.KeyboardButton("Хочу Обед") 
    button3 = types.KeyboardButton("КОРЗИНА")
    button4 = types.KeyboardButton("Очистить Корзину")

    keyboard.add (button1,button2,button3,button4)
    bot.send_message(message.chat.id ,"Добро пожаловать в таверну ВУ! Здесь ты можешь заказать поесть! ",reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text=="Хочу Обед")
def answerLANCH(message):

    keyboard = types.ReplyKeyboardMarkup(row_width=2)
    button1 = types.KeyboardButton("Паста Феттучини")
    button2 = types.KeyboardButton("Стейк Рибай") 
    button3 = types.KeyboardButton("Лосось на гриле") 
    button4 = types.KeyboardButton("Запеканка из шпината")
    button5 = types.KeyboardButton("КОРЗИНА")
    button6 = types.KeyboardButton("НАЗАД")

    keyboard.add (button1,button2,button3,button4,button5,button6)
    bot.send_message(message.chat.id,"Выбирайте!", reply_markup=keyboard) 


@bot.message_handler(func=lambda message: message.text=="Паста Феттучини" or message.text=="Стейк Рибай" or message.text=="Лосось на гриле" or message.text=="Запеканка из шпината")
def answerBREAKFESTIN(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=2)
    button1 = types.KeyboardButton("Паста Феттучини")
    button2 = types.KeyboardButton("Стейк Рибай") 
    button3 = types.KeyboardButton("Лосось на гриле") 
    button4 = types.KeyboardButton("Запеканка из шпината")
    button5 = types.KeyboardButton("КОРЗИНА")
    button6 = types.KeyboardButton("НАЗАД")
    global BASKET
    BASKET.append(message.text)

    keyboard.add (button1,button2,button3,button4,button5,button6)
    bot.send_message(message.chat.id,"Ещё что-то?", reply_markup=keyboard)  

@bot.message_handler(func=lambda message: message.text=="Очистить Корзину")
def CLEAN(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=2)
    button1 = types.KeyboardButton("Хочу Завтрак")
    button2 = types.KeyboardButton("Хочу Обед") 
    global BASKET
    BASKET.clear()

    keyboard.add (button1,button2)

    bot.send_message(message.chat.id ,"Ваша КОРЗИНА пуста!",reply_markup=keyboard)

bot.polling()
