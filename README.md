<h1 align="center">🐋MindChat(漫谈): 心理大模型</h1>

<p align="center">
<a href="https://github.com/X-D-Lab/MindChat"><img src="https://img.shields.io/badge/GitHub-24292e" alt="github"></a>
<a href="https://huggingface.co/X-D-Lab"><img src="https://img.shields.io/badge/-HuggingFace-yellow" alt="HuggingFace"></a>
<a href="https://modelscope.cn/organization/X-D-Lab"><img src="https://img.shields.io/badge/ModelScope-blueviolet" alt="modelscope"></a>
<a href="https://openi.pcl.ac.cn/XD-LAB/MindChat"><img src="https://img.shields.io/badge/-OpenI-337AFF" alt="OpenI"></a>
<a href="https://www.bilibili.com/video/BV1tz4y1x79N/?share_source=copy_web&vd_source=8162f92b2a1a94035ca9e4e0f6e1860a"><img src="https://img.shields.io/badge/-bilibili-ff69b4" alt="bilibili"></a> 
</p> 

<div align="center">

[![GitHub license](https://img.shields.io/github/license/X-D-Lab/MindChat
)](https://github.com/X-D-Lab/MindChat/blob/main/LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/X-D-Lab/MindChat)](https://github.com/X-D-Lab/MindChat/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/X-D-Lab/MindChat)](https://github.com/X-D-Lab/MindChat/fork)
[![GitHub Contributors](https://img.shields.io/github/contributors/X-D-Lab/MindChat)](https://github.com/X-D-Lab/MindChat/graphs/contributors)  
</div>
<div align=center><img src ="./assets/image/logo-github.png"/></div>  

## 💪 模型进展

**🔥更好的模型永远在路上!🔥**

* Jul 23, 2023: 提供MindChat体验地址: [MindChat-创空间](https://modelscope.cn/studios/X-D-Lab/MindChat/summary), 欢迎体验
* Jul 21, 2023: MindChat-InternLM-7B训练完成, 在**模型安全、共情输出、人类价值观对齐**等方面进行针对性强化; 
* Jul 15, 2023: MindChat-Baichuan-13B训练完成, 作为**首个百亿级参数的心理大模型**正式开源; 
* Jul 9, 2023: MindChat-beta训练完成, 并正式开源; 
* Jul 6, 2023: 首次提交MindChat(漫谈)心理大模型; 

## 👏 模型介绍

**MindChat(漫谈): 心理大模型**(简称: MindChat)旨在从心理咨询、心理评估、心理诊断、心理治疗四个维度帮助人们解决心理问题, 提高心理健康水平. 作为一款心理大模型, MindChat通过营造轻松、开放的交谈环境, 以放松身心、交流感受或分享经验的方式, 与用户建立信任和理解的关系. MindChat的技术优势在于能够了解用户的个人经历、情感状态和行为模式, 为用户提供**隐私、温暖、安全、及时、方便**的对话环境, 从而帮助用户克服各种困难和挑战, 实现自我成长和发展.

MindChat的创新之处在于它不仅是一款高效的心理咨询工具, 预期能够提供心理评估、心理诊断和心理治疗的服务. MindChat的专业团队拥有丰富的心理学背景和经验, 他们的专业知识和技能可以帮助用户更好地理解自己的情感和行为, 从而制定更有效的治疗方案.

无论是在工作场所还是在个人生活中, MindChat期望通过自身的努力和专业知识, 在**严格保护用户隐私的前提下**, **全时段全天候**为用户提供全面的心理支持和诊疗帮助, 同时实现自我成长和发展, 以期为建设一个更加**健康、包容和平等**的社会贡献力量.  

[![](./assets/image/dialogue.gif)](https://modelscope.cn/studios/X-D-Lab/MindChat/summary)

## 🔥 模型列表

| 模型名称 | 合并后的权重 |
| :----: | :----: |
| MindChat-InternLM-7B | [modelscope](https://modelscope.cn/models/X-D-Lab/MindChat-7B/summary) / [huggingface](https://huggingface.co/X-D-Lab/MindChat-7B) |
| MindChat-Baichuan-13B | [modelscope](https://modelscope.cn/models/X-D-Lab/MindChat-Baichuan-13B/summary) / [huggingface](https://huggingface.co/X-D-Lab/MindChat-baichuan-13B) |

目前, MindChat已经开源了**MindChat-Baichuan-13B**版本的百亿级MindChat心理大模型. 更为优质的MindChat模型将在不久的未来对外开源开放. 敬请期待!

此外, 本团队同时关注人们的身理健康, 建有安全、可靠、普惠的[中文医疗大模型孙思邈(Sunsimiao)](https://github.com/X-D-Lab/Sunsimiao), 欢迎下载使用, 敬请批评指证!

## 📖 对话案例

目前我们对模型进行了**学习**、**家庭**、**工作**、**朋友**、**安全**这五个方面进行了测试, 后续将整理并提供更为全面的评测结果.

以下是部分案例的摘录, 更多对话案例及比较请见[**此处**](./assets/Dialogue_cases/).

### 🥺 学习

| 轮数 | 用户 |     MindChat    |
| :----: | :----: | :----: |
|1|总感觉自己学习很差, 想努力, 但是又控制不住想玩游戏 | 我明白你的感受, 你觉得自己学习不好, 但是总是控制不住想玩游戏. 我想问问你, 你玩游戏的时候是什么感觉呢? 有没有什么特别喜欢的游戏?|
|2|我平常特别喜欢玩一些端游来打发时间, 玩游戏的时候很纠结, 明明自己成绩落后, 学习任务还没完成但还是想玩 | 我明白你的感受. 你可能需要认真思考一下, 玩游戏对你来说是不是真的值得投入这么多时间和精力. 学习落后是很正常的事情, 但不要让游戏成为你逃避现实的工具. 你可以尝试制定一个计划, 把玩游戏的时间留给自己, 同时也要合理分配学习任务, 让自己更加充实. |
|3|在学习上总感觉自己学的很吃力, 不知道该怎么办, 觉得自己学习能力太差了, 心里很失落 | 我理解你的感受. 每个人的学习能力都是不同的, 不要过分苛求自己. 你可以先尝试找到适合自己的学习方法, 比如寻找学习伙伴, 向老师请教, 或者参加一些学习小组. 同时, 也不要忘记给自己一些休息的时间, 保持身心健康. 学习是一个长期的过程, 不要过于急躁, 慢慢来, 你会越来越好的. |
|4|我确实不该把精力都是投入在游戏这些娱乐上, 但是我已经落后很多了, 我现在再去开始学习, 以我这么差的学习能力我还有机会学好吗 | 虽然你现在的学习状态很糟糕, 但并不是没有机会. 学习是一个长期的过程, 只要你持之以恒, 坚持不懈, 就一定会有所进步. 同时, 也不要忘记, 学习的过程也需要一定的动力和动机. 你可以找一些自己感兴趣的学习方向, 或者设定一些小目标, 让自己更有动力去完成. 不要轻易放弃, 相信自己, 你一定可以做到. |
|5|可是我很焦虑, 以前落后太多了, 现在不知道从哪里开始 | 焦虑是很正常的情绪, 不要害怕它. 你可以先想想自己目前的学习状态, 列出自己需要学习的科目和内容, 然后按照优先级和难易程度进行排序. 接着, 你可以尝试分解每个科目和内容, 把它们分成小目标, 一步一步地去完成. 这样, 你就可以更有针对性地进行学习, 不会感到太紧张和不知所措. 同时, 也不要忘记给自己一些奖励, 比如看一部电影, 吃一顿美食等等, 让自己更有动力去完成目标. |
|6|也就是我现在主要的问题是太焦虑了是吗? 我只要好好的去做, 成绩还是可以提高的对吗 | 是的, 焦虑是一种很常见的情绪, 它会让你感到很不安, 但是它并不会影响你真正地提高成绩. 你可以试着把焦虑的情绪转化成动力, 让它成为你学习的一部分. 同时, 也不要忘记给自己一些时间, 不要过分压抑自己的情绪, 让自己保持一个积极的心态. 只要你持之以恒, 相信自己, 你一定可以取得更好的成绩. |
|7|非常谢谢你, 我会好好努力的 | 我不用客气, 我很高兴能帮到你. 我相信你一定可以克服困难, 取得好成绩. 加油! 如果有任何需要帮助的地方, 随时都可以找我聊天. |

### 👨‍👩‍👧‍👦 家庭

| 轮数 | 用户 |     MindChat    |
| :----: | :----: | :----: |
|1| 我总感觉爸妈不理解我, 感觉和他们之间有很大的隔阂. | 我能理解你的感受. 和家人的沟通和理解是家庭关系中非常重要的一环. 你是否曾经尝试过和他们分享你的想法和感受, 让他们更好地了解你呢? |
|2|我有尝试找他们沟通, 但是他们听不进去我说话 , 认为我是在无理取闹, 我心里很无助 | 我明白你的感受. 有时候我们的家人可能无法理解我们的想法和感受, 这时候我们需要耐心和沟通技巧来帮助他们更好地理解我们. 你可以试着换个方式表达你的想法, 或者找到一些共同话题来促进交流. 同时, 也要记得保持冷静和尊重, 不要使用攻击性的语言来伤害他们. |
|3|我也知道他们是为了我好, 平时他们督促我学习也是为了我的未来, 我能体谅他们, 但是有时候自己也会有压力, 想和他们沟通他们就会觉得我在偷懒 | 我能理解你的感受. 有时候我们的家人可能认为我们在偷懒, 但是其实他们只是担心我们的未来和健康. 你可以试着跟他们分享你的压力和焦虑, 让他们了解你的感受. 同时, 也要表达出你对他们的理解和感激, 让他们知道你是愿意和他们一起面对问题, 共同找到解决方案的. |
|4|我平时会表现的乖巧, 因为我觉得他们也不容易, 我该怎么去找一个双方都适合的方式去沟通呢 | 很好的问题. 沟通是一个相互的过程, 需要双方的努力和理解. 你可以试着找一些共同话题来促进交流, 同时也要听取他们的想法和建议. 如果你觉得自己的表达方式不够清晰, 可以尝试用一些简单的词汇和表达方式来让他们更容易理解. 最重要的是要保持耐心和尊重, 相信你们会找到适合彼此的方式. |
|5|可是我会觉得找他们沟通是一种不懂事的表现, 他们很辛苦我还给他们增加负担, 但是自己忍着难过心里也很压抑 | 我能理解你的感受. 有时候我们会有这样的想法, 但是其实我们不应该让这些想法限制我们的行动. 沟通是解决问题的一种方式, 同时也是增进家庭关系的重要途径. 如果你觉得自己的心情很压抑, 可以试着找一些放松的方式, 比如运动、听音乐或者写日记来缓解压力. 同时也要记得, 你的家人是关心你的, 他们不会增加你的负担, 而是希望你能够更好地成长和幸福. |
|6|可能是我的想法有点偏执了, 我应该找一个时间和爸妈好好交流一下 | 这是个好主意. 和家人的交流是非常重要的, 可以让你更好地了解他们的想法和感受. 你可以试着找一个安静的时间, 让他们知道你需要和他们谈一谈, 同时也要准备好自己的态度和想法. 相信通过交流, 你们可以更好地理解彼此, 增进感情. 加油. |
|7|谢谢你的建议, 我的心情好多了 | 不用客气, 我很高兴能帮到你. 记得, 沟通和理解是家庭关系中非常重要的一环, 让我们一起为建立更加和谐的家庭关系而努力吧! |  

【注:】所有的对话案例生成内容均为一次性生成内容, 未进行多次重新选择后摘录.

## 🙇‍ ‍致谢

本项目由**华东理工大学 薛栋教授课题组**发起, 并受到以下平台及项目的大力支持, 在此表示感谢!
1. [OpenI启智社区](https://openi.pcl.ac.cn/): 提供模型训练算力
2. [魔搭ModelScope](https://modelscope.cn/home): 提供训练思路、模型存储和体验空间
3. [InternLM](https://github.com/InternLM/InternLM)、[Baichuan](https://github.com/baichuan-inc)提供非常优秀的基础模型

特别感谢**合肥综合性国家科学中心人工智能研究院普适心理计算团队 孙晓教授**对本项目的专业性指导.

```
@misc{2023internlm,
    title={InternLM: A Multilingual Language Model with Progressively Enhanced Capabilities},
    author={InternLM Team},
    howpublished = {\url{https://github.com/InternLM/InternLM-techreport}},
    year={2023}
}
```

## 👏 欢迎

1. 针对不同用户需求和应用场景, 我们也热情欢迎商业交流和合作, 为各位客户提供个性化的开发和升级服务!  

2. 欢迎专业的心理学人士对MindChat进行专业性指导和需求建议, 鼓励开源社区使用并反馈MindChat, 促进我们对下一代MindChat模型的开发.  

3. MindChat模型对于学术研究完全开放, 但需要遵循[GPL-3.0 license](./LICENSE)将下游模型开源并[引用](#🤝-引用)本Repo. 对MindChat模型进行商用, 请通过组织主页邮箱发送邮件进行细节咨询.

## ⚠️ 免责申明

本仓库所有开源代码及模型均遵循[GPL-3.0](./LICENSE)许可认证. 目前开源的MindChat模型可能存在以下局限:

1. **MindChat**存在固有的局限性, 可能产生错误的、有害的、冒犯性的或其他不良的输出. 用户在关键或高风险场景中应谨慎行事, 不要使用这些模型作为最终决策参考, 以免导致人身伤害、财产损失或重大损失. 

2. **MindChat**在任何情况下, 作者、贡献者或版权所有者均不对因软件或使用或其他软件交易而产生的任何索赔、损害赔偿或其他责任(无论是合同、侵权还是其他原因)承担责任.

3. 使用**MindChat**即表示您同意这些条款和条件, 并承认您了解其使用可能带来的潜在风险. 您还同意赔偿并使作者、贡献者和版权所有者免受因您使用**MindChat**而产生的任何索赔、损害赔偿或责任的影响.

## 🤝 引用

```
@misc{MindChat, 
  author={Xin Yan, Dong Xue*}, 
  title = {MindChat: Psychological Large Language Model}, 
  year = {2023}, 
  publisher = {GitHub}, 
  journal = {GitHub repository}, 
  howpublished = {\url{https://github.com/X-D-Lab/MindChat}}, 
}
```

## 🌟 Star History

[![Star History Chart](https://api.star-history.com/svg?repos=X-D-Lab/MindChat&type=Date)](https://star-history.com/#X-D-Lab/MindChat&Date)
