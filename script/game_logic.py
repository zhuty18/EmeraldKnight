# coding = utf-8

"""逻辑类"""
import json
from random import random


class Choice:
    """选项"""

    @staticmethod
    def get_by_id(choice_id):
        """通过ID获取选项"""
        return Choice(Logic.CHOICE_MAP[choice_id])

    def __init__(self, data):
        self._data = data

    def text(self):
        """选项文本"""
        if not "text" in self._data:
            return Logic.scene_name(self._data["target"])
        return self._data["text"]

    def show(self):
        """是否显示"""
        if not "show" in self._data:
            return True
        return Logic.KERNEL.check_is(
            self._data["show"]["op"],
            self._data["show"]["condition"],
        )

    def chosen(self):
        """选择后"""
        if "choose" in self._data:
            for action in self._data["choose"]:
                Logic.KERNEL.change_para(
                    action["para"],
                    action["change"],
                    action["value"],
                )
        Logic.KERNEL.to_scene(self._data["target"])


class Scene:
    """场景"""

    @staticmethod
    def get_by_id(scene_id):
        """通过ID获取场景"""
        if "end" in scene_id:
            Logic.mark_end(scene_id)
            return Scene(
                {
                    "id": scene_id,
                    "options": Logic.SCENE_MAP[Logic.START_OVER]["options"],
                }
            )
        elif scene_id == Logic.FINAL_BATTLE:
            return BattleScene(Logic.SCENE_MAP[scene_id])
        return Scene(Logic.SCENE_MAP[scene_id])

    def __init__(self, data):
        self._data = data

    def get_id(self):
        """获取ID"""
        return self._data["id"]

    def get_text(self):
        """获取文本"""
        s_id = (
            self._data["scene"] if "scene" in self._data else self._data["id"]
        )
        scene_text = Logic.read_file("story", f"{s_id}.txt", False)
        if "end" in self._data["id"]:
            scene_text += Logic.STORY_END + Logic.get_end_name(self._data["id"])
        scene_text = "    " + scene_text
        scene_text = scene_text.replace("\n", "\n    ")
        return scene_text

    def get_options(self, options=None, choices=None):
        """获取选项"""
        if not choices:
            if not options:
                options = self._data["options"]
            if "require" in self._data:
                if Logic.KERNEL.check_is(
                    self._data["require"]["op"],
                    self._data["require"]["condition"],
                ):
                    options = self._data["require"]["match_options"]
            choices = [Choice.get_by_id(x) for x in options]
        res = []
        for c in choices:
            if c.show():
                res.append(c)
        return res


