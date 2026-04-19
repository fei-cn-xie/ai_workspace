from langchain_core.prompts import PromptTemplate
from langchain_ollama import OllamaLLM

model = OllamaLLM(model="gemma4:26b")

prompt_template = PromptTemplate.from_template(
    "我是{name}，我喜欢{hobby}。我的朋友是{friend}。"
)

# 变量注入
prompt = prompt_template.format(name="小明", hobby="打篮球", friend="小红")

# res = model.stream(input=prompt)


# 直接将 prompt 模板和模型链式调用，模型会自动进行变量注入
input_ = {"name": "小明", "hobby": "打篮球", "friend": "小红"}
chain = prompt_template | model
res = chain.stream(input=input_)

for r in res:
    print(r, end="", flush=True)