# coding = utf-8

"""通用工具"""

import json

from data_sorting import sort_data


def censor_data_des(data):
    """删去说明"""


def write_data(x, file_name, censor_des=False):
    """写入数据"""
    data = sort_data(x)
    if censor_des:
        data = censor_data_des(data)
    with open(file_name, "w", encoding="utf-8") as f:
        f.write(json.dumps(data, ensure_ascii=False, indent=4))
