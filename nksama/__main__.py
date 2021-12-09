from nksama import bot , musicbot
import logging




if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    bot.run()
    musicbot.start()
    with bot:
        bot.send_message(-1001544622735 , "I'm Now online")
    
def main():

    if SUPPORT_CHAT is not None and isinstance(SUPPORT_CHAT, str):
        try:
            dispatcher.bot.sendMessage(f"@mano_sanjiro_support", "[I am ready to fight](https://telegra.ph/file/a11036803a02158d4ab3d.mp4)", parse_mode=ParseMode.MARKDOWN) 
        except Unauthorized:
            LOGGER.warning(
                "Bot isnt able to send message to support_chat, go and check!")
        except BadRequest as e:
            LOGGER.warning(e.message)
