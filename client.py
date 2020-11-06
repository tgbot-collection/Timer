#!/usr/local/bin/python3
# coding: utf-8

# NCMBot - client.py
# 10/26/20 19:32
#

__author__ = "Benny <benny.think@gmail.com>"


from telethon import TelegramClient, sync

api_id = 1
api_hash = '2'
client_id = '3'
message = "时间4啊"

client = TelegramClient('timer', api_id, api_hash, device_model="Timer", system_version="89", app_version="64")

client.start()
client.send_message(int(client_id), message)
