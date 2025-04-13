#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG

import os
import logging
import time

from logging.handlers import RotatingFileHandler

from .translation import Translation

# Change Accordingly While Deploying To A VPS
APP_ID = int(os.environ.get("28712296"))

API_HASH = os.environ.get("
 25a96a55e729c600c0116f38564a635f")

BOT_TOKEN = os.environ.get("7778279666:AAGmGvBn3iqt8EhD1943fJpxTiuhaxd41P")

DB_URI = os.environ.get(mongodb+srv://lucas:lucas@lucas.miigb0j.mongodb.net/?retryWrites=true&w=majority&appName=lucas"")

USER_SESSION = os.environ.get("USER_SESSION")

VERIFY = {}

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            "autofilterbot.txt",
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

start_uptime = time.time()


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
