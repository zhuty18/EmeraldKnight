# coding = utf-8

"""打包数据以供android发布"""

import json
import os

if __name__ == "__main__":
    # 所有选项打包为一个列表，存储在app/src/main/asset/choices.json里
    # 所有场景打包为一个列表，存储在app/src/main/asset/scenes.json里
    with open("../data/info.json", "r", encoding="utf-8") as f:
        info = json.loads(f.read())
    scenes = []
    choices = []
    for ch in range(1, info["chapters"] + 1):
        with open(
            f"../data/chapter/choices_ch{ch}.json", "r", encoding="utf-8"
        ) as f:
            choices.extend(json.loads(f.read()))
        with open(
            f"../data/chapter/scenes_ch{ch}.json", "r", encoding="utf-8"
        ) as f:
            scenes.extend(json.loads(f.read()))
    if not os.path.exists("app/src/main/asset"):
        os.mkdir("app/src/main/asset")
    with open("app/src/main/asset/choices.json", "w", encoding="utf-8") as f:
        f.write(json.dumps(choices, ensure_ascii=False, indent=4))
    with open("app/src/main/asset/scenes.json", "w", encoding="utf-8") as f:
        f.write(json.dumps(scenes, ensure_ascii=False, indent=4))

    # 所有场景文本打包为一个列表，存储在app/src/main/asset/scene_text.json
    # [{"id":"场景id","text":"场景文本"}]
    scene_text = []
    chapter_list = os.listdir("../data/story")
    for ch in chapter_list:
        scene_list = os.listdir(f"../data/story/{ch}")
        for i in scene_list:
            if i.endswith(".txt"):
                with open(
                    f"../data/story/{ch}/{i}", "r", encoding="utf-8"
                ) as f:
                    scene_text.append({"id": i[:-4], "text": f.read()})
    with open("app/src/main/asset/scene_text.json", "w", encoding="utf-8") as f:
        f.write(json.dumps(scene_text, ensure_ascii=False, indent=4))

    # 其他json配置文件移动到app/src/main/asset
    json_files = os.listdir("../data")
    json_files = {x if x.endswith(".json") else None for x in json_files}
    if None in json_files:
        json_files.remove(None)
    for file in json_files:
        os.system(
            f"cp {os.path.join("../data",file)} {os.path.join("app/src/main/asset",file)}"
        )

    # 图标文件移动到app/src/main/res/drawable
    icon_files = os.listdir("../data")
    icon_files = {x if x.endswith(".png") else None for x in icon_files}
    if None in icon_files:
        icon_files.remove(None)
    if not os.path.exists("app/src/main/res/drawable"):
        os.mkdir("app/src/main/res/drawable")
    for file in icon_files:
        os.system(
            f"cp {os.path.join("../data",file)} {os.path.join("app/src/main/res/drawable",file)}"
        )
