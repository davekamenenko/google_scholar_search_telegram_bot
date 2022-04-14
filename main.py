import time
import telebot
import  sqlite3
from serpapi import GoogleSearch
from telebot import types
params = {
  "api_key": "8e952a1324a7b295488f7ed8c8b5a414f3b1109b1f97ffe59fc3555eb28112f7",
  "engine": "google_scholar",
  "q": "milk",
  "hl": "ru"
}
user = {
    "mention": "",
    "test": ""
}
result = ""

bot = telebot.TeleBot('5305923588:AAG8GHSnlwwTquj-h5UnfgpK0QtXfBzNRCA')

@bot.message_handler(commands=['start'])
def welcome(message):
    mention = f'<a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a>'
    bot.send_message(message.chat.id, f"Ласкаво просимо, {mention}! Швидкі команди: \n/find_content - пошук статей \n/my_test - тест для формування iнтересiв \n/find_users - пошук однодумцiв", parse_mode="HTML")



@bot.message_handler(commands=['find_content'])
def welcome(message):
    bot.reply_to(message, 'Введіть запит')
    @bot.message_handler(content_types=['text'])
    def message_input_step(message):

        params["q"] = message.text
        search = GoogleSearch(params)
        results = search.get_dict()
        print(results)
        if("organic_results" in results.keys()):
            results_1 = results['organic_results']
            print(results_1)
            i = 0
            while i < 10:
                bot.send_message(message.chat.id, f"<b>{str(results['organic_results'][i]['title'])}</b> \n\n{str(results['organic_results'][i]['snippet'])} \n\nССЫЛКА: {str(results_1[i]['link'])}", parse_mode="HTML")
                i = i + 1
            bot.send_message(message.chat.id, "Kiнець. Повернутись в меню - /start")
        elif("organic_results" not in results.keys()):
            bot.send_message(message.chat.id, "Помилковий запит, спробуйте ще раз - /find_content")

@bot.message_handler(commands=['find_users'])
def welcome(message):
    conn = sqlite3.connect('bd.db')
    cursor = conn.cursor()
    query = cursor.execute("SELECT * FROM `users` WHERE `user_id` = ?", (message.from_user.id,))
    conn.commit()
    result = query.fetchone();
    print(result)
    if (result != None):
        if (result[1] == message.from_user.id):
            def tanimoto(s1, s2):
                a, b, c = len(s1), len(s2), 0.0

                for sym in s1:
                    if sym in s2:
                        c += 1

                return c / (a + b - c)

            query_1 = cursor.execute("SELECT * FROM `users`")
            for row in cursor.fetchall():
                if row[0]:  # проверка что строка в столбце url не пустая
                    interes = tanimoto(result[2],row[2])
                    if(interes > 2.3):
                        mention = f'<a href="tg://user?id={row[1]}">id:{row[1]}</a>'
                        bot.send_message(message.chat.id,
                                         f"Знайдено спiвдад iнтересiв, натиснiть щоб перейти в профiль - {mention}!",parse_mode="HTML")

            bot.send_message(message.chat.id, "Kiнець. Повернутись в меню - /start")
            cursor.close()
            print(result[2])
    if (result == None):
        bot.send_message(message.chat.id, "Спочатку пройдiть тест - /my_test")

@bot.message_handler(commands=['my_test'])
def welcome(message):
    conn = sqlite3.connect('bd.db')
    cursor = conn.cursor()
    user['test'] = ""
    user['mention'] = message.from_user.id
    xr = cursor.execute("SELECT `user_id` FROM `users` WHERE `user_id` = ?", (message.from_user.id,))
    conn.commit()

    res = xr.fetchone()

    if(res != None):
        if (res[0] == message.from_user.id):
            bot.send_message(message.chat.id, "Ви вже проходили тест. Повернутись в меню - /start")
    elif(res == None):

        markup = types.InlineKeyboardMarkup(row_width=2)
        item1 = types.InlineKeyboardButton("Так",callback_data="yes")
        item2 = types.InlineKeyboardButton("Нi",callback_data="no")

        markup.add(item1, item2)

        bot.send_message(message.chat.id, "Чи подобається тобі дізнаватися про відкриття в галузі фізики та математики?",reply_markup=markup)
        bot.send_message(message.chat.id, "Чи подобається тобі дивитися передачі про життя рослин та тварин?",reply_markup=markup)
        bot.send_message(message.chat.id, "Чи подобається тобі з'ясовувати пристрій електроприладів?",reply_markup=markup)
        bot.send_message(message.chat.id, "Чи подобається тобі дивитися передачі про життя людей у   різних країнах?",reply_markup=markup)
        bot.send_message(message.chat.id, "Чи подобається тобі бувати на виставках, концертах, виставах?",reply_markup=markup)
        bot.send_message(message.chat.id, "Чи подобається тобі спостерігати за роботою медсестри, лікаря?",reply_markup=markup)
        bot.send_message(message.chat.id, "Чи подобається тобі займатися математичними розрахунками та обчисленнями?",reply_markup=markup)
        bot.send_message(message.chat.id, "Чи подобається тобі дізнаватися про відкриття в галузі хімії та біології?",reply_markup=markup)
        bot.send_message(message.chat.id, "Чи подобається тобі ремонтувати побутові електроприлади?",reply_markup=markup)
        bot.send_message(message.chat.id, "Чи подобається тобі відвідувати технічні виставки, знайомитися з досягненнями науки та техніки?",reply_markup=markup)
        bot.send_message(message.chat.id, "Чи подобається тобі проводити досліди з фізики?",reply_markup=markup)
        bot.send_message(message.chat.id, "Чи подобається тобі читати біографії відомих політиків, книги з історії?",reply_markup=markup)
        bot.send_message(message.chat.id, "Чи подобається тобі помічати та пояснювати природні явища?",reply_markup=markup)

        time.sleep(40)

        uz = (user['mention'],user['test'])
        cursor.execute("INSERT INTO users (user_id, result) VALUES(?, ?);", uz)
        conn.commit()
        bot.send_message(message.chat.id, "Kiнець. Повернутись в меню - /start")
    conn.close()

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    str1 = ""
    try:
        if call.message:
            if call.data == "yes":
                user['test'] = user['test'] + " yes "
            elif call.data == "no":
                user['test'] = user['test'] + " no "

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Вiдповiдь збережено',
                              reply_markup=None)
        bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                  text="Вiдповiдь збережено")
    except Exception as e:
        print(repr(e))



bot.polling(none_stop=True)