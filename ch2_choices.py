from constant import *
from abstract import choice_abstract


class c2_1_1(choice_abstract):
    target = "2-4"

    def show(self):
        return gk.paras[TEMPORARY] % 2 == 0

    def chosen(self):
        gk.paras[TEMPORARY] += 1
        return super().chosen()


class c2_1_2(choice_abstract):
    target = "2-5"

    def show(self):
        return (gk.paras[TEMPORARY] >> 1) % 2 == 0

    def chosen(self):
        gk.paras[TEMPORARY] += 2
        return super().chosen()


class c2_1_3(choice_abstract):
    target = "2-6"

    def show(self):
        return (gk.paras[TEMPORARY] >> 2) % 2 == 0

    def chosen(self):
        gk.paras[TEMPORARY] += 4
        return super().chosen()


class c2_1_4(choice_abstract):
    target = "2-7"

    def show(self):
        return gk.paras[TEMPORARY] == 7

    def chosen(self):
        gk.paras[TEMPORARY] = 0
        return super().chosen()


class c2_2_1(choice_abstract):
    target = "2-8"

    def show(self):
        return gk.paras[TEAMMATE] == OLIVER_CODE


class c2_2_2(choice_abstract):
    target = "2-9"

    def show(self):
        return gk.paras[TEAMMATE] != OLIVER_CODE


class c2_3_1(choice_abstract):
    target = "2-24"

    def show(self):
        return gk.paras[SWORD_HOT_TIME] == 3

    def chosen(self):
        gk.paras[SWORD_HOT_TIME] += 1
        return super().chosen()


class c2_3_2(choice_abstract):
    target = "2-25"

    def show(self):
        return gk.paras[SWORD_HOT_TIME] == 1


class c2_7_1(choice_abstract):
    target = "3-2"


class c2_8_1(choice_abstract):
    target = "2-10"


class c2_8_2(choice_abstract):
    target = "2-11"


class c2_8_3(choice_abstract):
    target = "2-12"

    def chosen(self):
        gk.paras[OLIVER_LOVE] += 3
        return super().chosen()


class c2_9_1(choice_abstract):
    target = "2-20"

    def text(self):
        return "我走了，去翻龙骨雪山"


class c2_9_2(choice_abstract):
    target = "2-21"


class c2_9_3(choice_abstract):
    target = "2-19"


class c2_10_1(choice_abstract):
    target = "2-13"


class c2_10_2(choice_abstract):
    target = "2-14"

    def chosen(self):
        gk.paras[CREDIT] += 2
        return super().chosen()


class c2_11_1(choice_abstract):
    target = "2-17"

    def show(self):
        return gk.paras[TEMPORARY] % 2 == 0

    def chosen(self):
        gk.paras[TEMPORARY] += 1
        gk.paras[KNOWLEDGE] += 1
        return super().chosen()


class c2_11_2(choice_abstract):
    target = "2-18"

    def show(self):
        return (gk.paras[TEMPORARY] >> 1) % 2 == 0

    def chosen(self):
        gk.paras[TEMPORARY] += 2
        return super().chosen()


class c2_11_3(choice_abstract):
    target = "2-10"

    def show(self):
        return gk.paras[TEMPORARY] == 3

    def chosen(self):
        gk.paras[TEMPORARY] = 0
        return super().chosen()


class c2_14_1(choice_abstract):
    target = "2-15"


class c2_14_2(choice_abstract):
    target = "2-33"

    def text(self):
        return "它是不是有什么不同寻常的地方"

    def show(self):
        return gk.paras[SWORD_HOT_TIME] > 0

    def chosen(self):
        gk.paras[INTELLIGENCE] += 2
        return super().chosen()


class c2_15_1(choice_abstract):
    target = "2-16"


class c2_16_1(choice_abstract):
    target = "3-3"


class c2_20_1(choice_abstract):
    target = "2-22"

    def chosen(self):
        gk.paras[KNOWLEDGE] += 3
        return super().chosen()


class c2_20_2(choice_abstract):
    target = "2-23"


class c2_24_1(choice_abstract):
    target = "2-26"


class c2_24_2(choice_abstract):
    target = "2-27"

    def text(self):
        return "这下面是不是有黑暗力量？"

    def show(self):
        return gk.paras[KNOWLEDGE] > 5

    def chosen(self):
        gk.paras[INTELLIGENCE] += 2
        return super().chosen()


class c2_25_1(choice_abstract):
    target = "2-28"


class c2_28_1(choice_abstract):
    target = "2-29"


class c2_28_2(choice_abstract):
    target = "2-30"

    def chosen(self):
        if gk.scene == "2-28":
            gk.paras[INTELLIGENCE] += 1
        return super().chosen()


class c2_30_1(choice_abstract):
    target = "2-31"


class c2_30_2(choice_abstract):
    target = "2-32"

    def chosen(self):
        gk.paras[INTELLIGENCE] -= 1
        return super().chosen()


class c2_31_1(choice_abstract):
    target = "3-4"
