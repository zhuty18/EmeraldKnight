from ek_abstract import *
from constant import *


class c1_1_1(ek_choice):
    target = "1-2"

    def show(self):
        return (ek_choice.kernel.paras[BRUCE_STORY_LINE] >= 1)


class c1_1_2(ek_choice):
    target = "1-3"

    def show(self):
        return (ek_choice.kernel.paras[OLIVER_STORY_LINE] >= 1)


class c1_1_3(ek_choice):
    target = "1-4"

    def show(self):
        return (ek_choice.kernel.paras[SINESTRO_STORY_LINE] >= 1)


class c1_2_1(ek_choice):
    target = "1-5"


class c1_2_2(ek_choice):
    target = "1-3"


class c1_4_1(ek_choice):
    target = "1-2"

    def show(self):
        return False
