# coding = utf-8

"""测试章节配置"""

from test_ek import TestEmeraldKnight


class TestChapter(TestEmeraldKnight):
    """章节配置测试"""

    def test_chapter(self):
        """测试第一章"""
        self._game.new_game()
        for k in self._logic.DEFAULT_PARAS.keys():
            self.assertEqual(0, self._game.get_para(k))
