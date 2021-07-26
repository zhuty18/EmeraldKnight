import json, os
from constant import gk, debug_para, default_para, sceneName, GAME_OVER, res_path
from choices import getChoice
from abstract import choice_end, choice_unfinished

VERSION = "0.2"


class kernel:
    def __init__(self):
        self.scene = "0"
        gk.core = self

    def getChoice(self):
        return getChoice(self.scene)

    def load(self, name):
        if name == "0":
            self.scene = "1-1"
            self.paras = debug_para.copy()
            # self.paras = default_para()
        else:
            k = "./save/"
            with open(k + name + ".eks", "r") as f:
                j = json.loads(f.read())
                self.scene = j['scene']
                self.paras = j['paras']
            self.refresh()

    def save(self, name):
        k = "./save/"
        with open(k + name + ".eks", "w") as f:
            j = json.loads('{}')
            j['scene'] = self.scene
            j['paras'] = self.paras
            f.write(json.dumps(j))

    def getSceneName(self, s):
        return sceneName(s)

    def loadScene(self):
        if self.scene == GAME_OVER:
            return GAME_OVER, []
        else:
            try:
                fn = os.path.join("story", self.scene)
                with open(res_path(fn), "r", encoding="utf8") as f:
                    scenetext = f.read()
                scenetext = "    " + scenetext
                scenetext = scenetext.replace("\n", "\n    ")
                choice = self.getChoice()
                if choice is None:
                    choice = [choice_unfinished()]
                return scenetext, choice
            except FileNotFoundError:
                scenetext = "抱歉，这儿还没写呢。请先存档。"
                return scenetext, [choice_end()]

    def refresh(self):
        for i in debug_para.keys():
            if i not in self.paras:
                self.paras[i] = 0

    def openPara(self, end):
        f = open("./save/0.eks", "r")
        p = json.loads(f.read())
        f.close()
        p[end] = True
        f = open("./save/0.eks", "w")
        f.write(json.dumps(p) + "\n")
        f.close()
