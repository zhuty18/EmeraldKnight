import json
from ch1 import *
import constant
from abstract import gk


class kernel:
    def __init__(self):
        self.scene = "0"
        self.paras = constant.default_para
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
