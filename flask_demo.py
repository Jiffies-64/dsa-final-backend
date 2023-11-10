import json
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from transformers.generation.utils import GenerationConfig
from flask import Flask, render_template, request


def init_model():
    # 这里需要配置环境变量HF_HOME指定默认下载路径
    model_path = "ShengbinYue/DISC-LawLLM"
    offload_folder = "offload"
    model = AutoModelForCausalLM.from_pretrained(
        model_path, torch_dtype=torch.float16, device_map="auto", trust_remote_code=True, offload_folder=offload_folder
    )
    model.generation_config = GenerationConfig.from_pretrained(model_path)
    tokenizer = AutoTokenizer.from_pretrained(
        model_path, use_fast=False, trust_remote_code=True
    )
    return model, tokenizer


app = Flask(__name__)

# 初始化模型和tokenizer
model, tokenizer = init_model()

# 用于存储聊天历史的列表
chat_history = []


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.form.get('message')
    if user_message:
        # 用户消息
        chat_history.append({"role": "user", "content": user_message})

        # 生成助手回复
        response = generate_response(user_message)
        print(response)

        # 存储助手消息
        chat_history.append({"role": "assistant", "content": response})

        return json.dumps({"response": response})


def generate_response(user_message):
    # 生成助手回复的逻辑，使用模型和tokenizer
    messages = chat_history.copy()
    messages.append({"role": "user", "content": user_message})
    response = model.chat(tokenizer, messages)[-1]

    return response


if __name__ == '__main__':
    app.run(port=8502)
