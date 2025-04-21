# coding = utf-8

"""测试脚本"""

import sys
import unittest

sys.path.append(".")
sys.path.append("./script")
sys.path.append("./script/game")

from script.game.emerald_knight import EmeraldKnight


class EmeraldKnightTest(unittest.TestCase):
    """Emerald Knight的单元测试基类"""

    @classmethod
    def setUpClass(cls):
        return super().setUpClass()

    @classmethod
    def get_game(cls):
        """获取游戏实例"""
        ek = EmeraldKnight()
        return ek



if __name__ == "__main__":
    suite = unittest.defaultTestLoader.discover("script/test", "test_ek*.py")
    runner = unittest.TextTestRunner()
    runner.run(suite)
