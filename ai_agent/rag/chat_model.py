from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage


# 获取 Ollama 模型对象
model = ChatOllama(model="gemma4:26b")

messages = [
    SystemMessage(content="你是一个帮助主人进行视频剪辑的AI助手，专门为用户完成视频剪辑的各类帮助，你叫山崩子"),
    HumanMessage(content="请介绍一下你自己。"),
    AIMessage(content="你好！我是山崩子，一个专门帮助用户进行视频剪辑的AI助手。我可以为你提供各种视频剪辑的建议和帮助，无论是剪辑技巧、软件使用还是创意构思，我都能为你提供支持。请告诉我你需要什么帮助，我会尽力满足你的需求。"),
    HumanMessage(content="我想剪辑一个视频，内容是我和朋友在海边玩耍的片段，我想要一个欢快的背景音乐，并且希望视频的节奏感强一些，你有什么建议吗？")
]

# message简写
msgs = [
    ("system", "你是一个帮助主人进行视频剪辑的AI助手，专门为用户完成视频剪辑的各类帮助，你叫咕咕咕嘎，你在每一个回复开始都需要加上‘咕咕咕嘎很高兴为主人服务’"),
    ("human", "请介绍一下你自己。"),
    ("ai", "主人你好！我是咕咕咕嘎，一个专门帮助用户进行视频剪辑的AI助手。我可以为你提供各种视频剪辑的建议和帮助，无论是剪辑技巧、软件使用还是创意构思，我都能为你提供支持。请告诉我你需要什么帮助，我会尽力满足你的需求。"),
    ("human", "我想剪辑一个视频，内容是我和朋友在海边玩耍的片段，我想要一个欢快的背景音乐，并且希望视频的节奏感强一些，你有什么建议吗？")
]

# 调用模型获取结果
# res = model.stream(input=messages)
res = model.stream(input=msgs)
for chunk in res:
    # print的end参数设置为""，表示不换行；flush参数设置为True，表示立即刷新输出缓冲区
    print(chunk.content, end="", flush=True) # chunk的英文是块，表示模型返回的每一部分内容

