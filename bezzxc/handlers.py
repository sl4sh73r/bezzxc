from main import bot,dp
from aiogram.types import Message
from config import admin_id

async  def send_to_admin(dp):
    await bot.send_message(chat_id=admin_id,text="bot is ready")

@dp.message_handler()
async def echo(message: Message):
    text=f"Привет,спасибо что написал:{message.text}"
    await message.answer(text=text)