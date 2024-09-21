import requests
import os
import telegram
import random
from dotenv import load_dotenv

def download_image(url,filename):
  response = requests.get(url)
  response.raise_for_status()
  with open(filename, 'wb') as file:
   file.write(response.content)

def get_info_comics(number):
  url = f"https://xkcd.com/{number}/info.0.json"
  response = requests.get(url)
  response.raise_for_status()
  link_img = response.json()["img"]
  comentarion_author = response.json()["alt"]
  return link_img, comentarion_author

def upload_telegram(tg_token,chat_id,caption):
  bot = telegram.Bot(token=tg_token)
  with open("comics.png","rb") as f:
      bot.send_photo(chat_id=chat_id, photo=f,caption=caption)

def random_comics():
  url = "https://xkcd.com/info.0.json" 
  response = requests.get(url)
  response.raise_for_status()
  number_of_comics = response.json()["num"]
  random_number = random.randint(1,number_of_comics)
  return random_number

def main():
  load_dotenv()
  tg_token = os.environ['TG_TOKEN']
  chat_id = os.environ['TG_CHAT_ID']
  filename = 'comics.png'
  random_number = random_comics()
  link_img,comentarion_author = get_info_comics(random_number)
  download_image(link_img,filename)
  upload_telegram(tg_token,chat_id,comentarion_author)
  os.remove(filename)

if __name__ == "__main__":
   main()

  







