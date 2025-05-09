# coding = utf-8

"""游戏内核"""

import json
from random import random

from game_logic import Logic
from story_battle import Choice, Scene


class Kernel:
    """游戏逻辑核"""

    def __init__(self):
        """初始化游戏内核"""
        Logic(self)

        self._scene = None  # 当前场景
        self._paras = {}  # 参数存储
        self._fight = {}  # 战斗结果
        self.refresh_paras()

    def get_scene_id(self):
        """获取当前场景ID"""
        if not self._scene:
            return Logic.START_OVER
        return self._scene.get_id()

    def get_scene_text(self):
        """获取场景文本"""
        return self._scene.get_text()

    def get_choices(self):
        """获取选项"""
        return self._scene.get_options()

    def to_scene(self, scene_id):
        """改变场景"""
        self._scene = Scene.get_existence(scene_id)

    def get_para(self, para_name):
        """获取参数值"""
        return self._paras[Logic.DEFAULT_PARAS[para_name]["name"]]

    def get_paras(self):
        """获取参数表"""
        return self._paras

    def set_para(self, para_name, value):
        """设置参数值"""
        self._paras[Logic.DEFAULT_PARAS[para_name]["name"]] = value

    def refresh_paras(self):
        """刷新参数"""
        for k, v in Logic.DEFAULT_PARAS.items():
            if v["name"] not in self._paras:
                self.set_para(k, v["default_value"])

    def load_at(self, save_id):
        """加载存档"""
        self._fight = {}
        if save_id == 0:
            # 新游戏，读取默认参数
            self.to_scene(Logic.START_SCENE)
            for k, v in Logic.DEFAULT_PARAS.items():
                self.set_para(k, v["default_value"])
        else:
            save_file = Logic.read_file(Logic.PATH_SAVE, f"{save_id}.eks")
            self.to_scene(save_file["scene"])
            self._paras = save_file["paras"]
            self.refresh_paras()

    def save_at(self, save_id):
        """保存存档"""
        if self._scene.get_id() != Logic.FINAL_BATTLE:
            save_file = Logic.res_path(Logic.PATH_SAVE, f"{save_id}.eks")
            with open(save_file, "w", encoding="utf-8") as f:
                f.write(
                    json.dumps(
                        {"scene": self.get_scene_id(), "paras": self._paras}
                    )
                )

    def fight(self):
        """过场战斗"""
        hp = self.get_para("TEMPORARY")
        hp += 3 * self.get_para("INTELLIGENCE")
        hp += self.get_para("KNOWLEDGE")
        hp += 5 * self.get_para("BRUCE_LOVE")
        hp += 5 * self.get_para("SINESTRO_LOVE")
        hp += 5 * self.get_para("SINESTRO_TAME")
        hp += 20 * (1 if self.get_para("TEAMMATE") != 0 else 0)
        for _ in range(10):
            hp -= random() * 16
        return hp > 0

    def fight_result(self):
        """战斗结果"""
        if not self._scene.get_id() in self._fight:
            self._fight[self._scene.get_id()] = int(self.fight())
        return self._fight[self._scene.get_id()]

    def check_condition(self, check):
        """单个条件检测"""
        para_name = check["para"]
        check_act = check["check"]
        check_by = check["value"]

        if check_act == "CONDITION":
            return int(self.check_is(para_name)) == check_by
        check_para = None
        value = None
        if para_name in Logic.DEFAULT_FUNC_PARAS:
            match para_name:
                case "SCENE":
                    check_para = self.get_scene_id()
                case "FIGHT":
                    check_para = self.fight_result()
                case "CHOICE":
                    check_para = int(Choice.get_existence(check_by).show())
                    value = 1
        elif "end" in para_name:
            check_para = int(Logic.check_end(para_name))
        else:
            check_para = self.get_para(para_name)
        if not value:
            if isinstance(check_by, str) and "CODE" in check_by:
                value = Logic.DEFAULT_CODES[check_by]
            else:
                value = check_by

        match check_act:
            case "EQUAL":
                return check_para == value
            case "UNEQUAL":
                return check_para != value
            case "MORE":
                return check_para > value
            case "MORE_EQUAL":
                return check_para >= value
            case "LESS":
                return check_para < value
            case "LESS_EQUAL":
                return check_para <= value
            case "BINARY":
                return check_para >> (value - 1) & 1 == 1
            case "NON_BINARY":
                return check_para >> (value - 1) & 1 == 0

    def check_is(self, check):
        """条件检测"""
        check_op = check["op"]
        check_items = [self.check_condition(c) for c in check["condition"]]
        match check_op:
            case "AND":
                return all(check_items)
            case "OR":
                return any(check_items)

    def change_para(self, action):
        """改变参数"""
        para_name = action["para"]
        change_act = action["change"]
        change_by = action["value"]

        if change_act == "CONDITION":
            if self.check_is(para_name):
                for change in change_by:
                    self.change_para(change)
        else:
            if isinstance(change_by, str):
                value = Logic.DEFAULT_CODES[change_by]
            else:
                value = change_by
            match change_act:
                case "ADD":
                    self.set_para(para_name, self.get_para(para_name) + value)
                case "SET":
                    self.set_para(para_name, value)
