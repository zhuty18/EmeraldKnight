from click import option
from ch4_choices import *
from abstract import scene_abstract


class s4_3(scene_abstract):
    options = [c4_3_1, c4_3_2, c4_3_3]


class s4_4(scene_abstract):
    options = [c4_4_1, c4_4_2]


class s4_6(scene_abstract):
    options = [c4_6_1, c4_6_2, c4_6_3, c4_6_4]


class s4_7(scene_abstract):
    options = [c4_7_1, c4_7_2]

    def load(self):
        if gk.fight():
            return super().load()
        else:
            return [c4_7_3()]


class s4_11(scene_abstract):
    def load(self):
        if gk.fight():
            return [c4_11_1()]
        else:
            return [c4_11_2()]


class s4_13(scene_abstract):
    options = [c4_13_1, c4_13_2, c4_13_3]


class s4_14(scene_abstract):
    options = [c4_14_1, c4_14_2, c4_14_3]


class s4_20(scene_abstract):
    options = [c4_20_1, c4_20_2]


class s4_21(scene_abstract):
    options = [c4_21_1, c4_21_2]


class s4_25(scene_abstract):
    options = [c4_25_1, c4_25_2, c4_25_3]


class s4_27(scene_abstract):
    options = [c4_27_1, c4_27_2]


class s4_28(scene_abstract):
    options = [c4_28_1, c4_28_2]
