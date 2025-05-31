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

def sendPass(message):
 if message.text.lower() == "конь":
    bot.send_message(message.chat.id ,"Добро пожаловать в таверну ВУ! Здесь ты можешь заказать поесть! \n Введите /deserts - и я пришлю каталог десертов.\n Введите /food - и я пришлю каталог еды. ")
        
 else:
    bot.send_message(message.chat.id , "еще разок и у тебя получится...")
    start(message)

def afterPass(message) :
  bot.send_message(message.chat.id ,"Добро пожаловать в таверну ВУ! Здесь ты можешь заказать поесть! \n Введите /deserts - и я пришлю каталог десертов.\n Введите /food - и я пришлю каталог еды. ")   
  keyboard = types.InlineKeyboardMarkup(row_width=1)
  button1 = types.InlineKeyboardButton("СДЕЛАТЬ ЗАКАЗ",callback_data='СДЕЛАТЬ ЗАКАЗ')
  keyboard.add (button1)
  bot.send_document(message.chat.id,reply_markup=keyboard)

@bot.message_handler(commands=['deserts'])
def giveMenu(message):
    f = open('deserts.pdf','rb')
    # bot.send_document(message.chat.id, f,reply_markup=keyboard)
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton("СДЕЛАТЬ ЗАКАЗ",callback_data='СДЕЛАТЬ ЗАКАЗ')
    button2 = types.InlineKeyboardButton("ПРИСЛАТЬ МЕНЮ ЕДЫ",callback_data='ПРИСЛАТЬ МЕНЮ ЕДЫ')
    keyboard.add (button1,button2)
    bot.send_document(message.chat.id, f,reply_markup=keyboard)
    # bot.send_message(message.chat.id ,"Что быдем делать дальше?", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
 if call.message:
   if call.data=='СДЕЛАТЬ ЗАКАЗ':
      bot.send_message(call.message.chat.id ,"ВВЕДИТЕ ДАТУ НА КОТОРУЮ ВЫ ХОТИТЕ СДЕЛАТЬ ЗАКАЗ")
      bot.register_next_step_handler_by_chat_id(call.message.chat.id,addDate)

   elif call.data=='ПРИСЛАТЬ МЕНЮ ЕДЫ':
     f = open('food.pdf','rb')
     bot.send_document(call.message.chat.id, f)

