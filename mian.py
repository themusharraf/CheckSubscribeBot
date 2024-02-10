import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher, F
from aiogram.filters.command import Command
from aiogram.enums import ParseMode
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = "6752113285:AAFM7Wy86Q50-OlVpEI5jYZdZrzeAUzrj9U"

dp = Dispatcher()

check = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Submit", callback_data="submit")],
    [InlineKeyboardButton(text="Obuna", url="https://t.me/audiobooktestbot24")]
])


@dp.message(Command("start"))
async def start(message: Message, bot: Bot):
    await message.answer("Hello there, my", reply_markup=check)
    await bot.send_message(chat_id=-1002122098350,
                           text=f"botga yangi foydalanuvchi keldi {message.from_user.full_name}")


@dp.callback_query(F.data == "submit")
async def sub_callback(call: CallbackQuery, bot: Bot):
    user_status = await bot.get_chat_member(chat_id=-1002122098350, user_id=call.from_user.id)
    if user_status.status != "left":
        await bot.send_message(
            call.from_user.id, "ok"
        )
    else:
        await bot.send_message(call.from_user.id, 'not ok, subscribe please', reply_markup=check)
        text = ("Kanalga obuna bo'lmagansiz ⚠️"
                )
        show_alert = True
        await call.answer(text, show_alert=show_alert)


async def main() -> None:
    bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
