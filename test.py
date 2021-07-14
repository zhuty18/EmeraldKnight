import os
for i in range(1, 2):
    k = str(i)
    cmd = "python ek_test.py <test/" + k + ".in"
    p=os.popen(cmd)
    output=p.read()
    p.close()
    with open("test/"+k+".out",'w',encoding="utf8")as f:
        f.write(output)
    cmd = "diff -u test/" + k + ".true test/" + k + ".out"
    p = os.popen(cmd)
    output = p.read()
    p.close()
    if output != "":
        print(output)
        raise Exception("测试" + k + "未通过！")
