# coding = utf-8

"""参数处理器"""

import json
import os
import sys

sys.path.append(".")
sys.path.append("./script")
sys.path.append("./script/game")

from data_sorting import sort_data
from editor_setting import FILE_PARAS, PATH, PATH_DATA

from script.game.game_logic import Logic


class ParameterController:
    """参数处理器"""

    def __init__(self):
        self.load_paras()
        self._paras = {}
        self._function_paras = {}
        self._codes = {}
        self.load_paras()

    def load_paras(self):
        """加载参数设置"""
        if os.path.exists(os.path.join(PATH_DATA, FILE_PARAS)):
            with open(
                os.path.join(PATH_DATA, FILE_PARAS),
                "r",
                encoding="utf-8",
            ) as f:
                para = json.loads(f.read())
                self._paras = sort_data(para["para_list"])
                self._function_paras = sort_data(para["function_para_list"])
                self._codes = sort_data(para["code_list"])

    def save_paras(self):
        """保存参数设置"""
        if not os.path.exists(PATH):
            os.mkdir(PATH)
        if not os.path.exists(PATH_DATA):
            os.mkdir(PATH_DATA)
        with open(
            os.path.join(PATH_DATA, FILE_PARAS),
            "w",
            encoding="utf-8",
        ) as f:
            para = {
                "para_list": self._paras,
                "function_para_list": self._function_paras,
                "code_list": self._codes,
            }
            f.write(json.dumps(para, ensure_ascii=False))

    def import_paras(self):
        """导入参数设置"""
        if os.path.exists(os.path.join(Logic.PATH_DATA, Logic.FILE_PARAS)):
            with open(
                os.path.join(Logic.PATH_DATA, Logic.FILE_PARAS),
                "r",
                encoding="utf-8",
            ) as f:
                para = json.loads(f.read())
            for i in para["para_list"]:
                self.set_para(i["name"], i["id"], i["default_value"])
            for i in para["function_para_list"]:
                self._function_paras[i["id"]] = i["value"]
            for i in para["code_list"]:
                self._codes[i["id"]] = i["value"]

    def export_paras(self):
        """导出参数设置"""
        paras = {
            "para_list": self._paras,
            "function_para_list": self._function_paras,
            "code_list": "codes",
        }
        with open(
            Logic.res_path(Logic.PATH_DATA, Logic.FILE_PARAS),
            "w",
            encoding="utf-8",
        ) as f:
            f.write(json.dumps(paras, ensure_ascii=False))

    def set_para(self, para_id, para_name, para_default_value, description=""):
        """设置参数"""
        tmp = {
            "id": para_id.upper(),
            "name": para_name,
            "default_value": para_default_value,
        }
        if description:
            tmp["description"] = description
        if "description" not in tmp:
            tmp["description"] = ""
        self._paras[para_id] = sort_data(tmp)
        self._paras = sort_data(self._paras)
        self.save_paras()

    def delete_para(self, para_id):
        """删除参数"""
        self._paras.pop(para_id)

    def get_paras(self):
        """获取参数"""
        return self._paras

    def get_para_ids(self):
        """获取参数id"""
        return list(self._paras.keys())
