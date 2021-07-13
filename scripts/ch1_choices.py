from abstract import *
from constant import *


class c1_1_1(choice_abstract):
    target = "1-2"

    def show(self):
        return (gk.core.paras[BRUCE_STORY_LINE] >= 1)


class c1_1_2(choice_abstract):
    target = "1-3"

    def show(self):
        return (gk.core.paras[OLIVER_STORY_LINE] >= 1)


class c1_1_3(choice_abstract):
    target = "1-4"

    def show(self):
        return (gk.core.paras[SINESTRO_STORY_LINE] >= 1)


class c1_2_1(choice_abstract):
    target = "1-5"


class c1_2_2(choice_abstract):
    target = "1-3"


class c1_4_1(choice_abstract):
    target = "1-2"

    def show(self):
        return False
