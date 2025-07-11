from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

import app.keyboards as kb

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Привет!", reply_markup=kb.settings)


@router.message(Command("help"))
async def get_help(message: Message):
    await message.answer("Вы воспользовались командой /help!")


@router.message(F.text.lower() == "привет")
async def answer_hi(message: Message):
    await message.reply(f"Пользователь {message.from_user.first_name} с ID:{message.from_user.id} я рад, что вы нашли меня!",
	 							reply_markup=kb.main)


@router.message(F.photo)
async def get_photo(message: Message):
    await message.answer(f"ID этого фото: {message.photo[-1].file_id}")
    await message.answer_photo(photo=message.photo[-1].file_id, 
                            caption="Я тоже могу это отправить вам!")
    await message.answer_photo(photo="https://assets.monica.im/home-web/_next/static/media/chatPdfTranslation.9c971641.png",
                            caption="А еще вот это!")