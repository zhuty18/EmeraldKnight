# coding = utf-8

"""通用工具"""

import json
from copy import deepcopy

from data_sorting import sort_data


def censor_data_des(data):
    """删去说明"""
    if isinstance(data, dict):
        tmp = {}
        for key, value in data.items():
            if key != "description":
                tmp[key] = censor_data_des(value)
        return tmp
    elif isinstance(data, list):
        tmp = []
        for item in data:
            tmp.append(censor_data_des(item))
        return tmp
    return data


def write_data(x, file_name, censor_des=False):
    """写入数据"""
    data = sort_data(x)
    if censor_des:
        data = censor_data_des(data)
    with open(file_name, "w", encoding="utf-8") as f:
        f.write(json.dumps(data, ensure_ascii=False, indent=4))


def list_to_dict(l):
    """列表转字典"""
    if isinstance(l, str):
        return l
    elif isinstance(l, dict) and "id" in l:
        tmp = deepcopy(l)
        del tmp["id"]
        if len(tmp) == 1 and "value" in tmp:
            return tmp["value"]
        else:
            return tmp
    elif isinstance(l, dict):
        return {k: list_to_dict(v) for k, v in l.items()}
    elif isinstance(l, list) and isinstance(l[0], str):
        return l
    elif isinstance(l, list) and isinstance(l[0], dict):
        res = {}
        for i in l:
            t = deepcopy(i)
            del t["id"]
            if len(t) == 1 and "value" in t:
                res[i["id"]] = t["value"]
            else:
                res[i["id"]] = t
        return res
    else:
        return l


def export_data(x, file_name):
    """导出数据"""
    data = censor_data_des(x)
    data = sort_data(data)
    res = {}
    for k, v in data.items():
        if k == "name_list":
            res["chap_map"] = list_to_dict(v["chapter_names"])
            res["end_map"] = list_to_dict(v["end_names"])
        elif k == "func_list":
            res["func_list"] = list(list_to_dict(v).keys())
        else:
            res[k.replace("_list", "_map")] = list_to_dict(v)
    with open(file_name, "w", encoding="utf-8") as f:
        f.write(json.dumps(res, ensure_ascii=False, indent=4))
