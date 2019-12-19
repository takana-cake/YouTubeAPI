# YouTube-Script

ほぼ以下コードの引用</br>
https://github.com/takana-cake/Tweepy-script</br>


## やること
手入力でユーザを追加 or ユーザのアカウントがフォローしているユーザを追加</br>
追加したユーザのYoutubeチャンネルを登録(subscriptionすごく遅い)</br>
TLを収集(favは未実装)</br>
ハッシュタグをCSVに</br>
クエリサーチ(Queryの追加が未実装)</br>


## 残タスク
youtube apiのsecretファイル作成をinitに追加<br>
オブジェクトの名前と所属を更新<br>
ハッシュタグをQueryへ追加<br>
jsonをブラウザで閲覧＆編集<br>


## 必要なパッケージ
<pre>

</pre>


## 必要なモジュール
<pre>

</pre>


## youtube_client_secrets.jsonの内容
<pre>
{"installed":{
	"client_id":"<FILLIN>",
	"project_id":"<FILLIN>",
	"auth_uri":"https://accounts.google.com/o/oauth2/auth",
	"token_uri":"https://www.googleapis.com/oauth2/v3/token",
	"auth_provider_x509_cert_url":"https://www.googleapis.com/oauth2/v1/certs",
	"client_secret":"<FILLIN>",
	"redirect_uris":["urn:ietf:wg:oauth:2.0:oob","http://localhost"]
}}
</pre>


## db.jsonの内容

<pre>
json_dict = [
	{
		"name":"名前",
		"belong":"所属",
		"twitter":{
			"screen":SCREEN_NAME,
			"follower":USER_OBJECT.followers_count,
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
			{
				"title":title,
				"channel":channel, 
				"subscript":subscript,
				"videos":[
					{"id":videoId, "title":title, "view":viewCount, "day":ひづけ},
					...
				]
			},
			...
		]
	},
	...
]
</pre>


## php
|||
|||
|||


## ファイルツリー
<pre>
cwd
├ user01
│ ├ download
│ │ ├ MEDIAFILE
│ │ └ ...
│ └ yyyymmdd_user01_tags.csv
├ user02
├ ...
├ main.py
├ db.json
├ youtube_client_secrets.json
├ youtube_quickstart.json
├ index.php
└ yyyymmdd_log.txt
</pre>


## 参考サイト

### Youtube API
YouTube Data API</br>
https://google-api-client-libraries.appspot.com/documentation/youtube/v3/python/latest/index.html</br>
GoogleCloudPlatform/google-auth-library-python-oauthlib</br>
https://github.com/GoogleCloudPlatform/google-auth-library-python-oauthlib</br>
googleapis/google-api-python-client: ?? The official Python client library for Google's discovery based APIs.</br>
https://github.com/googleapis/google-api-python-client</br>
Python コード サンプル  |  YouTube Data API (v3)  |  Google Developers</br>
https://developers.google.com/youtube/v3/code_samples/python?hl=ja#add_a_channel_subscription</br>
Client Secrets  |  API Client Library for Python  |  Google Developers</br>
https://developers.google.com/api-client-library/python/guide/aaa_client_secrets</br>
Developer's Guide: Python ?|? YouTube ?|? Google Developers</br>
https://developers.google.com/youtube/1.0/developers_guide_python</br>

### API実装の参考にさせて頂きました
YouTubeAPIを使ってみた - Qiita</br>
https://qiita.com/tksnino/items/51c6dadfbf1e0214c89e</br>
YouTube Data API (v3)のサンプルコードを解釈する。 - Qiita</br>
https://qiita.com/somarihair/items/78df9383400e321233ce</br>

### 実際にAPIを使ってみる
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
Youtube API V3でユーザーがアップロードした動画リストを取得する方法</br>
https://mamewaza.com/support/blog/get-youtube-videoid-list.html</br>
