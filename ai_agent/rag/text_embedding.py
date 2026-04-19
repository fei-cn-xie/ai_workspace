from langchain_community.embeddings import OllamaEmbeddings, DashScopeEmbeddings


# 获取 embedding 模型对象
emb= OllamaEmbeddings(model="nomic-embed-text-v2-moe")
# emb = DashScopeEmbeddings() 需要阿里云的这个模型的apikey，并通过DASHSCOPE_API_KEY环境变量设置

# 测试
print(emb.embed_query("我喜欢你"))
print(emb.embed_documents(["我喜欢你", "我讨厌你", "我爱你"]))



