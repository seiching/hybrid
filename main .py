from chatgpt import ChatGPT

from flask import Flask, request, abort

from linebot.v3 import (
    WebhookHandler
)
from linebot.v3.exceptions import (
    InvalidSignatureError
)
from linebot.v3.messaging import (
    Configuration,
    ApiClient,
    MessagingApi,
    ReplyMessageRequest,
    TextMessage
)
from linebot.v3.webhooks import (
    MessageEvent,
    TextMessageContent
)

app = Flask(__name__)
chatgpt = ChatGPT()
inputmsg='最近一次重開機後客戶問的問題如下 '
outputmsg='Hybrid給的答案如下:\n '
import os
configuration = Configuration(access_token=os.getenv("LINE_CHANNEL_ACCESS_TOKEN"))
handler = WebhookHandler(os.getenv("LINE_CHANNEL_SECRET"))
@app.route('/')
def home():
    return 'Hello, World!'

@app.route("/webhook", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        app.logger.info("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'
def appendtext(filename, id, msg):
    with open(filename, 'a') as f:
        f.write(f'{id}: {msg}\n')
        
print('ok')
@handler.add(MessageEvent, message=TextMessageContent)
def handle_message(event):
   
    global inputmsg 
    global outputmsg
    user_id = event.source.user_id
    appendtext('userprompt',user_id,event.message.text )
    if event.message.type != "text":
        return
    if event.message.text !='q' and event.message.text !='Q'\
       and event.message.text !='a' and event.message.text !='A':
        inputmsg=inputmsg+'\n'+event.message.text
        
   
        
  
    
    with ApiClient(configuration) as api_client:
       
        line_bot_api = MessagingApi(api_client)
        if event.message.text == "q" or event.message.text == "Q" :
            reply_msg=inputmsg
            line_bot_api.reply_message_with_http_info(
            ReplyMessageRequest(
                reply_token=event.reply_token,
                messages=[TextMessage(text=reply_msg)]
                #messages=[TextMessage(text=event.message.text)]
               )
            ) 
            return
        if event.message.text == "a" or event.message.text == "A" :
            reply_msg=outputmsg 
            line_bot_api.reply_message_with_http_info(
            ReplyMessageRequest(
                reply_token=event.reply_token,
                messages=[TextMessage(text=reply_msg)]
                #messages=[TextMessage(text=event.message.text)]
               )
            ) 
            return
        chatgpt.add_msg(f"HUMAN:{event.message.text}?\n")
        reply_msg = chatgpt.get_response().replace("AI:", "", 1)
        chatgpt.add_msg(f"AI:{reply_msg}\n")
        outputmsg=outputmsg+'\n'+reply_msg
        line_bot_api.reply_message_with_http_info(
            ReplyMessageRequest(
                reply_token=event.reply_token,
                messages=[TextMessage(text=reply_msg)]
                #messages=[TextMessage(text=event.message.text)]
            )
        )

if __name__ == "__main__":
    #app.run()
    app.run( # Starts the site
		host='0.0.0.0',  # EStablishes the host, required for repl to detect the site
		port=8000  # Randomly select the port the machine hosts on.
    )