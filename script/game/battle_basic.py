# coding = utf-8

"""战斗基类"""

from game_logic import Logic
from logic_basic import BasicLogic


class Character(BasicLogic):
    """角色类"""

    @classmethod
    def get_existence(cls, para_1=None, para_2=None):
        """
        获取角色实例

        参数:
            para_1: 角色json配置
            para_2: None
        """
        return super().get_existence(para_1, para_2)

    def __init__(self, data):
        self._id = data["id"]
        self._attack = None
        self._speed = None
        self._life_max = None
        self._life = None
        self._name = data["name"]
        self._actions = []
        for act in data["actions"]:
            self._actions.append(Action.get_existence(act, self))
        self._record = ""

    def set(self):
        """完成设置"""
        self._life = self._life_max

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

    def tack_act(self, _):
        """进行回合"""
        return self._record

    def hurt(self, damage):
        """受到伤害"""
        self._life = max(self._life - damage, 0)

    def heal(self, heal):
        """治疗"""
        self._life = min(self._life + heal, self._life_max)

    def is_dead(self):
        """是否死亡"""
        return self._life == 0

    def set_text(self, message):
        """更新记录"""
        self._record = message

    def is_hero(self):
        """是否为英雄"""
        return False

    def is_enemy(self):
        """是否为敌人"""
        return False


class Action(BasicLogic):
    """动作类"""

    @classmethod
    def get_existence(cls, para_1=None, para_2=None):
        """
        获取动作实例

        参数:
            para_1: 动作json配置
            para_2: 动作主体
        """
        return super().get_existence(para_1, para_2)

    def __init__(self, data, owner):
        self._id = data["id"]
        self._owner = owner
        self._text = data["text"]

        self._show = None
        if "show" in data:
            self._show = data["show"]

        self._name = None
        if "name" in data:
            self._name = data["name"]

        self._condition = None
        self._first = None
        self._chance = None
        if "condition" in data:
            self._condition = data["condition"]
        if "first" in data:
            self._first = data["first"]
        if "chance" in data:
            self._chance = data["chance"]

    def execute(self, _: Character = None):
        """执行动作"""
        return self._text

    def get_name(self):
        """获取动作名"""
        return self._name

    def is_available(self):
        """是否可用"""
        if not self._show:
            return True
        else:
            return Logic.get_kernel().check_is(self._show)

    def get_first(self):
        """获取首次条件"""
        return self._first

    def get_condition(self):
        """获取触发条件"""
        return self._condition

    def get_chance(self):
        """获取触发几率"""
        return self._chance

    def is_heal(self):
        """是否为治疗"""
        return False
