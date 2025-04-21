import random
from functools import partial

from abstract import choice_abstract
from constant import *
from ending import end_scene, fail_choice


class character:
    def __init__(self, atk, spd, mlf):
        self.attack = atk
        self.max_life = mlf
        self.speed = spd
        self.life = mlf
        self.blood = 0

    def round(self):
        pass

    def is_dead(self):
        return self.life <= 0


class move:
    def hurt(
        src: character, tar: character, multiplier: float
    ) -> tuple[int, str]:
        dodge = 50 + src.speed - tar.speed
        if random.randint(0, 500) < dodge:
            return 0, "被躲开了！"
        else:
            attack = src.attack
            attack *= 0.8 + 0.4 * random.random()
            r = int(attack * multiplier)
            return r, "造成了%d点伤害！" % r


class sinestro(character):
    def __init__(self):
        love = gk.paras[SINESTRO_LOVE]
        tame = gk.paras[SINESTRO_TAME]
        attack = 100 - love * 5
        speed = 100 - tame * 2
        max_life = 500
        super().__init__(attack, speed, max_life)

    def take_act(self, target: character):
        res = None
        if self.blood == 0 and self.life < 250:
            res = self.treat
        elif self.blood == 1 and self.life < 100:
            res = self.treat
        else:
            if random.random() < 0.67:
                res = self.plain_attack
            else:
                res = self.special_attack
        return res(target)

    def plain_attack(self, hal: character) -> str:
        r, m = move.hurt(self, hal, 0.10)
        hal.life -= r
        return "魔王向你发动进攻，" + m

    def special_attack(self, hal: character) -> str:
        r, m = move.hurt(self, hal, 0.25)
        hal.life -= r
        return "魔王对你使用了魔法，" + m

    def treat(self, hal: character) -> str:
        tmp = random.randint(120, 180)
        self.life += tmp
        self.blood += 1
        return "魔王身上黑雾攒动，回复了%d点体力！" % tmp


class hal(character):
    def __init__(self):
        bru_love = gk.paras[BRUCE_LOVE]
        other_love = gk.paras[OLIVER_LOVE] + gk.paras[BARRY_LOVE]
        intel = gk.paras[INTELLIGENCE]
        egg = gk.paras[DRAGON_EGG]
        know = gk.paras[KNOWLEDGE]
        self.pegasus = gk.paras[PEGASUS]
        attack = 100 + (bru_love + intel) * 2 + egg * 10
        speed = 100 + know + self.pegasus * 20
        max_life = 100 + other_love * 10
        super().__init__(attack, speed, max_life)

    def moves(self) -> list[tuple]:
        res = [("普通攻击", self.plain_attack)]
        if self.pegasus == 1:
            res.append(("突袭", self.special_attack))
        res.append(("特殊攻击", self.sword_attack))
        if self.blood < 10:
            res.append(("治疗", self.treat))
        res.append(("开挂", self.cheat))
        return res

    def plain_attack(self, sinestro: character) -> str:
        r, m = move.hurt(self, sinestro, 0.15)
        sinestro.life -= r
        return "你向魔王发动进攻，" + m

    def special_attack(self, sinestro: character) -> str:
        r, m = move.hurt(self, sinestro, 0.30)
        sinestro.life -= r
        return "你借助飞马对魔王发起奇袭，" + m

    def sword_attack(self, sinestro: character) -> str:
        r, m = move.hurt(self, sinestro, 0.50)
        sinestro.life -= r
        tmp = random.randint(5, 15)
        self.life -= tmp
        return "翡翠剑面对魔王放出强光，消耗了你的%d点体力，" % tmp + m

    def treat(self, sinestro: character) -> str:
        tmp = random.randint(30, 50)
        self.life += tmp
        self.blood += 1
        if self.life >= self.max_life:
            tmp -= self.life - self.max_life
            self.life = self.max_life
        return "你吃下一颗雷电小球，回复了%d点体力！" % tmp

    def cheat(self, sinestro: character) -> str:
        sinestro.life = 0
        return "你开挂绝杀！"


class battle_choice(choice_abstract):
    def __init__(self, name, a):
        self.n = name
        self.a = a

    def text(self):
        return self.n

    def chosen(self):
        battle.hal_text = self.a()


class battle:
    def __init__(self):
        self.sinestro = sinestro()
        self.hal = hal()

    def choices(self):
        l = self.hal.moves()
        res = []
        for i in l:
            c = battle_choice(i[0], partial(i[1], self.sinestro))
            res.append(c)
        return res

    def status(self):
        text = "魔王\nHP: %d / %d\n" % (
            self.sinestro.life,
            self.sinestro.max_life,
        )
        text += "\n\n"
        text += " " * 46 + "你\n"
        s = "HP: %d / %d" % (self.hal.life, self.hal.max_life)
        text += " " * (48 - len(s)) + s + "\n"
        text += "\n\n"
        return text

    def first_round(self):
        text = self.status()
        text += "这场决定大陆未来的战斗，开始了！"
        return text, self.choices()

    def round(self):
        text = self.status()
        text += self.hal_text + "\n"
        if self.sinestro.is_dead():
            return text + "魔王倒下了！", end_scene().load()
        s_m = self.sinestro.take_act(self.hal)
        text += s_m
        if self.hal.is_dead():
            return text + "\n你被打败了！", [fail_choice()]
        return text, self.choices()
