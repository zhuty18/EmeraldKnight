from ch1_choices import *
from abstract import scene_abstract


class s1_1(scene_abstract):
    options = [c1_1_1(), c1_1_2(), c1_1_3()]


class s1_2(scene_abstract):
    options = [c1_2_1(), c1_1_2()]


class s1_3(scene_abstract):
    options = [c1_3_1(), c1_3_2(), c1_3_3()]


class s1_4(scene_abstract):
    options = [c1_4_1(), c1_4_2(), c1_4_3()]


class s1_5(scene_abstract):
    options = [c1_5_1(), c1_5_2()]


class s1_6(scene_abstract):
    options = [c1_6_1(), c1_6_2()]


class s1_7(scene_abstract):
    options = [c1_7_1(), c1_7_2()]


class s1_8(scene_abstract):
    options = [c1_6_1(), c1_8_2()]


class s1_11(scene_abstract):
    options = [c1_11_1(), c1_11_2(), c1_11_3()]


class s1_12(scene_abstract):
    options = [c1_12_1(), c1_12_2(), c1_12_3(), c1_12_4()]


class s1_14(scene_abstract):
    options = [c1_14_1(), c1_14_2(), c1_14_3()]


class s1_16(scene_abstract):
    options = [c1_16_1(), c1_16_2(), c1_16_3()]


class s1_17(scene_abstract):
    options = [c1_17_1(), c1_17_2()]


class s1_19(scene_abstract):
    options = [c1_8_2(), c1_19_2()]


class s1_24(scene_abstract):
    options = [c1_24_1(), c1_24_2(), c1_24_3(), c1_24_4(), c1_24_5()]


class s1_29(scene_abstract):
    options = [c1_29_1(), c1_29_2()]


class s1_31(scene_abstract):
    options = [c1_31_1(), c1_31_2()]


class s1_34(scene_abstract):
    options = [c1_34_1(), c1_34_2()]

    def load(self):
        gk.core.paras[BRUCE_SHOW_UP] = True
        return super().load()


class s1_35(scene_abstract):
    options = [c1_34_2(), c1_34_3()]


class s1_36(scene_abstract):
    options = [c1_34_1(), c1_34_3()]


class s1_37(scene_abstract):
    options = [c1_37_1(), c1_37_2()]


class s1_39(scene_abstract):
    options = [c1_39_1(), c1_39_2()]


class s1_40(scene_abstract):
    # options = [c1_40_1(), c1_40_2(), c1_40_3(), c1_40_4()]

    def load(self):
        if gk.core.paras[WIZARD_TOWER_CRYSTAL] == "green":
            return [c1_40_1()]
        else:
            if gk.core.paras[BRUCE_SHOW_UP]:
                return [c1_40_2()]
            else:
                return [c1_40_3()]


class s1_41(scene_abstract):
    # options = [c1_41_1(), c1_41_2(), c1_41_3(),c1_41_4()]
    def load(self):
        if gk.core.paras[BRUCE_SHOW_UP]:
            return [c1_41_4()]
        else:
            return [c1_41_3()]


class s1_46(scene_abstract):
    options = [c1_41_1(), c1_41_2()]


class s1_49(scene_abstract):
    options = [c1_49_1(), c1_49_2(), c1_49_3()]


class s1_52(scene_abstract):
    # options = [c1_52_1(), c1_52_2()]

    def load(self):
        if gk.core.paras[CREDIT] > 0:
            return [c1_52_1()]
        else:
            return [c1_52_2()]


class s1_58(scene_abstract):
    options = [c1_58_1(), c1_58_2(), c1_58_3()]


class s1_62(scene_abstract):
    # options = [c1_62_1(), c1_62_2()]
    def load(self):
        if gk.core.paras[SINESTRO_LOVE] > 0 or gk.core.paras[SINESTRO_TAME] > 0:
            return [c1_62_1()]
        else:
            return [c1_62_2()]


class s1_63(scene_abstract):
    options = [c1_63_1(), c1_63_2()]


class s1_64(scene_abstract):
    options = [c1_64_1(), c1_64_2()]


class s1_66(scene_abstract):
    options = [c1_66_1(), c1_66_2()]


class s1_67(scene_abstract):
    options = [c1_67_1(), c1_67_2()]


class s1_69(scene_abstract):
    options = [c1_67_2(), c1_67_3()]


class s1_70(scene_abstract):
    options = [c1_67_1(), c1_67_3()]
