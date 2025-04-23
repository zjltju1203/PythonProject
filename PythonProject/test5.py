from modelscope import snapshot_download
from transformers import AutoModelForCausalLM, AutoTokenizer

# Downloading model checkpoint to a local dir model_dir
# model_dir = snapshot_download('qwen/Qwen-7B')
# model_dir = snapshot_download('qwen/Qwen-7B-Chat')
# model_dir = snapshot_download('qwen/Qwen-14B')
model_dir = "/usr/zhaojingli/Qwen-1_8B-Chat-Int4"

# Loading local checkpoints
# trust_remote_code is still set as True since we still load codes from local dir instead of transformers
tokenizer = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(
    model_dir,
    device_map="auto",
    trust_remote_code=True,
).eval()

#response, history = model.chat(tokenizer, "你好", history=None)
#print(response)
#response, _ = model.chat(tokenizer, "你好呀", history=None, system="请用二次元可爱语气和我说话")
#print(response)

Q='青岛4月6日下雨么?'

prompt_template='''
给定一句话：“%s”，请你按步骤要求工作。

步骤1：识别这句话中的城市和日期共2个信息
步骤2：根据城市和日期信息，生成JSON字符串，格式为{"city":城市,"date":日期}

请问，这个JSON字符串是：
'''

prompt=prompt_template%(Q,)

resp, hist = model.chat(tokenizer, prompt, history=None)
print(resp)