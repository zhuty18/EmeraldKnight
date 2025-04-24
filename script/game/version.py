# coding = utf-8

"""版本信息"""

import json

VERSION = None
if not VERSION:
    with open("data/info.json", "r", encoding="utf-8") as f:
        data = json.loads(f.read())
    VERSION = data["version"]
    CHAPTERS = data["chapters"]
    GAME_NAME = data["name"]
    GAME_INFO = data

DEBUG = True
