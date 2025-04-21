import json
import re

CHAPTER = 7
MAX_CHAPTER = 7


def id_sort_by(x_id):
    """id排序器"""
    return [int(t) for t in x_id.split("-")]


def format_choices(ch):
    """格式化选项"""
    choices = []

    with open(f"script/ch{ch}_choices.py", "r", encoding="utf8") as f:
        data = f.read().split("class")

    for d in data[1:]:
        if "choice_abstract" in d:
            tmp = {}
            tmp["id"] = (
                d.split("(")[0].strip().replace("_", "-").replace("c", "")
            )
            try:
                tmp["target"] = re.findall(
                    re.compile(r"target = \"([end0-9\-]*)\"\n", re.S), d
                )[0].strip()
            except IndexError:
                pass

            if "text" in d:
                tmp1 = d.split("def")
                for j in tmp1:
                    if "text" in j:
                        tmp["text"] = re.findall(
                            re.compile(r"return\s\"(.*)\"", re.S), d
                        )[0].strip()
            if "show" in d:
                tmp["show"] = {"op": "", "condition": []}
            if "chosen" in d:
                tmp["choose"] = []
            choices.append(tmp)

    choices.sort(key=lambda x: id_sort_by(x["id"]))
    with open(f"game/choices_ch{ch}_auto.json", "w", encoding="utf8") as f:
        f.write(json.dumps(choices, ensure_ascii=False))


def format_scenes(ch):
    """格式化场景"""
    scenes = []

    with open(f"script/ch{ch}.py", "r", encoding="utf8") as f:
        data = f.read().split("class")
    with open("story/menu.json", "r", encoding="utf8") as f:
        scene_names = json.loads(f.read())

    scene_set = set()
    for d in data[1:]:
        if "scene_abstract" in d:
            tmp = {}
            tmp["id"] = (
                d.split("(")[0].strip().replace("_", "-").replace("s", "")
            )
            try:
                tmp["name"] = scene_names[tmp["id"]]
            except KeyError:
                pass
            for j in d.split("\n"):
                if "options =" in j:
                    try:
                        tmp["options"] = j.split("[")[1].strip("]").split(",")
                        tmp["options"] = [
                            i.replace("_", "-").replace("c", "").strip()
                            for i in tmp["options"]
                        ]
                    except TypeError:
                        tmp["options"] = []
            scenes.append(tmp)
            scene_set.add(tmp["id"])

    all_scenes = {}
    with open("script/choices.py", "r", encoding="utf8") as f:
        for line in f.readlines():
            if f'"{ch}-' in line:
                all_scenes[line.split('"')[1]] = (
                    line.split('"')[-1].strip("c,: \n").replace("_", "-")
                )
    all_scenes = {
        k: v
        for k, v in sorted(all_scenes.items(), key=lambda x: id_sort_by(x[0]))
    }
    for j in range(int(list(all_scenes.keys())[-1].split("-")[-1])):
        if f"{ch}-{j+1}" not in scene_set:
            tmp = {
                "id": f"{ch}-{j+1}",
                "name": scene_names[f"{ch}-{j+1}"],
                "options": [all_scenes[f"{ch}-{j+1}"]],
            }
            if all_scenes[f"{ch}-{j+1}"].startswith("s"):
                tmp["options"] = get_same_scene(
                    scenes, all_scenes[f"{ch}-{j+1}"].strip("s")
                )
            scenes.append(sort_json(tmp))
    scenes.sort(key=lambda x: id_sort_by(x["id"]))

    with open(f"game/scenes_ch{ch}_auto.json", "w", encoding="utf8") as f:
        f.write(json.dumps(scenes, ensure_ascii=False))


def key_piority(key):
    """键优先级"""
    keys = [
        "id",
        "target",
        "text",
        "show",
        "choose",
        "op",
        "condition",
        "check",
        "change",
        "para",
        "value",
        "name",
        "scene",
        "require",
        "match_options",
        "options",
        "options_win",
        "options_lose",
    ]
    return keys.index(key)


def legal_para(para):
    """合法的参数"""
    with open("game/paras.json", "r", encoding="utf8") as f:
        paras = json.loads(f.read())["para_list"]
    paras = [p["name"] for p in paras]
    paras.append("SCENE")
    paras.append("END")
    paras.append("FIGHT")
    paras.append("CHOICE")
    return para in paras


