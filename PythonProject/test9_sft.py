from peft import AutoPeftModelForCausalLM
from transformers import  AutoTokenizer

model_dir = "/usr/zhaojingli/Qwen/output_qwen"


model = AutoPeftModelForCausalLM.from_pretrained(
    model_dir,
    device_map="auto",
    trust_remote_code=True
).eval()

print(model)

prompt_template='''
给定一句话：“%s”，请你按步骤要求工作。

步骤1：识别这句话中的城市和日期共2个信息
步骤2：根据城市和日期信息，生成JSON字符串，格式为{"city":城市,"date":日期}

请问，这个JSON字符串是：
'''

tokenizer = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)

model.generation_config.top_p=0 # 只选择概率最高的token

Q_list=['2020年4月16号三亚下雨么？','青岛3-15号天气预报','5月6号下雪么，城市是威海','青岛2023年12月30号有雾霾么?','我打算6月1号去北京旅游，请问天气怎么样？','你们打算1月3号坐哪一趟航班去上海？','小明和小红是8月8号在上海结婚么?',
        '一起去东北看冰雕么，大概是1月15号左右，我们3个人一起']
for Q in Q_list:
    prompt=prompt_template%(Q,)
    A,hist=model.chat(tokenizer,prompt,history=None)
    print('Q:%s\nA:%s\n'%(Q,A))
