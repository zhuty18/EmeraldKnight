# coding = utf-8

"""测试脚本"""

import sys
import unittest

sys.path.append(".")
sys.path.append("./script")
sys.path.append("./script/game")

import os

from game_test import EmeraldKnightTest


class TestEmeraldKnight(unittest.TestCase):
    """Emerald Knight的单元测试基类"""

    @classmethod
    def setUpClass(cls):
        logic = EmeraldKnightTest().get_logic()
        with open(
            logic.res_path(logic.PATH_SAVE, logic.FILE_DEFAULT_SAVE),
            "w",
            encoding="utf8",
        ) as f:
            f.write("{}")
        saves = os.listdir(logic.res_path(logic.PATH_SAVE))
        for save in saves:
            save_id = save.split(".")[0]
            try:
                if int(save_id) > 30:
                    raise ValueError
            except ValueError:
                os.remove(os.path.join(logic.res_path(logic.PATH_SAVE), save))

    @classmethod
    def tearDownClass(cls):
        cls.setUpClass()

    def setUp(self):
        """设置测试环境"""
        self._game = EmeraldKnightTest()
        self._game.run()
        self._kernel = self._game.get_kernel()
        self._logic = self._game.get_logic()


# if __name__ == "__main__":
#     suite = unittest.defaultTestLoader.discover("script/test", "test_ek*.py")
#     runner = unittest.TextTestRunner()
#     runner.run(suite)
