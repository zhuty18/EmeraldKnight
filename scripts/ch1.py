from ch1_choices import *


class s1_1:
    def choices(self):
        ls = []
        tmp = c1_1_1()
        if tmp.show():
            ls.append(tmp)
        tmp = c1_1_2()
        if tmp.show():
            ls.append(tmp)
        tmp = c1_1_3()
        if tmp.show():
            ls.append(tmp)
        return ls


class s1_2:
    def choices(self):
        return []


class s1_4:
    def choices(self):
        ls = []
        tmp = c1_4_1()
        if tmp.show():
            ls.append(tmp)
        return ls
