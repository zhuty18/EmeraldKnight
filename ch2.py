from ch2_choices import *
from abstract import scene_abstract


class s2_1(scene_abstract):
    options = [c2_1_1, c2_1_2, c2_1_3, c2_1_4]


class s2_2(scene_abstract):
    options = [c2_2_1, c2_2_2]


class s2_7(scene_abstract):
    options = [c2_7_1]


class s2_8(scene_abstract):
    options = [c2_8_1, c2_8_2]

    def load(self):
        if gk.core.paras[KNOWLEDGE] == 1:
            return [c2_8_3()]
        else:
            return super().load()
