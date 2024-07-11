from aiogram import types, Router
from aiogram.filters.command import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

feedback_router = Router()

class ReviewDialog(StatesGroup):
    name = State()
    phone_number = State()
    visit_date = State()
    food_rating = State()
    cleanliness_rating = State()
    extra_comments = State()


@feedback_router.message(Command('feedback'))
async def start_write_feedback(message: types.Message, state: FSMContext):
    await state.set_state(ReviewDialog.name)
    await message.answer('Как вас зовут?')

@feedback_router.message(ReviewDialog.name)
async def process_name(message: types.Message, state: FSMContext):
    await state.set_state(ReviewDialog.phone_number)
    await state.update_data(name=message.text)
    await message.answer('Ваш номер телефона?')

@feedback_router.message(ReviewDialog.phone_number)
async def process_phone_number(message: types.Message, state: FSMContext):
    phone_number = message.text
    if not phone_number.isdigit():
        await message.answer('Пожалуйста вводите только цифры')
        return
    await state.set_state(ReviewDialog.visit_date)
    await state.update_data(phone_number=message.text)
    await message.answer('Дата вашего посещения нашего заведения?')

@feedback_router.message(ReviewDialog.visit_date)
async def process_visit_date(message: types.Message, state: FSMContext):
    visit_date = message.text
    if not visit_date.isdigit():
        await message.answer('Пожалуйста вводите только цифры')
        return
    await state.set_state(ReviewDialog.food_rating)
    await state.update_data(visit_day=message.text)
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [types.KeyboardButton(text='Отлично')],
            [types.KeyboardButton(text='Хорошо')],
            [types.KeyboardButton(text='Удовлетворительно')],
            [types.KeyboardButton(text='Плохо')],
            [types.KeyboardButton(text='Очень плохо')]
        ],
        resize_keyboard=True
    )
    await message.answer('Как оцениваете качество еды?',reply_markup=kb)

@feedback_router.message(ReviewDialog.food_rating)
async def process_food_rating(message: types.Message, state: FSMContext):
    await state.set_state(ReviewDialog.cleanliness_rating)
    await state.update_data(food_rating=message.text)
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [types.KeyboardButton(text='Блестяще')],
            [types.KeyboardButton(text='Чисто')],
            [types.KeyboardButton(text='Местами грязно')],
            [types.KeyboardButton(text='Грязно')],
            [types.KeyboardButton(text='Очень грязно')]
        ]
    )
    await message.answer('Как оцениваете чистоту заведения?', reply_markup=kb)


@feedback_router.message(ReviewDialog.cleanliness_rating)
async def process_cleanliness_rating(message: types.Message, state: FSMContext):
    await state.set_state(ReviewDialog.extra_comments)
    await state.update_data(cleanliness_rating=message.text)
    await message.answer('Напишите дополнительный отзыв')


@feedback_router.message(ReviewDialog.extra_comments)
async def process_extra_comments(message: types.Message, state: FSMContext):
    await state.update_data(extra_comments=message.text)
    data = await state.get_data()
    print(data)
    await message.answer('Спасибо за ваш отзыв.')



