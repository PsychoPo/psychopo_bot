from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

main = ReplyKeyboardMarkup(keyboard=[
	[KeyboardButton(text='Обо мне')],
	[KeyboardButton(text='Какая погода сейчас в Красноярске?'), KeyboardButton(text='Какая погода сейчас в Москве')],
	[KeyboardButton(text='Закрыть')]
],
	resize_keyboard=True,
	input_field_placeholder='Выберите пункт меню.')


settings = InlineKeyboardMarkup(inline_keyboard=[
			[InlineKeyboardButton(text='Переводчик', url='https://www.deepl.com/en/translator'),
			InlineKeyboardButton(text='Youtube', url='https://www.youtube.com/'),
			InlineKeyboardButton(text='Обо мне', callback_data='about_me')]
			])


cars_from_bd = ['Mazda', 'BMW', 'Kio', 'Mercedes', 'Hyndai', 'Honda']

# async def reply_cars():
# 	keyboard = ReplyKeyboardBuilder()
# 	for car in cars_from_bd:
# 		keyboard.add(KeyboardButton(text=car))
# 	return keyboard.adjust(2).as_markup()

async def inline_cars():
	keyboard = InlineKeyboardBuilder()
	for car in cars_from_bd:
		keyboard.add(InlineKeyboardButton(text=car, callback_data=car))
	return keyboard.adjust(2).as_markup()