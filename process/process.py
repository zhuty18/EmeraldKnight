# coding=utf-8

import os
import time

log = time.strftime("%y%m%d_%H%M%S", time.localtime(time.time()))
# f = open("./log/"+log+".log", 'w', encoding="utf=8")
writing = []

list = os.listdir("story")
k = 0
for i in list:
    with open("story/"+i, 'r', encoding='utf8') as f2:
        j = len(f2.read())
        # writing.append(i+"\t"+str(j)+"\n")
        k += j
writing.append("总字数"+"\t"+str(k))
writing = "".join(writing)
# f.write(writing)
print(writing)
# f.close()
