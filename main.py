from tinydb import TinyDB
import urllib.request
import datetime
import neocities        # you need to install it yourself
import eel

# !!INSERT YOUR NEOCITIES API KEY HERE!!
neocities_api_key = "" 

# !!INSERT YOUR PROFILE NAME OR FULL CUSTOM DOMAIN HERE!!
neocities_profile_name = ""

custom_domain = False
neocities_url = neocities_profile_name if custom_domain else neocities_profile_name + ".neocities.org"

posts_name = "posts"
posts_filename = posts_name + ".json"

# Where your post file will be saved on your neocities page (DEFAULT: "")
web_post_directory = ""

nc = neocities.NeoCities(api_key=neocities_api_key)

# TODO: add a check if remote file exists
urllib.request.urlretrieve("https://" + neocities_url + "/" + web_post_directory + posts_filename, posts_filename)

# How do you want your date displayed on your posts (Default: "%d.%m.%Y %H:%M" = "20.1.2000 12:00")
format_string = "%d.%m.%Y %H:%M"

def get_current_timedate():
    return str(datetime.datetime.now().strftime(format_string))

@eel.expose
def upload_new_post(title, body):
	db = TinyDB(posts_filename)
	db.insert({"title": title, "body": body, "date": get_current_timedate()})
	nc.upload((posts_filename, web_post_directory + posts_filename))
	eel.indicate_post()

eel.init("web")
eel.start("main.html", size=(570, 400))
