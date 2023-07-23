import time

import gradio as gr
from transformers import AutoModelForCausalLM, AutoTokenizer

from modelscope.hub.snapshot_download import snapshot_download

title = "🐋MindChat: 漫谈心理大模型"

description = """
🔎 MindChat(漫谈): 旨在通过营造轻松、开放的交谈环境, 以放松身心、交流感受或分享经验的方式, 为用户提供隐私、温暖、安全、及时、方便的对话环境, 从而帮助用户克服各种困难和挑战, 实现自我成长和发展.

🦊 无论是在工作场所还是在个人生活中, MindChat期望通过自身的努力和专业知识, 在严格保护用户隐私的前提下, 全时段全天候为用户提供全面的心理陪伴和倾听, 同时实现自我成长和发展, 以期为建设一个更加健康、包容和平等的社会贡献力量.

🙅‍ 目前，MindChat还不能替代专业的心理医生和心理咨询师，无法做出专业的心理诊断报告。虽MindChat在训练过程中极致注重模型安全和价值观正向引导，但仍无法保证模型输出正确且无害，内容上模型作者及平台不承担相关责任。

👏 欢迎关注：[MindChat Github](https://github.com/X-D-Lab/MindChat)
"""

submit_btn = '发送'

retry_btn = '🔄 重新生成'

undo_btn = '↩️ 撤销'

clear_btn = '🗑️ 清除历史'

cache_dir = './'


snapshot_download('X-D-Lab/MindChat-7B',
                              cache_dir=cache_dir,
                              revision='v1.0.0')

tokenizer = AutoTokenizer.from_pretrained(cache_dir + "X-D-Lab/MindChat-7B", trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(cache_dir + "X-D-Lab/MindChat-7B", trust_remote_code=True).cuda()
model = model.eval()


def stream_predict(message, history):
    dictionary  = {
        'prompt': message
    }
    print(dictionary)
    if history is None:
        history = []
    
    response, history = model.chat(tokenizer, message, history=history)
    print(history)

    for i in range(len(response)):
        time.sleep(0.03)
        yield  response[: i+1]

demo = gr.ChatInterface(stream_predict, title=title, description=description, cache_examples=True, submit_btn=submit_btn, retry_btn=retry_btn, clear_btn=clear_btn, undo_btn=undo_btn).queue()

if __name__ == "__main__":
    demo.launch()