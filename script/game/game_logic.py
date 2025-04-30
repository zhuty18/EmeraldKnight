# coding = utf-8

"""游戏整体逻辑"""

import json
import os
import time

from version import CHAPTERS, DEBUG, GAME_NAME, VERSION


class Logic:
    """逻辑类"""

    GAME_NAME = GAME_NAME  # 游戏名
    VERSION = VERSION  # 游戏版本
    DEBUG = DEBUG  # 是否为调试模式
    CHAPTERS = CHAPTERS  # 当前章节数

    PATH_DATA = "data"  # 游戏相关文件路径
    FILE_CONSTS = "consts.json"  # 常量配置文件
    FILE_PARAS = "paras.json"  # 参数配置文件
    FILE_NAMES = "names.json"  # 名称配置文件
    FILE_CHARACTERS = "characters.json"  # 角色配置文件

    PATH_CHAPTER = "data/chapter"  # 章节相关文件路径
    FILE_SCENES = "scenes_ch{ch}.json"  # 场景配置文件
    FILE_CHOICES = "choices_ch{ch}.json"  # 选项配置文件

    PATH_STORY = "data/story"  # 故事相关文件路径
    FILE_STORYS = "story_ch{ch}.json"

    PATH_SAVE = "save"  # 存档相关文件路径
    FILE_DEFAULT_SAVE = "0.eks"  # 初始存档文件

    DEFAULT_PARAS = {}  # 参数表
    DEFAULT_FUNC_PARAS = {}  # 功能参数表
    DEFAULT_CODES = {}  # 代码表
    DEFAULT_CONSTS = {}  # 常量表
    CHOICE_MAP = {}  # 选项表
    SCENE_MAP = {}  # 场景表
    SCENE_TEXT_MAP = {}  # 场景内容表
    END_NAME_MAP = {}  # 结局名表
    CHAPTER_NAME_MAP = {}  # 章名表
    CHARACTER_MAP = {}  # 角色表

    START_SCENE = ""  # 起始场景
    START_OVER = ""  # 重开场景
    FINAL_BATTLE = ""  # 战斗场景
    EMPTY_SAVE = ""  # 空存档字符串
    STORY_END = ""  # 故事结尾补充字符串
    BATTLE_STORY = {}  # 决战相关字符串

    @staticmethod
    def load_data(data_all, storage, full_data=True):
        """用id-全数据将数据加载进表"""
        for i in data_all:
            storage[i["id"]] = i if full_data else i["value"]

    def __init__(self, kernel):
        Logic._kernel = kernel

        Logic.load_data(
            Logic.read_file(Logic.PATH_DATA, Logic.FILE_CONSTS),
            Logic.DEFAULT_CONSTS,
            False,
        )

        para_data = Logic.read_file(Logic.PATH_DATA, Logic.FILE_PARAS)
        Logic.load_data(para_data["para_list"], Logic.DEFAULT_PARAS)
        Logic.load_data(para_data["code_list"], Logic.DEFAULT_CODES, False)
        Logic.load_data(para_data["func_list"], Logic.DEFAULT_FUNC_PARAS, False)

        end_scene = Logic.DEFAULT_CONSTS["END_SCENE"]
        Logic.SCENE_MAP[end_scene["id"]] = end_scene
        end_choice = Logic.DEFAULT_CONSTS["END_CHOICE"]
        Logic.CHOICE_MAP[end_choice["id"]] = end_choice
        for ch in range(Logic.CHAPTERS):
            Logic.load_data(
                Logic.read_file(
                    Logic.PATH_CHAPTER,
                    Logic.FILE_SCENES.replace("{ch}", str(ch + 1)),
                ),
                Logic.SCENE_MAP,
            )
            Logic.load_data(
                Logic.read_file(
                    Logic.PATH_CHAPTER,
                    Logic.FILE_CHOICES.replace("{ch}", str(ch + 1)),
                ),
                Logic.CHOICE_MAP,
            )
            Logic.load_data(
                Logic.read_file(
                    Logic.PATH_STORY,
                    Logic.FILE_STORYS.replace("{ch}", str(ch + 1)),
                ),
                Logic.SCENE_TEXT_MAP,
                False,
            )

        name_data = Logic.read_file(Logic.PATH_DATA, Logic.FILE_NAMES)
        Logic.load_data(name_data["end_names"], Logic.END_NAME_MAP, False)
        Logic.load_data(
            name_data["chapter_names"], Logic.CHAPTER_NAME_MAP, False
        )

        Logic.load_data(
            Logic.read_file(Logic.PATH_DATA, Logic.FILE_CHARACTERS),
            Logic.CHARACTER_MAP,
        )

        Logic.START_SCENE = Logic.DEFAULT_CONSTS["START_SCENE"]
        Logic.START_OVER = Logic.DEFAULT_CONSTS["START_OVER"]
        Logic.FINAL_BATTLE = Logic.DEFAULT_CONSTS["FINAL_BATTLE"]
        Logic.EMPTY_SAVE = Logic.DEFAULT_CONSTS["EMPTY_SAVE"]
        Logic.STORY_END = Logic.DEFAULT_CONSTS["STORY_END"]
        Logic.BATTLE_STORY = Logic.DEFAULT_CONSTS["BATTLE_STORY"]

        if not os.path.exists(Logic.res_path(Logic.PATH_SAVE)):
            os.mkdir(Logic.res_path(Logic.PATH_SAVE))
        if not os.path.exists(
            Logic.res_path(Logic.PATH_SAVE, Logic.FILE_DEFAULT_SAVE)
        ):
            with open(
                Logic.res_path(Logic.PATH_SAVE, Logic.FILE_DEFAULT_SAVE),
                "w",
                encoding="utf8",
            ) as f:
                f.write("{}")

    @staticmethod
    def res_path(file_dir, file_name=None):
        """相关文件路径"""
        if Logic.DEBUG:
            root = os.path.abspath(".")
        else:
            root = os.getenv("APPDATA")
            root = os.path.join(root, "EmeraldKnight")

        if file_name:
            return os.path.join(root, file_dir, file_name)
        return os.path.join(root, file_dir)

    @staticmethod
    def read_file(file_dir, file_name):
        """读取文件"""
        with open(
            Logic.res_path(file_dir, file_name), "r", encoding="utf8"
        ) as f:
            return json.loads(f.read())

    @staticmethod
    def get_scene_chapter(scene_id):
        """获取场景章节"""
        return scene_id.split("-")[0]

    @staticmethod
    def get_scene_text(scene_id):
        """读取场景文本"""
        return Logic.SCENE_TEXT_MAP[scene_id]

    @staticmethod
    def get_scene_name(scene_id):
        """获取场景名"""
        return Logic.SCENE_MAP[scene_id]["name"]

    @staticmethod
    def get_chapter_name(scene_id):
        """获取所在章节名"""
        if Logic.get_scene_chapter(scene_id) == "end":
            return Logic.CHAPTER_NAME_MAP["end"] + Logic.END_NAME_MAP[scene_id]
        return Logic.CHAPTER_NAME_MAP[f"ch{Logic.get_scene_chapter(scene_id)}"]

    @staticmethod
    def mark_end(end_id):
        """解锁结局"""
        static_save = Logic.read_file(Logic.PATH_SAVE, Logic.FILE_DEFAULT_SAVE)
        static_save[end_id] = 1
        with open(
            Logic.res_path(Logic.PATH_SAVE, Logic.FILE_DEFAULT_SAVE),
            "w",
            encoding="utf8",
        ) as f:
            f.write(json.dumps(static_save, ensure_ascii=False))

    @staticmethod
    def check_end(end_id):
        """检查结局是否解锁"""
        static_save = Logic.read_file(Logic.PATH_SAVE, Logic.FILE_DEFAULT_SAVE)
        return static_save.get(end_id, 0) == 1

    @staticmethod
    def get_end_name(end_id):
        """获取结局名称"""
        return Logic.END_NAME_MAP[end_id]

    @staticmethod
    def get_save_info(save_id):
        """获取存档信息"""
        save_path = Logic.res_path(Logic.PATH_SAVE, f"{save_id}.eks")
        if os.path.exists(save_path):
            save = Logic.read_file(Logic.PATH_SAVE, f"{save_id}.eks")
            save_pos = Logic.get_chapter_name(save["scene"])
            save_time = os.path.getmtime(
                Logic.res_path(Logic.PATH_SAVE, f"{save_id}.eks")
            )
            save_time = time.strftime("%m.%d\t%H:%M", time.localtime(save_time))
            if Logic.DEBUG:
                return f"{save["scene"]}{save_pos}\n{save_time}"
            else:
                return f"{save_pos}\n{save_time}"
        else:
            return Logic.EMPTY_SAVE

    @staticmethod
    def get_kernel():
        """获取逻辑核"""
        return Logic._kernel
