import json
from ch1 import *


class kernel:
    def __init__(self):
        self.scene = "0"
        self.paras = debug_para
        # self.paras = default_para
        gk.core = self

    def getChoice(self):
        name = self.scene
        if name == "1-1":
            return s1_1().load()
        elif name == "1-2":
            return s1_2().load()
        elif name == "1-3":
            return s1_3().load()
        elif name == "1-4":
            return s1_4().load()
        elif name == "1-5":
            return s1_5().load()
        elif name == "1-7":
            return s1_7().load()
        elif name == "1-17":
            return s1_17().load()
        elif name == "end-1":
            self.openPara("end-1")
            return [choice_end()]

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
        return sceneName[s]

    def loadScene(self):
        if self.scene == GAME_OVER:
            return GAME_OVER, []
        else:
            with open("story/"+self.scene+".ekt", "r", encoding="utf8") as f:
                scenetext = f.read()
            scenetext = "    "+scenetext
            scenetext = scenetext.replace("\n", "\n    ")
            choice = self.getChoice()
            return scenetext, choice

    def openPara(self, end):
        f = open("./data/0.eks", "r")
        default_para = json.loads(f.read())
        f.close()
        default_para[end] = 1
        f = open("./data/0.eks", "w")
        f.write(json.dumps(default_para)+"\n")
        f.close()
