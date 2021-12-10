from nksama import bot 
from pyrogram import filters

@bot.on_message(filters.command('setrules'))
def set_rules
    chat_id = update.effective_chat.id
    msg = update.effective_message  # type: Optional[Message]
    raw_text = msg.text
    args = raw_text.split(None, 1)  # use python's maxsplit to separate cmd and args
    if len(args) == 2:
        txt = args[1]
        offset = len(txt) - len(raw_text)  # set correct offset relative to command
        markdown_rules = markdown_parser(
            txt, entities=msg.parse_entities(), offset=offset
        )

        sql.set_rules(chat_id, markdown_rules)
        update.effective_message.reply_text("Successfully set rules for this group.")
    
    
    
    from nksama import bot 

from pyrogram import filters

@bot.on_message(filters.command('setrules'))

def setrules(_,message):

  message.reply('

def s
                
                


    chat_id = update.effective_chat.id

    msg = update.effective_message  # type: Optional[Message]

    raw_text = msg.text

    args = raw_text.split(None, 1)  # use python's maxsplit to separate cmd and args

    if len(args) == 2:

        txt = args[1]

        offset = len(txt) - len(raw_text)  # set correct offset relative to command

        markdown_rules = markdown_parser(

            txt, entities=msg.parse_entities(), offset=offset

        )

        sql.set_rules(chat_id, markdown_rules)

        update.effective_message.reply_text("Successfully set rules for this group.")

    

    ')

  
