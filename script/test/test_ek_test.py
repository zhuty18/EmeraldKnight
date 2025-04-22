# coding = utf-8

"""内核测试"""

import os

from test_ek import TestEmeraldKnight


class TestTest(TestEmeraldKnight):
    """测试版游戏测试"""

    def test_get_chapters(self):
        """测试获取配置数据量"""
        file_list = os.listdir(self._logic.res_path(self._logic.PATH_CHAPTER))

        choice_list = []
        scene_list = []
        for file in file_list:
            if "choices" in file:
                choice_list.append(file)
            elif "scenes" in file:
                scene_list.append(file)
        self.assertEqual(len(choice_list), len(scene_list))
        self.assertEqual(len(scene_list), self._game.get_max_chapter())

        for file in scene_list:
            scenes = self._logic.read_file(self._logic.PATH_CHAPTER, file)
            self.assertEqual(
                len(scenes),
                self._game.get_chapter_max_scene(
                    self._logic.get_scene_chapter(scenes[0]["id"])
                ),
            )

    def test_set_scene_id(self):
        """测试章节位置设置"""
        chapters = [str(i + 1) for i in range(self._game.get_max_chapter())]
        chapters.append("end")
        for ch in chapters:
            sc_list = []
            if ch == "end":
                sc_list = list(self._logic.END_NAME_MAP.keys())
            else:
                sc_list = [
                    x if self._logic.get_scene_chapter(x) == ch else None
                    for x in self._logic.SCENE_MAP.keys()
                ]
                sc_list = set(sc_list)
                sc_list.remove(None)
                sc_list = list(sc_list)
            for sc in sc_list:
                self._game.set_scene(str(sc))
                self.assertEqual(sc, self._game.get_scene_id())

    def test_para_set(self):
        """测试参数设置"""
        self._game.random_scene()
        for k in self._logic.DEFAULT_PARAS.keys():
            self._game.set_para(k, 99)
            self.assertEqual(99, self._game.get_para(k))
