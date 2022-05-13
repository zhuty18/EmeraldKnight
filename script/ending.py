from abstract import choice_abstract, scene_abstract
from constant import *


class end_choice(choice_abstract):
    def text(self):
        return "战斗结束了"


class fail_choice(end_choice):
    target = "end-15"


class end_16(end_choice):
    target = "end-16"


class end_17(end_choice):
    target = "end-17"


class end_18(end_choice):
    target = "end-18"


class end_scene(scene_abstract):
    def load(self):
        if gk.paras[TEMPORARY] == 2:
            return [end_16()]
        elif gk.paras[BRUCE_LOVE] == 20 and gk.paras[TEMPORARY] == 0:
            return [end_17()]
        else:
            return [end_18()]
