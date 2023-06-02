import logging

from aiogram import Bot, Dispatcher, executor, types
import wikipedia
wikipedia.set_lang('uz')

API_TOKEN = '5851858948:AAFq9Xg_lMjhZOmED4ztZgomUOhKph9n7dE'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Assalomu Alaykum. Mu WikiBotman\n Menga biror xabar yuboring!\nMen sizga shu haqida ma'lumot beraman.")



@dp.message_handler()
async def sentWiki(message: types.Message):
    try:
        respond = wikipedia.summary(message.text)
        await message.answer(respond)
    except:
        await message.answer("Bu mavzuga oid maqola topilmadi!\nBoshqa narsa kiritib ko'ring!")



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)