class Character:
    """角色类"""

    @staticmethod
    def get_character(character_id):
        """根据角色ID获取角色实例"""
        character = Logic.CHARACTER_MAP[character_id]
        if character["type"] == "ENEMY":
            return Enemy.get_enemy(character_id, character)
        else:
            return Hero.get_hero(character_id, character)

    def __init__(self, data):
        self._attack = None
        self._speed = None
        self._life_max = None
        self._life = None
        self._name = data["name"]
        self._actions = []
        for act in data["actions"]:
            self._actions.append(Action.get_action(act, self))
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

    def tack_act(self, target):
        """执行动作"""
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

        self._show = None
        if "show" in data:
            self._show = data["show"]

        self._name = None
        if isinstance(owner, Hero):
            self._name = data["name"]

        self._condition = None
        self._first = None
        self._chance = None
        if isinstance(owner, Enemy):
            if "condition" in data:
                self._condition = data["condition"]
            if "first" in data:
                self._first = data["first"]
            if "chance" in data:
                self._chance = data["chance"]

    def execute(self, target: Character):
        """执行动作"""

    def get_name(self):
        """获取动作名"""
        return self._name

    def is_available(self):
        """是否可用"""
        if not self._show:
            return True
        else:
            return Logic.KERNEL.check_condition(
                self._show["para"],
                self._show["check"],
                self._show["value"],
            )

    def get_first(self):
        """获取首次条件"""
        return self._first

    def get_condition(self):
        """获取触发条件"""
        return self._first

    def get_chance(self):
        """获取触发几率"""
        return self._chance


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
            self._owner.hurt(self_hurt)
            exe_text += self._self_hurt["description"].replace(
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

    def execute(self, target):
        """执行治疗"""
        self._used += 1
        heal = int(self._min + random() * (self._max - self._min))
        self._owner.heal(heal)
        exe_text = self._description + Logic.BATTLE_STORY["HEAL"].replace(
            Logic.BATTLE_STORY["BLANK"], str(heal)
        )
        return exe_text

    def is_available(self):
        return self._used < self._time

    def get_used(self):
        """获取使用次数"""
        return self._used


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
        return self._actions


class Hal(Hero):
    """主角类"""

    def __init__(self, data):
        super().__init__(data)
        self._attack = 100
        self._attack += Logic.KERNEL.get_para("BRUCE_LOVE") * 2
        self._attack += Logic.KERNEL.get_para("INTELLIGENCE") * 2
        self._attack += Logic.KERNEL.get_para("DRAGON_EGG") * 10
        self._speed = 100
        self._speed += Logic.KERNEL.get_para("KNOWLEDGE")
        self._speed += Logic.KERNEL.get_para("PEGASUS") * 20
        self._life_max = 100
        self._life_max += Logic.KERNEL.get_para("OLIVER_LOVE") * 10
        self._life_max += Logic.KERNEL.get_para("BARRY_LOVE") * 10

        self.set()


class Enemy(Character):
    """敌人类"""

    @staticmethod
    def get_enemy(enemy_id, data):
        """获取敌人"""
        match enemy_id:
            case "SINESTRO":
                return Sinestro(data)

    def tack_act(self, target):
        chance = []
        for act in self._actions:
            if isinstance(act, Heal) and self.need_heal(act):
                return act.execute(target)
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
        self._attack -= Logic.KERNEL.get_para("SINESTRO_LOVE") * 5
        self._speed = 100
        self._speed -= Logic.KERNEL.get_para("SINESTRO_LOVE") * 2
        self._life_max = data["max_life"]
        self.set()


class BattleChoice(Choice):
    """决战选项"""

    def __init__(self, battle_scene, move: Action, data=None):
        super().__init__(data)
        self._battle_scene = battle_scene
        self._move = move

    def text(self):
        return self._move.get_name()

    def show(self):
        return self._move.is_available()

    def chosen(self):
        self._battle_scene.get_hero().set_text(
            self._move.execute(self._battle_scene.get_enemy())
        )
        self._battle_scene.next_round()


class BattleScene(Scene):
    """决战场景"""

    def __init__(self, data):
        super().__init__(data)
        self._round = 0
        self._enemy = Character.get_character(Logic.BATTLE_STORY["ENEMY"])
        self._hero = Character.get_character(Logic.BATTLE_STORY["HERO"])

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
            return super().get_options(options=self._data["options_win"])
        elif self._hero.is_dead():
            return super().get_options(options=self._data["options_lose"])
        else:
            return super().get_options(
                choices=[BattleChoice(self, x) for x in self._hero.get_moves()]
            )

    def next_round(self):
        """下一轮"""
        self._round += 1


class Logic:
    """逻辑类"""

    KERNEL = None

    PATH_GAME = "game"  # 游戏相关文件路径
    FILE_PARAS = "paras.json"  # 参数存储文件
    FILE_SCENES = "scenes_ch{ch}.json"  # 场景存储文件
    FILE_CHOICES = "choices_ch{ch}.json"  # 选项存储文件
    FILE_NAMES = "names.json"  # 名称存储文件
    PATH_STORY = "story"  # 故事相关文件路径
    PATH_SAVE = "save"  # 存档相关文件路径
    FILE_DEFAULT_SAVE = "0.eks"  # 初始存档文件

    DEFAULT_PARAS = {}  # 参数表
    DEFAULT_CODES = {}  # 代码表
    DEFAULT_CONSTS = {}  # 常量表
    SCENE_MAP = {}  # 场景表
    CHOICE_MAP = {}  # 选项表
    END_NAME_MAP = {}  # 结局名表
    CHAPTER_NAME_MAP = {}  # 章名表
    CHARACTER_MAP = {}  # 角色表

    START_SCENE = ""  # 起始场景
    START_OVER = ""  # 重开场景
    FINAL_BATTLE = ""  # 重开场景
    SCENE = ""  # 场景变量名
    END = ""  # 结局变量名
    FIGHT = ""  # 战斗变量名
    CHOICE = ""  # 选项变量名
    EMPTY_SAVE = ""  # 空存档字符串
    STORY_END = ""  # 故事结尾补充字符串
    BATTLE_STORY = {}  # 决战相关字符串

    def __init__(self, kernel):
        Logic.KERNEL = kernel

        for i in Logic.read_file(Logic.PATH_GAME, Logic.FILE_PARAS)[
            "const_list"
        ]:
            Logic.DEFAULT_CONSTS[i["name"]] = i["value"]
        for i in Logic.read_file(Logic.PATH_GAME, Logic.FILE_PARAS)[
            "para_list"
        ]:
            Logic.DEFAULT_PARAS[i["name"]] = i
        for i in Logic.read_file(Logic.PATH_GAME, Logic.FILE_PARAS)[
            "code_list"
        ]:
            Logic.DEFAULT_CODES[i["name"]] = i["value"]
        for i in Logic.read_file(Logic.PATH_GAME, Logic.FILE_PARAS)[
            "character_list"
        ]:
            Logic.CHARACTER_MAP[i["id"]] = i

        end_scene = Logic.DEFAULT_CONSTS["END_SCENE"]
        Logic.SCENE_MAP[end_scene["id"]] = end_scene
        end_choice = Logic.DEFAULT_CONSTS["END_CHOICE"]
        Logic.CHOICE_MAP[end_choice["id"]] = end_choice
        for ch in range(Logic.KERNEL.CHAPTER):
            for i in Logic.read_file(
                Logic.PATH_GAME,
                Logic.FILE_SCENES.replace("{ch}", str(ch + 1)),
            ):
                Logic.SCENE_MAP[i["id"]] = i
            for i in Logic.read_file(
                Logic.PATH_GAME,
                Logic.FILE_CHOICES.replace("{ch}", str(ch + 1)),
            ):
                Logic.CHOICE_MAP[i["id"]] = i

        for k, v in Logic.read_file(Logic.PATH_GAME, Logic.FILE_NAMES)[
            "end_names"
        ].items():
            Logic.END_NAME_MAP[k] = v
        for k, v in Logic.read_file(Logic.PATH_GAME, Logic.FILE_NAMES)[
            "chapter_names"
        ].items():
            Logic.CHAPTER_NAME_MAP[k] = v

        Logic.START_SCENE = Logic.DEFAULT_CONSTS["START_SCENE"]
        Logic.START_OVER = Logic.DEFAULT_CONSTS["START_OVER"]
        Logic.FINAL_BATTLE = Logic.DEFAULT_CONSTS["FINAL_BATTLE"]
        Logic.SCENE = Logic.DEFAULT_CONSTS["SCENE"]
        Logic.END = Logic.DEFAULT_CONSTS["END"]
        Logic.FIGHT = Logic.DEFAULT_CONSTS["FIGHT"]
        Logic.CHOICE = Logic.DEFAULT_CONSTS["CHOICE"]
        Logic.EMPTY_SAVE = Logic.DEFAULT_CONSTS["EMPTY_SAVE"]
        Logic.STORY_END = Logic.DEFAULT_CONSTS["STORY_END"]
        Logic.BATTLE_STORY = Logic.DEFAULT_CONSTS["BATTLE_STORY"]

    @staticmethod
    def read_file(file_dir, file_name, load_json=True):
        """读取文件"""
        with open(
            Logic.KERNEL.res_path(file_dir, file_name), "r", encoding="utf8"
        ) as f:
            if load_json:
                return json.loads(f.read())
            else:
                return f.read()

    @staticmethod
    def scene_name(scene_id):
        """获取场景名"""
        return Logic.SCENE_MAP[scene_id]["name"]

    @staticmethod
    def mark_end(end_id):
        """解锁结局"""
        static_save = Logic.read_file(Logic.PATH_SAVE, Logic.FILE_DEFAULT_SAVE)
        static_save[end_id] = 1
        with open(
            Logic.KERNEL.res_path(Logic.PATH_SAVE, Logic.FILE_DEFAULT_SAVE),
            "w",
            encoding="utf8",
        ) as f:
            f.write(json.dumps(static_save, ensure_ascii=False))

    @staticmethod
    def check_end(end_id):
        """检查结局是否解锁"""
        static_save = Logic.read_file(Logic.PATH_SAVE, Logic.FILE_DEFAULT_SAVE)
        return static_save.get(end_id, 0) == 1

    @staticmethod
    def get_end_name(end_id):
        """获取结局名称"""
        return Logic.END_NAME_MAP[end_id]