def legal_action(act):
    """合法修改"""
    acts = ["ADD", "SET"]
    return act in acts


def legal_check_act(check):
    """合法检测"""
    checks = [
        "EQUAL",
        "UNEQUAL",
        "MORE",
        "LESS",
        "MORE_EQUAL",
        "LESS_EQUAL",
        "BINARY",
        "NON_BINARY",
        "CHECK_END",
    ]
    return check in checks


def legal_check_op(op):
    """合法运算"""
    ops = ["AND", "OR"]
    return op in ops


def sort_json(x):
    """将json排序"""
    return {k: v for k, v in sorted(x.items(), key=lambda t: key_piority(t[0]))}


def check_condition(c_id, c):
    """检查条件合法性"""
    a = legal_check_act(c["check"])
    if not a:
        print("Choice ID:", c_id, "Illegal check action:", c["check"])
    b = legal_para(c["para"])
    if not b:
        print("Choice ID:", c_id, "Illegal para name:", c["para"])


def check_show(c_id, check):
    """检查show合法性"""
    if not legal_check_op(check["op"]):
        print("Choice ID:", c_id, "Illegal check operation:", check["op"])
    tmp = sort_json(check)
    tmp["condition"] = []
    for c in check["condition"]:
        check_condition(c_id, c)
        tmp["condition"].append(sort_json(c))
    return tmp


def check_act(c_id, c):
    """检查修改合法性"""
    a = legal_action(c["change"])
    if not a:
        print("Choice ID:", c_id, "Illegal change:", c["change"])
    b = legal_para(c["para"])
    if not b:
        print("Choice ID:", c_id, "Illegal para name:", c["para"])
    return a and b


def check_choose(c_id, change):
    """检查choose合法性"""
    tmp = []
    for c in change:
        if c["change"] == "CONDITION":
            check_condition(c_id, c["para"])
            c["value"] = check_choose(c_id, c["value"])
        else:
            check_act(c_id, c)
        tmp.append(sort_json(c))
    return tmp


def check_choices(ch):
    """检查choices合法性"""
    with open(f"game/choices_ch{ch}.json", "r", encoding="utf8") as f:
        choices = json.loads(f.read())
    res = []
    choice_set = set()
    for c in choices:
        tmp = sort_json(c)
        if tmp["id"] not in choice_set:
            choice_set.add(tmp["id"])
        else:
            print("Duplicate id:", tmp["id"])
        if "show" in tmp:
            tmp["show"] = check_show(tmp["id"], tmp["show"])
        if "choose" in tmp:
            tmp["choose"] = check_choose(tmp["id"], tmp["choose"])
        res.append(tmp)

    res.sort(key=lambda x: id_sort_by(x["id"]))
    with open(f"game/choices_ch{ch}_auto.json", "w", encoding="utf8") as f:
        f.write(json.dumps(res, ensure_ascii=False))
    return choice_set


def check_options(s_id, option, choice_set):
    """检查options合法性"""
    for op in option:
        if not op in choice_set:
            print("Scene ID:", s_id, "Invalid option:", op)
    return sorted(option, key=id_sort_by)


def get_same_scene(scene_list, s_id):
    """获得场景选项"""
    for k in scene_list:
        if k["id"] == s_id:
            return k["options"]


def check_scenes(ch, choice_set):
    """检查scenes合法性"""
    with open(f"game/scenes_ch{ch}.json", "r", encoding="utf8") as f:
        scenes = json.loads(f.read())
    with open("story/menu.json", "r", encoding="utf8") as f:
        scene_names = json.loads(f.read())
    scene_set = set()
    res = []
    for s in scenes:
        if s["id"] not in scene_set:
            scene_set.add(s["id"])
        else:
            print(f"Duplicate ID found: {s['id']}")
        if not "scene" in s:
            s["name"] = scene_names[s["id"]]
        s["options"] = check_options(s["id"], s["options"], choice_set)
        res.append(sort_json(s))

    res.sort(key=lambda x: id_sort_by(x["id"]))

    with open(f"game/scenes_ch{ch}_auto.json", "w", encoding="utf8") as f:
        f.write(json.dumps(res, ensure_ascii=False))


if CHAPTER <= MAX_CHAPTER:
    format_choices(CHAPTER)
    format_scenes(CHAPTER)
for i in range(1, CHAPTER):
    choice_id = check_choices(i)
    check_scenes(i, choice_id)
