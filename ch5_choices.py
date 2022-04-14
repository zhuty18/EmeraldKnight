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
        return gk.paras[DRAGON_EGG] == 0

    def chosen(self):
        gk.paras[DRAGON_EGG] = 1
        gk.paras[KNOWLEDGE] += 3
        return super().chosen()


class c5_15_5(choice_abstract):
    target = "5-25"

    def show(self):
        return gk.paras[DRAGON_EGG] == 1


class c5_16_1(choice_abstract):
    target = "5-17"


class c5_18_1(choice_abstract):
    target = "5-28"

    def chosen(self):
        gk.paras[TEMPORARY] = 0
        return super().chosen()


class c5_28_1(choice_abstract):
    target = "5-29"

    def show(self):
        return (gk.paras[INTELLIGENCE] > 2) and (gk.paras[BRUCE_LOVE] > 8)


class c5_28_2(choice_abstract):
    target = "5-30"

    def show(self):
        return (gk.paras[INTELLIGENCE] > 2) and (gk.paras[BRUCE_LOVE] <= 8)


class c5_28_3(choice_abstract):
    target = "5-31"


class c5_29_1(choice_abstract):
    target = "5-32"


class c5_29_2(choice_abstract):
    target = "end-13"

    def text(self):
        return "让布鲁斯去操心"


class c5_31_1(choice_abstract):
    target = "end-13"

    def text(self):
        return "不再管了"


class c5_32_1(choice_abstract):
    target = "5-33"


class c5_32_2(choice_abstract):
    target = "5-40"

    def show(self):
        return gk.paras[TEMPORARY] % 2 == 0

    def chosen(self):
        gk.paras[TEMPORARY] += 1
        return super().chosen()


class c5_32_3(choice_abstract):
    target = "5-41"

    def show(self):
        return gk.paras[TEMPORARY] % 2 == 1


class c5_32_4(choice_abstract):
    target = "5-44"


class c5_32_5(c5_32_2):
    target = "5-46"


class c5_32_6(c5_32_3):
    target = "5-47"


class c5_32_7(choice_abstract):
    target = "5-51"

    def show(self):
        return (gk.paras[DRAGON_EGG] == 1) and (gk.scene == "5-32")

    def chosen(self):
        gk.paras[BRUCE_LOVE] += 4
        return super().chosen()


class c5_33_1(choice_abstract):
    target = "5-34"

    def show(self):
        return (gk.paras[TEMPORARY] >> 1) % 2 == 0

    def chosen(self):
        gk.paras[TEMPORARY] += 2
        return super().chosen()


class c5_33_2(choice_abstract):
    target = "5-35"

    def show(self):
        return (gk.paras[TEMPORARY] >> 2) % 2 == 0

    def chosen(self):
        gk.paras[TEMPORARY] += 4
        return super().chosen()


class c5_33_3(choice_abstract):
    target = "5-36"

    def show(self):
        return gk.paras[PROPS] == 1

    def chosen(self):
        if (gk.paras[TEMPORARY] >> 3) % 2 == 0:
            gk.paras[TEMPORARY] += 8
        return super().chosen()


class c5_37_1(choice_abstract):
    target = "5-38"

    def show(self):
        return gk.paras[PROPS] == 0


class c5_37_2(choice_abstract):
    target = "5-39"

    def show(self):
        return gk.paras[PROPS] == 1

    def chosen(self):
        gk.paras[TEMPORARY] = 0
        gk.paras[PROPS] = 0
        return super().chosen()


class c5_38_1(choice_abstract):
    target = "end-13"

    def text(self):
        return "专心备战"


class c5_41_1(choice_abstract):
    target = "5-42"

    def show(self):
        return (gk.paras[TEMPORARY] >> 2) % 2 == 1


class c5_41_2(choice_abstract):
    target = "5-43"

    def show(self):
        return (gk.paras[TEMPORARY] >> 2) % 2 == 0


class c5_44_1(choice_abstract):
    target = "5-45"

    def show(self):
        return (gk.paras[TEMPORARY] >> 1) % 2 == 1

    def chosen(self):
        if gk.paras[TEMPORARY] % 2 == 0:
            gk.paras[TEMPORARY] += 1
        gk.paras[PROPS] = 1
        return super().chosen()


class c5_44_2(choice_abstract):
    target = "end-14"

    def text(self):
        return "跳下去"

    def show(self):
        return (gk.paras[TEMPORARY] >> 1) % 2 == 0


class c5_44_3(choice_abstract):
    target = "5-63"


class c5_47_1(choice_abstract):
    target = "5-48"

    def show(self):
        return ((gk.paras[TEMPORARY] >> 3) % 2 == 1) and ((gk.paras[TEMPORARY] >> 2) % 2 == 1)


class c5_47_2(choice_abstract):
    target = "5-49"

    def show(self):
        return (gk.paras[TEMPORARY] >> 2) % 2 == 1


class c5_47_3(choice_abstract):
    target = "5-50"

    def show(self):
        return (gk.paras[TEMPORARY] >> 3) % 2 == 0


class c5_48_1(choice_abstract):
    target = "5-52"

    def chosen(self):
        gk.paras[TEMPORARY] = 1
        gk.paras[PROPS] = 0
        return super().chosen()


class c5_49_1(choice_abstract):
    target = "5-37"


class c5_52_1(choice_abstract):
    target = "5-53"


class c5_53_1(choice_abstract):
    target = "5-54"


class c5_53_2(choice_abstract):
    target = "5-55"


class c5_55_1(choice_abstract):
    target = "5-56"

    def chosen(self):
        gk.paras[TEMPORARY] = 0
        return super().chosen()


class c5_55_2(choice_abstract):
    target = "5-57"


class c5_55_3(choice_abstract):
    target = "5-58"

    def chosen(self):
        gk.paras[TEMPORARY] = 1
        return super().chosen()


class c5_58_1(choice_abstract):
    target = "5-59"


class c5_58_2(choice_abstract):
    target = "5-59"

    def text(self):
        return "西塔楼"


class c5_58_3(choice_abstract):
    target = "5-59"

    def text(self):
        return "城堡一楼"


class c5_58_4(choice_abstract):
    target = "5-60"

    def show(self):
        return gk.paras[DRAGON_EGG] == 1


class c5_58_5(choice_abstract):
    target = "5-61"

    def show(self):
        return gk.paras[DRAGON_EGG] == 0


class c5_59_1(choice_abstract):
    target = "6-1"

    def text(self):
        return "备战"


class c5_60_1(choice_abstract):
    target = "5-62"
