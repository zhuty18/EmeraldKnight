# coding = utf-8

"""打包数据以供android发布"""

import json
import os
import re
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
    write_data = bundle_data
    bundle_data = bundle_data.split("\n")
    for line in bundle_data:
        if "versionCode" in line:
            version_code = re.findall(
                re.compile(r"versionCode = (\d+)", re.S), line
            )[0]
            write_data = write_data.replace(
                line, line.replace(version_code, str(data["version_number"]))
            )
        elif "versionName" in line:
            version_name = re.findall(
                re.compile(r'versionName = "(.+)"', re.S), line
            )[0]
            write_data = write_data.replace(
                line, line.replace(version_name, data["version"])
            )
    with open("app/build.gradle.kts", "w", encoding="utf-8") as f:
        f.write(write_data)

    # 信息注入app/src/main/res/values/strings.xml
    with open(
        "app/src/main/res/values/strings.xml", "r", encoding="utf-8"
    ) as f:
        string_data = f.read()
    write_data = string_data
    string_data = string_data.split("\n")
    for line in string_data:
        ori_name = re.findall(
            re.compile(r'<string name="app_name">(.*)</string>', re.S), line
        )
        if ori_name:
            ori_name = ori_name[0]
            write_data = write_data.replace(
                line, line.replace(ori_name, data["name"])
            )

        version = re.findall(
            re.compile(r'<string name="version">v(.*)</string>', re.S), line
        )
        if version:
            version = version[0]
            write_data = write_data.replace(
                line, line.replace(version, data["version"])
            )

        old_poem = re.findall(
            re.compile(r'<string name="poem">(.*)</string>', re.S), line
        )
        if old_poem:
            old_poem = old_poem[0]
            write_data = write_data.replace(
                line,
                line.replace(
                    old_poem,
                    "\\n".join(
                        [
                            "&#160;&#160;&#160;&#160;".join(i)
                            for i in data["poem"]
                        ]
                    ),
                ),
            )
        author = re.findall(
            re.compile(r'<string name="author">by (.*)</string>', re.S), line
        )
        if author:
            author = author[0]
            write_data = write_data.replace(
                line, line.replace(author, data["author"])
            )

        contact_qq = re.findall(
            re.compile(
                r'<string name="author_info">QQ：(.*)\n.*</string>', re.S
            ),
            line,
        )
        if contact_qq:
            contact_qq = contact_qq[0]
            write_data = write_data.replace(
                line, line.replace(contact_qq, data["contact_qq"])
            )

        contact_email = re.findall(
            re.compile(
                r'<string name="author_info">.*邮箱：(.*)</string>', re.S
            ),
            line,
        )
        if contact_email:
            contact_email = contact_email[0]
            write_data = write_data.replace(
                line, line.replace(contact_email, data["contact_email"])
            )

        project_url = re.findall(
            re.compile(r'<string name="project_url">(.*)</string>', re.S),
            line,
        )
        if project_url:
            project_url = project_url[0]
            write_data = write_data.replace(
                line, line.replace(project_url, data["home_url"])
            )
    with open(
        "app/src/main/res/values/strings.xml", "w", encoding="utf-8"
    ) as f:
        f.write(write_data)
