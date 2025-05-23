# coding = utf-8

"""打包配置为一个文件"""

import json
from copy import deepcopy

from utils import write_data

config = {}


def add_map(name, data, value_only=False):
    """添加一个列表到配置中"""
    config[name] = {}
    for item in data:
        tmp = deepcopy(item)
        tmp.pop("id")
        config[name][item["id"]] = item["value"] if value_only else tmp


with open("data/characters.json", "r", encoding="utf-8") as f:
    add_map("char_map", json.load(f))

with open("data/choices.json", "r", encoding="utf-8") as f:
    add_map("choice_map", json.load(f))

with open("data/consts.json", "r", encoding="utf-8") as f:
    add_map("const_map", json.load(f))

with open("data/names.json", "r", encoding="utf-8") as f:
    names = json.load(f)
    add_map("chap_map", names["chapter_names"], True)
    add_map("end_map", names["end_names"], True)

with open("data/paras.json", "r", encoding="utf-8") as f:
    paras = json.load(f)
    add_map("para_map", paras["para_list"])
    config["func_list"] = paras["func_list"]
    add_map("code_map", paras["code_list"], True)

with open("data/scenes.json", "r", encoding="utf-8") as f:
    add_map("path_map", json.load(f))

with open("data/story_text.json", "r", encoding="utf-8") as f:
    add_map("story_map", json.load(f), True)


write_data(config, "data/config.json")
