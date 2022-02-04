import tarfile

from matplotlib.pyplot import cla
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

class c3_3_1(choice_abstract):
    target = "3-43"

    def chosen(self):
        gk.paras[TEMPORARY] += 1
        return super().chosen()

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

    def text(self):
        return "告辞离开"


class c3_30_1(choice_abstract):
    target = "3-2"


class c3_31_1(choice_abstract):
    target = "3-32"

    def show(self):
        return gk.paras[TEMPORARY] % 2 == 0

    def chosen(self):
        gk.paras[TEMPORARY] += 1
        return super().chosen()


class c3_31_2(choice_abstract):
    target = "3-33"

    def show(self):
        return (gk.paras[TEMPORARY] >> 1) % 2 == 0

    def chosen(self):
        gk.paras[TEMPORARY] += 2
        return super().chosen()


class c3_31_3(choice_abstract):
    target = "3-34"

    def show(self):
        return (gk.paras[TEMPORARY] >> 2) % 2 == 0

    def chosen(self):
        gk.paras[TEMPORARY] += 4
        return super().chosen()


class c3_31_4(choice_abstract):
    target = "3-49"

    def show(self):
        return gk.paras[TEMPORARY] == 7

    def chosen(self):
        gk.paras[TEMPORARY] = 0
        return super().chosen()


class c3_35_1(choice_abstract):
    target = "3-36"

    def text(self):
        return "处理羽毛"

    def show(self):
        return gk.paras[TEMPORARY] % 2 == 0

    def chosen(self):
        gk.paras[PROPS] = 1
        gk.paras[TEMPORARY] += 1
        return super().chosen()


class c3_35_2(choice_abstract):
    target = "3-36"

    def text(self):
        return "处理金属"

    def show(self):
        return (gk.paras[TEMPORARY] >> 1) % 2 == 0

    def chosen(self):
        gk.paras[PROPS] = 2
        gk.paras[TEMPORARY] += 2
        return super().chosen()


class c3_35_3(choice_abstract):
    target = "3-36"

    def text(self):
        return "处理骨头"

    def show(self):
        return (gk.paras[TEMPORARY] >> 2) % 2 == 0

    def chosen(self):
        gk.paras[PROPS] = 3
        gk.paras[TEMPORARY] += 4
        return super().chosen()


class c3_35_4(choice_abstract):
    target = "3-37"

    def text(self):
        return "附魔翅膀"

    def show(self):
        return (gk.paras[TEMPORARY] >> 3) % 2 == 0

    def chosen(self):
        gk.paras[PROPS] = 4
        gk.paras[TEMPORARY] += 8
        return super().chosen()


class c3_35_5(choice_abstract):
    target = "3-37"

    def text(self):
        return "附魔身体"

    def show(self):
        return (gk.paras[TEMPORARY] >> 4) % 2 == 0

    def chosen(self):
        gk.paras[PROPS] = 5
        gk.paras[TEMPORARY] += 16
        return super().chosen()


class c3_35_6(choice_abstract):
    target = "3-38"

    def show(self):
        return gk.paras[TEMPORARY] == 31 and gk.paras[PEGASUS] == 5

    def chosen(self):
        gk.paras[PROPS] = 0
        gk.paras[TEMPORARY] = 0
        gk.paras[PEGASUS] = 1
        return super().chosen()


class c3_35_7(choice_abstract):
    target = "3-39"

    def show(self):
        return gk.paras[TEMPORARY] == 31 and gk.paras[PEGASUS] != 5

    def chosen(self):
        gk.paras[PROPS] = 0
        gk.paras[TEMPORARY] = 0
        gk.paras[PEGASUS] = 0
        return super().chosen()


class c3_36_1(choice_abstract):
    target = "3-35"

    def text(self):
        return "清洁"

    def chosen(self):
        if gk.paras[PROPS] == 1:
            gk.paras[PEGASUS] += 1
        return super().chosen()


class c3_36_2(choice_abstract):
    target = "3-35"

    def text(self):
        return "熔化"

    def chosen(self):
        if gk.paras[PROPS] == 2:
            gk.paras[PEGASUS] += 1
        return super().chosen()


class c3_36_3(choice_abstract):
    target = "3-35"

    def text(self):
        return "粉碎"

    def chosen(self):
        if gk.paras[PROPS] == 3:
            gk.paras[PEGASUS] += 1
        return super().chosen()


class c3_37_1(choice_abstract):
    target = "3-35"

    def text(self):
        return "水属性"

    def chosen(self):
        if gk.paras[PROPS] == 5:
            gk.paras[PEGASUS] += 1
        return super().chosen()


class c3_37_2(choice_abstract):
    target = "3-35"

    def text(self):
        return "火属性"


class c3_37_3(choice_abstract):
    target = "3-35"

    def text(self):
        return "风属性"

    def chosen(self):
        if gk.paras[PROPS] == 4:
            gk.paras[PEGASUS] += 1
        return super().chosen()


class c3_37_4(choice_abstract):
    target = "3-35"

    def text(self):
        return "土属性"


class c3_37_5(choice_abstract):
    target = "3-35"

    def text(self):
        return "雷属性"


class c3_37_6(choice_abstract):
    target = "3-35"

    def text(self):
        return "空间属性"


class c3_38_1(choice_abstract):
    target = "3-40"


class c3_40_1(choice_abstract):
    target = "5-2"


class c3_41_1(choice_abstract):
    target = "3-42"

    def chosen(self):
        gk.paras[TEMPORARY] += 1
        return super().chosen()


class c3_41_2(choice_abstract):
    target = "3-43"

    def text(self):
        return "不拿"


class c3_42_1(choice_abstract):
    target = "3-43"


class c3_43_1(choice_abstract):
    target = "3-44"

    def chosen(self):
        gk.paras[TEMPORARY] += 2
        return super().chosen()


class c3_43_2(choice_abstract):
    target = "3-45"

    def text(self):
        return "不进"


class c3_44_1(choice_abstract):
    target = "3-45"


class c3_45_1(choice_abstract):
    target = "3-46"


class c3_45_2(choice_abstract):
    target = "3-47"


class c3_45_3(choice_abstract):
    target = "3-48"


class c3_46_1(choice_abstract):
    target = "5-1"

    def text(self):
        return "那座城"

    def chosen(self):
        gk.paras[TEMPORARY] = 0
        return super().chosen()


class c3_46_2(choice_abstract):
    target = "4-2"

    def chosen(self):
        gk.paras[TEMPORARY] = 0
        return super().chosen()


class c3_48_1(choice_abstract):
    target = "4-1"

    def text(self):
        return "继续前进"

    def chosen(self):
        gk.paras[TEMPORARY] = 0
        return super().chosen()


class c3_49_1(choice_abstract):
    target = "3-35"
