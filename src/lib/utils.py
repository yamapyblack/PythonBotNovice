import os
import time
import requests

#load env
config = {
    "USER_ADDRESS": os.getenv("USER_ADDRESS"),
    "SECRET_KEY": os.getenv("SECRET_KEY"),
    "DISCORD_WEBHOOK_URL": os.getenv("DISCORD_WEBHOOK_URL")
}

def get_config():
    return config

def notify_discord(message):
    webhook_url = get_config()["DISCORD_WEBHOOK_URL"]
    current_time = time.strftime("%Y-%m-%d %H:%M:%S")
    data = {
        "content": f"{current_time}: {message}"
    }
    requests.post(webhook_url, json=data)
    print(message)
