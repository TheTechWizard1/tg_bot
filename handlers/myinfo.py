from aiogram import types,Router
from aiogram.filters.command import Command

myinfo_router = Router()

@myinfo_router.message(Command('myinfo'))
async def myinfo_handler(message: types.Message):
    print(message.from_user)
    await message.answer(f'Ваш id: {message.from_user.id}| '
                         f'Имя: {message.from_user.first_name}| '
                         f'Имя пользователя: {message.from_user.username}')
