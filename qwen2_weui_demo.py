# coding:utf-8
import json
import os
import time

import gradio as gr
import torch
from modelscope.hub.snapshot_download import snapshot_download
from transformers import AutoModelForCausalLM, AutoTokenizer
from transformers.generation.utils import GenerationConfig

device = "cuda" # the device to load the model onto

cache_dir = './'

model_id = "X-D-Lab/MindChat-Qwen2-4B"

snapshot_download(model_id, cache_dir=cache_dir)

model_path = cache_dir + model_id

model = AutoModelForCausalLM.from_pretrained(
    model_path,
    device_map="auto"
)
tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)

title = "🐋MindChat: 漫谈心理大模型"

description = """
🔎 MindChat(漫谈): 旨在通过营造轻松、开放的交谈环境, 以放松身心、交流感受或分享经验的方式, 为用户提供隐私、温暖、安全、及时、方便的对话环境, 从而帮助用户克服各种困难和挑战, 实现自我成长和发展.

🦊 无论是在工作场所还是在个人生活中, MindChat期望通过自身的努力和专业知识, 在严格保护用户隐私的前提下, 全时段全天候为用户提供全面的心理陪伴和倾听, 同时实现自我成长和发展, 以期为建设一个更加健康、包容和平等的社会贡献力量.

🙅‍ 目前，MindChat还不能替代专业的心理医生和心理咨询师，无法做出专业的心理诊断报告。虽MindChat在训练过程中极致注重模型安全和价值观正向引导，但仍无法保证模型输出正确且无害，内容上模型作者及平台不承担相关责任。

👏 更为优质、安全、温暖的模型正在赶来的路上，欢迎关注：[MindChat Github](https://github.com/X-D-Lab/MindChat)
"""

submit_btn = '发送'
retry_btn = '🔄 重新生成'
undo_btn = '↩️ 撤销'
clear_btn = '🗑️ 清除历史'



def predict(message,history):
    if history is None:
        history = []
    history = history[-20:]

    # 将history 转为meaaages
    messages = [{"role": "system", "content": "You are a helpful assistant."}]
    for i in history:
        messages.append({"role": "user", "content": i[0]})
        messages.append({"role": "assistant", "content": i[1]})
    messages.append({"role": "user", "content": message})

    text = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True
    )
    model_inputs = tokenizer([text], return_tensors="pt").to(device)

    generated_ids = model.generate(
        model_inputs.input_ids,
        max_new_tokens=512
    )
    generated_ids = [
        output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
    ]

    response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]

    history.append((message, response))
    for i in range(len(response)):
        time.sleep(0.02)
        yield response[:i + 1]


demo = gr.ChatInterface(predict,
                        title=title,
                        description=description,
                        cache_examples=True,
                        submit_btn=submit_btn,
                        retry_btn=retry_btn,
                        clear_btn=clear_btn,
                        undo_btn=undo_btn).queue()

demo.launch()