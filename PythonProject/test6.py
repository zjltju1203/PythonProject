# 城市数据
with open('city.txt','r',encoding='utf-8') as fp:
    city_list=fp.readlines()
    city_list=[line.strip().split(' ')[1] for line in city_list]

print(city_list)

import random
import json
import time
import openpyxl

Q_arr=[]
A_arr=[]

Q_list=[
    ('{city}{year}年{month}月{day}日的天气','%Y-%m-%d'),
    ('{city}{year}年{month}月{day}号的天气','%Y-%m-%d'),
    ('{city}{month}月{day}日的天气','%m-%d'),
    ('{city}{month}月{day}号的天气','%m-%d'),

    ('{year}年{month}月{day}日{city}的天气','%Y-%m-%d'),
    ('{year}年{month}月{day}号{city}的天气','%Y-%m-%d'),
    ('{month}月{day}日{city}的天气','%m-%d'),
    ('{month}月{day}号{city}的天气','%m-%d'),

    ('你们{year}年{month}月{day}日去{city}玩吗？','%Y-%m-%d'),
    ('你们{year}年{month}月{day}号去{city}玩么？','%Y-%m-%d'),
    ('你们{month}月{day}日去{city}玩吗？','%m-%d'),
    ('你们{month}月{day}号去{city}玩吗？','%m-%d'),
]

Q='青岛4月6日下雨么?'
prompt_template='''
给定一句话：“%s”，请你按步骤要求工作。

步骤1：识别这句话中的城市和日期共2个信息
步骤2：根据城市和日期信息，生成JSON字符串，格式为{\\"city\\":城市,\\"date\\":日期}

请问，这个JSON字符串是：
'''

prompt=prompt_template%(Q,)

# 生成一批"1月2号"、"1月2日"、"2023年1月2号", "2023年1月2日", "2023-02-02", "03-02"之类的话术, 教会它做日期转换
for i in range(1000):
    Q=Q_list[random.randint(0,len(Q_list)-1)]
    city=city_list[random.randint(0,len(city_list)-1)]
    year=random.randint(1990,2025)
    month=random.randint(1,12)
    day=random.randint(1,28)
    time_str='{}-{}-{}'.format(year,month,day)
    date_field=time.strftime(Q[1],time.strptime(time_str,'%Y-%m-%d'))
    Q=Q[0].format(city=city,year=year,month=month,day=day) # 问题
    A=json.dumps({'city':city,'date':date_field},ensure_ascii=False)  # 回答

    Q_arr.append(prompt_template%(Q,))
    A_arr.append(A)

import pandas as pd

df=pd.DataFrame({'Prompt':Q_arr,'Completion':A_arr})
df.to_excel('train.xlsx')