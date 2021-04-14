import telebot
import sd
import logging
from chatbase import Message

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.DEBUG)

# инициируем бота
bot = telebot.TeleBot('*')
# Гениальное название для переменных - готово!
# Вызываем метод кнопок, обзываем кнопки
keyboard = telebot.types.InlineKeyboardMarkup()
leyboard = telebot.types.InlineKeyboardMarkup()
key_five = telebot.types.InlineKeyboardButton(text='Последние 5 задач', callback_data='five')
key_one = telebot.types.InlineKeyboardButton(text='Последняя задача', callback_data='one')
key_campus = telebot.types.InlineKeyboardButton(text='Кампус', callback_data='campus')
key_school = telebot.types.InlineKeyboardButton(text='Школа', callback_data='school')
key_kcu = telebot.types.InlineKeyboardButton(text='КЦУ', callback_data='kcu')
key_lyceum = telebot.types.InlineKeyboardButton(text='Лицей', callback_data='lyceum')
# группируем кнопки
leyboard.add(key_campus, key_school)
leyboard.add(key_kcu, key_lyceum)
keyboard.add(key_one, key_five)
global place


# запрашиваем местоположение пользователя
@bot.message_handler(commands=['start', 'object'])
def choice_object(message):
    bot.send_message(message.chat.id, text='Выбери свой объект', reply_markup=leyboard)


@bot.message_handler(content_types=['text'])
def text_object(mess):
    if mess.text.isdigit:
        issue = sd.search_issue(int(mess.text))
        text = f'Вот искомая заявка №{issue.id}:\n' \
               f'{issue.subject}\n' \
               f'Статус: {issue.status.name}\n' \
               f'Автор: {issue.author.name}\n' \
               f'Находится в: {issue.custom_fields[0].value}\n' \
               f'Полный текст заявки: \n' \
               f'{issue.description}\n' \
               f'https://sd.talantiuspeh.ru/issues/' + str(issue.id)
        bot.send_message(mess.chat.id, text=text, reply_markup=leyboard)


