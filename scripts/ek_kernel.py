import json
import ek_abstract
from ch1 import *
from constant import *


class ek_kernel:
    def __init__(self):
        self.scene = "0"
        self.paras = default_para
        ek_abstract.ek_choice.kernel = self

    def getChoice(self):
        name = self.scene
        if name == "1-1":
            return s1_1().choices()
        elif name == "1-2":
            return s1_2().choices()
        elif name == "1-4":
            return s1_4().choices()

    def load(self, name):
        if name == "0":
            self.scene = "1-1"
        else:
            with open("./save/"+name+".eks", "r") as f:
                self.scene = f.readline().strip()
                self.paras = json.loads(f.readline())

    def save(self, name):
        with open("./save/"+name+".eks", "w") as f:
            f.write(self.scene+"\n")
            f.write(json.dumps(self.paras)+"\n")

    def getSceneName(self, s):
        return ek_abstract.getName(s)
