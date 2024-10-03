from tinydb import TinyDB
import requests
import datetime
import neocities        # you need to install it yourself
import eel
import json

def get_remote_posts(url):
    response = requests.get(url)
    filepath = posts_filename
    if response.status_code == 200:
        with open(filepath, "wb") as file:
            file.write(response.content)
        return True
    else:
        return False

def load_config():
    with open("config.json", "r") as configfile:
        data = json.load(configfile)
    return data

def get_current_timedate():
    return str(datetime.datetime.now().strftime(format_string))

@eel.expose
def upload_new_post(title, body):
	db = TinyDB(posts_filename)
	db.insert({"title": title, "body": body, "date": get_current_timedate()})
	nc.upload((posts_filename, remote_directory + posts_filename))
	eel.indicate_post()

app_config = load_config()
nc_api_key = app_config["nc_api"]
nc_profile_name = app_config["nc_profile"]
custom_domain = True if app_config["custom_domain"].lower() == "true" else False
format_string = app_config["timedate_format"]
remote_directory = app_config["remote_directory"]

posts_name = "posts"
posts_filename = posts_name + ".json"
nc_url = nc_profile_name if custom_domain else (nc_profile_name + ".neocities.org")
url = "https://" + nc_url + "/" + remote_directory + posts_filename
get_remote_posts(url)

# Where your post file will be saved on your neocities page (DEFAULT: "")

nc = neocities.NeoCities(api_key=nc_api_key)

eel.init("web")
eel.start("main.html", size=(570, 400))
