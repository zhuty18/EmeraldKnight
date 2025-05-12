# coding = utf-8

"""打包数据以供android发布"""

import json
import os
import re
import shutil

if __name__ == "__main__":
    # json配置文件复制到app/src/main/assets
    json_files = os.listdir("../data")
    json_files = {x if x.endswith(".json") else None for x in json_files}
    if None in json_files:
        json_files.remove(None)
    if not os.path.exists("app/src/main/assets"):
        os.mkdir("app/src/main/assets")
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
    version_code = re.findall(r"versionCode = (\d+)\n", bundle_data)[0]
    bundle_data = bundle_data.replace(
        f"versionCode = {version_code}",
        f'versionCode = {data["version_number"]}',
    )

    version_name = re.findall(r'versionName = "(.+)"\n', bundle_data)[0]
    bundle_data = bundle_data.replace(
        f'versionName = "{version_name}"',
        f'versionName = "{data["version"]}"',
    )
    with open("app/build.gradle.kts", "w", encoding="utf-8") as f:
        f.write(bundle_data)

    # 信息注入app/src/main/res/values/strings.xml
    with open(
        "app/src/main/res/values/strings.xml", "r", encoding="utf-8"
    ) as f:
        string_data = f.read()
    name = re.findall(
        r'<string name="app_name">(.*)</string>',
        string_data,
    )
    string_data = string_data.replace(
        f'<string name="app_name">{name[0]}</string>',
        f'<string name="app_name">{data["name"]}</string>',
    )

    version = re.findall(r'<string name="version">v(.*)</string>', string_data)[
        0
    ]
    string_data = string_data.replace(
        f'<string name="version">v{version}</string>',
        f'<string name="version">v{data["version"]}</string>',
    )

    poem = re.findall(r'<string name="poem">(.*)</string>', string_data)[0]
    string_data = string_data.replace(
        f'<string name="poem">{poem}</string>',
        f'<string name="poem">{"\\n".join(["&#160;&#160;&#160;&#160;".join(line)for line in data["poem"]])}</string>',
    )

    author = re.findall(r'<string name="author">by (.*)</string>', string_data)[
        0
    ]
    string_data = string_data.replace(
        f'<string name="author">by {author}</string>',
        f'<string name="author">by {data["author"]}</string>',
    )

    contact_qq = re.findall(
        r'<string name="author_info">QQ：(.*)\\n(.*)</string>', string_data
    )[0]
    string_data = string_data.replace(
        f'<string name="author_info">QQ：{contact_qq[0]}\\n{contact_qq[1]}</string>',
        f'<string name="author_info">QQ：{data["contact_qq"]}\\n{contact_qq[1]}</string>',
    )

    contact_email = re.findall(
        r'<string name="author_info">(.*)邮箱：(.*)</string>', string_data
    )[0]
    string_data = string_data.replace(
        f'<string name="author_info">{contact_email[0]}邮箱：{contact_email[1]}</string>',
        f'<string name="author_info">{contact_email[0]}邮箱：{data["contact_email"]}</string>',
    )

    project_url = re.findall(
        r'<string name="project_url">(.*)</string>', string_data
    )[0]
    string_data = string_data.replace(
        f'<string name="project_url">{project_url}</string>',
        f'<string name="project_url">{data["home_url"]}</string>',
    )

    with open(
        "app/src/main/res/values/strings.xml", "w", encoding="utf-8"
    ) as f:
        f.write(string_data)
