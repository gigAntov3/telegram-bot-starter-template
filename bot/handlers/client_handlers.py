from aiogram import types
from aiogram import Dispatcher
from aiogram.filters import Command

from aiogram_dialog import DialogManager, StartMode

from bot.dialogs.client_menu.states import MainClient

from bot import db
    
async def start_client(message: types.Message, dialog_manager: DialogManager):
    await db.add_user(message.chat.id, message.from_user.first_name, message.from_user.username)
    await dialog_manager.start(state=MainClient.main, data={"user_id": message.chat.id}, mode=StartMode.RESET_STACK)   
    
def register_client_handlers(dp: Dispatcher):
    dp.message.register(start_client, Command("start"))