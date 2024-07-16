import telebot
from telebot import types
BASKET=[]
bot_key = open("telebot.key","r").readline()
print("token:",bot_key)

bot = telebot.TeleBot(bot_key[:-1])

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id , "Введите пароль")
    bot.register_next_step_handler_by_chat_id(message.chat.id, sendPass)

@bot.message_handler(func=lambda message:message.text==True)
def sendPass(message):
 if message.text.lower() == "конь":
    foto = open('DSCF2623.jpg','rb')
    bot.send_document(message.chat.id, foto)
        
 else:
    start(message)

# def password(message):
#     if bot.message_handler(func=lambda message: message.text.lower() == "конь"):
#      bot.send_message(message.chat.id ,"Добро пожаловать в таверну ВУ! Здесь ты можешь заказать поесть! \n Введите /deserts - и я пришлю каталог десертов.\n Введите /food - и я пришлю каталог еды. ")
#     else:
#      start()


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
    button6 = types.KeyboardButton("НАЗАД")

    keyboard.add (button1,button2,button3,button4,button5,button6)
    bot.send_message(message.chat.id ,"Выберайте!",reply_markup=keyboard)

# @bot.message_handler(func=lambda message: message.text==True)
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
def answerBASKET(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=2)
    button1 = types.KeyboardButton("ОТПРАВИТЬ ЗАКАЗ")
    button2 = types.KeyboardButton("НАЗАД")
    SORTED_BASKET = {}

    answer = "Позиции в вашей корзине: \n"

    for item in BASKET:
            if item in SORTED_BASKET:
                SORTED_BASKET[item] += 1
            else:
                SORTED_BASKET[item] = 1
        # print(SORTED_BASKET)
        # print(list(SORTED_BASKET.items()))

    for (key,value) in list(SORTED_BASKET.items()):

         answer += f" - {key} x {value} \n"

    keyboard.add (button1,button2)
    bot.send_message(message.chat.id, answer,reply_markup=keyboard) 

@bot.message_handler(func=lambda message: message.text=="ОТПРАВИТЬ ЗАКАЗ")
def sendOrder(message):
        SORTED_BASKET = {}

        answer = "Позиции в вашей корзине: \n"

        for item in BASKET:
            if item in SORTED_BASKET:
                SORTED_BASKET[item] += 1
            else:
                SORTED_BASKET[item] = 1
        # print(SORTED_BASKET)
        # print(list(SORTED_BASKET.items()))

        for (key,value) in list(SORTED_BASKET.items()):

         answer += f" - {key} x {value} \n"

        bot.send_message("-1002223170132", answer)

@bot.message_handler(func=lambda message: message.text=="НАЗАД")
def answerBACK(message):
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
