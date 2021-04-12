import json
import os
import sys

import praw
import requests
from dotenv import load_dotenv
from time import sleep
load_dotenv()

reddit = praw.Reddit(
    username=os.getenv('BOT_USERNAME'),
    password=os.getenv('PASSWORD'),
    client_id=os.getenv('CLIENT_ID'),
    client_secret=os.getenv('CLIENT_SECRET'),
    user_agent=f"r/{os.getenv('SUBREDDIT')}'s {os.getenv('BOT_USERNAME')}"
)


webhook_url = os.getenv('WEBHOOK_URL')

subreddit = os.getenv('SUBREDDIT')
first_alert = int(os.getenv('FIRST_ALERT_LEN'))
second_alert = int(os.getenv('SECOND_ALERT_LEN'))
modrole = os.getenv('MOD_ROLE_ID')

interval = int(os.getenv('INTERVAL'))


def send_message(message: str) -> None:
    requests.post(url=webhook_url, data=json.dumps({
        'content': message
    }), headers={
        'Content-Type': 'application/json'
    })


try:
    while True:
        modqueue_length: int = 0

        for i in reddit.subreddit(subreddit).mod.modqueue(limit=second_alert+1):
            modqueue_length += 1

        if modqueue_length > second_alert:
            send_message(f"<@&{modrole}>, the [modqueue](<https://reddit.com/r/{subreddit}/about/modqueue>) length has exceeded {second_alert}! Someone go check it out urgently!")
        elif modqueue_length > first_alert:
            send_message(f"The [modqueue](<https://reddit.com/r/{subreddit}/about/modqueue>) length has exceeded {first_alert}, someone go check it out!")

        sleep(interval)
except KeyboardInterrupt:
    sys.exit()
