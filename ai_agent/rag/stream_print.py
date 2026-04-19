from langchain_ollama import OllamaLLM

# 获取 Ollama 模型对象
model = OllamaLLM(model="qwen3:8b")

# 调用模型获取结果
res = model.stream(input="请介绍一下你自己。")

for chunk in res:
    # print的end参数设置为""，表示不换行；flush参数设置为True，表示立即刷新输出缓冲区
    print(chunk, end="", flush=True) # chunk的英文是块，表示模型返回的每一部分内容