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
        elif name == "1-12":
            return s1_12().load()
        elif name == "1-13":
            return [c1_5_1()]
        elif name == "1-17":
            return s1_17().load()
        elif (name == "1-20") or (name == "1-21") or (name == "1-22") or (name == "1-23"):
            return [c1_12_0()]
        elif name == "1-24":
            return s1_24().load()
        elif (name == "1-25") or (name == "1-26") or (name == "1-27") or (name == "1-28"):
            return [c1_24_0()]
        elif name == "1-29":
            return s1_29().load()
        elif name == "1-34":
            return s1_34().load()
        elif name == "1-35":
            return s1_35().load()
        elif name == "1-36":
            return s1_36().load()
        elif name == "1-37":
            return s1_37().load()
        elif name == "1-38":
            return [c1_38_1()]
        elif name == "1-39":
            return s1_39().load()
        elif name == "1-40":
            return s1_40().load()
        elif name == "1-41":
            return s1_41().load()
        elif name == "1-41-2":
            return [c1_41_3()]
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
            with open("story/"+self.scene, "r", encoding="utf8") as f:
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
