import json
BRUCE_STORY_LINE = "bsl"
BRUCE_SHOW_UP = "bsu"
OLIVER_STORY_LINE = "osl"
SINESTRO_STORY_LINE = "ssl"
SINESTRO_LOVE = "sinl"
SINESTRO_TAME = "sint"
SWORD_HOT_TIME = "sht"
END_NOTHING = "end-1"
KNOWLEDGE = "know"
INTELLIGENCE = "intel"
WIZARD_TOWER_CRYSTAL = "wtc"
WIZARD_TOWER_RUNE = "wtr"

GAME_OVER = "game over"

debug_para = {
    BRUCE_STORY_LINE: 1,
    BRUCE_SHOW_UP: 0,
    OLIVER_STORY_LINE: 0,
    SINESTRO_STORY_LINE: 1,
    SINESTRO_LOVE: 0,
    SINESTRO_TAME: 0,
    SWORD_HOT_TIME: 0,
    END_NOTHING: 0,
    KNOWLEDGE: 0,
    INTELLIGENCE: 0,
    WIZARD_TOWER_CRYSTAL: 0,
    WIZARD_TOWER_RUNE: 0,
}
f = open("./data/0.eks", "r")
default_para = json.loads(f.readline())
f.close()

sceneName = {
    "1-1": "出发",
    "1-2": "继续前进",
    "1-3": "原路返回",
    "1-4": "就地睡一觉",
    "1-5": "跟着前进",
    "1-6": "原地蹲守",  # TODO
    "1-7": "不理会",
    "1-8": "上树跟去看看",  # TODO
    "1-9": "呛回去",  # TODO
    "1-10": "谢谢他",  # TODO
    "1-11": "“你是谁？”",  # TODO
    "1-12": "进去",
    "1-13": "先四下看看",
    "1-14": "上去敲门",  # TODO
    "1-17": "回家睡觉",
    "1-19": "当然要继续",  # TODO
    "1-20": "红晶石",
    "1-21": "蓝晶石",
    "1-22": "紫晶石",
    "1-23": "绿晶石",
    "1-24": "继续前进",
    "1-25": "光明符文",
    "1-26": "大地符文",
    "1-27": "黑暗符文",
    "1-28": "雷电符文",
    "1-29": "推门离开",
    "1-30": "追上去",  # TODO
    "1-34": "用光明术",
    "end-1": "无事发生",
}

end = {
    END_NOTHING: 0
}
