# coding = utf-8

"""数据排序"""


def key_priority(key):
    """键优先级"""
    keys = [
        "id",
        "description",
        "name",
        "default_value",
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
        "scene",
        "require",
        "match_options",
        "options",
        "options_win",
        "options_lose",
    ]
    if key in keys:
        return keys.index(key)
    else:
        return key


def id_priority(x_id):
    """ID优先级"""
    if "-" in x_id:
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
