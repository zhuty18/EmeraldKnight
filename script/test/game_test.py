# coding utf-8

"""翡翠骑士游戏 v2 测试用"""


import random
import sys
from copy import deepcopy

sys.path.append(".")
sys.path.append("./script")
sys.path.append("./script/game")

from script.game.emerald_knight import EmeraldKnight, Logic


class EmeraldKnightTest(EmeraldKnight):
    """测试用游戏"""

    def get_logic(self):
        """获取基础逻辑"""
        return Logic

    def get_kernel(self):
        """获取逻辑核"""
        return self._kernel

    def get_scene_id(self):
        """获取场景id"""
        return self._kernel.get_scene_id()

    def set_scene(self, scene_id):
        """设置场景id"""
        return self._kernel.to_scene(scene_id)

    def get_choices(self):
        """获取场景选项"""
        return self._kernel.get_choices()

    def get_paras(self):
        """获取参数表"""
        return deepcopy(self._kernel.get_paras())

    def get_para(self, para_name):
        """获取参数"""
        return self._kernel.get_para(para_name)

    def set_para(self, para_name, value):
        """设置参数值"""
        return self._kernel.set_para(para_name, value)

    def get_max_chapter(self):
        """获取最大章节数"""
        return Logic.CHAPTERS

    def get_chapter_max_scene(self, chapter):
        """获取章节场景数"""
        scene_ids = [
            x if Logic.get_scene_chapter(x) == chapter else None
            for x in Logic.SCENE_MAP.keys()
        ]
        scene_ids = set(scene_ids)
        scene_ids.remove(None)
        return len(scene_ids)

    def get_ends(self):
        """获取结局数"""
        return len(Logic.END_NAME_MAP)

    def random_scene(self):
        """随机场景"""
        chapters = [str(i + 1) for i in range(self.get_max_chapter())]
        ch = random.choice(chapters)
        sc_list = [
            x if Logic.get_scene_chapter(x) == ch else None
            for x in Logic.SCENE_MAP.keys()
        ]
        sc_list = set(sc_list)
        sc_list.remove(None)
        sc_list = list(sc_list)
        sc = random.choice(sc_list)
        self.set_scene(str(sc))

    def get_random_para(self):
        """获取随机参数名"""
        return str(random.choice(list(Logic.DEFAULT_PARAS.keys())))

    def get_random_code(self):
        """获取随机代码名"""
        return str(random.choice(list(Logic.DEFAULT_CODES.keys())))
