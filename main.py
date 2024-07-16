from pydoc import html

from aiogram.enums import ParseMode

from data import getAllData
import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from config_reader import config
from aiogram.client.default import DefaultBotProperties
from aiogram.utils.formatting import Text, Bold

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token=config.bot_token.get_secret_value(), default=DefaultBotProperties(parse_mode='HTML'))
#bot = Bot(token="")
# Диспетчер
dp = Dispatcher()

# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("<i><b>Hello</b>!</i>")

@dp.message(F.text)
async def echo_with_time(message: types.Message):
    res = getAllData(message.text)
    for i in range(len(res)):
        res_str = str(list(res.keys())[i])+"\n"
        res_list = list(res.values())[i]
        for j in range(len(res_list)):
            res_str += str(res_list[j][0]) + "\nЦена:" + str(res_list[j][1]) + " руб.\n\n"
        await message.answer(res_str, parse_mode="HTML")
@dp.message(Command("dice"))
async def cmd_dice(message: types.Message):
    await message.answer_dice(emoji="🎲")
# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
    #maxiDoCsv('печенье')
    #magnitDoCsv("печенье")



