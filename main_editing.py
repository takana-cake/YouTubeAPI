#!/usr/bin python3
# _*_ coding: utf-8 _*_

import sys
import json
from apiclient.discovery import build
from apiclient.errors import HttpError

DEVELOPER_KEY = ""
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
CHANNEL_IDs = [ '', '' ]

deve_b = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

parameter = "id,snippet,statistics,contentDetails,topicDetails"

for CHANNEL_ID in CHANNEL_IDs:
	print("---------------")
	print(deve_b.channels().list(part=parameter,id=CHANNEL_ID).execute()["items"][0]["snippet"]["title"])
	print("チャンネル登録者数:" + deve_b.channels().list(part=parameter,id=CHANNEL_ID).execute()["items"][0]["statistics"]["subscriberCount"])
	print("投稿数:" + deve_b.channels().list(part=parameter,id=CHANNEL_ID).execute()["items"][0]["statistics"]["videoCount"])
