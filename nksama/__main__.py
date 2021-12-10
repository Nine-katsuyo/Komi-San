from nksama import bot , musicbot
import logging




if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    bot.run()
    musicbot.start()
    with bot:
        bot.send_video(-1001747095926 , "https://telegra.ph/file/a11036803a02158d4ab3d.mp4", caption="I am ready to fight")
    
