# coding = utf-8

"""战斗角色"""

from random import random

from battle_basic import Character
from game_logic import Logic


class Hero(Character):
    """英雄类"""

    @staticmethod
    def get_hero(data):
        """获取英雄"""
        match data["id"]:
            case "HAL":
                return Hal(data)

    def get_moves(self):
        """获取选项"""
        return self._actions


class Hal(Hero):
    """主角类"""

    def __init__(self, data):
        super().__init__(data)
        self._attack = 100
        self._attack += Logic.get_kernel().get_para("BRUCE_LOVE") * 2
        self._attack += Logic.get_kernel().get_para("INTELLIGENCE") * 2
        self._attack += Logic.get_kernel().get_para("DRAGON_EGG") * 10
        self._speed = 100
        self._speed += Logic.get_kernel().get_para("KNOWLEDGE")
        self._speed += Logic.get_kernel().get_para("PEGASUS") * 20
        self._life_max = 100
        self._life_max += Logic.get_kernel().get_para("OLIVER_LOVE") * 10
        self._life_max += Logic.get_kernel().get_para("BARRY_LOVE") * 10

        self.set()


class Enemy(Character):
    """敌人类"""

    @staticmethod
    def get_enemy(data):
        """获取敌人"""
        match data["id"]:
            case "SINESTRO":
                return Sinestro(data)

    def take_act(self, target):
        chance = []
        for act in self._actions:
            if act.is_heal() and self.need_heal(act) and act.is_available():
                return act.execute()
            elif act.get_chance():
                chance.append((act.get_chance(), act))
        dice = sum([x[0] for x in chance]) * random()
        for c, a in chance:
            dice -= c
            if dice <= 0:
                return a.execute(target)
        return ""

    def need_heal(self, act):
        """需要治疗"""
        if act.get_first() and act.get_used() == 0:
            return self._life < act.get_first()
        elif act.get_condition():
            return self._life < act.get_condition()
        else:
            return False


class Sinestro(Enemy):
    """魔王类"""

    def __init__(self, data):
        super().__init__(data)
        self._attack = 100
        self._attack -= Logic.get_kernel().get_para("SINESTRO_LOVE") * 5
        self._speed = 100
        self._speed -= Logic.get_kernel().get_para("SINESTRO_TAME") * 2
        self._life_max = data["max_life"]
        self.set()


def get_hero(character_data, _):
    """获取主角实例"""
    if character_data["type"] == "HERO":
        return Hero.get_hero(character_data)
    return None


def get_enemy(character_data, _):
    """获取敌人实例"""
    if character_data["type"] == "ENEMY":
        return Enemy.get_enemy(character_data)
    return None


Character.add_get_functions(get_hero)
Character.add_get_functions(get_enemy)
