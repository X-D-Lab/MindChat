import gradio as gr
import torch
import torch.nn as nn
from modelscope import Model, snapshot_download
from transformers import AutoModelForCausalLM, AutoTokenizer
from transformers.generation.utils import GenerationConfig

model_dir = snapshot_download("X-D-Lab/MindChat-Baichuan-13B",
                              revision='v1.0.0')

tokenizer = AutoTokenizer.from_pretrained(model_dir,
                                          use_fast=False,
                                          trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(model_dir,
                                             device_map="auto",
                                             torch_dtype=torch.float16,
                                             trust_remote_code=True)
model.generation_config = GenerationConfig.from_pretrained(model_dir)


def clear_session():
    return []


def predict(input, history):
    if history is None:
        history = []
    model_input = []
    for chat in history:
        model_input.append({"role": "user", "content": chat[0]})
        model_input.append({"role": "assistant", "content": chat[1]})
    model_input.append({"role": "user", "content": input})
    print(model_input)
    response = model.chat(tokenizer, model_input)
    history.append((input, response))
    history = history[-20:]
    return '', history


block = gr.Blocks()

with block as demo:
    gr.Markdown("""<h1><center>MindChat-13B</center></h1>
     <center>MindChat-13B：漫谈心理大模型，期望通过自身的努力和专业知识, 在严格保护用户隐私的前提下, 全时段全天候为用户提供全面的心理支持和诊疗帮助, 同时实现自我成长和发展, 以期为建设一个更加健康、包容和平等的社会贡献力量.</center>
    """)
    chatbot = gr.Chatbot(label='MindChat-13B')
    message = gr.Textbox()
    message.submit(predict,
                   inputs=[message, chatbot],
                   outputs=[message, chatbot])
    with gr.Row():
        clear_history = gr.Button("🧹 清除历史对话")
        send = gr.Button("🚀 发送")

    send.click(predict, inputs=[message, chatbot], outputs=[message, chatbot])
    clear_history.click(fn=clear_session,
                        inputs=[],
                        outputs=[chatbot],
                        queue=False)

demo.queue().launch(height=800, share=False)
