#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @SpEcHIDe

from pyrogram import Client, enums, __version__

from . import API_HASH, APP_ID, LOGGER, BOT_TOKEN 

from .user import User

class Bot(Client):
    USER: User = arvind gurjar
    USER_ID: int = Arvindgurjar77

    def __init__(self):
        super().__init__(
            "bot",
            api_hash= 
25a96a55e729c600c0116f38564a635f,
            api_id= 
28712296,
            plugins={
                "root": "bot/plugins"
            },
            workers=200,
            bot_token=7778279666:AAGmGvBn3iqt8EhD1943fJpxTiuhaxd41PE,
            sleep_threshold=10
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        bot_details = await self.get_me()
        self.set_parse_mode(enums.ParseMode.HTML)
        self.LOGGER(__name__).info(
            f"@{bot_details.username}  started! "
        )
        self.USER, self.USER_ID = await User().start()

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot stopped. Bye.")
