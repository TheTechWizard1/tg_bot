from aiogram import Router, F, types


dishes_router = Router()


@dishes_router.message(F.text == 'холодный напиток')
async def dishes_handler(message: types.Message):
    photo = types.FSInputFile('imagespy/квас.jpg')
    await message.answer_photo(
        photo=photo,
        caption="Квас")


@dishes_router.message(F.text == 'первое блюдо')
async def disnes_handler(message: types.Message):
    photo2 = types.FSInputFile('imagespy/борщ.jpg')
    await message.answer_photo(
        photo=photo2,
        caption='Борщ')

@dishes_router.message(F.text == 'второе блюдо')
async def disnes_handler(message: types.Message):
    photo2 = types.FSInputFile('imagespy/второе.jpg')
    await message.answer_photo(
        photo=photo2,
        caption='Лазанья')

@dishes_router.message(F.text == 'десерт')
async def disnes_handler(message: types.Message):
    photo2 = types.FSInputFile('imagespy/дес.jpg')
    await message.answer_photo(
        photo=photo2,
        caption='Лазанья')


