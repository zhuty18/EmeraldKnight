# coding = utf-8

"""数据排序"""


def key_priority_add(keys, new_keys):
    """添加新键"""
    for key in new_keys:
        if key not in keys:
            keys.append(key)


def key_priority(key):
    """键优先级"""
    keys = ["id", "description", "value"]

    choice_keys = ["id", "target", "show", "choose"]
    act_keys = ["op", "condition", "check", "change", "para", "value"]
    key_priority_add(choice_keys, act_keys)
    key_priority_add(keys, choice_keys)

    scene_keys = ["id", "name", "options", "require"]
    option_keys = ["match_options", "options_lose", "options_win"]
    key_priority_add(scene_keys, option_keys)
    key_priority_add(keys, scene_keys)

    char_keys = ["id", "name", "type", "max_life", "actions"]
    key_priority_add(keys, char_keys)

    actions_keys = ["id", "name", "type", "text"]
    attack_keys = ["strength", "self_hurt", "show", "chance"]
    key_priority_add(actions_keys, attack_keys)
    heal_keys = ["min", "max", "first", "trigger", "time"]
    key_priority_add(actions_keys, heal_keys)
    key_priority_add(keys, actions_keys)

    para_keys = ["id", "name", "default_value"]
    key_priority_add(keys, para_keys)

    if key in keys:
        return keys.index(key)
    else:
        return key


def id_priority(x_id):
    """ID优先级"""
    if "end-" in x_id:
        return [100, int(x_id.split("-")[1])]
    elif "-" in x_id:
        return [int(t) for t in x_id.split("-")]
    else:
        return x_id


def item_priority(x):
    """个体优先级"""
    if "id" in x:
        return id_priority(x["id"])
    else:
        return 0


def sort_dict(d):
    """字典排序"""
    for k, v in d.items():
        if isinstance(v, dict):
            d[k] = sort_dict(v)
        elif isinstance(v, list):
            d[k] = sort_list(v)
    # print([key_priority(t) for t in d.keys()])
    return {
        k: v for k, v in sorted(d.items(), key=lambda t: key_priority(t[0]))
    }


def sort_list(l):
    """列表排序"""
    return sorted(
        [
            (
                sort_dict(x)
                if isinstance(x, dict)
                else sort_list(x) if isinstance(x, list) else x
            )
            for x in l
        ],
        key=item_priority,
    )


def sort_data(x):
    """排序物体"""
    return (
        sort_dict(x)
        if isinstance(x, dict)
        else sort_list(x) if isinstance(x, list) else x
    )
