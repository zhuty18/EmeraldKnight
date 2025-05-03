# coding = utf-8

"""战斗故事类"""

from battle_actions import Action
from battle_characters import Character
from game_logic import Logic
from story_basic import Choice, Scene


class BattleChoice(Choice):
    """决战选项"""

    def __init__(self, battle_scene, move: Action):
        self._battle_scene = battle_scene
        self._move = move

    def get_id(self):
        return self._move.get_id()

    def text(self):
        return self._move.get_name()

    def show(self):
        return self._move.is_available()

    def choose(self):
        self._battle_scene.get_hero().set_text(
            self._move.execute(self._battle_scene.get_enemy())
        )
        self._battle_scene.next_round()


class BattleScene(Scene):
    """决战场景"""

    def __init__(self, data):
        self._id = Logic.FINAL_BATTLE
        self._round = 0
        self._enemy = Character.get_existence(
            Logic.CHARACTER_MAP[Logic.BATTLE_STORY["ENEMY"]]
        )
        self._hero = Character.get_existence(
            Logic.CHARACTER_MAP[Logic.BATTLE_STORY["HERO"]]
        )

        self._options_lose = data["options_lose"]
        self._options_win = data["options_win"]

    def get_enemy(self):
        """获取敌人"""
        return self._enemy

    def get_hero(self):
        """获取主角"""
        return self._hero

    def get_battle_status(self):
        """获取战斗状态"""
        battle_text = (
            f"{self._enemy.get_name()}\n"
            + f"HP: {self._enemy.get_life()} / {self._enemy.get_life_max()}"
            + "\n\n"
        )
        s = f"HP: {self._hero.get_life()} / {self._hero.get_life_max()}"
        battle_text += (
            f"{" "*46}{self._hero.get_name()}\n"
            + f"{" "*(48-len(s))}{s}\n"
            + "\n\n"
        )
        return battle_text

    def get_text(self):
        if self._round == 0:
            return self.get_battle_status() + Logic.BATTLE_STORY["START"]
        message = self._hero.tack_act(None)
        if self._enemy.is_dead():
            return (
                self.get_battle_status() + message + Logic.BATTLE_STORY["WIN"]
            )
        message += "\n" + self._enemy.tack_act(self._hero)
        if self._hero.is_dead():
            return (
                self.get_battle_status() + message + Logic.BATTLE_STORY["LOSE"]
            )
        else:
            return self.get_battle_status() + message

    def get_options(self, options=None, choices=None):
        if self._enemy.is_dead():
            return super().get_options(options=self._options_win)
        elif self._hero.is_dead():
            return super().get_options(options=self._options_lose)
        else:
            return super().get_options(
                choices=[BattleChoice(self, x) for x in self._hero.get_moves()]
            )

    def next_round(self):
        """下一轮"""
        self._round += 1


def get_battle_scene(scene_id, _):
    """获取战斗场景"""
    if scene_id == Logic.FINAL_BATTLE:
        return BattleScene(Logic.SCENE_MAP[scene_id])
    return None


Scene.add_get_functions(get_battle_scene, 0)
