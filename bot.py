import os
import praw
import requests
from dotenv import load_dotenv
load_dotenv()

reddit = praw.Reddit(
    username=os.getenv('BOT_USERNAME'),
    password=os.getenv('PASSWORD'),
    client_id=os.getenv('CLIENT_ID'),
    client_secret=os.getenv('CLIENT_SECRET'),
    user_agent=f"r/{os.getenv('SUBREDDIT')}'s {os.getenv('BOT_USERNAME')}"
)

webhook_url = "https://discordapp.com/api/webhooks/738012677753929799/T26LHl9mjaCNdoFEanYAfX_ZgR9k7w7K6ZYZsffEnf0X_U34XZrlVaMs_5VoPvaa_7Vw"
payload = {"content": "content"}
headers = {"Content-Type": "application/json"}

if len(reddit.subreddit(os.getenv("SUBREDDIT")).mod.modqueue) > os.getenv("MODQUEUE_FIRST_ALERT_LEN"):
    payload["content"] = f"Mod Queue length has exceeded {os.getenv('MODQUEUE_FIRST_ALERT_LEN')}, someone go check it out!"
    requests.post(webhook_url, data=json.dumps(payload), headers=headers)

elif len(reddit.subreddit(os.getenv("SUBREDDIT")).mod.modqueue) > os.getenv("MODQUEUE_SECOND_ALERT_LEN"):
    payload["content"] = f"@Evoker Mod Queue length has exceeded {os.getenv('MODQUEUE_SECOND_ALERT_LEN')}, someone go check it out urgently!"
    requests.post(webhook_url, data=json.dumps(payload), headers=headers)
