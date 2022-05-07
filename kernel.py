import json, os, time
from battle import battle
from constant import gk, GAME_OVER, res_path, FINAL_BATTLE
from choices import getChoice
from abstract import choice_end

VERSION = "0.7"


class kernel:
    def __init__(self):
        gk.scene = "0"

    def getChoice(self):
        return getChoice(gk.scene)

    def load(self, name):
        if name == "0":
            gk.scene = "1-1"
            gk.paras = gk.default_para()
        else:
            k = "./save/" + name + ".eks"
            with open(res_path(k), "r") as f:
                j = json.loads(f.read())
                gk.scene = j['scene']
                gk.paras = j['paras']
            self.refresh()

    def save(self, name):
        k = "./save/" + name + ".eks"
        with open(res_path(k), "w") as f:
            j = json.loads('{}')
            j['scene'] = gk.scene
            j['paras'] = gk.paras
            j['time'] = time.time()
            f.write(json.dumps(j))

    def loadScene(self) -> tuple[str, list]:
        if gk.scene == GAME_OVER:
            return GAME_OVER, []
        elif gk.scene == FINAL_BATTLE:
            if gk.battle == None:
                gk.battle = battle()
                return gk.battle.first_round()
            else:
                return gk.battle.round()
        else:
            try:
                fn = os.path.join("story", gk.scene + ".txt")
                with open(res_path(fn), "r", encoding="utf8") as f:
                    scenetext = f.read()
                if gk.scene.startswith("end"):
                    scenetext += "\n\n结局——" + gk.targetName(gk.scene)
                scenetext = "    " + scenetext
                scenetext = scenetext.replace("\n", "\n    ")
                choice = self.getChoice()
                # open_info_entry(gk.scene)
                return scenetext, choice
            except FileNotFoundError:
                scenetext = "抱歉，这儿还没写呢。请先存档。"
                return scenetext, [choice_end()]

    def refresh(self):
        for i in gk.debug_para.keys():
            if i not in gk.paras:
                gk.paras[i] = 0

    def getChapter(self, s):
        ch = s.split('-')[0]
        if ch == "end":
            return "结局\t" + gk.targetName(s)
        if ch == "1":
            return "第一章\t出发"
        elif ch == "2":
            return "第二章\t传说"
        elif ch == "3":
            return "第三章\t雪山"
        elif ch == "4":
            return "第四章\t远方"
        elif ch == "5":
            return "第五章\t危城"
        elif ch == "6":
            return "第六章\t孤光"
