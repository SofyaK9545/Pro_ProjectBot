from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from secret import secret
import asyncio
import logging
import sys
sys.path.append("/path/to/dictionary")
from dictionary import d,a

logging.basicConfig(level=logging.INFO)
token=secret.get('BOT_API_TOKEN')
bot=Bot(token)
dp=Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    kb=[
        [types.KeyboardButton(text = "➡️Задание 1")],
        [types.KeyboardButton(text="Просмотреть все задания")]
    ]
    keyboard=types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer("Привет!\nЯ бот, который поможет тебе в разработке проекта",
                        reply_markup=keyboard)

@dp.message(F.text == "➡️Задание 1")
async def button(message: types.Message):
    await message.answer(d[1], reply_markup=types.ReplyKeyboardRemove())
    kb = [
        [types.KeyboardButton(text="➡️Задание 2")],
        [types.KeyboardButton(text="Просмотреть все задания")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer("Как будешь готов(а) жми на кнпоку👇",
                         reply_markup=keyboard)

@dp.message(F.text == "➡️Задание 2")
async def button(message: types.Message):
    await message.answer(d[2], reply_markup=types.ReplyKeyboardRemove())
    kb = [
        [types.KeyboardButton(text="➡️Задание 3")],
        [types.KeyboardButton(text="Просмотреть все задания")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer("Ты уже делаешь первые шаги👶",
                         reply_markup=keyboard)

@dp.message(F.text == "➡️Задание 3")
async def button(message: types.Message):
    await message.answer(d[3], reply_markup=types.ReplyKeyboardRemove())
    kb = [
        [types.KeyboardButton(text="➡️Задание 4")],
        [types.KeyboardButton(text="Просмотреть все задания")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer("Я верю в тебя.Ты будешь у цели.🚶‍➡️",
                         reply_markup=keyboard)

@dp.message(F.text == "➡️Задание 4")
async def button(message: types.Message):
    await message.answer(d[4], reply_markup=types.ReplyKeyboardRemove())
    kb = [
        [types.KeyboardButton(text="➡️Задание 5")],
        [types.KeyboardButton(text="Просмотреть все задания")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer("Супер!👌 Но отдыхать пока рано☀️",
                         reply_markup=keyboard)

@dp.message(F.text == "➡️Задание 5")
async def button(message: types.Message):
    await message.answer(d[5], reply_markup=types.ReplyKeyboardRemove())
    kb = [
        [types.KeyboardButton(text="➡️Задание 6")],
        [types.KeyboardButton(text="Просмотреть все задания")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer("Ты делаешь успехи🎉",
                         reply_markup=keyboard)

@dp.message(F.text == "➡️Задание 6")
async def button(message: types.Message):
    await message.answer(d[6], reply_markup=types.ReplyKeyboardRemove())
    kb = [
        [types.KeyboardButton(text="➡️Задание 7")],
        [types.KeyboardButton(text="Просмотреть все задания")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer("Так держать!🫡",
                         reply_markup=keyboard)

@dp.message(F.text == "➡️Задание 7")
async def button(message: types.Message):
    await message.answer(d[7], reply_markup=types.ReplyKeyboardRemove())
    kb = [
        [types.KeyboardButton(text="➡️Задание 8")],
        [types.KeyboardButton(text="Просмотреть все задания")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer("Пока что рано расслабляться🚨",
                         reply_markup=keyboard)

@dp.message(F.text == "➡️Задание 8")
async def button(message: types.Message):
    await message.answer(d[8], reply_markup=types.ReplyKeyboardRemove())
    kb = [
        [types.KeyboardButton(text="➡️Задание 9")],
        [types.KeyboardButton(text="Просмотреть все задания")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer("Давай поднажмём🏇",
                         reply_markup=keyboard)

@dp.message(F.text == "➡️Задание 9")
async def button(message: types.Message):
    await message.answer(d[9], reply_markup=types.ReplyKeyboardRemove())
    kb = [
        [types.KeyboardButton(text="➡️Задание 10")],
        [types.KeyboardButton(text="Просмотреть все задания")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer("Выполни это задание, и ты будешь молодец⭐🏆",
                         reply_markup=keyboard)

@dp.message(F.text == "➡️Задание 10")
async def button(message: types.Message):
    await message.answer(d[10], reply_markup=types.ReplyKeyboardRemove())
    kb = [
        [types.KeyboardButton(text="➡️Задание 11")],
        [types.KeyboardButton(text="Просмотреть все задания")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer("Ты молодец🤩🥳",
                         reply_markup=keyboard)

@dp.message(F.text == "➡️Задание 11")
async def button(message: types.Message):
    await message.answer(d[11], reply_markup=types.ReplyKeyboardRemove())
    kb = [
        [types.KeyboardButton(text="➡️Задание 12")],
        [types.KeyboardButton(text="Просмотреть все задания")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer("Ещё немного и ты справишься☺️👍",
                         reply_markup=keyboard)

@dp.message(F.text == "➡️Задание 12")
async def button(message: types.Message):
    await message.answer(d[12], reply_markup=types.ReplyKeyboardRemove())
    kb = [
        [types.KeyboardButton(text="➡️Задание 13")],
        [types.KeyboardButton(text="Просмотреть все задания")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer("Ещё чуть-чуть, ты сможешь👍",
                         reply_markup=keyboard)

@dp.message(F.text == "➡️Задание 13")
async def button(message: types.Message):
    await message.answer(d[6], reply_markup=types.ReplyKeyboardRemove())
    kb = [
        [types.KeyboardButton(text="Хочу начать сначала.")],
        [types.KeyboardButton(text="Просмотреть все задания")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer("Это было последнее задание.\nНадеюсь у тебя всё получится, удачи!!!❤️💯\n Если волнуешься, просто возьми пример у моря, поволнуся и успокойся.✅",
                         reply_markup=keyboard)

@dp.message(F.text == "Хочу начать сначала.")
async def button(message: types.Message):
    await message.answer("👌", reply_markup=types.ReplyKeyboardRemove())
    kb = [
        [types.KeyboardButton(text="➡️Задание 1")],
        [types.KeyboardButton(text="Просмотреть все задания")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer("Погнали!!!😁",
                         reply_markup=keyboard)

@dp.message(F.text == "Просмотреть все задания")
async def button(message: types.Message):
    await message.answer(a[1])

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__' :
    asyncio.run(main())