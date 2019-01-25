#!/usr/bin python3
# _*_ coding: utf-8 _*_

from apiclient.discovery import build
from apiclient.errors import HttpError
import re
import urllib.request
import subprocess
import datetime
import json


DATE = datetime.datetime.today().strftime("%Y%m%d_%H%M_%S")
LOGFILE = "./" + DATE + "_log.txt"


def get_authenticated_service(DEVELOPER_KEY):
	flow = flow_from_clientsecrets(CLIENT_SECRETS_FILE,
		scope=YOUTUBE_READ_WRITE_SCOPE,
		message=MISSING_CLIENT_SECRETS_MESSAGE)
	credentials = storage.get()
	if credentials is None or credentials.invalid:
		credentials = run_flow(flow, storage, args)
	return build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
		http=credentials.authorize(httplib2.Http()))


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



def _channel_split(URL):
	if "channel" in URL:
		CHANNEL_ID = x.rsplit("/channel/")[1]
		CHANNEL_ID = CHANNEL_ID.split("?")[0]
	return CHANNEL_ID



def _add_subscription(BUILD_API, CHANNEL_ID):
	try:
		add_subscription_response = BUILD_API.subscriptions().insert(part='snippet',body=dict(snippet=dict(resourceId=dict(channelId=CHANNEL_ID)))).execute()
	except Exception as err_description:
		err_subject = CHANNEL_ID + " : _add_subscription"
		_log(err_subject, err_description)
		sleep(60)



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



def _parser():
	parser = argparse.ArgumentParser(
		usage=' python3 main.py [json-file]\n\\n\
	nohup python3 main.py [json-file] &',
		add_help=True,
		formatter_class=argparse.RawTextHelpFormatter
		)
	parser.add_argument("json_file", help="please set DBfile.json.", type=str, nargs=1, metavar="[json-file]")
	return parser.parse_args()



if __name__ == '__main__':
	cmd_args = _parser()
	DB_file = os.path.dirname(cmd_args.json_file[0]) + "/" + os.path.basename(cmd_args.json_file[0])
	date = datetime.datetime.today().strftime("%Y%m%d_%H%M_%S")
	LOGFILE = os.path.dirname(cmd_args.json_file[0]) + "/" + date + "_log.txt"
	f = open(DB_file,'r')
	json_dict = json.load(f)
	f.close()
	DEVELOPER_KEY = ""
	api = _apibuild(DEVELOPER_KEY)
	for i, USER in enumerate(json_dict):
		if "url" in USER:
			for u in USER["url"]
			CHANNEL_ID = _channel_split(u)
			_add_subscription(api, CHANNEL_ID)
