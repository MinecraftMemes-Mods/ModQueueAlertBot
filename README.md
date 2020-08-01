![logo](https://i.imgur.com/RgdAOWZ.png)

# Modqueue Alert Bot

Configure alerts for your Discord server when the modqueue fills up.

![screenshot of the bot's functionality](https://i.imgur.com/i4ByYTS.png)

## Config

Create a `.env` file at the top of the file tree. Fill it with the following content:

```
BOT_USERNAME= # The username of your bot account. That can be any account with the 'posts' permission on the subreddit.
PASSWORD= # Password of the aforementioned account

# Get those at https://reddit.com/prefs/apps by creating a new script-type app
CLIENT_ID=
CLIENT_TOKEN=

SUBREDDIT= # The subreddit you want to supervise
WEBHOOK_URL= # URL of the webhook. Learn how to create a hook and obtain the link here: https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks

FIRST_ALERT_LEN= # Minimum posts in the queue to trigger the first alert
SECOND_ALERT_LEN= # Minimum posts in the queue to trigger the second alert

MOD_ROLE_ID= # ID of the Discord role that the bot will ping when the queue reaches the second alert threshold.

INTERVAL= # How often the bot should check the queue (in seconds)
```
