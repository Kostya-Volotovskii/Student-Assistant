import telebot
from telebot import types
import sqlite3
TOKEN = '5082922706:AAFlHjixJZ4fqbC7m7JpdglDnfTWKKgxd6o'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])

def start(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    Main_menu(keyboard)
    bot.send_message(message.chat.id, 'Привет, Человек! Меня зовут Student Assistant👋🤓\n\nЯ помогаю ответить студентам на вопросы о стипендии😉💵\n\nВыбери подходящую тему, а я приведу тебе список вопросов, которые тебе будут полезны😌', reply_markup = keyboard)

db = sqlite3.connect('server.db', check_same_thread=False)
sql = db.cursor()

Sec1 = 'Социальная стипендия'
Sec2 = 'Оформление соц. стипендии'
Sec3 = 'Виды стипендии и сроки получения'
Sec4 = 'Материальные выплаты'
Sec5 = 'Льготы'
Sec6 = 'Оформление карты для получения стипендий'

Ques1_1 = "Что такое социальная стипендия?" #24
Ques1_2 = "Кто может получать соц. стипендию?" #1
Ques1_3 = "Сколько составляет соц. стипендия?" #9
Ques1_4 = "Получают ли соц. стипендию студенты, обучающиеся на коммерч. основе?" #7
Ques1_5 = "Могут ли получать соц. стипендию магистранты?" #8

Ques2_1 = "Как получить соц. стипендию малоимущим студентам?" #2
Ques2_2 = "Как получить уведомление на получение гос. соц. помощи?" #3
Ques2_3 = "Документы для получения уведомления на получение гос. соц. помощи?" #4
Ques2_4 = "Уведомление на получение гос. соц. помощи, если прописан один." #5
Ques2_5 = "Куда отнести уведомление на получение гос. соц. помощи?" #6

Ques3_1 = "Какие бывают стипендии за оценки?" #11
Ques3_2 = "Кому выплачивают стипендию?" #25
Ques3_3 = "В какие сроки выплачивается стипендия?" #10
Ques3_4 = "Имеет ли право получать стипендию студенты, обучающиеся по договору?" #16
Ques3_5 = "Как получить повышенную гос. академическую стипендию за достижения?" #17

Ques4_1 = "Как получить единовременную материальную помощь?" #27
Ques4_2 = "Почему материальная помощь может быть оказана?" #26
Ques4_3 = "Кто может получать материальную помощь?" #13


Ques5_1 = "На какие дополнительные гарантии может рассчитывать инвалид?" #14
Ques5_2 = "Какие выплаты получают сироты?" #15
Ques5_3 = "Какие выплаты гарантирует полное гос. обеспечение?" #28

Ques6_1 = "Как получить карту и можно ли дать свою карту для выплаты стипендии?" #19
Ques6_2 = "Где оформить банковскую карту?" #20
Ques6_3 = "Что делать если потерял или не успел оформить карту?" #21
Ques6_4 = "Что делать при смене персональных данных?" #23
Ques6_5 = "Как заказать справку о доходах?" #22

B_Exit = "В главное меню"

@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == Sec1:
            Menu(Ques1_1,Ques1_2,Ques1_3,Ques1_4,Ques1_5,Sec1,message)
        
        elif message.text == Sec2:
            Menu(Ques2_1,Ques2_2,Ques2_3,Ques2_4,Ques2_5,Sec2,message)

        elif message.text == Sec3:
            Menu(Ques3_1,Ques3_2,Ques3_3,Ques3_4,Ques3_5,Sec3,message)

        elif message.text == Sec4:
            Menu_2(Ques4_1,Ques4_2,Ques4_3,Sec4,message)
         
        elif message.text == Sec5:
            Menu_2(Ques5_1,Ques5_2,Ques5_3,Sec5,message)

        elif message.text == Sec6:
            Menu(Ques6_1,Ques6_2,Ques6_3,Ques6_4,Ques6_5,Sec6,message)

        elif message.text == B_Exit:
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
            Main_menu(keyboard)
            bot.send_message(message.chat.id, 'Главное меню', reply_markup = keyboard)
        
        elif message.text == Ques1_1:
            Request("24",message)     
        elif message.text == Ques1_2:
            Request("1",message)       
        elif message.text == Ques1_3:
            Request("9",message) 
        elif message.text == Ques1_4:
            Request("7",message)
        elif message.text == Ques1_5:
            Request("8",message)
            
        elif message.text == Ques2_1:
            Request("2",message)
        elif message.text == Ques2_2:
            Request("3",message)     
        elif message.text == Ques2_3:
            Request("4",message)       
        elif message.text == Ques2_4:
            Request("5",message) 
        elif message.text == Ques2_5:
            Request("6",message)
            
        elif message.text == Ques3_1:
            Request("11",message)
        elif message.text == Ques3_2:
            Request("25",message)
        elif message.text == Ques3_3:
            Request("10",message)     
        elif message.text == Ques3_4:
            Request("16",message)       
        elif message.text == Ques3_5:
            Request("17",message) 
            
        elif message.text == Ques4_1:
            Request("27",message)
        elif message.text == Ques4_2:
            Request("26",message)
        elif message.text == Ques4_3:
            Request("13",message)
            
        elif message.text == Ques5_1:
            Request("14",message)     
        elif message.text == Ques5_2:
            Request("15",message)       
        elif message.text == Ques5_3:
            Request("28",message)
            
        elif message.text == Ques6_1:
            Request("19",message)
        elif message.text == Ques6_2:
            Request("20",message)
        elif message.text == Ques6_3:
            Request("21",message)
        elif message.text == Ques6_4:
            Request("23",message)
        elif message.text == Ques6_5:
            Request("22",message)   
        
        
def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")

def Request(ID,message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    Req = "SELECT question,Answer FROM 'Questions' WHERE id_record == " + ID
    Q = execute_read_query(db, Req)
    for row in Q:
        S1 = row[0]
        S1 = row[1]
    bot.send_message(message.chat.id, row[0] + row[1], reply_markup = markup)

def Main_menu(keyboard):
    item1 = types.KeyboardButton('Социальная стипендия')
    item2 = types.KeyboardButton('Оформление соц. стипендии')
    item3 = types.KeyboardButton('Виды стипендии и сроки получения')
    item4 = types.KeyboardButton('Материальные выплаты')
    item5 = types.KeyboardButton('Льготы')
    item6 = types.KeyboardButton('Оформление карты для получения стипендий')
    keyboard.add(item1)
    keyboard.add(item2)
    keyboard.add(item3)
    keyboard.add(item4)
    keyboard.add(item5)
    keyboard.add(item6)


def Menu(Q1,Q2,Q3,Q4,Q5,ID_Sec,message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button_1 = types.KeyboardButton(text=Q1)
    button_2 = types.KeyboardButton(text=Q2)
    button_3 = types.KeyboardButton(text=Q3)
    button_4 = types.KeyboardButton(text=Q4)
    button_5 = types.KeyboardButton(text=Q5)
    button_Exit = types.KeyboardButton(text=B_Exit)
    
    keyboard.add(button_1)          
    keyboard.add(button_2)
    keyboard.add(button_3)
    keyboard.add(button_4)
    keyboard.add(button_5)
    keyboard.add(button_Exit)
    
    bot.send_message(message.chat.id, ID_Sec, reply_markup = keyboard)    

def Menu_2(Q1,Q2,Q3,ID_Sec,message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button_1 = types.KeyboardButton(text=Q1)
    button_2 = types.KeyboardButton(text=Q2)
    button_3 = types.KeyboardButton(text=Q3)
    button_Exit = types.KeyboardButton(text=B_Exit)

    keyboard.add(button_1)          
    keyboard.add(button_2)
    keyboard.add(button_3)
    keyboard.add(button_Exit)

    bot.send_message(message.chat.id, ID_Sec, reply_markup = keyboard)    

        
        
bot.polling(none_stop = True)    