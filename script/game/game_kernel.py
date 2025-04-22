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

    def load_at(self, save_id):
        """加载存档"""
        if save_id == 0:
            # 新游戏，读取默认参数
            self.to_scene(Logic.START_SCENE)
            for _, value in Logic.DEFAULT_PARAS.items():
                self._paras[value["id"]] = value["default_value"]
        else:
            save_file = Logic.read_file(Logic.PATH_SAVE, f"{save_id}.eks")
            self._scene = Scene.get_existence(save_file["scene"])
            self._paras = save_file["paras"]
            self.refresh_paras()

    def save_at(self, save_id):
        """保存存档"""
        if self._scene != Logic.FINAL_BATTLE:
            save_file = Logic.res_path(Logic.PATH_SAVE, f"{save_id}.eks")
            with open(save_file, "w", encoding="utf-8") as f:
                f.write(
                    json.dumps(
                        {"scene": self.get_scene_id(), "paras": self._paras}
                    )
                )

    def refresh_paras(self):
        """刷新参数"""
        for _, v in Logic.DEFAULT_PARAS.items():
            if v["id"] not in self._paras:
                self._paras[v["id"]] = v["default_value"]
            if "pro" in self._paras:
                self._paras["pr1"] = self._paras["pro"] % 8
                self._paras["pr2"] = self._paras["pro"] >> 3
                self._paras.pop("pro")

    def get_para(self, para_name):
        """获取参数值"""
        return self._paras[Logic.DEFAULT_PARAS[para_name]["id"]]

    def get_paras(self):
        """获取参数表"""
        return self._paras

    def set_para(self, para_name, value):
        """设置参数值"""
        self._paras[Logic.DEFAULT_PARAS[para_name]["id"]] = value

    def change_para(self, para_name, change_act, change_by):
        """改变参数"""
        if change_act == "CONDITION":
            if self.check_condition(
                para_name["para"],
                para_name["check"],
                para_name["value"],
            ):
                for change in change_by:
                    self.change_para(
                        change["para"],
                        change["change"],
                        change["value"],
                    )
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

    def to_scene(self, scene_id):
        """改变场景"""
        self._scene = Scene.get_existence(scene_id)

    def check_condition(self, para_name, check_act, check_by):
        """单个条件检测"""
        check_para = None
        value = None
        if para_name in Logic.DEFAULT_FUNCTION_PARAS:
            match Logic.DEFAULT_FUNCTION_PARAS[para_name]:
                case "SCENE":
                    check_para = self.get_scene_id()
                case "FIGHT":
                    check_para = self.fight_result()
                case "CHOICE":
                    check_para = int(Choice.get_existence(check_by).show())
                    value = 1
                case "END":
                    check_para = para_name
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
            case "CHECK_END":
                return Logic.check_end(f"end-{value}")

    def check_is(self, show_op, show_condition):
        """条件检测"""
        res = True if show_op == "AND" else False
        for condition in show_condition:
            check = self.check_condition(
                condition["para"],
                condition["check"],
                condition["value"],
            )
            match show_op:
                case "AND":
                    res &= check
                case "OR":
                    res |= check
        return res

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

    def print_debug(self):
        """打印调试信息"""
        print(f"当前场景ID: {self.get_scene_id()}")
        print(f"当前变量: {self._paras}")
        print(f"当前选项: {[x.get_id() for x in self.get_choices()]}")
