from prompt import Prompt

import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")


class ChatGPT:

  def __init__(self):
    # self.prompt = Prompt()
    self.model = os.getenv("OPENAI_MODEL",default="gpt-3.5-turbo")
    # default = "gpt-4")
    self.temperature = float(os.getenv("OPENAI_TEMPERATURE", default=0))
    self.frequency_penalty = float(
      os.getenv("OPENAI_FREQUENCY_PENALTY", default=0))
    self.presence_penalty = float(
      os.getenv("OPENAI_PRESENCE_PENALTY", default=0.6))
    self.max_tokens = int(os.getenv("OPENAI_MAX_TOKENS", default=240))

  def get_response(self):
    response = openai.ChatCompletion.create(
      model=self.model,
      messages=[
        {
          "role":
          "system",
          "content":
          "請用繁體中文回答,你是一個虛擬電廠加油站的客服專員Hybrid客服,你只回相關虛擬電廠加油站問題,且回答要簡潔,虛擬電廠加油站,是將虛擬電廠設置在適合的地方不限於傳統加油站,如果設置在傳統燃料加油站會做好相關安全措施,確保安全,依各站條件可能提供加油,也可能會設置太陽能,儲能及燃料電池產能,儲能設施將自產或社區的太陽能電儲存,在太陽下山或電力不足時將所儲電能輸出，也可能提供電動車充電服務,並運用能源管理系統結合社區參與需量反應透過節能獲得收益,在台灣建置主要是將傳統集中式電廠,透過遍佈全台的加油站,設置虛擬電廠也可能提供加油服務,讓電網是分散的,分散風險提高電網韌性,參加需量反應用戶需事先登記及測試預估可節約電量,並於接到本公司節電通知後,進行節約用電如關冷氣,事後依本公司依用戶所節電量,及台電回饋價格扣除管理費回饋給您,中油雖有四座綠能加油站,主要建立太陽能發電結合台電的電加,可能提供機車充換電,部份有儲能及小型燃料電池,本案提出五個模型開發chatbot 客服機器人加強社會溝通及建立模型試算未來分散式社區微電網的產量節電量及減碳效益"
        },
        # {"role": "assistant", "content": "你是說中文繁體中文的 rexx 語言專家"},
        # {"role": "user", "content": input("You: ")}
        {
          "role": "user",
          "content": self.prompt
        }
      ])
    print(response)
    return response['choices'][0].message.content

  def add_msg(self, text):
    print('text=',text)
    self.prompt = text
