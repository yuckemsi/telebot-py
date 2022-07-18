import telebot
import cfg
from telebot import types

client = telebot.TeleBot(cfg.config['token'])


@client.message_handler(commands = ['get_info', 'info'])
def get_user_info(message):
	markup_inline = types.InlineKeyboardMarkup()
	item_ucheba = types.InlineKeyboardButton(text = 'Учеба', callback_data = 'ucheba')
	item_uchitelya = types.InlineKeyboardButton(text = 'Учителя', callback_data = 'uchitelya')


	markup_inline.add(item_ucheba, item_uchitelya)
	client.send_message(message.chat.id, 'Что ты хочешь узнать? (Псс, нажми на кнопку)',
		reply_markup = markup_inline 
	)


@client.callback_query_handler(func = lambda call: True)
def answer(call):
	client.answer_callback_query(callback_query_id=call.id)
	if call.data == 'ucheba':
		markup_reply = types.ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard=True)
		item_dz = types.KeyboardButton('Дз')
		item_raspis = types.KeyboardButton('Расписание')

		markup_reply.add(item_dz, item_raspis)
		client.send_message(call.message.chat.id, 'Нажми на одну из кнопок',
			reply_markup = markup_reply
		)
	if call.data == 'uchitelya':
		markup_reply = types.ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard=True)
		item_uchit = types.KeyboardButton('Учителя')
		item_vneuch = types.KeyboardButton('Учителя внеурочек')

		markup_reply.add(item_uchit, item_vneuch)
		client.send_message(call.message.chat.id, 'Нажми на одну из кнопок',
			reply_markup = markup_reply
		)

@client.message_handler(content_types = ['text'])
def get_text(message):
	if message.text == 'Расписание':
		client.send_message(message.chat.id, f'Учеба еще не началась!')
	if message.text == 'Дз':
		client.send_message(message.chat.id, f'Учеба еще не началась!')
	if message.text == 'Учителя':
		client.send_message(message.chat.id, f'Учеба еще не началась!')


client.polling(none_stop = True, interval = 0)
