from abstract import scene_end, choice_unfinished
from ch1 import *
from ch2 import *
from ch3 import *
from ch4 import *
from ch5 import *

all_choices = {
    "1-1": s1_1,
    "1-2": s1_2,
    "1-3": s1_3,
    "1-4": s1_4,
    "1-5": s1_5,
    "1-6": s1_6,
    "1-7": s1_7,
    "1-8": s1_8,
    "1-9": c1_4_3,
    "1-10": c1_4_3,
    "1-11": s1_11,
    "1-12": s1_12,
    "1-13": c1_5_1,
    "1-14": s1_14,
    "1-15": c1_15_1,
    "1-16": s1_16,
    "1-17": s1_17,
    "1-18": c1_6_1,
    "1-19": s1_19,
    "1-20": c1_12_0,
    "1-21": c1_12_0,
    "1-22": c1_12_0,
    "1-23": c1_12_0,
    "1-24": s1_24,
    "1-25": c1_24_0,
    "1-26": c1_24_0,
    "1-27": c1_24_0,
    "1-28": c1_24_0,
    "1-29": s1_29,
    "1-30": s1_39,
    "1-31": s1_31,
    "1-32": c1_31_2,
    "1-33": c1_16_1,
    "1-34": s1_34,
    "1-35": s1_35,
    "1-36": s1_36,
    "1-37": s1_37,
    "1-38": c1_38_1,
    "1-39": s1_39,
    "1-40": s1_40,
    "1-41": s1_41,
    "1-42": c1_41_2,
    "1-43": c1_16_3,
    "1-44": s1_31,
    "1-45": c1_31_2,
    "1-46": s1_46,
    "1-47": c1_16_1,
    "1-48": c1_14_1,
    "1-49": s1_49,
    "1-50": c1_16_3,
    "1-51": c1_16_2,
    "1-52": s1_52,
    "1-53": c1_52_2,
    "1-54": c1_16_2,
    "1-55": c1_11_4,
    "1-56": c1_11_4,
    "1-57": c1_11_4,
    "1-58": s1_58,
    "1-59": c1_58_4,
    "1-60": c1_58_4,
    "1-61": c1_58_4,
    "1-62": s1_62,
    "1-63": s1_63,
    "1-64": s1_64,
    "1-65": c1_64_2,
    "1-66": s1_66,
    "1-67": s1_67,
    "1-68": c1_67_3,
    "1-69": s1_69,
    "1-70": s1_70,
    "1-71": c1_71_1,
    "1-72": s1_72,
    "1-73": s1_73,
    "1-74": s1_74,
    "1-75": s1_75,
    "1-76": s1_76,
    "1-77": c1_16_2,
    "1-78": c1_76_4,
    "1-79": c1_76_4,
    "1-80": c1_76_4,
    "1-81": c1_81_1,
    "2-1": s2_1,
    "2-2": s2_2,
    "2-3": s2_3,
    "2-4": s2_1,
    "2-5": s2_1,
    "2-6": s2_1,
    "2-7": s2_7,
    "2-8": s2_8,
    "2-9": s2_9,
    "2-10": s2_10,
    "2-11": s2_11,
    "2-12": s2_8,
    "2-13": c2_10_2,
    "2-14": s2_14,
    "2-15": c2_15_1,
    "2-16": c2_16_1,
    "2-17": s2_11,
    "2-18": s2_11,
    "2-19": s2_9,
    "2-20": s2_20,
    "2-21": c2_9_1,
    "2-22": c2_20_2,
    "2-23": c2_7_1,
    "2-24": s2_24,
    "2-25": c2_25_1,
    "2-26": c2_25_1,
    "2-27": c2_25_1,
    "2-28": s2_28,
    "2-29": c2_28_2,
    "2-30": s2_30,
    "2-31": c2_31_1,
    "2-32": c2_30_1,
    "2-33": c2_14_1,
    "3-1": s3_1,
    "3-2": s3_2,
    "3-3": c3_3_1,
    "3-4": s3_4,
    "3-5": s3_5,
    "3-6": s3_6,
    "3-7": c3_5_1,
    "3-8": s3_8,
    "3-9": c3_6_1,
    "3-10": s3_10,
    "3-11": c3_8_1,
    "3-12": s3_12,
    "3-13": c3_14_1,
    "3-14": c3_14_1,
    "3-15": c3_14_1,
    "3-16": s3_16,
    "3-17": c3_17_1,
    "3-18": s3_18,
    "3-19": s3_19,
    "3-20": s3_20,
    "3-21": s3_21,
    "3-22": s3_22,
    "3-23": s3_23,
    "3-24": c3_24_1,
    "3-25": c3_28_1,
    "3-26": c3_28_1,
    "3-27": c3_27_1,
    "3-28": c3_28_1,
    "3-29": c3_29_1,
    "3-30": c3_30_1,
    "3-31": s3_31,
    "3-32": s3_31,
    "3-33": s3_31,
    "3-34": s3_31,
    "3-35": s3_35,
    "3-36": s3_36,
    "3-37": s3_37,
    "3-38": c3_38_1,
    "3-39": c3_38_1,
    "3-40": c3_40_1,
    "3-41": s3_41,
    "3-42": c3_42_1,
    "3-43": s3_43,
    "3-44": c3_44_1,
    "3-45": s3_45,
    "3-46": s3_46,
    "3-47": c3_46_2,
    "3-48": c3_48_1,
    "3-49": c3_49_1,
    "3-50": c3_4_3,
    "3-51": c3_4_3,
    "3-52": s3_52,
    "3-53": s3_52,
    "3-54": s3_52,
    "3-55": s3_52,
    "3-56": s3_52,
    "3-57": s3_52,
    "3-58": s3_58,
    "3-59": s3_59,
    "3-60": s3_60,
    "3-61": s3_61,
    "3-62": s3_62,
    "3-63": c3_60_1,
    "3-64": c3_64_1,
    "3-65": s3_65,
    "3-66": s3_66,
    "3-67": c3_67_1,
    "3-68": s3_68,
    "3-69": c3_69_1,
    "3-70": c3_68_4,
    "3-71": c3_68_4,
    "3-72": c3_68_4,
    "3-73": s3_73,
    "3-74": c3_73_2,
    "3-75": s3_75,
    "3-76": c3_75_4,
    "3-77": c3_75_4,
    "3-78": s3_78,
    "3-79": c3_78_4,
    "3-80": c3_78_4,
    "3-81": c3_78_4,
    "4-1": c4_1_1,
    "4-2": c4_1_1,
    "4-3": s4_3,
    "4-4": s4_4,
    "4-5": c4_5_1,
    "4-6": s4_6,
    "4-7": s4_7,
    "4-8": s4_6,
    "4-9": s4_6,
    "4-10": s4_6,
    "4-11": s4_11,
    "4-12": c4_12_1,
    "4-13": s4_13,
    "4-14": s4_14,
    "4-15": s4_14,
    "4-16": s4_14,
    "4-17": c4_14_4,
    "4-18": c4_14_4,
    "4-19": c4_14_4,
    "4-20": s4_20,
    "4-21": s4_21,
    "4-22": c4_22_1,
    "4-23": c4_23_1,
    "4-24": c4_23_2,
    "4-25": s4_25,
    "4-26": s4_25,
    "4-27": s4_27,
    "4-28": s4_28,
    "4-29": c4_22_1,
    "5-1": s5_1,
    "5-2": s5_2,
    "5-3": c5_3_1,
    "5-4": s5_4,
    "5-5": c5_2_4,
    "5-6": c5_2_4,
    "5-7": c5_2_4,
    "5-8": c5_8_1,
    "5-9": c5_4_3,
    "5-10": s5_10,
    "5-11": c5_4_3,
    "5-12": c5_3_1,
    "5-13": c5_13_1,
    "5-14": c5_14_1,
    "5-15": s5_15,
    "5-16": c5_16_1,
    "5-17": s5_15,
    "5-18": s5_18,
    "5-19": c5_16_1,
    "5-20": c5_16_1,
    "5-21": c5_16_1,
    "5-22": c5_16_1,
    "5-23": c5_16_1,
    "5-24": c5_16_1,
    "5-25": c5_16_1,
    "5-26": c5_1_2,
    "5-27": c5_8_1,
    "5-28": s5_28,
    "5-29": s5_29,
    "5-30": s5_29,
    "5-31": c5_31_1,
    "5-32": s5_32,
    "5-33": s5_33,
    "5-34": s5_32,
    "5-35": s5_32,
    "5-36": s5_32,
    "5-37": s5_37,
    "5-38": c5_38_1,
    "5-39": c5_52_1,
    "5-40": s5_32,
    "5-41": s5_41,
    "5-42": c5_38_1,
    "5-43": c5_38_1,
    "5-44": s5_44,
    "5-45": s5_32,
    "5-46": s5_32,
    "5-47": s5_47,
    "5-48": c5_48_1,
    "5-49": c5_49_1,
    "5-50": c5_38_1,
    "5-51": s5_32,
    "5-52": c5_52_1,
    "5-53": s5_53,
    "5-54": c5_53_2,
    "5-55": s5_55,
    "5-56": c5_59_1,
    "5-57": s5_57,
    "5-58": s5_58,
    "5-59": c5_59_1,
    "5-60": c5_60_1,
    "5-61": c5_60_1,
    "5-62": c5_59_1,
    "5-63": s5_33,
    "5-64": c5_49_1,
}


def castle_choices(i):
    if i == 1:
        return s5_15_1().load()
    elif i == 2:
        return s5_15_2().load()
    elif i == 3:
        return s5_15_3().load()
    else:
        return [choice_unfinished()]


def getChoice(name):
    if name.__contains__("end"):
        return scene_end(name).load()
    elif gk.pos != 0:
        return castle_choices(gk.pos)
    else:
        k = all_choices.get(name)()
        if isinstance(k, scene_abstract):
            return k.load()
        elif isinstance(k, choice_abstract):
            return [k]
        else:
            return [choice_unfinished()]
