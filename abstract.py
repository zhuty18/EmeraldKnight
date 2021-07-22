from constant import GAME_OVER, sceneName, gk


class choice_abstract:
    target = ""

    def text(self):
        return sceneName(self.target)

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
        return "看到这个，说明出bug了\n麻烦存个档发给我，谢谢\n（13718054285@163.com）"


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
