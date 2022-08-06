import telebot
from config import TOKEN
from telebot import types
bot = telebot.TeleBot(TOKEN)

play_ground = [[],[]]
board = [
        ['-', '-', '-'],
        ['-', '-', '-'],
        ['-', '-', '-']
    ]

#@bot.message_handler(content_types=['text'])
#def get_text_messages(message):
    #if message.text == "Привет":
        #bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
    #elif message.text =="Играть":
        #bot.send_message(message.from_user.id, "Поиск игры")
    #elif message.text == "Help" or "help":
        #bot.send_message(message.from_user.id, "Команды бота : Играть-начинается игра")
    #elif message.text == "рейтинг":
        #bot.send_message(message.from_user.id, "кд")
    #else:
        #bot.send_message(message.from_user.id, "Я тебя не понимаю") fdcd

@bot.message_handler(commands=['start'])
def start_game(message):
    markup_reply = types.InlineKeyboardMarkup()
    item_id= types.InlineKeyboardButton('начать игру', callback_data = 'start the game')
    markup_reply.add(item_id)
    bot.send_message(message.chat.id,'нажмите на одну из конпок', reply_markup = markup_reply)
    inline_start_game(message)

    @bot.message_handler(content_types=['text'])
    def main(message):
        if message.text == "начать игру":
            bot.send_message(message.from_user.id, "Let's start the game")
            choose(message)
            inline_start_game(message)

    @bot.message_handler(commands=['choose'])
    def choose (message):
        markup_reply_a = types.InlineKeyboardMarkup()
        item_id_a = types.InlineKeyboardButton('Выбирете персонажа', callback_data='Choose a character')
        markup_reply_a.add(item_id_a)
        bot.send_message(message.chat.id, 'нажмите на одну из конпок', reply_markup=markup_reply)
        inline_start_game(message)



@bot.message_handler(commands=['inline'])
def inline_start_game(message):
    markup_inline = types.InlineKeyboardMarkup()
    x = 'X'
    o = 'O'
    # chosing = chose()
    # if chosing == 'x' || chosing == 'X':

#def deаfewes(message):
    if (message.text == 'X') or (message.text == 'O'):
       bot.send_message(message.from_user.id,choose())

    item_1_1 = types.InlineKeyboardButton(f'{board[0][0]}', callback_data = 'b_1_1')
    item_1_2 = types.InlineKeyboardButton(f'{board[0][1]}', callback_data = 'b_1_2')
    item_1_3 = types.InlineKeyboardButton(f'{board[0][2]}', callback_data = 'b_1_3')
    item_2_1 = types.InlineKeyboardButton(f'{board[1][0]}', callback_data = 'b_2_1')
    item_2_2 = types.InlineKeyboardButton(f'{board[1][1]}', callback_data = 'b_2_2')
    item_2_3 = types.InlineKeyboardButton(f'{board[1][2]}', callback_data = 'b_2_3')
    item_3_1 = types.InlineKeyboardButton(f'{board[2][0]}', callback_data = 'b_3_1')
    item_3_2 = types.InlineKeyboardButton(f'{board[2][1]}', callback_data = 'b_3_2')
    item_3_3 = types.InlineKeyboardButton(f'{board[2][2]}', callback_data = 'b_3_3')
    markup_inline.add(item_1_1, item_1_2, item_1_3, item_2_1, item_2_2, item_2_3, item_3_1, item_3_2, item_3_3)
    bot.send_message(message.chat.id, 'Теперь Вы можете играть, управляя полем с помощью кнопок:', reply_markup = markup_inline)
    print(f'Comand from user id {message.from_user.id} with the name {message.from_user.first_name}:       {message.text}')

@bot.callback_query_handler(func = lambda call: True)
def callback(call):

    if call.message:
        if call.data == 'b_1_1':
            board[0][0] = 'X'
            print(f'User press:        b_1_1, {board[0][0]}')
        elif call.data == 'b_1_2':
            board[0][1] = 'X'
            print(f'User press:        b_1_2, {board[0][1]}')
        elif call.data == 'b_1_3':
            board[0][2] = 'X'
            print(f'User press:        b_1_3, {board[0][2]}')
        elif call.data == 'b_2_1':
            board[1][0] = '!'
            print(f'User press:        b_2_1, {board[1][0]}')
        elif call.data == 'b_2_2':
            board[1][1] = '!'
            print(f'User press:        b_2_2, {board[1][1]}')
        elif call.data == 'b_2_3':
            board[1][2] = '!'
            print(f'User press:        b_2_3, {board[1][2]}')
        elif call.data == 'b_3_1':
            board[2][0] = '!'
            print(f'User press:        b_3_1, {board[2][0]}')
        elif call.data == 'b_3_2':
            board[2][1] = '!'
            print(f'User press:        b_3_2, {board[2][1]}')
        elif call.data == 'b_3_3':
            board[2][2] = '!'
            print(f'User press:        b_3_3, {board[2][2]}')
        if call.data == "start the game":
            print('Start')
            # markup_buttons_pers = types.InlineKeyboardMarkup()
            # item_x = types.InlineKeyboardButton('X')
            # item_o = types.InlineKeyboardButton('O')
            # markup_buttons_pers.add(item_x, item_o)
            # bot.send_message(message.chat.id, 'хороший выбор', reply_markup=markup_buttons_pers)

@bot.message_handler(commands=['web'])
def website(message):
  markup = types.InlineKeyboardMarkup()
  markup.add(types.InlineKeyboardButton("Go", url = "https://www.youtube.com/watch?v=HodO2eBEz_8&t=430s"))
  bot.send_message(message.chat.id, "Класный ход", reply_markup=markup)

class MessageHandler:
    def menu(bot, message, user):
        print("Вова гей")
        bot.send_message(message.chat.id, " гей")

#@bot.message_handler(content_types=["text"])
#def handle_text(message):
#    print(f"{message.chat.id} {message.chat.first_name} |{message.text}|")
#    message.text = message.text.strip().replace(" ", " ").replace("\t\t", "\t")
#    user = get_user(message)
#    message.text = message.text.upper()
#    log(message, user)
#    action = {
#        "menu": MessageHandler.menu
#    }

#messege.text = message.text.upper()
bot.polling()