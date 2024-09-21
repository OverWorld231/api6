import telegram
import os
import random
import time


def main():
    tg_token = os.environ['TG_TOKEN']
    chat_id = os.environ['TG_CHAT_ID']
    bot = telegram.Bot(token=tg_token)

    with open("comics.png","rb") as f:
        bot.send_document(chat_id=chat_id, document=f)
        


if __name__ == "__main__":
   main()