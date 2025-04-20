# coding = utf-8

"""决斗相关代码"""

from random import random

from game_kernel import Choice, Kernel, Scene


class Character:
    """角色类"""

    @staticmethod
    def get_character(character_id):
        """根据角色ID获取角色实例"""
        character = Kernel.CHARACTER_MAP[character_id]
        if character["type"] == "ENEMY":
            return Enemy.get_enemy(character_id, character)
        else:
            return Hero.get_hero(character_id, character)

    def __init__(self, data):
        self._attack = None
        self._speed = None
        self._life_max = None
        self._life = None
        self._heal = 0
        self._name = data["name"]
        self._actions = []
        for act in data["actions"]:
            self._actions.append(Action.get_action(act, self))

    def get_name(self):
        """获取角色名称"""
        return self._name

    def get_attack(self):
        """获取攻击力"""
        return self._attack

    def get_speed(self):
        """获取速度"""
        return self._speed

    def get_life(self):
        """获取生命值"""
        return self._life

    def get_life_max(self):
        """获取最大生命值"""
        return self._life_max

    def get_heal(self):
        """获取治疗次数"""
        return self._heal

    def tack_act(self, target):
        """执行动作"""
        return ""

    def hurt(self, damage):
        """受到伤害"""
        self._life -= damage

    def heal(self, heal):
        """治疗"""
        self._life = min(self._life + heal, self._life_max)

    def is_dead(self):
        """是否死亡"""
        return self._life <= 0


class Action:
    """动作类"""

    @staticmethod
    def get_action(data, owner):
        """获取动作"""
        match data["type"]:
            case "ATTACK":
                return Attack(data, owner)
            case "HEAL":
                return Heal(data, owner)
            case "CHEAT":
                return Cheat(data, owner)

    def __init__(self, data, owner: Character):
        self._owner = owner
        self._description = data["description"]

    def execute(self, target: Character):
        """执行动作"""


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
        exe_text = self._description
        if self._self_hurt:
            self_hurt = int(
                random() * (self._self_hurt["max"] - self._self_hurt["min"])
                + self._self_hurt["min"]
            )
            self._owner.hurt(self._self_hurt)
            exe_text += self._self_hurt["description"].replace(
                Kernel.BATTLE_STORY["BLANK"], str(self_hurt)
            )
        dodge = 50 + self._owner.get_speed() - target.get_speed()
        if random() * 500 < dodge:
            exe_text += Kernel.BATTLE_STORY["DODGE"]
        else:
            damage = int(
                self._owner.get_attack()
                * (0.8 + 0.4 * random())
                * self._strength
            )
            target.hurt(damage)
            exe_text += Kernel.BATTLE_STORY["HURT"].replace(
                Kernel.BATTLE_STORY["BLANK"], str(damage)
            )
        return exe_text


class Heal(Action):
    """治疗动作"""

    def __init__(self, data, owner):
        super().__init__(data, owner)
        self._min = data["min"]
        self._max = data["max"]

    def execute(self, target):
        """执行治疗"""
        heal = int(self._min + random() * (self._max - self._min))
        self._owner.heal(heal)
        exe_text = self._description + Kernel.BATTLE_STORY["HEAL"].replace(
            Kernel.BATTLE_STORY["BLANK"], str(heal)
        )
        return exe_text


class Cheat(Action):
    """作弊动作"""

    def execute(self, target):
        """作弊"""
        target.hurt(target.get_life())
        return self._description


class Hero(Character):
    """英雄类"""

    @staticmethod
    def get_hero(hero_id, data):
        """获取英雄"""
        match hero_id:
            case "HAL":
                return Hal(data)

    def get_moves(self):
        """获取选项"""


class Hal(Hero):
    """主角类"""

    def __init__(self, data):
        super().__init__(data)
        self._attack = 100
        self._attack += Kernel.KERNEL.get_para("BRUCE_LOVE") * 2
        self._attack += Kernel.KERNEL.get_para("INTELLIGENCE") * 2
        self._attack += Kernel.KERNEL.get_para("DRAGON_EGG") * 10
        self._speed = 100
        self._speed += Kernel.KERNEL.get_para("KNOWLEDGE")
        self._speed += Kernel.KERNEL.get_para("PEGASUS") * 20
        self._life_max = 100
        self._life_max += Kernel.KERNEL.get_para("OLIVER_LOVE") * 10
        self._life_max += Kernel.KERNEL.get_para("BARRY_LOVE") * 10

        self._life = self._life_max


class Enemy(Character):
    """敌人类"""

    @staticmethod
    def get_enemy(enemy_id, data):
        """获取敌人"""
        match enemy_id:
            case "SINESTRO":
                return Sinestro(data)


class Sinestro(Enemy):
    """魔王类"""


class BattleChoice(Choice):
    """决战选项"""

    def __init__(self, battle_scene, data=None):
        super().__init__(data)
        self._battle_scene = battle_scene

    def text(self):
        return super().text()

    def show(self):
        return super().show()

    def chosen(self):
        self._battle_scene.next_round()


class BattleScene(Scene):
    """决战场景"""

    def __init__(self, data=None):
        super().__init__(data)
        self._round = 0
        self._enemy = Character.get_character(Kernel.BATTLE_STORY["ENEMY"])
        self._hero = Character.get_character(Kernel.BATTLE_STORY["HERO"])

    def get_id(self):
        return Kernel.FINAL_BATTLE

    def get_text(self):
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
        if self._round == 0:
            return battle_text + Kernel.BATTLE_STORY["START"]
        battle_text += self._hero.tack_act(None)
        if self._enemy.is_dead():
            return battle_text + Kernel.BATTLE_STORY["WIN"]
        battle_text += self._enemy.tack_act(self._hero)
        if self._hero.is_dead():
            return battle_text + Kernel.BATTLE_STORY["LOSE"]
        else:
            return battle_text

    def get_options(self):
        if self._enemy.is_dead():
            pass
        elif self._hero.is_dead():
            pass
        else:
            return self._hero.get_moves()

    def next_round(self):
        """下一轮"""
        self._round += 1
