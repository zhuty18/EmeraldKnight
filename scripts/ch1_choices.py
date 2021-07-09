from ek_abstract import *


class c1_1_1(ek_choice):
    target = "1-2"

    def show(self):
        return (ek_choice.kernel.paras["osl"] >= 1)


class c1_1_2(ek_choice):
    target = "1-3"

    def show(self):
        return (ek_choice.kernel.paras["bsl"] >= 1)


class c1_1_3(ek_choice):
    target = "1-4"

    def show(self):
        return (ek_choice.kernel.paras["ssl"] >= 1)


class c1_4_1(ek_choice):
    target = "1-2"

    def show(self):
        return (ek_choice.kernel.paras["osl"] >= 1)
