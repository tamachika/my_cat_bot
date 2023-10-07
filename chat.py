import os
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
from dotenv import load_dotenv
import openai


load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

system_content = os.getenv("CHATGPT_SYSTEM_CONTENT")
 

def chat_completion(user_content):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": system_content}, {"role": "user", "content": user_content}],
    )
    reply_message = completion.choices[0].message.content
    return reply_message


def main():
    user_content = "Hello!"
    reply_message = chat_completion(user_content)
    print(reply_message)


if __name__ == "__main__":
    main()