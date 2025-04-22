# coding = utf-8

"""测试脚本"""

import sys
import unittest

sys.path.append(".")
sys.path.append("./script")
sys.path.append("./script/game")

from game_test import EmeraldKnightTest


class TestEmeraldKnight(unittest.TestCase):
    """Emerald Knight的单元测试基类"""

    @classmethod
    def setUpClass(cls):
        return super().setUpClass()

    def setUp(self):
        """设置测试环境"""
        self._game = EmeraldKnightTest()
        self._kernel = self._game.get_kernel()
        self._logic = self._game.get_logic()
        with open(
            self._logic.res_path(
                self._logic.PATH_SAVE, self._logic.FILE_DEFAULT_SAVE
            ),
            "w",
            encoding="utf8",
        ) as f:
            f.write("{}")


if __name__ == "__main__":
    suite = unittest.defaultTestLoader.discover("script/test", "test_ek*.py")
    runner = unittest.TextTestRunner()
    runner.run(suite)
