from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery

from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

import app.keyboards as kb

router = Router()


class Reg(StatesGroup):
    name = State()
    number = State()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Привет!', reply_markup=kb.settings)


@router.message(Command('help'))
async def get_help(message: Message):
    await message.answer('Вы воспользовались командой /help!\nВы можете воспользоваться /start, /reg, /help.')


@router.message(F.text.lower() == 'привет')
async def answer_hi(message: Message):
    await message.reply(f'Пользователь {message.from_user.first_name} с ID:{message.from_user.id} я рад, что вы нашли меня!',
	 							reply_markup=kb.main)


@router.message(F.photo)
async def get_photo(message: Message):
    await message.answer(f'ID этого фото: {message.photo[-1].file_id}')
    await message.answer_photo(photo=message.photo[-1].file_id, 
                            caption='Я тоже могу это отправить вам!')
    await message.answer_photo(photo='https://assets.monica.im/home-web/_next/static/media/chatPdfTranslation.9c971641.png',
                            caption='А еще вот это!')


@router.callback_query(F.data == 'about_me')
async def about_me(callback: CallbackQuery):
    await callback.answer('') #('Вы выбрали "Обо мне"', show_alert=True)
    # await callback.message.answer('Я -- бот созданный PsychoPo!\nЯ нахожусь в разработке, поэтому некоторые мои функции могут не работать!')
    await callback.message.edit_text('Я -- бот созданный PsychoPo!\nЯ нахожусь в разработке, поэтому некоторые мои функции могут не работать!',
                                reply_markup=await kb.inline_cars())


@router.message(Command('reg'))
async def reg_first(message: Message, state: FSMContext):
    await state.set_state(Reg.name)
    await message.answer('Введите ваше имя:')


@router.message(Reg.name)
async def reg_second(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Reg.number)
    await message.answer('Введите ваш номер телефона:')


@router.message(Reg.number)
async def reg_third(message: Message, state: FSMContext):
    await state.update_data(number=message.text)
    data = await state.get_data()
    await message.answer(f'Спасибо, регистрация завершена!\nВаши сохраненные данные:\n1. {data['name']}\n2. {data['number']}')
    await state.clear()