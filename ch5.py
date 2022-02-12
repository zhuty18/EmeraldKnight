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
