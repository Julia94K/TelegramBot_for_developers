import json

from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.markdown import hlink
from aiogram.dispatcher.filters import Text
from Config import token

bot = Bot(token=token, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)


@dp.message_handler(commands="start")
async def start(message: types.Message):  # функция по команде старт для вывода кнопок
    start_buttons = ["Новости JavaRush", "Новости The Code", "Новости TechCrunch"]
    keyword = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyword.add(*start_buttons)
    await message.answer("Приветствую! Выбери действие ", reply_markup=keyword)


@dp.message_handler(Text(equals="Новости JavaRush"))
async def get_all_news(message: types.Message):  # функция для вывода всех новостей из списка
    with open("javarush_data_base.json") as file:
        news_file = json.load(file)

    for k, v, in sorted(news_file.items()):
        news = f"{hlink(v['post_title'], v['post_url'])}"  # вшиваем url в название новости

        await message.answer(news)


@dp.message_handler(Text(equals="Новости The Code"))
async def get_all_news(message: types.Message):
    with open("javarush_data_base.json") as file:
        news_file = json.load(file)

    for k, v, in sorted(news_file.items()):
        news = f"{hlink(v['post_title'], v['post_url'])}"

        await message.answer(news)

if __name__ == '__main__':
    executor.start_polling(dp)
