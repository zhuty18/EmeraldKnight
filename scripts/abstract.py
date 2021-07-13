from constant import sceneName


class choice_abstract:
    target = ""

    def text(self):
        return sceneName[self.target]

    def show(self):
        return True

    def chosen(self):
        gk.core.scene = self.target


class scene_abstract:
    options = []

    def choices(self):
        ls = []
        for i in self.options:
            if i.show():
                ls.append(i)
        return ls

    def load(self):
        return self.choices()


class gk:
    core = None
