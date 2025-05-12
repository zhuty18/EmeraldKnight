# coding = utf-8

"""测试章节配置"""

from test_ek import TestEmeraldKnight

from script.game.story_basic import StoryChoice, StoryScene


class TestConfig(TestEmeraldKnight):
    """测试配置完备性"""

    def test_chapter_name(self):
        """测试章节名称"""
        for i in range(self._game.get_max_chapter()):
            self._logic.get_scene_chapter(f"{i+1}-1")

    def test_scene_text(self):
        """测试场景文本量"""
        for key in self._logic.SCENE_TEXT_MAP.keys():
            self.assertTrue(
                key in self._logic.SCENE_MAP.keys()
                or key in self._logic.END_NAME_MAP.keys()
            )
        self.assertEqual(
            len(self._logic.SCENE_TEXT_MAP),
            len(self._logic.SCENE_MAP)
            + len(self._logic.END_NAME_MAP)
            - 2,  # 减去决战场景和game_over场景
        )

    def test_choice(self):
        """测试选择生成"""
        choice = StoryChoice(
            {
                "id": "test_choice",
                "target": "1-1",
                "text": "test_text",
                "show": {
                    "op": "AND",
                    "condition": [
                        {"check": "EQUAL", "para": "TEMPORARY", "value": 0}
                    ],
                },
                "choose": [{"change": "ADD", "para": "TEMPORARY", "value": 1}],
            }
        )
        self.assertEqual(choice.get_id(), "test_choice")
        self.assertEqual(choice.text(), "test_text")
        self.assertTrue(choice.show())
        choice.choose()
        self.assertEqual(self._game.get_para("TEMPORARY"), 1)
        self.assertFalse(choice.show())

    def test_scene(self):
        """测试场景生成"""
        scene = StoryScene(
            {
                "id": "test_scene",
                "options": ["1-1-1"],
                "require": {
                    "op": "AND",
                    "condition": [
                        {"check": "EQUAL", "para": "TEMPORARY", "value": 1}
                    ],
                    "match_options": ["1-1-2"],
                },
            }
        )
        self.assertEqual(scene.get_id(), "test_scene")
        self.assertEqual(scene.get_options()[0].get_id(), "1-1-1")
        self._game.set_para("TEMPORARY", 1)
        self.assertEqual(scene.get_options()[0].get_id(), "1-1-2")
