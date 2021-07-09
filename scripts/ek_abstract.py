from constant import sceneName


class ek_choice:
    target = ""
    kernel = None

    def text(self):
        return sceneName[self.target]

    def show(self):
        return True

    def chosen(self):
        self.kernel.scene = self.target


class ek_scene:
    options = []

    def choices(self):
        ls = []
        for i in self.options:
            if i.show():
                ls.append(i)
        return ls
