import json
import ek_abstract


class ek_kernel:
    def __init__(self):
        self.scene = "0"
        self.paras = {
            "osl": 0,  # Oliver Story Line
            "bsl": 0,  # Bruce Story Line
            "ssl": 0,  # Sinestro Story Line
            "sinl": 0,  # Sinestro Love
            "sint": 0  # Sinestro Tame
        }
        ek_abstract.ek_choice.kernel = self

    def getChoice(self):
        name = self.scene
        if name == "1-1":
            return s1_1.choices()
        elif name == "1-4":
            return s1_4.choices()

    def load(self, name):
        with open("./save/"+name+".eks", "r") as f:
            self.scene = f.readline().strip()
            self.paras = json.loads(f.readline())

    def save(self, name):
        with open("./save/"+name+".eks", "w") as f:
            f.write(self.scene+"\n")
            f.write(json.dumps(self.paras)+"\n")

    def getSceneName(self, s):
        return ek_abstract.getName(s)
