import logging
import os
import slack
import asyncio
import ssl as ssl_lib
import config
# from perotfact import perotFact
import pandas as pd
import random


df = pd.read_csv('facts.csv', sep='\n')

@slack.RTMClient.run_on(event="message")
def message(**payload):
    data = payload["data"]
    web_client = payload["web_client"]
    channel_id = data.get("channel")
    user_id = data.get("user")
    text = data.get("text")
    print(text, type(text))
    if text is not None:
        if "!perotfact" in text:
            print(user_id)
            n = df.shape[0]
            fact = df.iloc[random.randint(0, n)]['Facts']
            web_client.chat_postMessage(
                channel=channel_id,
                text=f"Hi <@{user_id}>! " + fact
            )

if __name__ == "__main__":
    slack_token = config.SLACK_BOT_TOKEN
    rtm_client = slack.RTMClient(token=slack_token)
    rtm_client.start()
