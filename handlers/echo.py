from aiogram import types,Router
from aiogram.filters.command import Command

echo_router = Router()

@echo_router.message()
async def echo_handler(message: types.Message):
    print(message.from_user)
    await message.answer('Неправильная команда. Команды которые я понимаю \n/start - Начало, \n/myinfo - Моя информация, \n/random_recipe - Отправка рецепта блюда')