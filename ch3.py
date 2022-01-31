from ch3_choices import *
from abstract import scene_abstract


class s3_1(scene_abstract):
    options = [c3_1_1, c3_1_2]


class s3_2(scene_abstract):
    options = [c3_2_1, c3_2_2]


class s3_5(scene_abstract):
    options = [c3_5_1, c3_5_2]


class s3_6(scene_abstract):
    options = [c3_6_1, c3_6_2]


class s3_8(scene_abstract):
    options = [c3_8_1, c3_8_2]


class s3_10(scene_abstract):
    options = [c3_10_1, c3_10_2]


class s3_12(scene_abstract):
    options = [c3_12_1, c3_12_2]


class s3_16(scene_abstract):
    options = [c3_16_1, c3_16_2]


class s3_18(scene_abstract):
    options = [c3_18_1, c3_18_2, c3_18_3]


class s3_19(scene_abstract):
    options = [c3_19_1, c3_19_2]


class s3_20(scene_abstract):
    options = [c3_20_1, c3_20_2]


class s3_21(scene_abstract):
    options = [c3_21_1, c3_21_2]


class s3_22(scene_abstract):
    options = [c3_22_1, c3_22_2, c3_22_3]


class s3_23(scene_abstract):
    options = [c3_23_1, c3_23_2]


class s3_31(scene_abstract):
    options = [c3_31_1, c3_31_2, c3_31_3, c3_31_4]


class s3_35(scene_abstract):
    options = [c3_35_1, c3_35_2, c3_35_3, c3_35_4, c3_35_5, c3_35_6, c3_35_7]


class s3_36(scene_abstract):
    options = [c3_36_1, c3_36_2, c3_36_3]


class s3_37(scene_abstract):
    options = [c3_37_1, c3_37_2, c3_37_3, c3_37_4, c3_37_5, c3_37_6]


class s3_41(scene_abstract):
    options = [c3_41_1, c3_41_2]


class s3_43(scene_abstract):
    options = [c3_43_1, c3_43_2]


class s3_45(scene_abstract):
    def load(self):
        if gk.paras[TEMPORARY] == 3:
            return [c3_45_1()]
        elif gk.paras[TEMPORARY] == 2:
            return [c3_45_2()]
        else:
            gk.paras[c3_45_3()]


class s3_46(scene_abstract):
    options = [c3_46_1, c3_46_2]