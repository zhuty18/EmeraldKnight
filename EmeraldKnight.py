import os
from functools import partial
import PySide2.QtWidgets as qt
import PySide2.QtCore as core
import PySide2.QtGui as gui


class EmeraldKnight:
    def __init__(self):
        self.kernel = kernel.kernel()
        self.scenetext = ""
        self.choices = []
        self.loading = False
        self.saving = True
        self.app = qt.QApplication()
        self.main = qt.QMainWindow()
        self.main.resize(400, 640)
        self.setMenu()
        self.main.show()
        self.hello()

    def setMenu(self):
        menu = self.main.menuBar()
        new = menu.addAction("新的游戏")
        new.triggered.connect(self.newGame)
        save = menu.addAction("保存进度")
        save.triggered.connect(self.saveGame)
        load = menu.addAction("读取存档")
        load.triggered.connect(self.loadGame)
        exit = menu.addAction("退出游戏")
        exit.triggered.connect(self.exitGame)

    def update(self, layout):
        self.game = qt.QWidget(self.main)
        self.game.setLayout(layout)
        self.main.setCentralWidget(self.game)
        self.main.update()

    def hello(self):
        hello_str = "<font size=60>翡翠骑士\n</font>"

        hello_layout = qt.QVBoxLayout()
        hello_label = qt.QLabel()
        hello_label.setText(hello_str)
        hello_label.setAlignment(core.Qt.AlignCenter)
        hello_layout.addWidget(hello_label)
        self.update(hello_layout)

    def newGame(self):
        self.startGame("0")

    def showSave(self):
        saves = qt.QDialog()
        self.dia = saves
        saves_layout = qt.QVBoxLayout()
        for i in range(1, 11):
            try:
                with open("save/"+str(i)+".eks", "r") as f:
                    s = f.readline().strip()
                    s = "存档"+str(i)+"\t"+s+"\t"+self.kernel.getSceneName(s)
                    btn = qt.QPushButton(s)
                    btn.clicked.connect(partial(self.pick, i))
                    saves_layout.addWidget(btn)
            except FileNotFoundError:
                s = "空存档"
                btn = qt.QPushButton(s)
                btn.clicked.connect(partial(self.pick, i))
                saves_layout.addWidget(btn)
        saves.setLayout(saves_layout)
        saves.show()
        saves.exec_()

    def pick(self, i):
        self.picked = i
        self.dia.close()
        if self.loading:
            self.loading = False
            # print("读档"+str(i))
            self.startGame(str(i))
        elif self.saving:
            self.kernel.save(str(i))
            # print("保存成功！")

    def pickSave(self):
        self.picked = 0
        self.showSave()

    def loadGame(self):
        havesave = False
        for i in range(1, 11):
            try:
                open("save/"+str(i)+".eks", "r")
                havesave = True
            except FileNotFoundError:
                pass
        if havesave:
            self.loading = True
            self.pickSave()
        else:
            m = qt.QMessageBox(self.main)
            m.critical(self.main, "警告！", "当前无可用存档！")

    def saveGame(self):
        if self.scenetext == "":
            m = qt.QMessageBox(self.main)
            m.critical(self.main, "警告！", "还没有进入游戏！")
        else:
            self.saving = True
            self.pickSave()

    def exitGame(self):
        self.app.exit()

    def startGame(self, name):
        self.kernel.load(name)
        self.loadScene()

    def loadScene(self):
        self.scenetext, self.choices = self.kernel.loadScene()
        game_layout = qt.QVBoxLayout()
        text = qt.QLabel(self.scenetext+"\n")
        text.setWordWrap(True)
        game_layout.addWidget(text)
        for i in range(0, len(self.choices)):
            s = chr(i+ord('A'))+"\t"+self.choices[i].text()
            btn = qt.QPushButton(s)
            btn.clicked.connect(partial(self.choose, i))
            game_layout.addWidget(btn)
        self.update(game_layout)

    def choose(self, c):
        self.choices[c].chosen()
        self.loadScene()


if __name__ == "__main__":
    from sys import path
    path.append("./scripts")
    from scripts import kernel
    ek = EmeraldKnight()
    ek.app.exec_()
