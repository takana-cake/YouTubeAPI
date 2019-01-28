# YouTube-Script

twitterの部分は全引用</br>
https://github.com/takana303/Tweepy-script</br>

https://developers.google.com/youtube/v3/code_samples/python?hl=ja#add_a_channel_subscription
https://developers.google.com/api-client-library/python/guide/aaa_client_secrets

<pre>
print("---------------")
print(deve_b.channels().list(part=parameter,id=CHANNEL_ID).execute()["items"][0]["snippet"]["title"])
print("チャンネル登録者数:" + deve_b.channels().list(part=parameter,id=CHANNEL_ID).execute()["items"][0]["statistics"]["subscriberCount"])
print("投稿数:" + deve_b.channels().list(part=parameter,id=CHANNEL_ID).execute()["items"][0]["statistics"]["videoCount"])
</pre>

<pre>
json_dict{
	"name":"名前",
	"belong":"所属",
	"twitter":{
		"screen":SCREEN_NAME,
		"follower":"",
		"Profileflag":,
		"hashtagflag":,
		"Query":{},
		"TLflag":,
		"RTflag":,
		"videoflag":,
		"gifflag":,
		"urls":[]
	},
	"youtube":[
		{"channel":channel, subscript":subscript}
	]
}
</pre>

YouTube Data API</br>
https://google-api-client-libraries.appspot.com/documentation/youtube/v3/python/latest/index.html</br>
googleapis/google-api-python-client: ?? The official Python client library for Google's discovery based APIs.</br>
https://github.com/googleapis/google-api-python-client</br>

YouTube Data API (v3)のサンプルコードを解釈する。 - Qiita</br>
https://qiita.com/somarihair/items/78df9383400e321233ce</br>

Developer's Guide: Python ?|? YouTube ?|? Google Developers</br>
https://developers.google.com/youtube/1.0/developers_guide_python</br>

YouTuberマイニング #1 - Qiita</br>
https://qiita.com/myaun/items/7425ad451638c6367f20</br>

youtubeAPIを使って特定のチャンネルの動画タイトルを取得 - Qiita</br>
https://qiita.com/y-i-p/items/fdd9aaaccc0ba377261b</br>

YouTube APIとは：Data API v3を使って動画情報を取得してみた。 | D2Cスマイル</br>
https://www.d2c-smile.com/201611018039</br>

YouTube Data APIを触ってみよう【導入編】｜プラカンブログ | WEB制作会社プラスデザインカンパニー</br>
https://www.plusdesign.co.jp/blog/?p=7752</br>

YouTube Data API v3 で、特定チャンネルの最新の動画IDを取得するには？ │ スーパーハリネズミ</br>
https://www.superharinezumi.com/entry/youtube-data-api-v3</br>

YouTube Data API v3を試してみました｜YouTubeAPI｜音声・動画配信（ストリーミング）｜PHP & JavaScript Room</br>
http://phpjavascriptroom.com/?t=strm&p=youtubedataapi_v3_list</br>

Youtube API V3でユーザーがアップロードした動画リストを取得する方法 [無料ホームページ作成クラウドサービス　まめわざ]</br>
https://mamewaza.com/support/blog/get-youtube-videoid-list.html</br>
