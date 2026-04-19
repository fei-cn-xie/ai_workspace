from openai import OpenAI
import json

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="1233"
)

schema = {'日期', '股票名称', '开盘价', '收盘价', '成交量'}

example_data = [
    {
        "content": "2023-01-01, 股市震荡。股票强大科技A股开盘价100元，一度飙升至104人民币，随后跌落至89人民币，最终收盘价为90人民币，成交量为100万股。",
        "answer": {
            "日期": "2023-01-01",
            "股票名称": "强大科技A股",
            "开盘价": 100,
            "收盘价": 90,
            "成交量": 1000000
        }
    },
    {
        "content": "2023-01-02, 股市继续震荡。股票英伟达美股开盘价90元，一度飙升至95人民币，随后跌落至85人民币，最终收盘价为88人民币，成交量为150万股。",
        "answer": {
            "日期": "2023-01-02",
            "股票名称": "英伟达美股",
            "开盘价": 90,
            "收盘价": 88,
            "成交量": 1500000
        }
    }
]

question = [
    "2026-05-03, 股市利好。腾讯科技A股开盘价150元，一度飙升至160人民币，随后跌落至140人民币，最终收盘价为155人民币",
    "2026-05-04, 股市下跌。阿里巴巴美股开盘价80元，一度跌至75人民币，随后回升至85人民币，最终收盘价为82人民币"
]

messages = [
    {
        "role": "system",
        "content": f"你是一个AI金融助手，专门为用户完成信息抽取。你会根据{schema}信息，按照JSON字符串输出，如果某些信息不存在，用<原文未提供>替换。严格按照示例格式输出，不要添加任何多余的解释和文本。"
    },
    {
        "role": "assistant",
        "content": "你好！我是你的AI助手，很高兴为你服务。请告诉我你需要什么帮助，我会尽力满足你的需求。"
    }
]

for example in example_data:
    messages.append({
        "role": "user",
        "content": example["content"]
    })
    messages.append({
        "role": "assistant",
        "content": json.dumps(example["answer"], ensure_ascii=False) # 防止中文被转义
    })

for q in question:
    print("问题：", q)
    messages.append({
        "role": "user",
        "content": q
    })
    response = client.chat.completions.create(
        model="qwen3:0.6b", 
        messages=messages
    )
    print(response.choices[0].message.content)