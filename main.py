import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from dotenv import load_dotenv
from os import getenv
import logging
import random
from random import choice


load_dotenv()
bot = Bot(token=getenv('TOKEN'))
dp = Dispatcher()

@dp.message(Command("start"))
async def start_handler(message):
    print(message.from_user)
    await message.answer(f"Привет, {message.from_user.first_name}")

@dp.message(Command('myinfo'))
async def myinfo_handler(message):
    print(message.from_user)
    await message.answer(f'Ваш id: {message.from_user.id}| '
                         f'Имя: {message.from_user.first_name}| '
                         f'Имя пользователя: {message.from_user.username}')


@dp.message(Command('random_recipe'))
async def random_recipe(message):
    print(message.from_user)
    recipes = [
        '*Омлет*| '
        'Ингредиенты: '
        '- 2 яйца'
        '- Соль и перец по вкусу'
        '- Масло для жарки| '

        'Рецепт: '
        '- Взбейте яйца в миске с солью и перцем.'
        '- Разогрейте сковороду с маслом.'
        '- Вылейте взбитые яйца в сковороду и жарьте до готовности. Готовый омлет подавайте горячим.',

        '*Салат "Цезарь"*| '
        'Ингредиенты: '
        '- 1 головка салата романо'
        '- 2 куриных грудок'
        '- 1 яйцо'
        '- Сухарики'
        '- Соус "Цезарь"| '

        'Рецепт: '
        '- Приготовьте курицу, нарезав ее на кусочки.'
        '- Смешайте листья салата, курицу, порезанное яйцо и сухарики.'
        '- Заправьте салат соусом "Цезарь" и перемешайте.',

        '*Паста с томатным соусом*| '
        'Ингредиенты: '
        '- Спагетти'
        '- Томаты'
        '- Чеснок'
        '- Лук'
        '- Масло оливковое| '

        'Рецепт: '
        '- Обжарьте лук с чесноком на сковороде.'
        '- Добавьте нарезанные помидоры и тушите их.'
        '- Варите спагетти по инструкции на упаковке. Затем смешайте их с томатным соусом.'
    ]

    random_recipe = choice(recipes)
    await message.answer(random_recipe)


@dp.message()
async def echo_handler(message):
    print(message.from_user)
    await message.answer('Неправильная команда')


async def main():
    # запуск бота
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())