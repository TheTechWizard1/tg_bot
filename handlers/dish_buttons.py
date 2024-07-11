from aiogram import Router, F, types
from aiogram.filters.command import Command

dishes_button_router = Router()

@dishes_button_router.message(Command("dishes"))
async def show_meals(message: types.Message):
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text="Холодный напиток")
            ],
            [
                types.KeyboardButton(text="Первое блюдо"),
                types.KeyboardButton(text="Второе блюдо")
            ],
            [
                types.KeyboardButton(text="Десерт")
            ]
        ],
        resize_keyboard=True
    )
    await message.answer(
        text="Выберите блюдо",
        reply_markup=kb
    )


@dishes_button_router.message(F.text.lower() == "холодный напиток")
async def drink_handler(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    await message.answer("Холодные напитки", reply_markup=kb)

@dishes_button_router.message(F.text.lower() == "первое блюдо")
async def first_meal_handler(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    await message.answer("Первые блюда", reply_markup=kb)

@dishes_button_router.message(F.text.lower() == "второе блюдо")
async def second_meal_handler(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    await message.answer("Вторые блюда", reply_markup=kb)

@dishes_button_router.message(F.text.lower() == "десерт")
async def desert_meal_handler(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    await message.answer("Десерты", reply_markup=kb)