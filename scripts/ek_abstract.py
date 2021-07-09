class ek_choice:
    target = ""
    kernel = None

    def text(self):
        return getName(self.target)

    def show(self):
        return True

    def chosen(self):
        self.kernel.scene = self.target


class ek_section:
    cho = []

    def choices(self):
        ls = []
        for i in self.cho:
            if i.show():
                ls.append(i)
        return ls


def getName(s):
    if s == "1-1":
        return "出发"
    elif s == "1-2":
        return "继续前进"
    elif s == "1-3":
        return "原路返回"
    elif s == "1-4":
        return "就地睡一觉"
    elif s == "1-5":
        return "跟着前进"
