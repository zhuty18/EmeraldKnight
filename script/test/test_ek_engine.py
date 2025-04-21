# coding = utf-8

"""引擎测试"""

from test_ek import EmeraldKnightTest


class EKEngineTest(EmeraldKnightTest):
    """引擎基础功能测试"""

    def test_start_scene(self):
        """测试初始场景"""
        game = self.get_game()
        game.new_game()
        self.assertEqual(game.get_logic().START_SCENE, game.get_scene_id())
