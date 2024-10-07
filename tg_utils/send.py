import os
import asyncio
from telegram import  InputMediaPhoto, InputMediaVideo
from telegram.error import NetworkError
from datetime import datetime
from telebot.types import InputMediaPhoto

async def send_media(bot,group_id,folder_path, folder_name):
    media_files = []
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            media_files.append(InputMediaPhoto(open(file_path, 'rb')))
        elif file.lower().endswith(('.mp4', '.avi', '.mov')):
            media_files.append(InputMediaVideo(open(file_path, 'rb')))

    # 分批发送媒体文件
    max_files_per_message = 10
    for i in range(0, len(media_files), max_files_per_message):
        media_group = media_files[i:i + max_files_per_message]
        if media_group:
            try:
                await bot.send_media_group(chat_id=group_id, media=media_group, caption=folder_name, read_timeout=1000,
                                           write_timeout=1000, connect_timeout=1000 )

                print(f"{datetime.now()} - Sent {len(media_group)} items from {folder_name}")
            except NetworkError as e:
                print(f"Failed to send due to {e}")
        await asyncio.sleep(5)  # 避免过快发送


async def send_video(bot,group_id,video_path):
    await bot.send_video(chat_id=group_id,video=open(video_path, 'rb'),
    read_timeout = 1000,
    write_timeout = 1000, connect_timeout = 1000,supports_streaming=True,width=1280,height=720
    )