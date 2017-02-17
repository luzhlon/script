#! /usr/bin/python3
# FileName    : type.py
# Author      : luzhlon
# Description : 弥补写export.py脚本时的不足
# Note        : 临时性脚本
# LastChange  : 2017/2/17

import re
import sqlite3

con = sqlite3.connect('data.db')
cur = con.cursor()

data = open('data.csv', 'r', encoding='utf-8')
data.readline()

m = {
        '一': 1,
        '二': 2,
        '三': 3,
        '四': 4,
        '五': 5,
        '六': 6,
        '七': 7,
        '八': 8,
        '九': 9
}

i = 1
while i:
    line = data.readline()
    cells = re.split(',', line)
    if len(cells) < 5:
        break
    cur.execute('update bank set section=? where id=?', [m[cells[5][1:2]], i])
    i += 1

con.commit()
con.close()
