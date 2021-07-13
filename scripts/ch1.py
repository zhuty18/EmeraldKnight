from ch1_choices import *


class s1_1(scene_abstract):
    options = [c1_1_1(), c1_1_2(), c1_1_3()]

    def load(self):
        gk.core.paras[SWORD_HOT_TIME] += 1
        return super().load()


class s1_2(scene_abstract):
    options = [c1_2_1(), c1_2_2()]


class s1_3(scene_abstract):
    # TODO 1-3节
    options = []


class s1_4(scene_abstract):
    # TODO 1-4节
    options = [c1_4_1()]


class s1_5(scene_abstract):
    # TODO 1-5节
    options = []
