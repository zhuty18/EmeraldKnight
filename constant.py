import json
from random import random

BRUCE_STORY_LINE = "bsl"
BRUCE_SHOW_UP = "bsu"
BRUCE_LOVE = "brl"
OLIVER_STORY_LINE = "osl"
OLIVER_LOVE = "oll"
SINESTRO_STORY_LINE = "ssl"
SINESTRO_LOVE = "sil"
SINESTRO_TAME = "sit"
BARRY_LOVE = "bal"

SWORD_HOT_TIME = "sht"
KNOWLEDGE = "knw"
INTELLIGENCE = "int"
TEMPORARY = "tmp"
PROPS = "pro"
CREDIT = "cre"
PEGASUS = "pgs"

TEAMMATE = "tmm"
BRUCE_CODE = 1
SINESTRO_CODE = 2
OLIVER_CODE = 3
BARRY_CODE = 4

GAME_OVER = "game over"

character_para = {
    BRUCE_STORY_LINE: 0,
    BRUCE_SHOW_UP: 0,
    BRUCE_LOVE: 0,
    OLIVER_STORY_LINE: 0,
    OLIVER_LOVE: 0,
    SINESTRO_STORY_LINE: 0,
    SINESTRO_LOVE: 0,
    SINESTRO_TAME: 0,
    BARRY_LOVE: 0,
}
stroy_para = {
    TEAMMATE: 0,
    SWORD_HOT_TIME: 0,
    KNOWLEDGE: 0,
    INTELLIGENCE: 0,
    TEMPORARY: 0,
    PROPS: 0,
    CREDIT: 0,
    PEGASUS: 0,
}

debug_para = {**character_para, **stroy_para}


def res_path(fn):
    import sys, os
    if getattr(sys, 'frozen', False):  #是否Bundle Resource
        root = sys._MEIPASS
    else:
        root = os.path.abspath(".")
    return os.path.join(root, fn)


def default_para():
    return debug_para


__sn__ = {}


def sceneName(scene):
    global __sn__
    if len(__sn__) == 0:
        import json
        f = open(res_path("story/menu.json"), "r", encoding="utf8")
        __sn__ = json.loads(f.read())
        f.close()
    return __sn__.get(scene, "找不到场景名")


class gk:
    scene = ""
    paras = {}
    pos = 0

    def openPara(para_name):
        f = open(res_path("save/0.eks"), "r")
        p = json.loads(f.read())
        f.close()
        p[para_name] = 1
        f = open(res_path("save/0.eks"), "w")
        f.write(json.dumps(p) + "\n")
        f.close()

    def readPara(para_name):
        f = open(res_path("save/0.eks"), "r")
        p = json.loads(f.read())
        f.close()
        return p[para_name]

    def fight():
        hp = gk.paras[TEMPORARY]
        hp += 3 * gk.paras[INTELLIGENCE]
        hp += gk.paras[KNOWLEDGE]
        hp += 5 * gk.paras[BRUCE_LOVE]
        hp += 5 * (gk.paras[SINESTRO_LOVE] + gk.paras[SINESTRO_TAME])
        hp += 20 * (gk.paras[TEAMMATE] != 0)
        for i in range(10):
            hp -= random() * 16
        return hp > 0


f = open(res_path("story/info.json"), "r", encoding="utf8")
info_map = json.loads(f.read())
f.close()


def open_info_entry(name):
    for i in info_map.keys():
        if name in info_map[i]["scene"]:
            gk.openPara(i)
