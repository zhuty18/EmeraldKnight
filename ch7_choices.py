from constant import *
from abstract import choice_abstract


class c7_1_1(choice_abstract):
    target = "end-19"

    def text(self) -> str:
        return "打断他"


class c7_1_2(choice_abstract):
    target = "7-2"


class c7_2_1(choice_abstract):
    target = "7-3"


class c7_3_1(choice_abstract):
    target = "end-19"

    def text(self) -> str:
        return "瞎几把扯"


class c7_3_2(choice_abstract):
    target = "7-5"


class c7_3_3(choice_abstract):
    target = "7-4"


class c7_5_1(choice_abstract):
    target = "7-6"

    def show(self) -> bool:
        return gk.paras[KNOWLEDGE] >= 5


class c7_5_2(choice_abstract):
    target = "7-8"

    def show(self) -> bool:
        return gk.paras[BRUCE_INTRODUCE] == 1 and gk.paras[KNOWLEDGE] < 5


class c7_5_3(choice_abstract):
    target = "7-9"


class c7_6_1(choice_abstract):
    target = "end-20"

    def text(self) -> str:
        return "讨伐魔王"


class c7_6_2(choice_abstract):
    target = "7-7"


class c7_8_1(choice_abstract):
    target = "end-21"

    def text(self) -> str:
        return "你这样，来阻止我？"