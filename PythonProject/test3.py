from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

path = "F:/zjl-work/models/DeepSeek-Coder-V2-Lite-Base"

tokenizer = AutoTokenizer.from_pretrained(path, trust_remote_code=True)
print(tokenizer)
model = AutoModelForCausalLM.from_pretrained(path, trust_remote_code=True, torch_dtype=torch.bfloat16).cuda()
print(model)
input_text = "#write a quick sort algorithm"
inputs = tokenizer(input_text, return_tensors="pt").to(model.device)
outputs = model.generate(**inputs, max_length=256)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))