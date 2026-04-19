from langchain_ollama import OllamaLLM

# 获取 Ollama 模型对象
model = OllamaLLM(model="qwen3:8b")

# 调用模型获取结果
res = model.invoke("请介绍一下你自己。")
print(res)