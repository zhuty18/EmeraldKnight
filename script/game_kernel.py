# coding = utf-8

"""游戏内核"""

import json
import os
import time
from random import random

from battle_scene import BattleScene


class Choice:
    """选项"""

    @staticmethod
    def get_by_id(choice_id):
        """通过ID获取选项"""
        return Choice(Kernel.CHOICE_MAP[choice_id])

    def __init__(self, data):
        self._data = data

    def text(self):
        """选项文本"""
        if not "text" in self._data:
            return Kernel.scene_name(self._data["target"])
        return self._data["text"]

    def show(self):
        """是否显示"""
        if not "show" in self._data:
            return True
        return Kernel.KERNEL.check_is(
            self._data["show"]["op"],
            self._data["show"]["condition"],
        )

    def chosen(self):
        """选择后"""
        if "choose" in self._data:
            for action in self._data["choose"]:
                Kernel.KERNEL.change_para(
                    action["para"],
                    action["change"],
                    action["value"],
                )
        Kernel.KERNEL.to_scene(self._data["target"])


class Scene:
    """场景"""

    @staticmethod
    def get_by_id(scene_id):
        """通过ID获取场景"""
        if "end" in scene_id:
            Kernel.mark_end(scene_id)
            return Scene(
                {
                    "id": scene_id,
                    "options": Kernel.SCENE_MAP[Kernel.START_OVER]["options"],
                }
            )
        elif scene_id == Kernel.FINAL_BATTLE:
            return BattleScene()
        return Scene(Kernel.SCENE_MAP[scene_id])

    def __init__(self, data):
        self._data = data

    def get_id(self):
        """获取ID"""
        return self._data["id"]

    def get_text(self):
        """获取文本"""
        s_id = (
            self._data["scene"] if "scene" in self._data else self._data["id"]
        )
        scene_text = Kernel.read_file("story", f"{s_id}.txt", False)
        if "end" in self._data["id"]:
            scene_text += Kernel.STORY_END + Kernel.get_end_name(
                self._data["id"]
            )
        scene_text = "    " + scene_text
        scene_text = scene_text.replace("\n", "\n    ")
        return scene_text

    def get_options(self):
        """获取选项"""
        options = self._data["options"]
        if "require" in self._data:
            if Kernel.KERNEL.check_is(
                self._data["require"]["op"],
                self._data["require"]["condition"],
            ):
                options = self._data["require"]["match_options"]
        res = []
        for c in [Choice.get_by_id(x) for x in options]:
            if c.show():
                res.append(c)
        return res


