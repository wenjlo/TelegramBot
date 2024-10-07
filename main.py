import asyncio
from telegram import Bot
from config import TOKEN,GROUP_ID,BASE_URL
from tg_utils.send import send_video
import os

print('BASE_URL :',BASE_URL)
bot = Bot(token=TOKEN, base_url=f'{BASE_URL}/bot', base_file_url=f'{BASE_URL}/file/bot')

print(os.listdir('/send_tg/data/'))
if __name__ == "__main__":
    print(os.listdir('/send_tg/data/'))
    asyncio.run(send_video(bot=bot,group_id=GROUP_ID,video_path='/send_tg/data/PRED-704 - 1of6.mp4'))