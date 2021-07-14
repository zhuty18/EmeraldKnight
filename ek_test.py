import os


class EmeraldKnight:
    def __init__(self):
        self.kernel = kernel.kernel()
        self.scenetext = ""
        self.choices = []
        self.hello()

    def hello(self):
        # print("感谢你打开这个游戏！")
        # print("=======================")
        # print("翡翠骑士\nEmerald Knight")
        # print("=======================")
        # print("N\t新的游戏")
        # print("L\t载入存档")
        # print("Q\t退出游戏")
        # print("\n（不区分大小写）")

        while (True):
            t = input().capitalize()
            if t == "N":
                self.newGame()
                break
            elif t == "L":
                self.loadGame()
                break
            elif t == "Q":
                break
            else:
                print("请重新输入")

    def newGame(self):
        self.startGame("0")

    def printSave(self):
        havesave = False
        for i in range(1, 11):
            try:
                with open("save/" + str(i) + ".eks", "r") as f:
                    if not havesave:
                        havesave = True
                        print("以下是你的存档：")
                    s = f.readline().strip()
                    print("存档" + str(i) + "\t" + s + "\t" + self.kernel.getSceneName(s))
            except FileNotFoundError:
                pass
        return havesave

    def loadGame(self):
        havesave = self.printSave
        if not havesave:
            print("没有存档！")
            print("N\t新的游戏\nB\t返回\nQ\t退出游戏\n")
            while (True):
                t = input().capitalize()
                if t == "N":
                    self.newGame()
                    break
                elif t == "B":
                    if self.kernel.scene == "0":
                        self.hello()
                    break
                elif t == "Q":
                    quit()
                else:
                    print("请重新输入！")
        else:
            print()
            s = input("你要载入的存档编号为：")
            while (True):
                if os.path.exists("save/" + s + ".eks"):
                    self.startGame(s)
                    break
                else:
                    print("存档不存在，请重新选择！")
                    s = input()

    def saveGame(self):
        havesave = self.printSave()
        if havesave:
            print("\n以上是你的存档\n")
        print("请输入一个[1,10]内的数字来保存当前进度，输入B返回")
        while (True):
            try:
                s = input().capitalize()
                if s == "B":
                    break
                index = int(s)
                if index > 0 and index <= 10:
                    self.kernel.save(str(index))
                    print("保存成功！")
                    break
                else:
                    raise TypeError
            except TypeError:
                print("请重新输入！")

    def startGame(self, name):
        self.kernel.load(name)
        # self.tips()
        while (True):
            self.loadScene()

    def loadScene(self):
        self.scenetext, self.choices = self.kernel.loadScene()
        self.scenetext = self.kernel.scene
        # with open("story/" + self.kernel.scene, "r", encoding="utf8") as f:
        #     self.scenetext = f.read()
        # self.choices = self.kernel.getChoice()
        self.choose()

    def tips(self):
        print("游戏过程中，全程支持以下操作：\nS\t保存进度\nL\t读取进度\nQ\t退出游戏\n祝您游戏愉快！\n\n输入任意字符开始")
        input()

    def choose(self):
        # print(self.scenetext + "\n")
        print(self.scenetext)
        for i in range(0, len(self.choices)):
            print(chr(i + ord('A')) + "\t" + self.choices[i].text())
        # print()
        while (True):
            s = input().capitalize()
            try:
                t = ord(s[0]) - ord("A")
                if t >= 0 and t < len(self.choices):
                    self.choices[t].chosen()
                    break
                elif s == "S":
                    self.saveGame()
                    break
                elif s == "L":
                    self.loadGame()
                    break
                elif s == "Q":
                    quit()
                else:
                    raise TypeError
            except TypeError:
                print("请重新输入！")


if __name__ == "__main__":
    from sys import path
    path.append("./scripts")
    from scripts import kernel
    kernel.TEST = True
    ek = EmeraldKnight()
