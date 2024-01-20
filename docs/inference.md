## 前述

目前MindChat系列的多数模型是在Internlm2系列、Qwen系列基模型进行领域微调实现(当然后续可能会根据LLM开源社区发展进行其他基模型系列的探索, 如Yi模型等), 因此若本文档未涵盖相关内容, 用户也可以直接使用各自基模型社区的相关生态工具. 当然也非常欢迎开发者提PR完善.

## 推理脚本

MindChat在进行领域微调的时候基本遵循基模型对应的Chat模型所采用的Template. 因此推理脚本可以直接参考基模型对应的Chat模型的推理脚本.

如针对**MindChat-Qwen-v2**, 您可以使用[以下脚本](../scripts/)进行简单推理:

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
from transformers.generation import GenerationConfig

tokenizer = AutoTokenizer.from_pretrained("X-D-Lab/MindChat-Qwen-7B-v2", trust_remote_code=True)

model = AutoModelForCausalLM.from_pretrained("X-D-Lab/MindChat-Qwen-7B-v2", device_map="auto", trust_remote_code=True).eval()

model.generation_config = GenerationConfig.from_pretrained("X-D-Lab/MindChat-Qwen-7B-v2", trust_remote_code=True)

response, history = model.chat(tokenizer, "总感觉自己学习很差，想努力，但是又控制不住想玩游戏。", history=None)
print(response)
# 我理解你的感受，学习确实需要耐心和毅力。不过，你也可以通过制定学习计划和目标来提高自己的学习效率。同时，也可以考虑寻求专业帮助，例如找老师或心理咨询师。

# 第二轮对话
response, history = model.chat(tokenizer, "我制定了计划，但经常不按照计划执行，我不够自律。", history=history)
print(response)
# 自律确实是一个需要不断练习和培养的品质。你可以通过一些方法来提高自己的自律能力，例如制定奖励和惩罚机制、找到适合自己的学习方法等。同时，也可以寻求他人的帮助和支持，例如找同学一起学习、向老师请教等。

# 第三轮对话
response, history = model.chat(tokenizer, "我害怕他们嘲笑我。", history=history)
print(response)
# 这种担心是很正常的，但是你需要知道，每个人都有自己的弱点和不足。你不必因为这些弱点而自卑或自责。相反，你可以积极地寻求帮助和支持，让自己变得更加自信和坚强。

# 第四轮对话
response, history = model.chat(tokenizer, "你说的对，可是我现在的学习已经落后很多了，你觉得我还有机会么？", history=history)
print(response)
# 当然有。每个人都有自己的机会和潜力，只要你肯努力和坚持，就一定能够取得成功。同时，你也可以通过参加一些学习活动、交流学习经验等方式来提高自己的学习能力和自信心。
```

这和**Qwen-7B-Chat**的推理脚本是一致的, 其他模型同理. 

## 模型服务

由于MindChat选择的是社区内具有广泛影响力的基模型, 因此可以直接借助其广泛的生态工具. 例如在进行模型部署的时候, 可以使用[FastChat](https://github.com/lm-sys/FastChat)来帮助我们.

* **第一步**: 安装
您应该安装最新的FastChat包

```
    git clone https://github.com/lm-sys/FastChat.git
    cd FastChat
    pip install .
```

* **第二步(可选)**: 环境变量  
若您希望从魔搭Modelscope下载模型则需要设置两个环境变量

    

```
    export VLLM_USE_MODELSCOPE=True
    export FASTCHAT_USE_MODELSCOPE=True
```  

若您希望从HuggingFace下载模型或者已经将模型存在本地则可跳过本步骤.

* **第三步:** 模型部署
1. 启动一个controller:

```

    python -m fastchat.serve.controller --host 0.0.0.0

```

2. 发布一个model worker(s)  
```

    python -m fastchat.serve.model_worker --model-path X-D-Lab/MindChat-Qwen-7B-v2 --revision master --host 0.0.0.0

```

* **第四步:** 模型体验
  + 启动命令行客户端服务  
```

    python3 -m fastchat.serve.test_message --model-name MindChat-Qwen-7B-v2 --message 总感觉自己学习很差, 想努力, 但是又控制不住想玩游戏.

```

  + 启动gradio的WebUI服务  

```

    python3 -m fastchat.serve.gradio_web_server --host 0.0.0.0 --port 8000

```

* **第五步:** OpenAI API服务

```

    python3 -m fastchat.serve.openai_api_server --host 0.0.0.0 --port 8000

```

更为详细的信息可以参考[FastChat docs](https://github.com/lm-sys/FastChat/tree/main/docs).
