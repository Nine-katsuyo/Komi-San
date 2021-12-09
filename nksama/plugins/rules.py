
from nksama import bot 
from pyrogram import filters

@bot.on_message(filters.command('rules'))
def rules(_,message):
  message.reply('rules')
  

__help__ = """
 ❍ /rules*:* get the rules for this chat.

*Admins only:*
 ❍ /setrules <your rules here>*:* set the rules for this chat.
 ❍ /clearrules*:* clear the rules for this chat.
"""

__mod_name__ = "Rules"

