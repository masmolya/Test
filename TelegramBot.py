import telebot
import config
from telebot import types
from string import Template

bot = telebot.TeleBot(config.TOKEN) # токен бота

# Узнать id группы или почти любого пользователя можно с помощью другого бота "IDBot" 

"""
# Ограничитель на взаимодействие с ботом по id. Раскомментировав код ниже, необходимо ввести желаемый id.
# users - список id для которых будет доступен тест, просто вводим id пользователей через запятую

users = [0000000000] 
@bot.message_handler(func=lambda message: message.chat.id not in users)
def some(message):
        bot.send_message(message.chat.id, "Sorry")"""


user_dict = {}

class User:
    def __init__(self, idUser):
        self.idUser = idUser

        keys = ['idUser', 'supername', 'mail', 'fullname', 'age', 'height', 
                'eyeColor', 'favoriteColor', 'favoriteDish', 
                'film', 'song', 'haveCat', 'catName']
        
        for key in keys:
            self.key = None

# если /help, /start
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    itembtn1 = types.KeyboardButton('/about')
    itembtn2 = types.KeyboardButton('/reg')
    markup.add(itembtn1, itembtn2)
    
    bot.send_message(message.chat.id,  "Здравствуйте  "   +   message.from_user.first_name
    +   ", я - бот, нажмите /about?", reply_markup=markup)

# /about
@bot.message_handler(commands=['about'])
def send_about(message):
	bot.send_message(message.chat.id, "Это бот-опросник.Как только Вы нажмете /reg начнется регистрация Ваших ответов в формате Вопрос-Ответ(в свободной форме)")
	
# /reg
@bot.message_handler(commands=["reg"])
def user_reg(message):
       
       msg = bot.send_message(message.chat.id, 'Hallo') # что бы не ввел пользователь, вы получите id пользователя.
       bot.register_next_step_handler(msg, process_idUser_step)

def process_idUser_step(message):
    try:
        chat_id = message.chat.id
        user_dict[chat_id] = User(message.from_user.id) # Присылает ID пользователя

        
        msg = bot.send_message(chat_id, 'Ваше Уникальное Имя  Telegram аккаунта?')
        bot.register_next_step_handler(msg, process_supername_step)

    except Exception as e:
        bot.reply_to(message, 'ooops!!')

def process_supername_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.supername = message.text
        
        msg = bot.send_message(chat_id, 'Ваш рабочий mail')
        bot.register_next_step_handler(msg, process_mail_step)

    except Exception as e:
        bot.reply_to(message, 'ooops!!')

        

def process_mail_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.mail = message.text

        msg = bot.send_message(chat_id, 'Фамилия Имя Отчество')
        bot.register_next_step_handler(msg, process_fullname_step)

    except Exception as e:
        bot.reply_to(message, 'ooops!!')

def process_fullname_step(message):
    try:
        
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.fullname = message.text

        msg = bot.send_message(chat_id, 'Ваш возраст?')
        bot.register_next_step_handler(msg, process_age_step)

    except Exception as e:
        bot.reply_to(message, 'ooops!!')

def process_age_step(message):
    try:

        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.age = message.text

        msg = bot.send_message(chat_id, 'Ваш рост')
        bot.register_next_step_handler(msg, process_height_step)

    except Exception as e:
        msg = bot.reply_to(message, 'ooops!!')
        bot.register_next_step_handler(msg, process_height_step)

def process_height_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.height = message.text

        msg = bot.send_message(chat_id, 'Какого цвета Ваши глаза?')
        bot.register_next_step_handler(msg, process_eyeColor_step)

    except Exception as e:
        bot.reply_to(message, 'ooops!!')

def process_eyeColor_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.eyeColor = message.text
       
        msg = bot.send_message(chat_id, 'Скажите мне Ваш любимый цвет')
        bot.register_next_step_handler(msg, process_favoriteColor_step)

    except Exception as e:
        bot.reply_to(message, 'ooops!!')

def process_favoriteColor_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.favoriteColor = message.text

        msg = bot.send_message(chat_id, 'Что любите покушать?')
        bot.register_next_step_handler(msg, process_favoriteDish_step)

    except Exception as e:
        bot.reply_to(message, 'ooops!!')

def process_favoriteDish_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.favoriteDish = message.text

        msg = bot.send_message(chat_id, 'Какой фильм нравится?')
        bot.register_next_step_handler(msg, process_film_step)

    except Exception as e:
        bot.reply_to(message, 'ooops!!')

def process_film_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.film = message.text

        msg = bot.send_message(chat_id, 'Любимая песня?')
        bot.register_next_step_handler(msg, process_song_step)

    except Exception as e:
        bot.reply_to(message, 'ooops!!')

def process_song_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.song = message.text

        msg = bot.send_message(chat_id, 'Есть кот?')
        bot.register_next_step_handler(msg, process_haveCat_step)

    except Exception as e:
        bot.reply_to(message, 'ooops!!')

def process_haveCat_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.haveCat = message.text

        msg = bot.send_message(chat_id, 'Как зовут симпотягу?')
        bot.register_next_step_handler(msg, process_catName_step)

    except Exception as e:
        bot.reply_to(message, 'ooops!!')

def process_catName_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.catName = message.text

        # отправить в группу
        

        bot.send_message(00000000000, getRegData(user, 'Данные от бота', bot.get_me().username), parse_mode="Markdown")# 0000000000 сюда вбиваем id группы которую создаем и добавляем себя и бота.
        

    except Exception as e:
        bot.reply_to(message, 'ooops!!')

# формирует вид заявки регистрации
# нельзя делать перенос строки Template, так как пока не нашел более красивого способа.
# в send_message должно стоять parse_mode="Markdown"
def getRegData(user, title, name):
    t = Template('$title *$name* \n ID Пользователя: *$idUser* \n "Уникальное Имя" аккаунта: *$supername* \n Рабочий Mail: *$mail* \n ФИО: *$fullname* \n Возраст: *$age* \n Рост: *$height* \n Цвет глаз: *$eyeColor* \n Цвет: *$favoriteColor* \n Блюдо: *$favoriteDish* \n Фильм: *$film* \n Песня: *$song* \n Наличие кота: *$haveCat* \n Имя Кота: *$catName*')

    return t.substitute({
        'title': title,
        'name': name,
        'idUser': user.idUser,
        'supername': user.supername,
        'mail': user.mail,
        'fullname': user.fullname,
        'age': user.age,
        'height': user.height,
        'eyeColor': user.eyeColor,
        'favoriteColor': user.favoriteColor,
        'favoriteDish': user.favoriteDish,
        'film': user.film,
        'song': user.song,
        'haveCat': user.haveCat,
        'catName': user.catName,
    })


# произвольный текст
@bot.message_handler(content_types=["text"])
def send_help(message):
    bot.send_message(message.chat.id, 'О боте - /about\nРегистрация - /reg')
            


if __name__ == '__main__':
    bot.polling(none_stop=True)
