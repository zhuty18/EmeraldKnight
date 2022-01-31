from constant import *
from abstract import choice_abstract


class c3_1_1(choice_abstract):
    target = "3-5"

    def chosen(self):
        gk.paras[SINESTRO_TAME] += 1
        return super().chosen()


class c3_1_2(choice_abstract):
    target = "3-30"


class c3_2_1(choice_abstract):
    target = "3-31"


class c3_2_2(choice_abstract):
    target = "3-41"


class c3_5_1(choice_abstract):
    target = "3-6"


class c3_5_2(choice_abstract):
    target = "3-7"


class c3_6_1(choice_abstract):
    target = "3-8"


class c3_6_2(choice_abstract):
    target = "3-9"


class c3_8_1(choice_abstract):
    target = "3-10"


class c3_8_2(choice_abstract):
    target = "3-11"


class c3_10_1(choice_abstract):
    target = "3-12"


class c3_10_2(choice_abstract):
    target = "3-13"


class c3_12_1(choice_abstract):
    target = "3-14"

    def chosen(self):
        gk.paras[SINESTRO_TAME] += 2
        return super().chosen()


class c3_12_2(choice_abstract):
    target = "3-15"


class c3_14_1(choice_abstract):
    target = "3-16"


class c3_16_1(choice_abstract):
    target = "3-17"


class c3_16_2(choice_abstract):
    target = "end-5"

    def text(self):
        return "直接跳"


class c3_17_1(choice_abstract):
    target = "3-18"


class c3_18_1(choice_abstract):
    target = "3-19"


class c3_18_2(choice_abstract):
    target = "3-20"


class c3_18_3(choice_abstract):
    target = "3-21"


class c3_19_1(choice_abstract):
    target = "3-27"

    def text(self):
        return "我捡到了他的信"


class c3_19_2(choice_abstract):
    target = "3-22"

    def text(self):
        return "我以为他会在山上"


class c3_20_1(choice_abstract):
    target = "3-22"

    def text(self):
        return "瑟尔在这里吗"


class c3_20_2(choice_abstract):
    target = "3-21"

    def text(self):
        return "阿琳是谁"


class c3_21_1(choice_abstract):
    target = "3-27"


class c3_21_2(choice_abstract):
    target = "3-28"


class c3_22_1(choice_abstract):
    target = "3-23"


class c3_22_2(choice_abstract):
    target = "3-24"


class c3_22_3(choice_abstract):
    target = "3-27"

    def text(self):
        return "我还捡到了他的信"


class c3_23_1(choice_abstract):
    target = "3-25"


class c3_23_2(choice_abstract):
    target = "3-26"

    def show(self):
        return gk.paras[SINESTRO_TAME] == 6

    def chosen(self):
        gk.paras[SINESTRO_LOVE] += 3
        return super().chosen()


class c3_24_1(choice_abstract):
    target = "3-23"

    def text(self):
        return "告诉他全过程"


class c3_27_1(choice_abstract):
    target = "3-23"

    def text(self):
        return "信上的瑟尔又是谁？"


class c3_28_1(choice_abstract):
    target = "3-29"


class c3_29_1(choice_abstract):
    target = "4-1"


class c3_30_1(choice_abstract):
    target = "3-2"


class c3_31_1(choice_abstract):
    target = "3-2"

    def show(self):
        return gk


class c3_31_2(choice_abstract):
    target = "3-2"


class c3_31_3(choice_abstract):
    target = "3-2"
