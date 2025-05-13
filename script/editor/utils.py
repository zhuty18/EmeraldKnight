# coding = utf-8

"""通用工具"""

import json

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
