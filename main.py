from os import getenv

import asyncio
from aiogram import Bot, Dispatcher, F, Router
from aiogram.filters.command import CommandStart
from aiogram.types import Message, ReplyKeyboardRemove
from dotenv import load_dotenv

user = Router()
@user.message(CommandStart())
async def cmd_comand(message: Message, state: FSMContext):
    await message.answer('Добро пожаловать в бота!\n\nВведите ваше имя:',
                         reply_markup=ReplyKeyboardRemove())
    await state.set_state(Reg.name)

async def main():
    load_dotenv()
    tg_tok = getenv('TOKEN')
    bot = Bot(token = tg_tok)
    db = Dispatcher()
    db.include_router(user)
    await db.start_polling(bot)

if __name__ == "__main__":
    try:
        import asyncio
        asyncio.run(main())
    except KeyboardInterrupt:
        pass