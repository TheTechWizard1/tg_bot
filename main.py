import asyncio
import logging
from bot_config import bot,dp

from handlers.start import start_router
from handlers.echo import echo_router
from handlers.myinfo import myinfo_router
from handlers.random_recipe import random_recipe_router
from handlers.dishes import dishes_router


async def main():
    # Все команды
    dp.include_router(start_router)
    dp.include_router(myinfo_router)
    dp.include_router(random_recipe_router)
    dp.include_router(dishes_router)

    # Неправильная команда
    dp.include_router(echo_router)
    # Запуск бота
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())