
from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="1233"
)

response = client.chat.completions.create(
    model="qwen3:0.6b",
    messages=[
        {"role": "system", "content": "你是一个AI助手，专门为用户提供各种服务。你会根据用户的需求，提供相应的帮助和建议。你会尽力满足用户的要求，并且保持友好和礼貌。提供的信息非常详细， 每次内容不少于1000字"},
        {"role": "assistant", "content": "你好！我是你的AI助手，很高兴为你服务。请告诉我你需要什么帮助，我会尽力满足你的需求。"},
        {"role": "user", "content": "今天天气怎么样？"}
    ]
)

print(response.choices[0].message.content)

