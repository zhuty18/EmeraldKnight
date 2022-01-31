from abstract import scene_end, choice_unfinished
from ch1 import *
from ch2 import *
from ch3 import *

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
    "3-30": c3_30_1
}


def getChoice(name):
    if name.__contains__("end"):
        return scene_end(name).load()
    else:
        k = all_choices.get(name)()
        if isinstance(k, scene_abstract):
            return k.load()
        elif isinstance(k, choice_abstract):
            return [k]
        else:
            return [choice_unfinished()]