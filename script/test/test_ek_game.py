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
        self._game.get_choices()
        self._kernel.get_scene_text()

    def test_battle_scene(self):
        """测试决战场景"""
        self._game.set_scene(self._logic.FINAL_BATTLE)
        self._game.set_para("PEGASUS", 1)
        self.assertEqual(self._game.get_scene_id(), self._logic.FINAL_BATTLE)
        self._kernel.get_scene_text()
        self.assertEqual(len(self._game.get_choices()), 5)

    def test_plain_attack(self):
        """测试普通攻击"""
        self._game.set_scene(self._logic.FINAL_BATTLE)
        self._game.set_para("PEGASUS", 1)
        plain_attack = self._game.get_choices()[0]
        self.assertTrue("PLAIN_ATTACK" in plain_attack.get_id())
        self._game.choose(plain_attack)

    def test_flying_attack(self):
        """测试奇袭攻击"""
        self._game.set_scene(self._logic.FINAL_BATTLE)
        self._game.set_para("PEGASUS", 1)
        flying_attack = self._game.get_choices()[1]
        self.assertTrue("FLYING_ATTACK" in flying_attack.get_id())
        self._game.choose(flying_attack)

    def test_special_attack(self):
        """测试特殊攻击"""
        self._game.set_scene(self._logic.FINAL_BATTLE)
        self._game.set_para("PEGASUS", 1)
        special_attack = self._game.get_choices()[2]
        self.assertTrue("SPECIAL_ATTACK" in special_attack.get_id())
        self._game.choose(special_attack)

    def test_hero_heal(self):
        """测试治疗"""
        self._game.set_scene(self._logic.FINAL_BATTLE)
        self._game.set_para("PEGASUS", 1)
        heal = self._game.get_choices()[3]
        self.assertTrue("HEAL" in heal.get_id())
        self._game.choose(heal)
        heal = self._game.get_choices()[3]
        self.assertEqual(heal._move.get_used(), 1)

    def test_cheat(self):
        """测试开挂"""
        self._game.set_scene(self._logic.FINAL_BATTLE)
        self._game.set_para("PEGASUS", 1)
        cheat = self._game.get_choices()[4]
        self.assertTrue("CHEAT" in cheat.get_id())
        self._game.choose(cheat)
        self.assertTrue(self._kernel._scene.get_enemy().is_dead())

    def test_enemy_fight(self):
        """测试敌人战斗"""
        self._game.set_scene(self._logic.FINAL_BATTLE)
        self._kernel.get_scene_text()
        self._game.get_choices()[0].choose()
        self._kernel.get_scene_text()
        self._kernel.get_choices()

    def test_enemy_heal_1(self):
        """测试敌人治疗1"""
        self._game.set_scene(self._logic.FINAL_BATTLE)
        enemy = self._kernel._scene.get_enemy()
        enemy.hurt(300)
        enemy.take_act(self._kernel._scene.get_hero())
        self.assertGreater(enemy.get_life(), 200)

    def test_enemy_heal_2(self):
        """测试敌人治疗2"""
        self._game.set_scene(self._logic.FINAL_BATTLE)
        enemy = self._kernel._scene.get_enemy()
        enemy.hurt(300)
        enemy.take_act(self._kernel._scene.get_hero())
        enemy._life = 1
        enemy.take_act(self._kernel._scene.get_hero())
        self.assertGreater(enemy.get_life(), 1)

    def test_win(self):
        """测试胜利"""
        self._game.set_scene(self._logic.FINAL_BATTLE)
        self._game.get_choices()[0].choose()
        self._kernel._scene.get_enemy()._life = 0
        self._kernel.get_scene_text()
        self.assertTrue("end" in self._game.get_choices()[0]._target)

    def test_lose(self):
        """测试失败"""
        self._game.set_scene(self._logic.FINAL_BATTLE)
        self._game.get_choices()[0].choose()
        self._kernel._scene.get_hero()._life = 0
        self._kernel.get_scene_text()
        self.assertEqual(self._game.get_choices()[0].get_id(), "6-6-1")

    def test_end_1(self):
        """测试结局1"""
        self._game.new_game()
        self.assertTrue(self._game.choose_by_id("1-1-2"))
        self.assertEqual(self._game.get_scene_id(), "1-3")
        self.assertTrue(self._game.choose_by_id("1-3-2"))
        self.assertEqual(self._game.get_scene_id(), "1-7")
        self.assertTrue(self._game.choose_by_id("1-7-2"))
        self.assertEqual(self._game.get_scene_id(), "1-17")
        self.assertTrue(self._game.choose_by_id("1-17-1"))
        self.assertEqual(self._game.get_scene_id(), "end-1")
        self._kernel.get_scene_text()
        self._logic.get_chapter_name(self._game.get_scene_id())
        self.assertTrue(self._game.choose_by_id("end"))
        self.assertEqual(self._game.get_scene_id(), "game_over")
