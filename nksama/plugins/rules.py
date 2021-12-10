from nksama import bot 
from nksama.db import database as db
from pyrogram import filters

@bot.on_message(filters.command(commands=('setrules')))

async def set_rules(client, message):

    

    chat_id = message.chat.id 

    chat_title = message.chat.title

   

    

    if not (

        len(message.command) >= 2

    ):

        await message.reply(

            "You need to give me rules to set!",

            quote=True

        )

        return

    

    get_rules = message.text.markdown[len(message.command[0]) + 2 :]

     db(chat_id, get_rules)

    await message.reply(

        f"New rules for {html.escape(chat_title)} set successfully!",

        quote=True

    )


  

