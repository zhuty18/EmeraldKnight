from abstract import *
from constant import *


class c1_1_1(choice_abstract):
    target = "1-2"

    def show(self):
        return (gk.core.paras[BRUCE_STORY_LINE] >= 1)


class c1_1_2(choice_abstract):
    target = "1-3"


class c1_1_3(choice_abstract):
    target = "1-4"

    def show(self):
        return (gk.core.paras[SINESTRO_STORY_LINE] >= 1)


class c1_2_1(choice_abstract):
    target = "1-5"


class c1_3_1(choice_abstract):
    target = "1-6"


class c1_3_2(choice_abstract):
    target = "1-7"


class c1_3_3(choice_abstract):
    target = "1-8"


class c1_4_1(choice_abstract):
    target = "1-9"


class c1_4_2(choice_abstract):
    target = "1-10"


class c1_4_3(choice_abstract):
    target = "1-11"


class c1_5_1(choice_abstract):
    target = "1-12"


class c1_5_2(choice_abstract):
    target = "1-13"
