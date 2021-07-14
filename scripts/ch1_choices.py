from abstract import *
from constant import *


class c1_1_1(choice_abstract):
    target = "1-2"

    def show(self):
        return (gk.core.paras[BRUCE_STORY_LINE] >= 1)

    def chosen(self):
        gk.core.paras[SWORD_HOT_TIME] += 1
        return super().chosen()


class c1_1_2(choice_abstract):
    target = "1-3"


class c1_1_3(choice_abstract):
    target = "1-4"

    def show(self):
        return (gk.core.paras[SINESTRO_STORY_LINE] >= 1)


class c1_2_1(choice_abstract):
    target = "1-5"

    def chosen(self):
        gk.core.paras[SWORD_HOT_TIME] += 1
        return super().chosen()


class c1_3_1(choice_abstract):
    target = "1-6"


class c1_3_2(choice_abstract):
    target = "1-7"


class c1_3_3(choice_abstract):
    target = "1-8"


class c1_4_1(choice_abstract):
    target = "1-9"


class c1_4_2(choice_abstract):
    target = "1-10"


class c1_4_3(choice_abstract):
    target = "1-11"


class c1_5_1(choice_abstract):
    target = "1-12"


class c1_5_2(choice_abstract):
    target = "1-13"

    def chosen(self):
        gk.core.paras[KNOWLEDGE] += 1
        return super().chosen()


class c1_7_1(choice_abstract):
    target = "1-14"


class c1_7_2(choice_abstract):
    target = "1-17"


class c1_12_0(choice_abstract):
    target = "1-24"


class c1_12_1(choice_abstract):
    target = "1-20"

    def chosen(self):
        gk.core.paras[WIZARD_TOWER_CRYSTAL] = 1
        return super().chosen()

    def text(self):
        return "带有火焰纹路的红晶石"


class c1_12_2(choice_abstract):
    target = "1-21"

    def chosen(self):
        gk.core.paras[WIZARD_TOWER_CRYSTAL] = 2
        return super().chosen()

    def text(self):
        return "带有雪花纹路的蓝晶石"


class c1_12_3(choice_abstract):
    target = "1-22"

    def chosen(self):
        gk.core.paras[WIZARD_TOWER_CRYSTAL] = 3
        return super().chosen()

    def text(self):
        return "带有漩涡纹路的紫晶石"


class c1_12_4(choice_abstract):
    target = "1-23"

    def chosen(self):
        gk.core.paras[WIZARD_TOWER_CRYSTAL] = 4
        return super().chosen()

    def text(self):
        return "带有草叶纹路的绿晶石"


class c1_17_1(choice_abstract):
    target = "end-1"

    def text(self):
        return "不了"


class c1_17_2(choice_abstract):
    target = "1-19"


class c1_24_0(choice_abstract):
    target = "1-29"


class c1_24_1(choice_abstract):
    target = "1-25"

    def chosen(self):
        gk.core.paras[WIZARD_TOWER_RUNE] = 1
        return super().chosen()

    def text(self):
        return "看看书架"


class c1_24_2(choice_abstract):
    target = "1-26"

    def chosen(self):
        gk.core.paras[WIZARD_TOWER_RUNE] = 2
        return super().chosen()

    def text(self):
        return "看看卷轴"


class c1_24_3(choice_abstract):
    target = "1-27"

    def chosen(self):
        gk.core.paras[WIZARD_TOWER_RUNE] = 3
        return super().chosen()

    def text(self):
        return "看看挂毯"


class c1_24_4(choice_abstract):
    target = "1-28"

    def chosen(self):
        gk.core.paras[WIZARD_TOWER_RUNE] = 4
        return super().chosen()

    def text(self):
        return "看看徽章"


class c1_24_5(choice_abstract):
    target = "1-29"

    def chosen(self):
        gk.core.paras[INTELLIGENCE] -= 2
        return super().chosen()


class c1_29_1(choice_abstract):
    target = "1-30"


class c1_29_2(choice_abstract):
    target = "1-34"

    def show(self):
        return gk.core.paras[WIZARD_TOWER_RUNE] == 1


class c1_34_1(choice_abstract):
    target = "1-35"

    def show(self):
        return gk.core.paras[TEMPORARY] < 2

    def chosen(self):
        gk.core.paras[TEMPORARY] += 1
        return super().chosen()


class c1_34_2(choice_abstract):
    target = "1-36"

    def show(self):
        return gk.core.paras[TEMPORARY] < 2

    def chosen(self):
        gk.core.paras[TEMPORARY] += 1
        return super().chosen()


class c1_34_3(choice_abstract):
    target = "1-37"

    def show(self):
        return gk.core.paras[TEMPORARY] == 2

    def chosen(self):
        gk.core.paras[TEMPORARY] = 0
        return super().chosen()


class c1_37_1(choice_abstract):
    target = "1-38"

    def chosen(self):
        gk.core.paras[BRUCE_LOVE] -= 5
        return super().chosen()


class c1_37_2(choice_abstract):
    target = "1-39"

    def chosen(self):
        gk.core.paras[BRUCE_LOVE] += 1
        return super().chosen()


class c1_38_1(choice_abstract):
    target = "1-31"

    def text(self):
        return "四处走走"


class c1_39_1(choice_abstract):
    target = "1-40"

    def show(self):
        return gk.core.paras[KNOWLEDGE] >= 1

    def text(self):
        return "四处走走"


class c1_39_2(choice_abstract):
    target = "1-31"

    def show(self):
        return gk.core.paras[KNOWLEDGE] < 1

    def text(self):
        return "四处走走"


class c1_40_1(choice_abstract):
    target = "1-41"

    def text(self):
        return "仔细看看"

    def chosen(self):
        gk.core.paras[SWORD_HOT_TIME] += 1
        gk.core.paras[BRUCE_LOVE] += 10
        return super().chosen()


class c1_40_2(choice_abstract):
    target = "1-41-2"

    def text(self):
        return "仔细看看"

    def chosen(self):
        gk.core.paras[SWORD_HOT_TIME] += 1
        gk.core.paras[BRUCE_LOVE] += 4
        return super().chosen()


class c1_40_3(choice_abstract):
    target = "1-45"

    def chosen(self):
        gk.core.paras[BRUCE_LOVE] += 2
        return super().chosen()


class c1_40_4(choice_abstract):
    target = "1-31"

    def text(self):
        return "起身走开"


class c1_41_1(choice_abstract):
    target = "1-42"

    def show(self):
        return gk.core.paras[INTELLIGENCE] >= 0

    def chosen(self):
        gk.core.paras[KNOWLEDGE] += 5
        return super().chosen()


class c1_41_2(choice_abstract):
    target = "1-43"


class c1_41_3(choice_abstract):
    target = "1-44"
