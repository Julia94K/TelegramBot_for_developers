import json

from aiogram import Bot, Dispatcher, executor, types
#added
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
#
from aiogram.utils.markdown import hlink
from aiogram.dispatcher.filters import Text
from Config import token
from Javarush_parser import get_news
from Code_parser import get_news_code
from TechCrunch import get_news_tech1



bot = Bot(token=token, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)


@dp.message_handler(commands="start")
async def start(message: types.Message):  # функция по команде старт для вывода кнопок
    start_buttons = ['Новости JavaRush', "More on Java Rush", "Новости КОД", "Новости TechCrunch"]
    keyword = types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=2)
    keyword.add(*start_buttons)
    await message.answer("Приветствую! Выбери действие ", reply_markup=keyword)

#настраиваем клавиатуру
urlkb = InlineKeyboardMarkup(row_width=1)
urlButton = InlineKeyboardButton(text='Задачи Javarush', url='https://javarush.ru/tasks')
urlButton2 = InlineKeyboardButton(text='Лекции Javarush',url='https://javarush.ru/quests/lectures')
urlkb.add(urlButton,urlButton2)

#метод для вызова Inlinekeyboard с кнопками-ссылками
@dp.message_handler(Text(equals='More on Java Rush'))
async def url_message(message:types.Message):
    await message.answer('Links:',reply_markup=urlkb)


@dp.message_handler(Text(equals="Новости JavaRush"))
async def get_all_news(message: types.Message):  # функция для вывода всех новостей из списка
    #загрузи джейсон заново
    get_news()
    with open("javarush_data_base.json") as file:
        news_file = json.load(file)

    for k, v, in sorted(news_file.items()):
        news = f"{hlink(v['post_title'], v['post_url'])}"  # вшиваем url в название новости

        await message.answer(news)


@dp.message_handler(Text(equals="Новости КОД"))
async def get_all_news(message: types.Message):
    #загрузи джейсон заново
    get_news_code()
    with open("code_data_base.json") as file:
        news_file = json.load(file)

    for k, v, in sorted(news_file.items()):
        news = f"{hlink(v['post_title'], v['post_url'])}"

        await message.answer(news)


@dp.message_handler(Text(equals="Новости TechCrunch"))
async def get_news_tech(message: types.Message):
    #загрузи джейсон заново
    get_news_tech1()
    with open("techcrunch_data_base.json") as file:
        news_file = json.load(file)

    for k, v, in sorted(news_file.items()):
        news = f"{hlink(v['article_title'], v['article_url'])}"

        await message.answer(news)

if __name__ == '__main__':
    executor.start_polling(dp)
