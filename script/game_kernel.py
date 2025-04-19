# coding = utf-8

"""游戏内核"""

import json
import os


class Choice:
    """选项"""

    @staticmethod
    def get_by_id(choice_id):
        """通过ID获取选项"""
        return Choice(Kernel.CHOICE_MAP[choice_id])

    def __init__(self, data):
        self._data = data

    def get_id(self):
        """获取选项ID"""
        return self._data["id"]

    def text(self):
        """选项文本"""
        if not "text" in self._data:
            return Kernel.scene_name(self._data["target"])
        return self._data["text"]

    def show(self):
        """是否显示"""
        if not "show" in self._data:
            return True
        res = True if self._data["show"] == "AND" else False
        index = 0
        while True:
            index += 1
            if not f"show_action_{index}" in self._data:
                break
            check = Kernel.KERNEL.check_condition(
                self._data[f"show_para_{index}"],
                self._data[f"show_action_{index}"],
                self._data[f"show_value_{index}"],
            )
            match self._data["show"]:
                case "AND":
                    res &= check
                case "OR":
                    res |= check
        return res

    def chosen(self):
        """选择后"""
        index = 0
        while True:
            index += 1
            if not f"action_{index}" in self._data:
                break
            Kernel.KERNEL.change_para(
                self._data[f"change_para_{index}"],
                self._data[f"action_{index}"],
                self._data[f"change_value_{index}"],
            )
        Kernel.KERNEL.to_scene(self._data["target"])


class Scene:
    """场景"""

    @staticmethod
    def get_by_id(scene_id):
        """通过ID获取场景"""
        if "end" in scene_id:
            Kernel.open_end(scene_id)
            return Scene(
                {
                    "id": scene_id,
                    "options": Kernel.SCENE_MAP[Kernel.START_OVER]["options"],
                }
            )
        return Scene(Kernel.SCENE_MAP[scene_id])

    def __init__(self, data):
        self._data = data

    def get_id(self):
        """获取ID"""
        return self._data["id"]

    def get_text(self):
        """获取文本"""
        return Kernel.read_file("story", f"{self._data["id"]}.txt", False)

    def get_options(self):
        """获取选项"""
        res = []
        for c in [Choice.get_by_id(x) for x in self._data["options"]]:
            if c.show():
                res.append(c)
        return res


class Kernel:
    """游戏逻辑核"""

    VERSION = "2.0"
    DEBUG = True

    KERNEL = None  # 游戏内核实例

    PATH_GAME = "game"  # 游戏相关文件路径
    FILE_PARAS = "paras.json"  # 参数存储文件
    FILE_SCENES = "scenes.json"  # 场景存储文件
    FILE_CHOICES = "choices.json"  # 选项存储文件
    PATH_STORY = "story"  # 故事相关文件路径
    FILE_SCENE_NAMES = "menu.json"
    PATH_SAVE = "save"
    FILE_DEFAULT_SAVE = "0.eks"

    DEFAULT_PARAS = {}  # 参数表
    DEFAULT_CODES = {}  # 代码表
    DEFAULT_CONSTS = {}  # 常量表
    SCENE_MAP = {}  # 场景表
    CHOICE_MAP = {}  # 选项表
    SCENE_NAME_MAP = {}  # 场景名表

    START_SCENE = ""
    START_OVER = ""
    SCENE = ""

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
        return Kernel.SCENE_NAME_MAP[scene_id]

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
        for i in Kernel.read_file(Kernel.PATH_GAME, Kernel.FILE_SCENES):
            Kernel.SCENE_MAP[i["id"]] = i
        for i in Kernel.read_file(Kernel.PATH_GAME, Kernel.FILE_CHOICES):
            Kernel.CHOICE_MAP[i["id"]] = i
        for k, v in Kernel.read_file(
            Kernel.PATH_STORY, Kernel.FILE_SCENE_NAMES
        ).items():
            Kernel.SCENE_NAME_MAP[k] = v

        Kernel.START_SCENE = Kernel.DEFAULT_CONSTS["START_SCENE"]
        Kernel.START_OVER = Kernel.DEFAULT_CONSTS["START_OVER"]
        Kernel.SCENE = Kernel.DEFAULT_CONSTS["SCENE"]

        self._scene = None  # 当前场景
        self._paras = {}  # 参数存储

        Kernel.KERNEL = self

    def load_save(self, save_id):
        """加载存档"""
        if save_id == 0:
            # 新游戏，读取默认参数
            self.to_scene(Kernel.START_SCENE)
            for _, value in Kernel.DEFAULT_PARAS.items():
                self._paras[value["id"]] = value["default_value"]

    def change_para(self, para_name, change_act, change_by):
        """改变参数"""
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
        """条件检测"""
        if para_name == Kernel.SCENE:
            check_para = self.get_scene_id()
        else:
            para_id = Kernel.DEFAULT_PARAS[para_name]["id"]
            check_para = self._paras[para_id]
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

    def get_scene_id(self):
        """获取当前场景ID"""
        return self._scene.get_id()

    def get_scene_text(self):
        """获取场景文本"""
        return self._scene.get_text()

    def get_choices(self):
        """获取选项"""
        return self._scene.get_options()

    @staticmethod
    def open_end(end_id):
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

    def print_debug(self):
        """打印调试信息"""
        print(f"当前场景ID: {self.get_scene_id()}")
        print(f"当前变量: {self._paras}")
        print(f"当前选项: {[x.get_id() for x in self.get_choices()]}")
