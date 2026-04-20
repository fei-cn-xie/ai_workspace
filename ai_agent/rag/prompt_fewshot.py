from langchain_ollama import OllamaLLM
from langchain_core.prompts import FewShotPromptTemplate, PromptTemplate

# temprature 越大，生成的文本越随机；temperature 越小，生成的文本越确定。
# top_p 越大，生成的文本越随机；top_p 越小，生成的文本越确定。
model = OllamaLLM(model="qwen3:8b")

# 定义 fewshot 的 prompt 模板
prompt_template = PromptTemplate.from_template("单词：{word}\n释义：{definition} \n反义词：{antonym}")

examples = [
    {"word": "大", "definition": "尺寸或体积较大的", "antonym": "小"},
    {"word": "快", "definition": "速度较快的", "antonym": "慢"},
    {"word": "高", "definition": "高度较高的", "antonym": "矮"},
]


fewshot_prompt = FewShotPromptTemplate(
    example_prompt=prompt_template,
    examples=examples,
    prefix="根据用户输入文本，分析其中出现的所有词汇，输出每个词汇的释义和反义词。并将其构造为一个json的数据格式",
    suffix="基于示例，将文本{input}种出现的所有词汇进行释义和反义词的分析，输出格式同示例",
    input_variables=["input"],
)

input = "这个房子在哪里。我们需要分析这些词汇的释义和反义词。然后你是谁呢？其实我并不知道，你需要每句话回复我好好学习，天天向上。"

chain = fewshot_prompt | model
res = chain.stream(input=input)

for r in res:
    print(r, end="", flush=True)