#!/usr/bin python3
# _*_ coding: utf-8 _*_

from apiclient.discovery import build
from apiclient.errors import HttpError

DEVELOPER_KEY = ""
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
deve_b = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

parameter = "id,snippet,statistics,contentDetails,topicDetails"
USERS = [ {user_name:"name", channel_id:"id"}, {user_name:"name", channel_id:"id"} ]
file_path_cap = ""

def _get_user_object():
	try:
		user_object = deve_b.channels().list(part=parameter,id=CHANNEL_ID).execute()
	except Exception as err:
		if _count < 2:
			_count = _count + 1
			err_subject = screen_name + " : "
			_log(err_subject, err_description)
			sleep(60)
			_get_user_object()

def _youtube_follow_counter_cap():
	user_name = USER["user_name"]
	channel_id = USER["channel_id"]
	counter = user_object["items"][0]["statistics"]["subscriberCount"]
	for kiri in [1000000, 100000, 10000, 1000, 100]:
		if counter % kiri ==0:
			url_user = "" + channel_id
			capture_banner_file = file_path_cap + user_name + "_" + kiri + "_" + date + ".jpg"
			cmd_capture_banner = "wkhtmltoimage --crop-h 380 --crop-w 1023 --crop-x 1 --crop-y 40 " + url_user + " " + capture_banner_file
			subprocess.call(cmd_capture_banner.split(), shell=False)
			break
		else:
			pass

for USER in USERS:
	user_object = _get_user_object(parameter, CHANNEL_ID)
	_youtube_follow_counter_cap()

