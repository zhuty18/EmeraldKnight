from constant import GAME_OVER, gk


class choice_abstract:
    target: str = ""

    # def __init__(self, tar: str):
    #     self.target = tar

    def text(self) -> str:
        return gk.targetName(self.target)

    def show(self) -> bool:
        return True

    def chosen(self) -> None:
        gk.scene = self.target


class choice_end(choice_abstract):
    target = GAME_OVER

    def text(self):
        return "回到开始界面"


class choice_unfinished(choice_abstract):
    target = GAME_OVER

    def text(self):
        return "看到这个，说明出bug了\n麻烦存个档发给我，谢谢\n（13718054285@163.com）"


class scene_abstract:
    options: list = []

    def load(self) -> list[choice_abstract]:
        ls = []
        for i in self.options:
            h: choice_abstract = i()
            if h.show():
                ls.append(h)
        return ls


class scene_end(scene_abstract):
    def __init__(self, name):
        self.e = name

    def load(self):
        gk.openPara(self.e)
        return [choice_end()]
