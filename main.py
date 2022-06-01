from tinydb import TinyDB
import datetime
import neocities
import eel

nc = neocities.NeoCities(api_key="***REMOVED***")

db = TinyDB("../90ssite/posts.json")

@eel.expose
def uploadpost(title, body):
	db.insert({"title": title, "body": body, "date": str(datetime.datetime.now().strftime("%d.%m.%Y %H:%M"))})
	nc.upload(('../90ssite/posts.json', 'posts.json'))

@eel.expose
def uploadguest(title, body, date):
	# date (d.m.y H:M)
	db.insert({"name": name, "body": body, "date": date})
	nc.upload(('../90ssite/guestbook.json', 'guestbook.json'))

eel.init("web")
eel.start("main.html")