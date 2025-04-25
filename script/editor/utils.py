# coding = utf-8

"""通用工具"""

import json

from data_sorting import sort_data


def write_data(x, file_name):
    """写入数据"""
    with open(file_name, "w", encoding="utf-8") as f:
        f.write(json.dumps(sort_data(x), ensure_ascii=False, indent=4))
