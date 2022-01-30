BRUCE_STORY_LINE = "bsl"
BRUCE_SHOW_UP = "bsu"
BRUCE_LOVE = "brul"
OLIVER_STORY_LINE = "osl"
OLIVER_LOVE = "oll"
SINESTRO_STORY_LINE = "ssl"
SINESTRO_LOVE = "sinl"
SINESTRO_TAME = "sint"
BARRY_LOVE = "bal"

SWORD_HOT_TIME = "sht"
KNOWLEDGE = "know"
INTELLIGENCE = "intel"
WIZARD_TOWER_CRYSTAL = "wtc"
WIZARD_TOWER_RUNE = "wtr"
TEMPORARY = "tmp"
CREDIT = "cre"

TEAMMATE = "tm"
BRUCE_CODE = 1
SINESTRO_CODE = 2
OLIVER_CODE = 3

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
    WIZARD_TOWER_CRYSTAL: 0,
    WIZARD_TOWER_RUNE: 0,
    TEMPORARY: 0,
    CREDIT: 0,
}
# end = {END_NOTHING: 0}

debug_para = {**character_para, **stroy_para}
# debug_para = {**debug_para, **end}


def res_path(fn):
    import sys, os
    if getattr(sys, 'frozen', False):  #是否Bundle Resource
        root = sys._MEIPASS
    else:
        root = os.path.abspath(".")
    return os.path.join(root, fn)


def default_para():
    # f = open("./save/0.eks", "r")
    # default = json.loads(f.readline())
    # f.close()
    # return default
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
    core = None
