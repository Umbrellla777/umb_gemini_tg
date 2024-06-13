####--------------------------------####
#--# Author:   by Umbrellla777      #--#
#--# Telegram: @Umbrellla777        #--#
#--# VK:       @Umbrellla777        #--#
####--------------------------------####

###########################
## Импорт библиотек
###########################
import sys
import asyncio
import time
import random

from google.cloud import aiplatform
from asyncio import sleep
from collections import deque
from telethon.sync import TelegramClient
from telethon import TelegramClient
from telethon import events

##from telethon                       import functions, types
##from telethon.tl.types              import ChatBannedRights
##from telethon.tl.functions.users    import GetFullUserRequest
##from telethon.tl.functions.channels import EditBannedRequest


###########################
## Цвет консоли
###########################
red = [206, 76, 54]
green = [68, 250, 123]
blue = [253, 127, 233]
yellow = [241, 250, 118]
orange = [255, 184, 107]


def colored(color, text):
    return "\033[38;2;{};{};{}m{}\033[38;2;255;255;255m".format(color[0], color[1], color[2], text)


###########################
## Настройки
###########################
api_id = int(sys.argv[1])
api_hash = str(sys.argv[2])
GOOGLE_CLOUD_API_KEY = AIzaSyC9C9AKPA-uSNJykmjhq9uSDJo9dLG32ts
aiplatform.init(location="us-central1", credentials=GOOGLE_CLOUD_API_KEY)  

## Connect
client = TelegramClient('users/current_user', api_id, api_hash)
client.start()


###########################
## Информация о аккаунте
###########################
entity = client.get_entity("me")
MY_ID = entity.id
print(
    "["
    + colored(green, "PROFILE: ")
    + str(entity.first_name)
    + " | " + colored(orange, "Id: ") + str(MY_ID)
    + " | " + colored(orange, "Uname: ") + "@" + str(entity.username)
    + "]"
) 
##########################
## Запрос .ai 
##########################
@client.on(events.NewMessage(pattern=r".ais+(.+)"))
async def handle_ai_request(event):
    try:
        # Извлекаем запрос пользователя
        request = event.pattern_match.group(1)

        # Используем Google Cloud AI Platform для получения ответа от Gemini
        endpoint = aiplatform.Endpoint(YOUR_ENDPOINT_NAME)
        response = endpoint.predict(instances=[{"text": request}])

        # Обрабатываем ответ
        if response.predictions:
            response_text = response.predictions[0]["text"]
            await event.reply(response_text)
        else:
            await event.reply("Произошла ошибка. Попробуйте позже.")
    except ValueError:
        await event.reply("Неверный формат запроса. Используйте: .ai [запрос]")


client.run_until_disconnected()