class Kernel:
    """游戏逻辑核"""

    VERSION = "2.0"  # 游戏版本
    DEBUG = True  # 是否为调试模式

    KERNEL = None  # 游戏内核实例

    CHAPTER = 6  # 章节数
    PATH_GAME = "game"  # 游戏相关文件路径
    FILE_PARAS = "paras.json"  # 参数存储文件
    FILE_SCENES = "scenes_ch{ch}.json"  # 场景存储文件
    FILE_CHOICES = "choices_ch{ch}.json"  # 选项存储文件
    FILE_NAMES = "names.json"  # 名称存储文件
    PATH_STORY = "story"  # 故事相关文件路径
    PATH_SAVE = "save"  # 存档相关文件路径
    FILE_DEFAULT_SAVE = "0.eks"  # 初始存档文件

    DEFAULT_PARAS = {}  # 参数表
    DEFAULT_CODES = {}  # 代码表
    DEFAULT_CONSTS = {}  # 常量表
    SCENE_MAP = {}  # 场景表
    CHOICE_MAP = {}  # 选项表
    END_NAME_MAP = {}  # 结局名表
    CHAPTER_NAME_MAP = {}  # 章名表
    CHARACTER_MAP = {}  # 角色表

    START_SCENE = ""  # 起始场景
    START_OVER = ""  # 重开场景
    FINAL_BATTLE = ""  # 重开场景
    SCENE = ""  # 场景变量名
    END = ""  # 结局变量名
    FIGHT = ""  # 结局变量名
    EMPTY_SAVE = ""  # 空存档字符串
    STORY_END = ""  # 故事结尾补充字符串
    BATTLE_STORY = {}  # 决战相关字符串

    @staticmethod
    def res_path(file_dir, file_name=None):
        """相关文件路径"""
        if Kernel.DEBUG:
            root = os.path.abspath(".")
        else:
            root = os.getenv("APPDATA")
            root = os.path.join(root, "EmeraldKnight")

        if file_name:
            return os.path.join(root, file_dir, file_name)
        else:
            return os.path.join(root, file_dir)

    @staticmethod
    def read_file(file_dir, file_name, load_json=True):
        """读取文件"""
        with open(
            Kernel.res_path(file_dir, file_name), "r", encoding="utf8"
        ) as f:
            if load_json:
                return json.loads(f.read())
            else:
                return f.read()

    @staticmethod
    def scene_name(scene_id):
        """获取场景名"""
        return Kernel.SCENE_MAP[scene_id]["name"]

    @staticmethod
    def mark_end(end_id):
        """解锁结局"""
        static_save = Kernel.read_file(
            Kernel.PATH_SAVE, Kernel.FILE_DEFAULT_SAVE
        )
        static_save[end_id] = 1
        with open(
            Kernel.res_path(Kernel.PATH_SAVE, Kernel.FILE_DEFAULT_SAVE),
            "w",
            encoding="utf8",
        ) as f:
            f.write(json.dumps(static_save, ensure_ascii=False))

    @staticmethod
    def check_end(end_id):
        """检查结局是否解锁"""
        static_save = Kernel.read_file(
            Kernel.PATH_SAVE, Kernel.FILE_DEFAULT_SAVE
        )
        return static_save.get(end_id, 0) == 1

    @staticmethod
    def get_end_name(end_id):
        """获取结局名称"""
        return Kernel.END_NAME_MAP[end_id]

    def __init__(self):
        """初始化游戏内核"""

        for i in Kernel.read_file(Kernel.PATH_GAME, Kernel.FILE_PARAS)[
            "const_list"
        ]:
            Kernel.DEFAULT_CONSTS[i["name"]] = i["value"]
        for i in Kernel.read_file(Kernel.PATH_GAME, Kernel.FILE_PARAS)[
            "para_list"
        ]:
            Kernel.DEFAULT_PARAS[i["name"]] = i
        for i in Kernel.read_file(Kernel.PATH_GAME, Kernel.FILE_PARAS)[
            "code_list"
        ]:
            Kernel.DEFAULT_CODES[i["name"]] = i["value"]
        for i in Kernel.read_file(Kernel.PATH_GAME, Kernel.FILE_PARAS)[
            "character_list"
        ].items():
            Kernel.CHARACTER_MAP[i["id"]] = i

        end_scene = Kernel.DEFAULT_CONSTS["END_SCENE"]
        Kernel.SCENE_MAP[end_scene["id"]] = end_scene
        end_choice = Kernel.DEFAULT_CONSTS["END_CHOICE"]
        Kernel.CHOICE_MAP[end_choice["id"]] = end_choice
        for ch in range(Kernel.CHAPTER):
            for i in Kernel.read_file(
                Kernel.PATH_GAME,
                Kernel.FILE_SCENES.replace("{ch}", str(ch + 1)),
            ):
                Kernel.SCENE_MAP[i["id"]] = i
            for i in Kernel.read_file(
                Kernel.PATH_GAME,
                Kernel.FILE_CHOICES.replace("{ch}", str(ch + 1)),
            ):
                Kernel.CHOICE_MAP[i["id"]] = i

        for k, v in Kernel.read_file(Kernel.PATH_GAME, Kernel.FILE_NAMES)[
            "end_names"
        ].items():
            Kernel.END_NAME_MAP[k] = v
        for k, v in Kernel.read_file(Kernel.PATH_GAME, Kernel.FILE_NAMES)[
            "chapter_names"
        ].items():
            Kernel.CHAPTER_NAME_MAP[k] = v

        Kernel.START_SCENE = Kernel.DEFAULT_CONSTS["START_SCENE"]
        Kernel.START_OVER = Kernel.DEFAULT_CONSTS["START_OVER"]
        Kernel.FINAL_BATTLE = Kernel.DEFAULT_CONSTS["FINAL_BATTLE"]
        Kernel.SCENE = Kernel.DEFAULT_CONSTS["SCENE"]
        Kernel.END = Kernel.DEFAULT_CONSTS["END"]
        Kernel.FIGHT = Kernel.DEFAULT_CONSTS["FIGHT"]
        Kernel.EMPTY_SAVE = Kernel.DEFAULT_CONSTS["EMPTY_SAVE"]
        Kernel.STORY_END = Kernel.DEFAULT_CONSTS["STORY_END"]
        Kernel.BATTLE_STORY = Kernel.DEFAULT_CONSTS["BATTLE_STORY"]

        self._scene = None  # 当前场景
        self._paras = {}  # 参数存储
        self._fight = {}  # 战斗结果

        Kernel.KERNEL = self

    def get_save_info(self, save_id):
        """获取存档信息"""
        save_path = Kernel.res_path(Kernel.PATH_SAVE, f"{save_id}.eks")
        if os.path.exists(save_path):
            save = Kernel.read_file(Kernel.PATH_SAVE, f"{save_id}.eks")
            if save["scene"].split("-")[1] == "end":
                save_pos = (
                    Kernel.CHAPTER_NAME_MAP["end"]
                    + Kernel.END_NAME_MAP[save["scene"]]
                )
            else:
                save_pos = Kernel.CHAPTER_NAME_MAP[
                    f"ch{save["scene"].split("-")[0]}"
                ]
            save_time = os.path.getmtime(
                Kernel.res_path(Kernel.PATH_SAVE, f"{save_id}.eks")
            )
            save_time = time.strftime("%m.%d\t%H:%M", time.localtime(save_time))
            if Kernel.DEBUG:
                return f"{save["scene"]}{save_pos}\n{save_time}"
            else:
                return f"{save_pos}\n{save_time}"
        else:
            return Kernel.EMPTY_SAVE

    def load_at(self, save_id):
        """加载存档"""
        if save_id == 0:
            # 新游戏，读取默认参数
            self.to_scene(Kernel.START_SCENE)
            for _, value in Kernel.DEFAULT_PARAS.items():
                self._paras[value["id"]] = value["default_value"]
        else:
            save_file = Kernel.read_file(Kernel.PATH_SAVE, f"{save_id}.eks")
            self._scene = Scene.get_by_id(save_file["scene"])
            self._paras = save_file["paras"]
            self.refresh_paras()

    def save_at(self, save_id):
        """保存存档"""
        save_file = Kernel.res_path(Kernel.PATH_SAVE, f"{save_id}.eks")
        with open(save_file, "w", encoding="utf-8") as f:
            f.write(
                json.dumps({"scene": self.get_scene_id(), "paras": self._paras})
            )

    def refresh_paras(self):
        """刷新参数"""
        for _, v in Kernel.DEFAULT_PARAS.items():
            if v["id"] not in self._paras:
                self._paras[v["id"]] = v["default_value"]
            if "pro" in self._paras:
                self._paras["pr1"] = self._paras["pro"] % 8
                self._paras["pr2"] = self._paras["pro"] >> 3
                self._paras.pop("pro")

    def get_para(self, para_name):
        """获取参数值"""
        return self._paras[Kernel.DEFAULT_PARAS[para_name]["id"]]

    def change_para(self, para_name, change_act, change_by):
        """改变参数"""
        if change_act == "CONDITION":
            if Kernel.KERNEL.check_condition(
                para_name["para"],
                para_name["check"],
                para_name["value"],
            ):
                for change in change_by:
                    Kernel.KERNEL.change_para(
                        change["para"],
                        change["change"],
                        change["value"],
                    )
        else:
            para_id = Kernel.DEFAULT_PARAS[para_name]["id"]
            if isinstance(change_by, str):
                value = Kernel.DEFAULT_CODES[change_by]
            else:
                value = change_by
            match change_act:
                case "ADD":
                    self._paras[para_id] += value
                case "SET":
                    self._paras[para_id] = value

    def to_scene(self, scene_id):
        """改变场景"""
        self._scene = Scene.get_by_id(scene_id)

    def check_condition(self, para_name, check_act, check_by):
        """单个条件检测"""
        if para_name == Kernel.SCENE:
            check_para = self.get_scene_id()
        elif para_name != Kernel.END:
            check_para = self.get_para(para_name)
        elif check_by == Kernel.FIGHT:
            check_para = self.fight_result()
        else:
            check_para = para_name
        if isinstance(check_by, str) and "CODE" in check_by:
            value = Kernel.DEFAULT_CODES[check_by]
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
                return Kernel.check_end(f"end-{value}")

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
            return Kernel.START_OVER
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