# обрабатываем нажатие кнопок выбора местоположения
@bot.callback_query_handler(func=lambda call: True)
def press_button(call):
    global key1, key2, key3, key4
    if call.data == 'campus':
        key1 = telebot.types.InlineKeyboardMarkup()
        key_five1 = telebot.types.InlineKeyboardButton(text='Последние 5 задач', callback_data='five_camp')
        key_one1 = telebot.types.InlineKeyboardButton(text='Последняя задача', callback_data='one_camp')
        key1.add(key_one1, key_five1)
        issue = sd.get_issue('campus')
        text = f'Привет, вот новая задачка на сегодня в кампусе:\n' \
               f'{issue[0].subject};\n' \
               f'Создана: {issue[0].created_on.day}/{issue[0].created_on.month}/{issue[0].created_on.year} ' \
               f'{issue[0].created_on.hour + 3}:{issue[0].created_on.minute}\n' \
               f'Статус: {issue[0].status.name}\n' \
               f'Автор: {issue[0].author.name};\n' \
               f'Находится в: {issue[0].custom_fields[0].value};\n' \
               f'https://sd.talantiuspeh.ru/issues/' + str(issue[0].id)
        bot.send_message(call.message.chat.id, text=text, reply_markup=key1)

    elif call.data == 'school':
        key2 = telebot.types.InlineKeyboardMarkup()
        key_five2 = telebot.types.InlineKeyboardButton(text='Последние 5 задач', callback_data='five_school')
        key_one2 = telebot.types.InlineKeyboardButton(text='Последняя задача', callback_data='one_school')
        key2.add(key_one2, key_five2)
        issue = sd.get_issue('school')
        text = f'Привет, вот новая задачка на сегодня в школе:\n' \
               f'{issue[0].subject};\n' \
               f'Создана: {issue[0].created_on.day}/{issue[0].created_on.month}/{issue[0].created_on.year} ' \
               f'{issue[0].created_on.hour + 3}:{issue[0].created_on.minute}\n' \
               f'Статус: {issue[0].status.name}\n' \
               f'Автор: {issue[0].author.name};\n' \
               f'Находится в: {issue[0].custom_fields[0].value};\n' \
               f'https://sd.talantiuspeh.ru/issues/' + str(issue[0].id)
        bot.send_message(call.message.chat.id, text=text, reply_markup=key2)

    elif call.data == 'kcu':
        key3 = telebot.types.InlineKeyboardMarkup()
        key_five3 = telebot.types.InlineKeyboardButton(text='Последние 5 задач', callback_data='five_kcu')
        key_one3 = telebot.types.InlineKeyboardButton(text='Последняя задача', callback_data='one_kcu')
        key3.add(key_one3, key_five3)
        issue = sd.get_issue('kcu')
        text = f'Привет, вот новая задачка на сегодня в кцу:\n' \
               f'{issue[0].subject};\n' \
               f'Создана: {issue[0].created_on.day}/{issue[0].created_on.month}/{issue[0].created_on.year} ' \
               f'{issue[0].created_on.hour + 3}:{issue[0].created_on.minute}\n' \
               f'Статус: {issue[0].status.name}\n' \
               f'Автор: {issue[0].author.name};\n' \
               f'Находится в: {issue[0].custom_fields[0].value};\n' \
               f'https://sd.talantiuspeh.ru/issues/' + str(issue[0].id)
        bot.send_message(call.message.chat.id, text=text, reply_markup=key3)

    elif call.data == 'lyceum':
        key4 = telebot.types.InlineKeyboardMarkup()
        key_five4 = telebot.types.InlineKeyboardButton(text='Последние 5 задач', callback_data='five_lyceum')
        key_one4 = telebot.types.InlineKeyboardButton(text='Последняя задача', callback_data='one_lyceum')
        key4.add(key_one4, key_five4)
        issue = sd.get_issue('lyceum')
        text = f'Привет, вот новая задачка на сегодня в лицее:\n' \
               f'{issue[0].subject};\n' \
               f'Создана: {issue[0].created_on.day}/{issue[0].created_on.month}/{issue[0].created_on.year} ' \
               f'{issue[0].created_on.hour + 3}:{issue[0].created_on.minute}\n' \
               f'Статус: {issue[0].status.name}\n' \
               f'Автор: {issue[0].author.name};\n' \
               f'Находится в: {issue[0].custom_fields[0].value};\n' \
               f'https://sd.talantiuspeh.ru/issues/' + str(issue[0].id)
        bot.send_message(call.message.chat.id, text=text, reply_markup=key4)

    if call.data == 'five_camp':
        issue1 = sd.get_issue('campus')
        msg = f'Вот список последних задач в кампусе: \n'
        for i in range(len(issue1)):
            msg += f'{issue1[i].subject};\n' \
                   f'Создана: {issue1[i].created_on.day}/{issue1[i].created_on.month}/{issue1[i].created_on.year} ' \
                   f'{issue1[i].created_on.hour + 3}:{issue1[i].created_on.minute}\n' \
                   f'Статус: {issue1[i].status.name}\n' \
                   f'Автор: {issue1[i].author.name};\n' \
                   f'Находится в: {issue1[i].custom_fields[0].value};\n' \
                   f'https://sd.talantiuspeh.ru/issues/{str(issue1[i].id)}\n' \
                   f'\n'
        bot.send_message(call.message.chat.id, text=msg, disable_web_page_preview=True, reply_markup=key1)
    elif call.data == 'one_camp':
        issue1 = sd.get_issue('campus')
        msg = f'Вот последняя заявка в кампусе:\n' \
              f'{issue1[0].subject};\n' \
              f'Создана: {issue1[0].created_on.day}/{issue1[0].created_on.month}/{issue1[0].created_on.year} ' \
              f'{issue1[0].created_on.hour + 3}:{issue1[0].created_on.minute}\n' \
              f'Статус: {issue1[0].status.name}\n' \
              f'Автор: {issue1[0].author.name};\n' \
              f'Находится в: {issue1[0].custom_fields[0].value};\n' \
              f'https://sd.talantiuspeh.ru/issues/' + str(issue1[0].id)
        bot.send_message(call.message.chat.id, text=msg, reply_markup=key1)
    elif call.data == 'five_school':
        issue1 = sd.get_issue('school')
        msg = f'Вот список последних задач в школе: \n'
        for i in range(len(issue1)):
            msg += f'{issue1[i].subject};\n' \
                   f'Создана: {issue1[i].created_on.day}/{issue1[i].created_on.month}/{issue1[i].created_on.year} ' \
                   f'{issue1[i].created_on.hour + 3}:{issue1[i].created_on.minute}\n' \
                   f'Статус: {issue1[i].status.name}\n' \
                   f'Автор: {issue1[i].author.name};\n' \
                   f'Находится в: {issue1[i].custom_fields[0].value};\n' \
                   f'https://sd.talantiuspeh.ru/issues/{str(issue1[i].id)}\n' \
                   f'\n'
        bot.send_message(call.message.chat.id, text=msg, disable_web_page_preview=True, reply_markup=key2)
    elif call.data == 'one_school':
        issue1 = sd.get_issue('school')
        msg = f'Вот новая задача в школе:\n' \
              f'{issue1[0].subject};\n' \
              f'Создана: {issue1[0].created_on.day}/{issue1[0].created_on.month}/{issue1[0].created_on.year} ' \
              f'{issue1[0].created_on.hour + 3}:{issue1[0].created_on.minute}\n' \
              f'Создана: {issue1[0].created_on}\n' \
              f'Статус: {issue1[0].status.name}\n' \
              f'Автор: {issue1[0].author.name};\n' \
              f'Находится в: {issue1[0].custom_fields[0].value};\n' \
              f'https://sd.talantiuspeh.ru/issues/' + str(issue1[0].id)
        bot.send_message(call.message.chat.id, text=msg, reply_markup=key2)
    elif call.data == 'five_kcu':
        issue1 = sd.get_issue('kcu')
        msg = f'Вот список последних задач на КЦУ: \n'
        for i in range(len(issue1)):
            msg += f'{issue1[i].subject};\n' \
                   f'Создана: {issue1[i].created_on.day}/{issue1[i].created_on.month}/{issue1[i].created_on.year} ' \
                   f'{issue1[i].created_on.hour + 3}:{issue1[i].created_on.minute}\n' \
                   f'Статус: {issue1[i].status.name}\n' \
                   f'Автор: {issue1[i].author.name};\n' \
                   f'Находится в: {issue1[i].custom_fields[0].value};\n' \
                   f'https://sd.talantiuspeh.ru/issues/{str(issue1[i].id)}\n' \
                   f'\n'
        bot.send_message(call.message.chat.id, text=msg, disable_web_page_preview=True, reply_markup=key3)
    elif call.data == 'one_kcu':
        issue1 = sd.get_issue('kcu')
        msg = f'Вот последняя задача на КЦУ:\n' \
              f'{issue1[0].subject};\n' \
              f'Создана: {issue1[0].created_on.day}/{issue1[0].created_on.month}/{issue1[0].created_on.year} ' \
              f'{issue1[0].created_on.hour + 3}:{issue1[0].created_on.minute}\n' \
              f'Статус: {issue1[0].status.name}\n' \
              f'Автор: {issue1[0].author.name};\n' \
              f'Находится в: {issue1[0].custom_fields[0].value};\n' \
              f'https://sd.talantiuspeh.ru/issues/' + str(issue1[0].id)
        bot.send_message(call.message.chat.id, text=msg, reply_markup=key3)
    elif call.data == 'five_lyceum':
        issue1 = sd.get_issue('lyceum')
        msg = f'Вот список последних задач в лицее: \n'
        for i in range(len(issue1)):
            msg += f'{issue1[i].subject};\n' \
                   f'Создана: {issue1[i].created_on.day}/{issue1[i].created_on.month}/{issue1[i].created_on.year} ' \
                   f'{issue1[i].created_on.hour + 3}:{issue1[i].created_on.minute}\n' \
                   f'Статус: {issue1[i].status.name}\n' \
                   f'Автор: {issue1[i].author.name};\n' \
                   f'Находится в: {issue1[i].custom_fields[0].value};\n' \
                   f'https://sd.talantiuspeh.ru/issues/{str(issue1[i].id)}\n' \
                   f'\n'
        bot.send_message(call.message.chat.id, text=msg, disable_web_page_preview=True, reply_markup=key4)
    elif call.data == 'one_lyceum':
        issue1 = sd.get_issue('lyceum')
        msg = f'Вот последняя задача в лицее:\n' \
              f'{issue1[0].subject};\n' \
              f'Создана: {issue1[0].created_on.day}/{issue1[0].created_on.month}/{issue1[0].created_on.year} ' \
              f'{issue1[0].created_on.hour + 3}:{issue1[0].created_on.minute}\n' \
              f'Статус: {issue1[0].status.name}\n' \
              f'Автор: {issue1[0].author.name};\n' \
              f'Находится в: {issue1[0].custom_fields[0].value};\n' \
              f'https://sd.talantiuspeh.ru/issues/' + str(issue1[0].id)
        bot.send_message(call.message.chat.id, text=msg, reply_markup=key4)


bot.polling(none_stop=True)
