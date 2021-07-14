import json

BRUCE_STORY_LINE = "bsl"
BRUCE_SHOW_UP = "bsu"
BRUCE_LOVE = "brul"
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
TEMPORARY = "tmp"

GAME_OVER = "game over"

debug_para = {
    BRUCE_STORY_LINE: 1,
    BRUCE_SHOW_UP: 0,
    BRUCE_LOVE: 0,
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
    TEMPORARY: 0,
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
    "1-30": "追上去",
    "1-31": "四处走走",
    "1-32": "去追黑影",
    "1-33": "在湖边休息",  #TODO 银鳞村
    "1-34": "用光明术",
    "1-35": "这是什么地方？",
    "1-36": "你是什么人？",
    "1-37": "怎么离开这儿？",
    "1-38": "你确定吗？",
    "1-39": "阵眼是什么样的？",
    "1-40": "黑球",
    "1-41": "绿光",
    "1-42": "法师塔是什么？",
    "1-43": "你叫什么？",  #TODO 天使城
    "1-44": "四下看看",
    "1-45": "这应该就是阵眼",
    "1-46": "布鲁斯",
    "end-1": "无事发生",
}

end = {END_NOTHING: 0}
