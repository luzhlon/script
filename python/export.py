#! /usr/bin/python3
# FileName    : export.py
# Author      : luzhlon
# Description : 提取文本文件里的关键信息导入到数据库
# Note        : 临时性脚本
# LastChange  : 2017/2/17

import re
import sqlite3

data = open('data.txt', 'r', encoding='utf-8')
subj = ''
patSub = re.compile('\d+')
patAnw = re.compile('^答案')

con = sqlite3.connect('data.db')
cur = con.cursor()

i = 1
while 1:
    line = data.readline()
    if not line:
        break
    num = patSub.match(line)
    if num:
        num = int(num.group())                  # 题号
        subj = re.sub('[\d.、]+', '', line)
        line = data.readline()

        while not patAnw.match(line):           # 题目到答案之间的内容是选项
            subj += line
            line = data.readline()

        anw = re.sub('答案|[:\s\.]', '', line)  # 提取答案
#        con.execute('insert into bank (id, number, content, answer) values(?,?,?,?)', [i, num, subj, anw])
        i+=1                                    # 序号加1
        print(num, subj, anw)
    input()

con.commit()
con.close()
