from ch2_choices import *
from abstract import scene_abstract


class s2_1(scene_abstract):
    options = [c2_1_1, c2_1_2, c2_1_3, c2_1_4]


class s2_2(scene_abstract):
    options = [c2_2_1, c2_2_2]


class s2_3(scene_abstract):
    options = [c2_3_1, c2_3_2]


class s2_7(scene_abstract):
    options = [c2_7_1]


class s2_8(scene_abstract):
    options = [c2_8_1, c2_8_2]

    def load(self):
        if gk.paras[KNOWLEDGE] == 1 and gk.scene != "2-12":
            return [c2_8_3()]
        else:
            return super().load()


class s2_9(scene_abstract):
    options = [c2_9_1, c2_9_2]

    def load(self):
        if gk.paras[KNOWLEDGE] == 1 and gk.scene != "2-19":
            return [c2_9_3()]
        else:
            return super().load()


class s2_10(scene_abstract):
    options = [c2_10_1, c2_10_2]


class s2_11(scene_abstract):
    options = [c2_11_1, c2_11_2, c2_11_3]


class s2_14(scene_abstract):
    options = [c2_14_1, c2_14_2]


class s2_20(scene_abstract):
    options = [c2_20_1, c2_20_2]


class s2_24(scene_abstract):
    options = [c2_24_1, c2_24_2]


class s2_28(scene_abstract):
    options = [c2_28_1, c2_28_2]


class s2_30(scene_abstract):
    options = [c2_30_1, c2_30_2]
