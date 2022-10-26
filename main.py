from tinydb import TinyDB
import urllib.request
import datetime
import neocities
import eel

nc = neocities.NeoCities(api_key="***REMOVED***")
urllib.request.urlretrieve("https://***REMOVED***/guestbook.json", "guestbook.json")
urllib.request.urlretrieve("https://***REMOVED***/posts.json", "posts.json")

@eel.expose
def uploadpost(title, body):
	db = TinyDB("posts.json")
	db.insert({"title": title, "body": body, "date": str(datetime.datetime.now().strftime("%d.%m.%Y %H:%M"))})
	nc.upload(('posts.json', 'posts.json'))
	eel.shitsposted()

@eel.expose
def uploadguest(title, body, date):
	# date (d.m.y H:M)
	db = TinyDB("guestbook.json")
	db.insert({"name": title, "body": body, "date": date})
	nc.upload(('guestbook.json', 'guestbook.json'))
	eel.shitsposted()

eel.init("web")
eel.start("main.html", size=(570, 400))
