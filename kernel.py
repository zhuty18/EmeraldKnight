import json, os
from constant import gk, debug_para, default_para, sceneName, GAME_OVER, res_path, open_info_entry
from choices import getChoice
from abstract import choice_end, choice_unfinished

VERSION = "0.5"


class kernel:
    def __init__(self):
        gk.scene = "0"

    def getChoice(self):
        return getChoice(gk.scene)

    def load(self, name):
        if name == "0":
            gk.scene = "1-1"
            gk.paras = default_para()
        else:
            k = "./save/"
            with open(k + name + ".eks", "r") as f:
                j = json.loads(f.read())
                gk.scene = j['scene']
                gk.paras = j['paras']
            self.refresh()

    def save(self, name):
        k = "./save/"
        with open(k + name + ".eks", "w") as f:
            j = json.loads('{}')
            j['scene'] = gk.scene
            j['paras'] = gk.paras
            f.write(json.dumps(j))

    def getSceneName(self, s):
        return sceneName(s)

    def loadScene(self):
        if gk.scene == GAME_OVER:
            return GAME_OVER, []
        else:
            try:
                fn = os.path.join("story", gk.scene + ".txt")
                with open(res_path(fn), "r", encoding="utf8") as f:
                    scenetext = f.read()
                scenetext = "    " + scenetext
                scenetext = scenetext.replace("\n", "\n    ")
                choice = self.getChoice()
                if choice is None:
                    choice = [choice_unfinished()]
                # open_info_entry(gk.scene)
                return scenetext, choice
            except FileNotFoundError:
                scenetext = "抱歉，这儿还没写呢。请先存档。"
                return scenetext, [choice_end()]

    def refresh(self):
        for i in debug_para.keys():
            if i not in gk.paras:
                gk.paras[i] = 0
