# coding = utf-8

"""打包数据以供android发布"""

import json
import os
import shutil

if __name__ == "__main__":
    # 所有选项打包为一个列表，存储在app/src/main/assets/choices.json里
    # 所有场景打包为一个列表，存储在app/src/main/assets/scenes.json里
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
    if not os.path.exists("app/src/main/assets"):
        os.mkdir("app/src/main/assets")
    with open("app/src/main/assets/choices.json", "w", encoding="utf-8") as f:
        f.write(json.dumps(choices, ensure_ascii=False, indent=4))
    with open("app/src/main/assets/scenes.json", "w", encoding="utf-8") as f:
        f.write(json.dumps(scenes, ensure_ascii=False, indent=4))

    # 所有场景文本打包为一个列表，存储在app/src/main/assets/scene_text.json
    # [{"id":"场景id","value":"场景文本"}]
    scene_text = []
    chapter_list = os.listdir("../data/story")
    for ch in range(1, info["chapters"] + 1):
        with open(
            f"../data/story/story_ch{ch}.json", "r", encoding="utf-8"
        ) as f:
            scene_text.extend(json.loads(f.read()))
    with open("../data/story/story_end.json", "r", encoding="utf-8") as f:
        scene_text.extend(json.loads(f.read()))
    with open(
        "app/src/main/assets/scene_text.json", "w", encoding="utf-8"
    ) as f:
        f.write(json.dumps(scene_text, ensure_ascii=False, indent=4))

    # 其他json配置文件移动到app/src/main/assets
    json_files = os.listdir("../data")
    json_files = {x if x.endswith(".json") else None for x in json_files}
    if None in json_files:
        json_files.remove(None)
    for file in json_files:
        shutil.copyfile(f"../data/{file}", f"app/src/main/assets/{file}")

    # 图标文件移动到app/src/main/res/drawable
    icon_files = os.listdir("../data")
    icon_files = {x if x.endswith(".png") else None for x in icon_files}
    if None in icon_files:
        icon_files.remove(None)
    if not os.path.exists("app/src/main/res/drawable"):
        os.mkdir("app/src/main/res/drawable")
    for file in icon_files:
        shutil.copyfile(f"../data/{file}", f"app/src/main/res/drawable/{file}")

    with open("../data/info.json", "r", encoding="utf-8") as f:
        data = json.loads(f.read())
    # 版本号等信息注入app/build.gradle.kts
    with open("app/build.gradle.kts", "r", encoding="utf-8") as f:
        bundle_data = f.read()
    bundle_data = bundle_data.replace(
        "versionCode = 1", f"versionCode = {data["version_number"]}"
    )
    bundle_data = bundle_data.replace(
        'versionName = "1.0"', f'versionName = "{data["version"]}"'
    )
    with open("app/build.gradle.kts", "w", encoding="utf-8") as f:
        f.write(bundle_data)

    # 信息注入app/src/main/res/values/strings.xml
    with open(
        "app/src/main/res/values/strings.xml", "r", encoding="utf-8"
    ) as f:
        string_data = f.read()
    string_data = string_data.replace(
        '<string name="app_name">翡翠骑士</string>',
        f'<string name="app_name">{data["name"]}</string>',
    )
    string_data = string_data.replace(
        '<string name="version">v1.2</string>',
        f'<string name="version">v{data["version"]}</string>',
    )
    poem = "\n".join(["#160;&#160;&#160;&#160;".join(i) for i in data["poem"]])
    string_data = string_data.replace(
        '<string name="poem">雪山之巅&#160;&#160;&#160;&#160;英魂渐远\n危城影下&#160;&#160;&#160;&#160;一念不灭\n剑心重铸&#160;&#160;&#160;&#160;翡翠长明\n孤星陨灭&#160;&#160;&#160;&#160;万灵恸哭</string>',
        f'<string name="poem">{poem}</string>',
    )
    string_data = string_data.replace(
        '<string name="author_info">作者：兔子草\nQQ：3440950898\n邮箱：13718054285@163.com</string>',
        f'<string name="author_info">作者：{data["author"]}\nQQ：{data["contact_qq"]}\n邮箱：{data["contact_email"]}</string>',
    )
    string_data = string_data.replace(
        '<string name="project_url">https://github.com/zhuty18/EmeraldKnight</string>',
        f'<string name="project_url">{data["home_url"]}</string>',
    )
    with open(
        "app/src/main/res/values/strings.xml", "w", encoding="utf-8"
    ) as f:
        f.write(string_data)
