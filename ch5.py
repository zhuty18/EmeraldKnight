from ch5_choices import *
from abstract import scene_abstract


class s5_2(scene_abstract):
    def load(self):
        if gk.paras[BRUCE_LOVE] >= 4:
            return [c5_2_1()]
        elif gk.paras[BRUCE_SHOW_UP] == 1:
            return [c5_2_2()]
        else:
            return [c5_2_3()]


class s5_3(scene_abstract):
    options = [c5_3_1, c5_3_2, c5_3_3]


class s5_4(scene_abstract):
    options = [c5_4_1, c5_4_2, c5_4_3]


class s5_15(scene_abstract):
    options = [c5_15_1, c5_15_2, c5_15_3, c5_15_4, c5_15_5]


class s5_15_1(scene_abstract):
    options = [c5_15_1_1, c5_15_1_2, c5_15_1_3]


class s5_15_2(scene_abstract):
    options = [c5_15_2_1, c5_15_2_2]


class s5_15_3(scene_abstract):
    options = [c5_15_3_1, c5_15_3_2]


class s5_18(scene_abstract):
    options = [c5_18_1, c5_16_1]
