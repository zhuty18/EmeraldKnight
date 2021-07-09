# coding=utf-8

import os
list = os.listdir("story")
k = 0
for i in list:
    if i.endswith(".ekt"):
        with open("story/"+i, 'r', encoding='utf8') as f:
            j = len(f.read())
            print(i.replace(".ekt",""), j)
            k += j
print(k)
