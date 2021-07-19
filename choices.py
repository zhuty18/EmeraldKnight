from ch1 import *


def getChoice(name):
    if name.startswith("1-"):
        return getCh1(name)
    elif name.__contains__("end"):
        return scene_end(name).load()


def getCh1(name):
    if name == "1-1":
        return s1_1().load()
    elif name == "1-2":
        return s1_2().load()
    elif name == "1-3":
        return s1_3().load()
    elif name == "1-4":
        return s1_4().load()
    elif name == "1-5":
        return s1_5().load()
    elif name == "1-6":
        return s1_6().load()
    elif name == "1-7":
        return s1_7().load()
    elif name == "1-8":
        return s1_8().load()
    elif name == "1-9":
        return [c1_4_3()]
    elif name == "1-10":
        return [c1_4_3()]
    elif name == "1-11":
        return s1_11().load()
    elif name == "1-12":
        return s1_12().load()
    elif name == "1-13":
        return [c1_5_1()]
    elif name == "1-14":
        return s1_14().load()
    elif name == "1-15":
        return [c1_15_1()]
    elif name == "1-16":
        return s1_16().load()
    elif name == "1-17":
        return s1_17().load()
    elif name == "1-18":
        return [c1_6_1()]
    elif name == "1-19":
        return s1_19().load()
    elif name == "1-20" or name == "1-21" or name == "1-22" or name == "1-23":
        return [c1_12_0()]
    elif name == "1-24":
        return s1_24().load()
    elif name == "1-25" or name == "1-26" or name == "1-27" or name == "1-28":
        return [c1_24_0()]
    elif name == "1-29":
        return s1_29().load()
    elif name == "1-30":
        return s1_39().load()
    elif name == "1-31":
        return s1_31().load()
    elif name == "1-32":
        return [c1_31_2()]
    elif name == "1-33":
        return [c1_16_1()]
    elif name == "1-34":
        return s1_34().load()
    elif name == "1-35":
        return s1_35().load()
    elif name == "1-36":
        return s1_36().load()
    elif name == "1-37":
        return s1_37().load()
    elif name == "1-38":
        return [c1_38_1()]
    elif name == "1-39":
        return s1_39().load()
    elif name == "1-40":
        return s1_40().load()
    elif name == "1-41":
        return s1_41().load()
    elif name == "1-42":
        return [c1_41_2()]
    elif name == "1-43":
        return [c1_16_3()]
    elif name == "1-44":
        return s1_31().load()
    elif name == "1-45":
        return [c1_31_2()]
    elif name == "1-46":
        return s1_46().load()
    elif name == "1-47":
        return [c1_16_1()]
    elif name == "1-48":
        return [c1_14_1()]
    elif name == "1-49":
        return s1_49().load()
    elif name == "1-50":
        return [c1_16_3()]
    elif name == "1-51":
        return [c1_16_2()]
    elif name == "1-52":
        return s1_52().load()
    elif name == "1-53":
        return [c1_52_2()]
    elif name == "1-54":
        return [c1_16_2()]
    elif name == "1-55" or name == "1-56" or name == "1-57":
        return [c1_11_4()]
    elif name == "1-58":
        return s1_58().load()
    elif name == "1-59" or name == "1-60" or name == "1-61":
        return [c1_58_4()]
    elif name == "1-62":
        return s1_62().load()
    elif name == "1-63":
        return s1_63().load()
    elif name == "1-64":
        return s1_64().load()
    elif name == "1-65":
        return [c1_64_2()]
    elif name == "1-66":
        return s1_66().load()
    else:
        return [choice_unfinished()]