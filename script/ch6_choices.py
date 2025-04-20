from abstract import choice_abstract
from constant import *


class c6_1_1(choice_abstract):
    target = "6-2"


class c6_2_1(choice_abstract):
    target = "6-3"


class c6_3_1(choice_abstract):
    target = "6-4"


class c6_4_1(choice_abstract):
    target = "6-5"


class c6_5_1(choice_abstract):
    target = FINAL_BATTLE

    def text(self):
        return "决战"

    def chosen(self):
        gk.battle = None
        return super().chosen()
