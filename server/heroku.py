from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)
import os
import sys
import random

app = Flask(__name__)

YOUR_CHANNEL_ACCESS_TOKEN = os.environ["YOUR_CHANNEL_ACCESS_TOKEN"]
YOUR_CHANNEL_SECRET = os.environ["YOUR_CHANNEL_SECRET"]

line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(YOUR_CHANNEL_SECRET)

import markovify

with open('./data/learned_data.json', 'r') as f:
    text_model = markovify.Text.from_json(f.read())

text_list = []

@app.route("/sample", methods=['POST'])
def callback():

    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

text_list = []

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
  profile = line_bot_api.get_profile(event.source.user_id)
  for i in range(20):
    m = text_model.make_short_sentence(140)
    m = m.replace(' ', '')
    text_list.append(m)

  try:
    line_bot_api.reply_message(
      event.reply_token,
      TextSendMessage(text=random.choice(text_list)))
  except LineBotApiError as e:
    print(e)
    sys.exit(1)

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
