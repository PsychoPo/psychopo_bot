from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

main = ReplyKeyboardMarkup(keyboard=[
	[KeyboardButton(text="Обо мне")],
	[KeyboardButton(text="Какая погода сейчас в Красноярске?"), KeyboardButton(text="Какая погода сейчас в Москве")],
	[KeyboardButton(text="Закрыть")]
],
	resize_keyboard=True,
	input_field_placeholder="Выберите пункт меню.")


settings = InlineKeyboardMarkup(inline_keyboard=[
			[InlineKeyboardButton(text="Переводчик", url="https://www.deepl.com/en/translator"),
			InlineKeyboardButton(text="Youtube", url="https://www.youtube.com/")]
			])