from pyrogram import filters
from pyrogram.types.bots_and_keyboards import callback_game
from pyrogram.types.bots_and_keyboards.inline_keyboard_button import InlineKeyboardButton
from pyrogram.types.bots_and_keyboards.inline_keyboard_markup import InlineKeyboardMarkup 
from nksama import bot ,help_message
from typing import List , Any

HELPP_TEXT = """Yo, [mikey](https://telegra.ph/file/52c571e44fdb38e150dca.jpg) here a telegram management bot written on pyrogram library 

Check the following buttons for more info 

Report bugs at - @Mano_sanjiro_support"""

@bot.on_message(filters.command('help') | filters.command('help@KomiSanRobot'))
def bothelp(_,message):
    if message.chat.type == "private":
        keyboard = []
        for x in help_message:
            keyboard.append([InlineKeyboardButton(f"{x['Module_Name']}" , callback_data=f"help:{x['Module_Name']}")])


        bot.send_message(message.chat.id , HELPP_TEXT , reply_markup=InlineKeyboardMarkup(keyboard))

    else:
        bot.send_photo(message.chat.id , "https://telegra.ph/file/79d19fe1900a4946e50d4.jpg" ,  caption=HELPP_TEXT , reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("Pm me for more details"  , url="t.me/Sanjiro_probot?start=help")]
            
            ]))
