import json

path = 'DISC-Law-SFT-Pair-QA-released.jsonl'

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

def process_jsonl(input_file, output_file):
    result = "["
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        index = 0
        for line in infile:
            # 读取每一行并解析JSON
            data = json.loads(line)
            prompt = template_format % (index, data["input"], data["output"])
            prompt = prompt.replace("\n", '').replace(" ", "").replace("\"", "\"")
            index +=1
            result+= prompt +","
            outfile.write(prompt + ",")
            outfile.write('\n')


new_path = 'test.jsonl'
process_jsonl(path,new_path)