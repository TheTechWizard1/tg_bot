from aiogram import types, Router, F
from aiogram.filters.command import Command


start_router = Router()

@start_router.message(Command("start"))
async def start_handler(message: types.Message):
    # print(message.from_user)
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text='О нас', callback_data='about_us'),
                types.InlineKeyboardButton(text='Наш сайт', url='https://pythonbar.kg/')
            ],
            [
                types.InlineKeyboardButton(text='Наш адрес', callback_data='address'),
                types.InlineKeyboardButton(text='Контакты', callback_data='contact')
            ],
            [
                types.InlineKeyboardButton(text='Наш инстаграм', url='https://www.instagram.com/pythonbar/'),
                types.InlineKeyboardButton(text='График работы', callback_data='work_day')
            ],
            [
                types.InlineKeyboardButton(text='Отзывы', callback_data='feedback'),
                types.InlineKeyboardButton(text='Наши вакансии', callback_data='jobs')
            ],
            [
                types.InlineKeyboardButton(text='Оставить отзыв', callback_data='feedback')
            ]
        ]
    )

    await message.reply(f"Привет, {message.from_user.first_name}. Наш бот для бара Python Bar&Coffee.", reply_markup=kb)

@start_router.callback_query(F.data == 'about_us')
async def about_us_handler(callback: types.CallbackQuery):
    await callback.message.answer('Добро пожаловать в "Python Bar&Coffee" - оазис вкуса и уюта в г. Бишкек. '
                                  '"Python Bar&Coffee" - не просто очередной бар, кафе, это место, где встречаются интересные люди, элитные алкогольные напитки, великолепная кухня, хорошее настроение и ароматные кальяны.')

@start_router.callback_query(F.data == 'address')
async def address_handler(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.answer('Улица Байтик Баатыра, 4/2, Бишкек')

@start_router.callback_query(F.data == 'contact')
async def contact_handler(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.answer('W/A +996 778 911 911')

@start_router.callback_query(F.data == 'work_day')
async def work_day_handler(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.answer('Круглосуточно 24/7')
#
@start_router.callback_query(F.data == 'feedback')
async def feedback_handler(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.answer('Еда: 5 из 5  |  Сервис: 5 из 5  |  Атмосфера: 5 из 5')

@start_router.callback_query(F.data == 'jobs')
async def jobs_handler(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.answer('Помощник повара \nКассир \nОфициант')

