# coding=utf-8
from ek_abstract import *


def choices():
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


class c1_1_1(ek_choice):
    def text(self):
        return "继续前进"

    def show(self):
        return (ek_choice.kernel.paras["osl"] >= 1)

    def chosen(self):
        ek_choice.kernel.scene = "1-2"


class c1_1_2(ek_choice):
    def text(self):
        return "原路返回"

    def show(self):
        return (ek_choice.kernel.paras["bsl"] >= 1)

    def chosen(self):
        ek_choice.kernel.scene = "1-3"


class c1_1_3(ek_choice):
    def text(self):
        return "就地睡一觉"

    def show(self):
        return (ek_choice.kernel.paras["ssl"] >= 1)

    def chosen(self):
        ek_choice.kernel.scene = "1-4"
