from constant import *
from abstract import choice_abstract


class c5_1_1(choice_abstract):
    target = "5-26"


class c5_1_2(choice_abstract):
    target = "5-2"

    def chosen(self):
        gk.paras[TEMPORARY] = 0
        return super().chosen()


class c5_1_3(choice_abstract):
    target = "5-27"


class c5_2_1(choice_abstract):
    target = "5-5"


class c5_2_2(choice_abstract):
    target = "5-6"


class c5_2_3(choice_abstract):
    target = "5-7"


class c5_2_4(choice_abstract):
    target = "5-8"


class c5_3_1(choice_abstract):
    target = "5-13"


class c5_4_1(choice_abstract):
    target = "5-9"


class c5_4_2(choice_abstract):
    target = "5-10"


class c5_4_3(choice_abstract):
    target = "5-12"


class c5_8_1(choice_abstract):
    target = "5-3"

    def text(self):
        return "走吧"


class c5_10_1(choice_abstract):
    target = "5-11"


class c5_13_1(choice_abstract):
    target = "5-14"


class c5_14_1(choice_abstract):
    target = "5-15"


class c5_15_1(choice_abstract):
    def text(self):
        return "主建筑"

    def chosen(self):
        gk.pos = 1


class c5_15_1_1(choice_abstract):
    target = "5-16"

    def chosen(self):
        gk.pos = 0
        return super().chosen()


class c5_15_1_2(choice_abstract):
    target = "5-18"

    def chosen(self):
        gk.pos = 0
        return super().chosen()


class c5_15_1_3(choice_abstract):
    target = "5-19"

    def chosen(self):
        gk.pos = 0
        return super().chosen()


class c5_15_2(choice_abstract):
    def text(self):
        return "东塔楼"

    def chosen(self):
        gk.pos = 2


class c5_15_2_1(choice_abstract):
    target = "5-20"

    def chosen(self):
        gk.pos = 0
        return super().chosen()


class c5_15_2_2(choice_abstract):
    target = "5-21"

    def chosen(self):
        gk.pos = 0
        if gk.paras[TEMPORARY] % 2 == 0:
            gk.paras[TEMPORARY] += 1
            gk.paras[KNOWLEDGE] += 1
        return super().chosen()


class c5_15_3(choice_abstract):
    def text(self):
        return "西塔楼"

    def chosen(self):
        gk.pos = 3


class c5_15_3_1(choice_abstract):
    target = "5-22"

    def chosen(self):
        gk.pos = 0
        if (gk.paras[TEMPORARY] >> 1) % 2 == 0:
            gk.paras[TEMPORARY] += 2
            gk.paras[KNOWLEDGE] += 2
        return super().chosen()


class c5_15_3_2(choice_abstract):
    target = "5-23"

    def chosen(self):
        gk.pos = 0
        if (gk.paras[TEMPORARY] >> 2) % 2 == 0:
            gk.paras[TEMPORARY] += 4
            gk.paras[INTELLIGENCE] += 1
        return super().chosen()


class c5_15_4(choice_abstract):
    target = "5-24"

    def show(self):
        return (gk.paras[TEMPORARY] >> 3) % 2 == 0

    def chosen(self):
        gk.paras[TEMPORARY] += 8
        gk.paras[KNOWLEDGE] += 3
        return super().chosen()


class c5_15_5(choice_abstract):
    target = "5-25"

    def show(self):
        return (gk.paras[TEMPORARY] >> 3) % 2 == 1


class c5_16_1(choice_abstract):
    target = "5-17"


class c5_18_1(choice_abstract):
    target = "5-28"

    def chosen(self):
        gk.paras[TEMPORARY] = 0
        return super().chosen()
