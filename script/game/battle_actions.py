# coding = utf-8

"""战斗动作"""

from random import random

from battle_basic import Action, Character
from game_logic import Logic


class Attack(Action):
    """攻击动作"""

    def __init__(self, data, owner):
        super().__init__(data, owner)
        self._strength = data["strength"]
        if "self_hurt" in data:
            self._self_hurt = data["self_hurt"]
        else:
            self._self_hurt = None

    def execute(self, target: Character):
        """执行攻击"""
        exe_text = self._text
        if self._self_hurt:
            self_hurt = int(
                random() * (self._self_hurt["max"] - self._self_hurt["min"])
                + self._self_hurt["min"]
            )
            self._owner.hurt(self_hurt)
            exe_text += self._self_hurt["text"].replace(
                Logic.BATTLE_STORY["BLANK"], str(self_hurt)
            )
        dodge = 50 + self._owner.get_speed() - target.get_speed()
        if random() * 500 < dodge:
            exe_text += Logic.BATTLE_STORY["DODGE"]
        else:
            damage = int(
                self._owner.get_attack()
                * (0.8 + 0.4 * random())
                * self._strength
            )
            target.hurt(damage)
            exe_text += Logic.BATTLE_STORY["HURT"].replace(
                Logic.BATTLE_STORY["BLANK"], str(damage)
            )
        return exe_text


class Heal(Action):
    """治疗动作"""

    def __init__(self, data, owner):
        super().__init__(data, owner)
        self._min = data["min"]
        self._max = data["max"]
        self._time = data["time"]
        self._used = 0

    def execute(self, _):
        """执行治疗"""
        self._used += 1
        heal = int(self._min + random() * (self._max - self._min))
        self._owner.heal(heal)
        exe_text = self._text + Logic.BATTLE_STORY["HEAL"].replace(
            Logic.BATTLE_STORY["BLANK"], str(heal)
        )
        return exe_text

    def is_available(self):
        return self._used < self._time

    def get_used(self):
        """获取使用次数"""
        return self._used

    def is_heal(self):
        return True


class Cheat(Action):
    """作弊动作"""

    def execute(self, target):
        """作弊"""
        target.hurt(target.get_life())
        return self._text


def get_actions(data, owner):
    """获取动作"""
    match data["type"]:
        case "ATTACK":
            return Attack(data, owner)
        case "HEAL":
            return Heal(data, owner)
        case "CHEAT":
            return Cheat(data, owner)


Action.add_get_functions(get_actions)
