#!/usr/bin python3
# _*_ coding: utf-8 _*_

from apiclient.discovery import build
from apiclient.errors import HttpError
import re
import urllib.request
import subprocess
import datetime


DATE = datetime.datetime.today().strftime("%Y%m%d_%H%M_%S")
LOGFILE = "./" + DATE + "_log.txt"


def _apibuild(DEVELOPER_KEY):
	YOUTUBE_API_SERVICE_NAME = "youtube"
	YOUTUBE_API_VERSION = "v3"
	BUILD_API = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)
	return BUILD_API



def _log(err_subject, err_description):
	print(str(datetime.datetime.now()) + " : " + str(err_subject) + " : " + str(err_description))
	with open(LOGFILE,'a') as f:
		f.write(str(datetime.datetime.now()) + " : " + str(err_subject) + " : " + str(err_description) + "\n")



def _get_user_object(BUILD_API, USERNAME, CHANNEL_ID):
	parameter = "id,snippet,statistics,contentDetails,topicDetails"
	errcount = 0
	try:
		USER_OBJECT = BUILD_API.channels().list(part=parameter,id=CHANNEL_ID).execute()
		return USER_OBJECT
	except Exception as err_description:
		if errcount < 2:
			errcount = errcount + 1
			err_subject = USERNAME + " : _get_user_object"
			_log(err_subject, err_description)
			sleep(60)
			_get_user_object()



def _youtube_follow_counter_cap(USERNAME, CHANNEL_ID, USER_OBJECT):
	counter = USER_OBJECT["items"][0]["statistics"]["subscriberCount"]
	def _get_cap():
		url_user = "https://www.youtube.com/channel/" + CHANNEL_ID
		capture_banner_file = file_path_cap + USER_NAME + "_" + kiri + "_" + DATE + ".jpg"
		cmd_capture_banner = "wkhtmltoimage --crop-h 276 --crop-w 858 --crop-x 83 --crop-y 145 " + url_user + " " + capture_banner_file
		subprocess.call(cmd_capture_banner.split(), shell=False)
	for kiri in [1000000, 100000, 10000, 1000, 100]:
		if counter % kiri ==0:
			_get_cap()
			break
		else:
			pass



if __name__ == '__main__':
	USERS = [
		{'user_name': '', 'channel_id': '', 'nickname': ''}, 
	]
	file_path_cap = ""
	DEVELOPER_KEY = ""
	BUILD_API = _apibuild(DEVELOPER_KEY)
	for i, USER in enumerate(USERS):
		USER_NAME = USER["user_name"]
		CHANNEL_ID = USER["channel_id"]
		USER_OBJECT = _get_user_object(BUILD_API, USER)
		_youtube_follow_counter_cap(USER, USER_OBJECT)
