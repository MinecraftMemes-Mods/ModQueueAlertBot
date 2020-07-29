import os
import praw
from dotenv import load_dotenv
load_dotenv()


reddit = praw.Reddit(
    username=os.getenv('BOT_USERNAME'),
    password=os.getenv('PASSWORD'),
    client_id=os.getenv('CLIENT_ID'),
    client_secret=os.getenv('CLIENT_SECRET'),
    user_agent=f"r/{os.getenv('SUBREDDIT')}'s {os.getenv('BOT_USERNAME')}"
)

if len(reddit.subreddit(os.getenv("SUBREDDIT")).mod.modqueue) > os.getenv("MODQUEUE_FIRST_ALERT_LEN"):
    # send message in discord
    pass
elif len(reddit.subreddit(os.getenv("SUBREDDIT")).mod.modqueue) > os.getenv("MODQUEUE_SECOND_ALERT_LEN"):
    # ping evokers in discord
    pass