from nksama import bot , musicbot, dispatcher
import logging




if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    bot.run()
    musicbot.start()
    dispatcher.bot.send_video(-1001747095926 , "https://telegra.ph/file/a11036803a02158d4ab3d.mp4", caption="I am ready to fight")
    
