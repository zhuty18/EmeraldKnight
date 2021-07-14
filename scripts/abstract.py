from constant import GAME_OVER, sceneName


class choice_abstract:
    target = ""

    def text(self):
        return sceneName[self.target]

    def show(self):
        return True

    def chosen(self):
        gk.core.scene = self.target


class choice_end(choice_abstract):
    target = GAME_OVER

    def text(self):
        return "回到开始界面"


class choice_unfinished(choice_abstract):
    target = GAME_OVER

    def text(self):
        return "看到这个就存档吧，后面还没做呢"


class scene_abstract:
    options = []

    def load(self):
        ls = []
        for i in self.options:
            if i.show():
                ls.append(i)
        return ls


class scene_end(scene_abstract):
    def __init__(self, name):
        self.e = name

    def load(self):
        gk.core.openPara(self.e)
        return [choice_end()]


class gk:
    core = None
