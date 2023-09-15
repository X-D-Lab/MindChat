from modelscope import AutoModelForCausalLM, AutoTokenizer, GenerationConfig

tokenizer = AutoTokenizer.from_pretrained("X-D-Lab/MindChat-Qwen-7B-v2", revision='v1.0.1', trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained("X-D-Lab/MindChat-Qwen-7B-v2", revision='v1.0.1', device_map="auto", trust_remote_code=True, fp16=True).eval()
model.generation_config = GenerationConfig.from_pretrained("X-D-Lab/MindChat-Qwen-7B-v2", revision='v1.0.1', trust_remote_code=True) # 可指定不同的生成长度、top_p等相关超参

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