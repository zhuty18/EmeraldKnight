from matplotlib.pyplot import cla
from ch5_choices import *
from abstract import scene_abstract


class s5_1(scene_abstract):
    def load(self):
        if gk.paras[TEAMMATE] == BRUCE_CODE:
            return [c5_1_3()]
        elif gk.paras[TEMPORARY] == 1:
            return [c5_1_2()]
        else:
            return [c5_1_1()]


class s5_2(scene_abstract):
    def load(self):
        if gk.paras[BRUCE_LOVE] >= 4:
            return [c5_2_1()]
        elif gk.paras[BRUCE_SHOW_UP] == 1:
            return [c5_2_2()]
        else:
            return [c5_2_3()]


class s5_4(scene_abstract):
    def load(self):
        if gk.paras[BRUCE_LOVE] >= 4:
            return [c5_4_1()]
        else:
            return [c5_4_2()]


class s5_10(scene_abstract):
    def load(self):
        if gk.paras[BRUCE_SHOW_UP] == 1:
            return [c5_10_1()]
        else:
            return [c5_4_3()]


class s5_15(scene_abstract):
    options = [c5_15_1, c5_15_2, c5_15_3, c5_15_4, c5_15_5]


class s5_15_1(scene_abstract):
    options = [c5_15_1_1, c5_15_1_2, c5_15_1_3]


class s5_15_2(scene_abstract):
    options = [c5_15_2_1, c5_15_2_2]


class s5_15_3(scene_abstract):
    options = [c5_15_3_1, c5_15_3_2]


class s5_18(scene_abstract):
    options = [c5_18_1, c5_16_1]


class s5_28(scene_abstract):
    options = [c5_28_1, c5_28_2, c5_28_3]


class s5_29(scene_abstract):
    options = [c5_29_1, c5_29_2]


class s5_32(scene_abstract):
    options = [c5_32_1, c5_32_2, c5_32_3, c5_32_4, c5_32_5, c5_32_6, c5_32_7]


class s5_33(scene_abstract):
    options = [c5_33_1, c5_33_2, c5_33_3]


class s5_37(scene_abstract):
    options = [c5_37_1, c5_37_2]


class s5_41(scene_abstract):
    options = [c5_41_1, c5_41_2]


class s5_44(scene_abstract):
    options = [c5_44_1, c5_44_2, c5_44_3]


class s5_47(scene_abstract):
    options = [c5_47_1, c5_47_4, c5_47_2, c5_47_3]


class s5_53(scene_abstract):
    def load(self):
        if gk.paras[PEGASUS] == 1:
            return [c5_53_1()]
        else:
            return [c5_53_2()]


class s5_55(scene_abstract):
    options = [c5_55_1]

    def load(self):
        if gk.paras[TEMPORARY] == 1:
            self.options.append(c5_55_2)
        else:
            self.options.append(c5_55_3)
        return super().load()


class s5_57(scene_abstract):
    options = [c5_55_1, c5_55_3]


class s5_58(scene_abstract):
    options = [c5_58_1, c5_58_2, c5_58_3, c5_58_4, c5_58_5]
