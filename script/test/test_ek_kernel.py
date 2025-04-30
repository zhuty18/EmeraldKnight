# coding = utf-8

"""内核测试"""


import random

from test_ek import TestEmeraldKnight


class TestKernel(TestEmeraldKnight):
    """逻辑核功能测试"""

    def test_save_game(self):
        """测试存读档场景"""
        self._game.random_scene()
        while (
            self._logic.get_scene_chapter(self._game.get_scene_id()) == "6"
            or self._logic.get_scene_chapter(self._game.get_scene_id()) == "end"
        ):
            self._game.random_scene()
        self._game.set_para(self._game.get_random_para(), 99)
        self._game.set_para(self._game.get_random_para(), 99)
        self._game.set_para(self._game.get_random_para(), 99)
        paras = self._game.get_paras()
        scene_id = self._game.get_scene_id()
        self._game.save_at(99)
        self._game.set_para(self._game.get_random_para(), 101)
        self._game.set_para(self._game.get_random_para(), 101)
        self._game.set_para(self._game.get_random_para(), 101)
        self._game.load_at(99)
        self.assertEqual(self._game.get_scene_id(), scene_id)
        self.assertEqual(self._game.get_paras(), paras)

    def test_change_para(self):
        """测试配置改变参数值"""
        k = self._game.get_random_para()
        self._kernel.change_para({"change": "SET", "para": k, "value": 99})
        self.assertEqual(99, self._game.get_para(k))
        self._kernel.change_para({"change": "ADD", "para": k, "value": 99})
        self.assertEqual(198, self._game.get_para(k))

    def test_condition_check(self):
        """测试配置条件检测"""
        k = self._game.get_random_para()
        self._game.set_para(k, 99)
        self.assertTrue(
            self._kernel.check_condition(
                {"check": "EQUAL", "para": k, "value": 99}
            )
        )
        self.assertFalse(
            self._kernel.check_condition(
                {"check": "UNEQUAL", "para": k, "value": 99}
            )
        )
        self.assertFalse(
            self._kernel.check_condition(
                {"check": "MORE", "para": k, "value": 99}
            )
        )
        self.assertTrue(
            self._kernel.check_condition(
                {"check": "MORE_EQUAL", "para": k, "value": 99}
            )
        )
        self.assertFalse(
            self._kernel.check_condition(
                {"check": "LESS", "para": k, "value": 99}
            )
        )
        self.assertTrue(
            self._kernel.check_condition(
                {"check": "LESS_EQUAL", "para": k, "value": 99}
            )
        )

        self._game.set_para(k, 3)
        self.assertTrue(
            self._kernel.check_condition(
                {"check": "BINARY", "para": k, "value": 1}
            )
        )
        self.assertFalse(
            self._kernel.check_condition(
                {"check": "NON_BINARY", "para": k, "value": 1}
            )
        )
        self.assertTrue(
            self._kernel.check_condition(
                {"check": "BINARY", "para": k, "value": 2}
            )
        )
        self.assertFalse(
            self._kernel.check_condition(
                {"check": "NON_BINARY", "para": k, "value": 1}
            )
        )
        self.assertFalse(
            self._kernel.check_condition(
                {"check": "BINARY", "para": k, "value": 3}
            )
        )
        self.assertTrue(
            self._kernel.check_condition(
                {"check": "NON_BINARY", "para": k, "value": 3}
            )
        )

    def test_condition_end(self):
        """测试结局条件检测"""
        self.assertFalse(
            self._kernel.check_condition(
                {"check": "UNEQUAL", "para": "end-99", "value": 0}
            )
        )
        self._logic.mark_end("end-99")
        self.assertTrue(
            self._kernel.check_condition(
                {"check": "EQUAL", "para": "end-99", "value": 1}
            )
        )

    def test_condition_change(self):
        """测试配置：条件改变"""
        k = self._game.get_random_para()
        self._game.set_para(k, 99)
        self._kernel.change_para(
            {
                "change": "CONDITION",
                "para": {
                    "op": "AND",
                    "condition": [{"check": "EQUAL", "para": k, "value": 99}],
                },
                "value": [{"change": "ADD", "para": k, "value": 2}],
            }
        )
        self.assertEqual(101, self._game.get_para(k))
        self._kernel.change_para(
            {
                "change": "CONDITION",
                "para": {
                    "op": "AND",
                    "condition": [{"check": "EQUAL", "para": k, "value": 99}],
                },
                "value": [{"change": "ADD", "para": k, "value": 2}],
            }
        )
        self.assertEqual(101, self._game.get_para(k))

    def test_check_set(self):
        """测试配置：系列条件"""
        i = self._game.get_random_para()
        j = self._game.get_random_para()
        while j == i:
            j = self._game.get_random_para()
        self._game.set_para(i, 99)
        self._game.set_para(j, -99)
        self.assertTrue(
            self._kernel.check_is(
                {
                    "op": "AND",
                    "condition": [{"check": "EQUAL", "para": i, "value": 99}],
                }
            )
        )
        self.assertFalse(
            self._kernel.check_is(
                {
                    "op": "AND",
                    "condition": [
                        {"check": "EQUAL", "para": i, "value": 99},
                        {"check": "EQUAL", "para": j, "value": 99},
                    ],
                }
            )
        )
        self.assertTrue(
            self._kernel.check_is(
                {
                    "op": "OR",
                    "condition": [
                        {"check": "EQUAL", "para": i, "value": 99},
                        {"check": "EQUAL", "para": j, "value": 99},
                    ],
                }
            )
        )

    def test_value_code(self):
        """测试代码值"""
        c = self._game.get_random_code()
        k = self._game.get_random_para()
        self._kernel.change_para({"change": "SET", "para": k, "value": c})
        self.assertEqual(self._logic.DEFAULT_CODES[c], self._game.get_para(k))
        self.assertTrue(
            self._kernel.check_condition(
                {"check": "EQUAL", "para": k, "value": c}
            )
        )

    def test_fight_win(self):
        """测试过场战斗"""
        self._game.random_scene()
        self._game.set_para("TEMPORARY", 10000)
        self.assertEqual(1, self._kernel.fight_result())
        self.assertTrue(
            self._kernel.check_condition(
                {"check": "EQUAL", "para": "FIGHT", "value": 1}
            )
        )

    def test_fight_fail(self):
        """测试过场战斗"""
        self._game.random_scene()
        self._game.set_para("TEMPORARY", 0)
        self.assertEqual(0, self._kernel.fight_result())
        self.assertFalse(
            self._kernel.check_condition(
                {"check": "EQUAL", "para": "FIGHT", "value": 1}
            )
        )

    def test_check_scene(self):
        """测试章节检测"""
        self._game.random_scene()
        self.assertTrue(
            self._kernel.check_condition(
                {
                    "check": "EQUAL",
                    "para": "SCENE",
                    "value": self._game.get_scene_id(),
                }
            )
        )