@bot.message_handler(commands=['food'])
def giveMenu(message):
    f = open('food.pdf','rb')
    bot.send_document(message.chat.id, f)
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton("СДЕЛАТЬ ЗАКАЗ",callback_data='СДЕЛАТЬ ЗАКАЗ')
    button2 = types.InlineKeyboardButton("ПРИСЛАТЬ МЕНЮ ДЕСЕРТОВ",callback_data='ПРИСЛАТЬ МЕНЮ ДЕСЕРТОВ')
    keyboard.add (button1,button2)
    bot.send_message(message.chat.id ,"Что будем делать дальше?", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
 if call.message:
   if call.data=='СДЕЛАТЬ ЗАКАЗ':
      bot.send_message(call.message.chat.id ,"ВВЕДИТЕ ДАТУ НА КОТОРУЮ ВЫ ХОТИТЕ СДЕЛАТЬ ЗАКАЗ")
      bot.register_next_step_handler_by_chat_id(call.message.chat.id,addDate)

   elif call.data=='ПРИСЛАТЬ МЕНЮ ДЕСЕРТОВ':
       f = open('deserts.pdf','rb')
       bot.send_message(call.message.chat.id ,f)
    # keyboard = types.ReplyKeyboardMarkup(row_width=2)
    # button1 = types.KeyboardButton("Хочу Завтрак")
    # button2 = types.KeyboardButton("Хочу Обед")
    
    # keyboard.add (button1,button2)
    # bot.send_message(message.chat.id ,"Выберайте!",reply_markup=keyboard)

# @bot.message_handler(func=lambda message: message.text=="Хочу Завтрак")
# def answerBREAKFEST(message):
#     keyboard = types.ReplyKeyboardMarkup(row_width=2)
#     button1 = types.KeyboardButton("Яичница")
#     button2 = types.KeyboardButton("Овсянка") 
#     button3 = types.KeyboardButton("Мюсли с молоком") 
#     button4 = types.KeyboardButton("Фритата")
#     button5 = types.KeyboardButton("КОРЗИНА")
#     button6 = types.KeyboardButton("НАЗАД")

#     keyboard.add (button1,button2,button3,button4,button5,button6)
#     bot.send_message(message.chat.id ,"Выберайте!",reply_markup=keyboard)

#     global BASKET
#     BASKET.append(message.text)

#     keyboard.add (button1,button2,button3,button4,button5)
#     bot.send_message(message.chat.id ,"Ещё что-то?",reply_markup=keyboard)

# @bot.message_handler(func=lambda message: message.text=="Яичница" or message.text=="Овсянка" or message.text=="Мюсли с молоком" or message.text=="Фритата")
# def answerBREAKFESTIN(message):
#     keyboard = types.ReplyKeyboardMarkup(row_width=2)
#     button1 = types.KeyboardButton("Яичница")
#     button2 = types.KeyboardButton("Овсянка") 
#     button3 = types.KeyboardButton("Мюсли с молоком") 
#     button4 = types.KeyboardButton("Фритата")
#     button5 = types.KeyboardButton("КОРЗИНА")
#     button6 = types.KeyboardButton("НАЗАД")

@bot.message_handler(func=lambda message: message.text=="СДЕЛАТЬ ЗАКАЗ")
def makeOrder(message):
    bot.send_message(message.chat.id , "ВВЕДИТЕ ДАТУ НА КОТОРУЮ ВЫ ХОТИТЕ СДЕЛАТЬ ЗАКАЗ:")
    bot.register_next_step_handler_by_chat_id(message.chat.id, addDate)
def addDate(message):
    global BASKET
    BASKET.append(message.text)
    bot.send_message(message.chat.id , "ВВЕДИТЕ АДРЕС ВАШЕЙ ТОРГОВОЙ ТОЧКИ:")
    bot.register_next_step_handler_by_chat_id(message.chat.id, addAdress)
def addAdress(message):
    global BASKET
    BASKET.append(message.text)
    bot.send_message(message.chat.id , "ВВЕДИТЕ НАЗВАНИЕ ВАШЕЙ ТОРГОВОЙ ТОЧКИ:")
    bot.register_next_step_handler_by_chat_id(message.chat.id, addNameTT)
def addNameTT(message):   
    global BASKET
    BASKET.append(message.text)
    bot.send_message(message.chat.id , "ВВЕДИТЕ ТЕЛЕФОН ДЛЯ СВЯЗИ:")
    bot.register_next_step_handler_by_chat_id(message.chat.id, addPhoneNumber)
def addPhoneNumber(message):   
    global BASKET
    BASKET.append(message.text)
    bot.send_message(message.chat.id , "Готово! \n Теперь вы можете написать ваш заказ \n Вот вам пример: \n - Cэндвич с курицей - 5 \n - Цезарь ролл с креветкой - 5 \n - Наполеон веган - 5 \n - Маффины с черникой 4 \n \n Напоминаю, что некотрые позиции такие как мафины и кексы заказываются только кратно 4шт")
    bot.register_next_step_handler_by_chat_id(message.chat.id, addORDER)
def addORDER(message):   
    global BASKET
    BASKET.append(message.text)
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton('ОТПРАВИТЬ ЗАКАЗ',callback_data='ОТПРАВИТЬ ЗАКАЗ')
    button2 = types.InlineKeyboardButton("ПОСМОТРЕТЬ ЗАКАЗ",callback_data='ПОСМОТРЕТЬ ЗАКАЗ')
    keyboard.add (button1,button2)
    bot.send_message(message.chat.id ,"Я оформил ваш заказ!\n Что будем делать дальше?", reply_markup=keyboard)

   
    
@bot.callback_query_handler(func=lambda call: call.data in ["ПОСМОТРЕТЬ ЗАКАЗ", "ОТПРАВИТЬ ЗАКАЗ"])
def callbackto(call):
    if call.data == 'ПОСМОТРЕТЬ ЗАКАЗ':
        bot.send_message(call.message.chat.id, str(BASKET))
    elif call.data == 'ОТПРАВИТЬ ЗАКАЗ':
        bot.send_message(call.message.chat.id, "Заказ отправлен!")
   
# @bot.message_handler(func=lambda message: message.text=="ПОСМОТРЕТЬ ЗАКАЗ" or "ОТПРАВИТЬ ЗАКАЗ" )
# def callbackto(call):

#  if call.message:
#   if call.data =='ПОСМОТРЕТЬ ЗАКАЗ':  
#     # SORTED_BASKET = {}  # Создаем пустую корзину в виде словаря
#     #answer = print(list(BASKET))
#     bot.send_document(call.message.chat.id, str(BASKET))
    # while True:
    #     item = input("Введите название товара и количество через пробел (или 'стоп' для выхода): ")
    #     if item.lower() == 'стоп':
    #         break  # Завершаем ввод, если пользователь ввел 'стоп'
    
    #     parts = item.rsplit(" ", 1)
    #     if len(parts) == 2 and parts[1].isdigit():
    #         item_name, quantity = parts[0], int(parts[1])
    #     else:
    #         item_name, quantity = item, 1  # Если количество не указано, берем 1
    
    #     if item_name in SORTED_BASKET:
    #          SORTED_BASKET[item_name] += quantity # Увеличиваем количество, если товар уже есть в корзине
    #          bot.send_message(call.message.chat_id,f"Товар '{item_name}' добавлен в корзину! Количество: {SORTED_BASKET[item_name]}") 
    #     else:
    #          SORTED_BASKET[item_name] = quantity
    #          bot.send_message(call.message.chat_id,f"Товар '{item_name}' добавлен в корзину! Количество: {SORTED_BASKET[item_name]}")    
    # bot.send_message(call.message.chat_id("\nВаши товары в корзине:"))
    # for i, (product, quantity) in enumerate(SORTED_BASKET.items(), 1):
    #     bot.send_message(call.message.chat_id (f"{i}. {product} - {quantity} шт."))  

    # for (key,value) in list(SORTED_BASKET.items()):

    #     answer += f"  {key}  \n"      
    #     bot.send_message(call.chat.id,answer) 

#  elif call.data=='ОТПРАВИТЬ ЗАКАЗ':  
    # SORTED_BASKET = {}
    # answer = "Позиции в вашей корзине: \n"
    # for item in BASKET:
    #  if item in SORTED_BASKET:
    #     SORTED_BASKET[item] +=1
    #     print(SORTED_BASKET)
    #  else:
    #     SORTED_BASKET[item] = 1
    #     print(SORTED_BASKET)
    #     print(list(SORTED_BASKET.items()))

    # for (key,value) in list(SORTED_BASKET.items()):
    #     answer += f" {key}  \n"
    #     bot.send_message("-1002223170132", answer)
    #     bot.send_message(call.chat.id, "Ваш заказ принят! Спасибо что выбрали наш ресторан!")

# @bot.message_handler(func=lambda message: message.text=="НАЗАД")
# def answerBACK(message):
#  bot.send_message(message.chat.id ,"Добро пожаловать в таверну ВУ! Здесь ты можешь заказать поесть! \n Введите /deserts - и я пришлю каталог десертов.\n Введите /food - и я пришлю каталог еды. ")   
    
    # keyboard = types.ReplyKeyboardMarkup(row_width=2)
    # button1 = types.KeyboardButton("Хочу Завтрак")
    # button2 = types.KeyboardButton("Хочу Обед") 
    # button3 = types.KeyboardButton("КОРЗИНА")
    # button4 = types.KeyboardButton("Очистить Корзину")

    # keyboard.add (button1,button2,button3,button4)
    # bot.send_message(message.chat.id ,"Добро пожаловать в таверну ВУ! Здесь ты можешь заказать поесть! ",reply_markup=keyboard)

# @bot.message_handler(func=lambda message: message.text=="Хочу Обед")
# def answerLANCH(message):

#     keyboard = types.ReplyKeyboardMarkup(row_width=2)
#     button1 = types.KeyboardButton("Паста Феттучини")
#     button2 = types.KeyboardButton("Стейк Рибай") 
#     button3 = types.KeyboardButton("Лосось на гриле") 
#     button4 = types.KeyboardButton("Запеканка из шпината")
#     button5 = types.KeyboardButton("КОРЗИНА")
#     button6 = types.KeyboardButton("НАЗАД")

#     keyboard.add (button1,button2,button3,button4,button5,button6)
#     bot.send_message(message.chat.id,"Выбирайте!", reply_markup=keyboard) 


# @bot.message_handler(func=lambda message: message.text=="Паста Феттучини" or message.text=="Стейк Рибай" or message.text=="Лосось на гриле" or message.text=="Запеканка из шпината")
# def answerBREAKFESTIN(message):
#     keyboard = types.ReplyKeyboardMarkup(row_width=2)
#     button1 = types.KeyboardButton("Паста Феттучини")
#     button2 = types.KeyboardButton("Стейк Рибай") 
#     button3 = types.KeyboardButton("Лосось на гриле") 
#     button4 = types.KeyboardButton("Запеканка из шпината")
#     button5 = types.KeyboardButton("КОРЗИНА")
#     button6 = types.KeyboardButton("НАЗАД")
#     global BASKET
#     BASKET.append(message.text)

    # keyboard.add (button1,button2,button3,button4,button5,button6)
    # bot.send_message(message.chat.id,"Ещё что-то?", reply_markup=keyboard)  

# @bot.message_handler(func=lambda message: message.text=="УДАЛИТЬ")
# def CLEAN(message):
#     keyboard = types.ReplyKeyboardMarkup(row_width=2)
#     button1 = types.KeyboardButton("Хочу Завтрак")
#     button2 = types.KeyboardButton("Хочу Обед") 
#     global BASKET
#     BASKET.clear()

#     keyboard.add (button1,button2)
bot.polling()