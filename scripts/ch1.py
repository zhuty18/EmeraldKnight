from ch1_choices import *


class s1_1(scene_abstract):
    options = [c1_1_1(), c1_1_2(), c1_1_3()]

    def load(self):
        gk.core.paras[SWORD_HOT_TIME] += 1
        return super().load()


class s1_2(scene_abstract):
    options = [c1_2_1(), c1_1_2()]


class s1_3(scene_abstract):
    options = [c1_3_1(), c1_3_2(), c1_3_3()]


class s1_4(scene_abstract):
    options = [c1_4_1(), c1_4_2(), c1_4_3()]


class s1_5(scene_abstract):
    options = [c1_5_1(), c1_5_2()]

    def load(self):
        gk.core.paras[SWORD_HOT_TIME] += 1
        return super().load()


class s1_7(scene_abstract):
    options = [c1_7_1(), c1_7_2()]


class s1_12(scene_abstract):
    options = [c1_12_1(), c1_12_2(), c1_12_3(), c1_12_4()]


class s1_17(scene_abstract):
    options = [c1_17_1(), c1_17_2()]


class s1_24(scene_abstract):
    options = [c1_24_1(), c1_24_2(), c1_24_3(), c1_24_4(), c1_24_5()]


class s1_29(scene_abstract):
    options = [c1_29_1(), c1_29_2()]


class s1_34(scene_abstract):
    options = []
