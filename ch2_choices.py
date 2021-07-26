from abstract import choice_abstract
from constant import *


class c2_1_1(choice_abstract):
    target = "2-4"

    def show(self):
        t = gk.core.paras[TEMPORARY]
        return t % 2 == 0

    def chosen(self):
        gk.core.paras[TEMPORARY] += 1
        return super().chosen()


class c2_1_2(choice_abstract):
    target = "2-5"

    def show(self):
        t = gk.core.paras[TEMPORARY]
        return (t / 2) % 2 == 0

    def chosen(self):
        gk.core.paras[TEMPORARY] += 2
        return super().chosen()


class c2_1_3(choice_abstract):
    target = "2-6"

    def show(self):
        t = gk.core.paras[TEMPORARY]
        return (t / 4) % 2 == 0

    def chosen(self):
        gk.core.paras[TEMPORARY] += 4
        return super().chosen()


class c2_1_4(choice_abstract):
    target = "2-7"

    def show(self):
        return gk.core.paras[TEMPORARY] == 7

    def chosen(self):
        gk.core.paras[TEMPORARY] = 0
        return super().chosen()


class c2_2_1(choice_abstract):
    target = "2-8"

    def show(self):
        return gk.core.paras[TEAMMATE] == "oliver"


class c2_2_2(choice_abstract):
    target = "2-9"

    def show(self):
        return gk.core.paras[TEAMMATE] != "oliver"


class c2_7_1(choice_abstract):
    target = "3-2"


class c2_8_1(choice_abstract):
    target = "2-10"


class c2_8_2(choice_abstract):
    target = "2-11"


class c2_8_3(choice_abstract):
    target = "2-12"

    def chosen(self):
        gk.core.paras[OLIVER_LOVE] += 3
        return super().chosen()
