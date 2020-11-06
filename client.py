#!/usr/local/bin/python3
# coding: utf-8

# NCMBot - client.py
# 10/26/20 19:32
#

__author__ = "Benny <benny.think@gmail.com>"

import logging
import os

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from telethon import TelegramClient

api_id = os.environ.get("API_ID") or 123421
api_hash = os.environ.get("API_HASH") or '123131'
client_ids = os.environ.get("CLIENT") or '1112'
message = os.environ.get("MESSAGE", "🙄️")

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(filename)s [%(levelname)s]: %(message)s')

client = TelegramClient('timer', api_id, api_hash, device_model="Timer", system_version="89", app_version="64")

scheduler = AsyncIOScheduler()


async def send_message():
    id_list = client_ids.split(",")
    logging.info("Sending info to %s", id_list)
    for user in id_list:
        entity = await client.get_entity(int(user))
        await client.send_message(entity, message)


scheduler.add_job(send_message, 'cron', hour='23', minute="55")
scheduler.start()

if __name__ == '__main__':
    client.start()
    client.run_until_disconnected()
