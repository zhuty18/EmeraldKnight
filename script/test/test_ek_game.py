# coding = utf-8

"""引擎测试"""

from test_ek import TestEmeraldKnight


class TestEngine(TestEmeraldKnight):
    """引擎基础功能测试"""

    def test_no_scene(self):
        """测试无场景"""
        self.assertEqual(self._game.get_scene_id(), self._logic.START_OVER)

    def test_start_scene(self):
        """测试初始场景"""
        self._game.new_game()
        self.assertEqual(self._game.get_scene_id(), self._logic.START_SCENE)

    def test_battle_scene(self):
        """测试决战场景"""
        self._game.set_scene(self._logic.FINAL_BATTLE)
        self.assertEqual(self._game.get_scene_id(), self._logic.FINAL_BATTLE)
