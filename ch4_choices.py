from constant import *
from abstract import choice_abstract


class c4_1_1(choice_abstract):
    target = "4-3"


class c4_3_1(choice_abstract):
    target = "4-4"


class c4_3_2(choice_abstract):
    target = "4-5"

    def chosen(self):
        gk.paras[KNOWLEDGE] += 5
        return super().chosen()


class c4_3_3(choice_abstract):
    target = "4-6"


class c4_4_1(choice_abstract):
    target = "end-6"

    def text(self):
        return "答应"


class c4_4_2(choice_abstract):
    target = "4-7"


class c4_5_1(choice_abstract):
    target = "4-7"

    def text(self):
        return "出发"


class c4_6_1(choice_abstract):
    target = "4-8"

    def show(self):
        return gk.paras[PROPS] % 2 == 0

    def chosen(self):
        gk.paras[PROPS] += 1
        return super().chosen()


class c4_6_2(choice_abstract):
    target = "4-9"

    def show(self):
        return (gk.paras[PROPS] >> 1) % 2 == 0

    def chosen(self):
        gk.paras[PROPS] += 2
        return super().chosen()


class c4_6_3(choice_abstract):
    target = "4-10"

    def show(self):
        return (gk.paras[PROPS] >> 2) % 2 == 0

    def chosen(self):
        gk.paras[PROPS] += 4
        return super().chosen()


class c4_6_4(choice_abstract):
    target = "4-11"

    def show(self):
        return gk.paras[PROPS] == 7

    def chosen(self):
        gk.paras[PROPS] = 0
        gk.paras[TEAMMATE] = BARRY_CODE
        return super().chosen()


class c4_7_1(choice_abstract):
    target = "end-7"

    def text(self):
        return "战斗"

    def show(self):
        return gk.paras[SINESTRO_LOVE] < 5

    def chosen(self):
        gk.paras[TEMPORARY] = 0
        return super().chosen()


class c4_7_2(choice_abstract):
    target = "4-13"

    def text(self):
        return "战斗"

    def show(self):
        return gk.paras[SINESTRO_LOVE] >= 5

    def chosen(self):
        gk.paras[TEMPORARY] = 0
        return super().chosen()


class c4_7_3(choice_abstract):
    target = "end-6"

    def text(self):
        return "战斗"

    def chosen(self):
        gk.paras[TEMPORARY] = 0
        return super().chosen()


class c4_11_1(choice_abstract):
    target = "4-12"

    def text(self):
        return "战斗"

    def chosen(self):
        gk.paras[TEMPORARY] = 0
        return super().chosen()


class c4_11_2(choice_abstract):
    target = "end-6"

    def text(self):
        return "战斗"

    def chosen(self):
        gk.paras[TEMPORARY] = 0
        return super().chosen()


class c4_12_1(choice_abstract):
    target = "5-4"


class c4_13_1(choice_abstract):
    target = "4-14"

    def chosen(self):
        gk.paras[SINESTRO_LOVE] -= 1
        return super().chosen()


class c4_13_2(choice_abstract):
    target = "4-15"


class c4_13_3(choice_abstract):
    target = "4-16"

    def chosen(self):
        gk.paras[SINESTRO_TAME] += 1
        return super().chosen()


class c4_14_1(choice_abstract):
    target = "4-17"

    def chosen(self):
        gk.paras[SINESTRO_TAME] -= 1
        return super().chosen()


class c4_14_2(choice_abstract):
    target = "4-18"

    def chosen(self):
        gk.paras[SINESTRO_LOVE] += 1
        return super().chosen()


class c4_14_3(choice_abstract):
    target = "4-19"


class c4_14_4(choice_abstract):
    target = "4-20"


class c4_20_1(choice_abstract):
    target = "4-29"


class c4_20_2(choice_abstract):
    target = "4-22"

    def chosen(self):
        gk.paras[SINESTRO_TAME] = 0
        return super().chosen()


class c4_21_1(choice_abstract):
    target = "4-23"


class c4_21_2(choice_abstract):
    target = "4-24"

    def chosen(self):
        gk.paras[SINESTRO_LOVE] = 0
        return super().chosen()


class c4_22_1(choice_abstract):
    target = "4-21"


class c4_23_1(choice_abstract):
    target = "4-25"


class c4_23_2(choice_abstract):
    target = "4-26"


class c4_25_1(choice_abstract):
    target = "4-27"

    def show(self):
        return gk.paras[SINESTRO_TAME] == 8


class c4_25_2(choice_abstract):
    target = "4-28"

    def show(self):
        return gk.paras[SINESTRO_LOVE] < 8


class c4_25_3(choice_abstract):
    target = "end-10"

    def text(self):
        return "怎么了？"


class c4_27_1(choice_abstract):
    target = "end-11"

    def show(self):
        return gk.paras[SINESTRO_LOVE] == 8

    def text(self):
        return "再给他一次机会"


class c4_27_2(choice_abstract):
    target = "end-12"

    def text(self):
        return "瑟尔早该死了"


class c4_28_1(choice_abstract):
    target = "end-8"

    def text(self):
        return "你想怎样"

    def show(self):
        return gk.paras[SINESTRO_TAME] == 8


class c4_28_2(choice_abstract):
    target = "end-9"

    def text(self):
        return "你想怎样"

    def show(self):
        return gk.paras[SINESTRO_TAME] < 8
