import pandas as pd
import json

path = "train.xlsx"
data = pd.read_excel(path, index_col=0, skiprows=0)

template_format = '''
{
"id": "identity_%s",
"conversations": [
  {
    "from": "user",
    "value": "%s"
  },
  {
    "from": "assistant",
    "value": "%s"
  }
]
}
'''
prompt_arr = []
for index, row in data.iterrows():
    Prompt = row['Prompt']
    Completion = row['Completion']
    Prompt = Prompt.replace("\"", "\"").replace("\n", '')
    Completion = Completion.replace('"', '\\"').replace("\n", '')
    prompt = template_format % (index, Prompt, Completion)
    prompt = prompt.replace("\n", '').replace(" ", "")
    prompt_arr.append(prompt)

result = "["
for data in prompt_arr:
    result += data + ","

result += "]"

print(result)