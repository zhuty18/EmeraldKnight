from functools import partial
import PySide2.QtWidgets as qt
import PySide2.QtCore as core

import kernel
from constant import GAME_OVER

VERSION = "0.1"


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
        # self.tips()

    def setMenu(self):
        self.main.setWindowTitle("翡翠骑士 v" + VERSION)
        menu = self.main.menuBar()
        new = menu.addAction("新的游戏")
        new.triggered.connect(self.newGame)
        save = menu.addAction("保存进度")
        save.triggered.connect(self.saveGame)
        load = menu.addAction("读取存档")
        load.triggered.connect(self.loadGame)
        exit = menu.addAction("退出游戏")
        exit.triggered.connect(self.exitGame)
        # exit = menu.addAction("刷新存档")
        # exit.triggered.connect(self.refresh)
        exit = menu.addAction("关于")
        exit.triggered.connect(self.about)

    def update(self, layout):
        self.game = qt.QWidget(self.main)
        self.game.setLayout(layout)
        self.main.setCentralWidget(self.game)
        self.main.update()

    def hello(self):
        hello_str = "<font size=10>翡翠骑士<br></font><font size=6>v" + VERSION + "<br></font>"
        hello_str += "<font size=4><br>雪山之巅，英魂渐远。<br>危城影下，一念不灭。<br>剑心重铸，翡翠长明。<br>孤星陨灭，万灵恸哭。<br></font>"
        hello_str += "<br><br>"
        hello_str += "<font size=3>作者：兔子草<br></font>"
        hello_layout = qt.QVBoxLayout()
        hello_label = qt.QLabel()
        hello_label.setText(hello_str)
        hello_label.setWordWrap(True)
        hello_label.setAlignment(core.Qt.AlignCenter)
        hello_layout.addWidget(hello_label)
        self.update(hello_layout)

    def newGame(self):
        self.startGame("0")

    def showSave(self):
        saves = qt.QDialog()
        saves.setWindowTitle("当前存档")
        self.dia = saves
        saves_layout = qt.QVBoxLayout()
        for i in range(1, 11):
            try:
                with open("save/" + str(i) + ".eks", "r") as f:
                    s = f.readline().strip()
                    s = "存档" + str(i) + "\t" + s + "\t" + self.kernel.getSceneName(s)
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
            try:
                open("save/" + str(i) + ".eks", "r")
                self.loading = False
                # print("读档"+str(i))
                self.startGame(str(i))
            except FileNotFoundError:
                m = qt.QMessageBox(self.main)
                m.critical(self.main, "警告！", "不可读取空存档！")
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
                open("save/" + str(i) + ".eks", "r")
                havesave = True
            except FileNotFoundError:
                pass
        if havesave:
            self.saving = True
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
            self.loading = False
            self.saving = True
            self.pickSave()

    def exitGame(self):
        self.app.exit()

    def startGame(self, name):
        self.kernel.load(name)
        self.loadScene()

    def loadScene(self):
        self.scenetext, self.choices = self.kernel.loadScene()
        if self.scenetext == GAME_OVER:
            self.hello()
        else:
            game_layout = qt.QVBoxLayout()
            text = qt.QLabel(self.scenetext + "\n")
            text.setWordWrap(True)
            scroll=qt.QScrollArea()
            scroll.setWidgetResizable(True)
            scroll.setWidget(text)
            scroll.setFrameShape(qt.QScrollArea.NoFrame)
            game_layout.addWidget(scroll)
            for i in range(0, len(self.choices)):
                s = chr(i + ord('A')) + "\t" + self.choices[i].text()
                btn = qt.QPushButton(s)
                btn.clicked.connect(partial(self.choose, i))
                game_layout.addWidget(btn)
            self.update(game_layout)

    def tips(self):
        m = qt.QMessageBox(self.main)
        m.information(self.main, "提示", "如使用之前版本的存档，请在读档后先点击刷新存档按钮再继续游戏")

    def choose(self, c):
        self.choices[c].chosen()
        self.loadScene()

    def refresh(self):
        self.kernel.refresh()

    def about(self):
        s = "作者：兔子草<br><br>"
        s += "联系方式：<br>"
        s += "QQ: 34409508988<br>"
        s += "邮箱：13718054285@163.com<br><br>"
        s += "游戏地址：<br>"
        s += "<a href=\"https://github.com/zhuty18/EmeraldKnight\">github.com/zhuty18/EmeraldKnight</a>"
        about = qt.QDialog()
        about.setWindowTitle("游戏信息")
        layout = qt.QVBoxLayout()
        label = qt.QLabel()
        label.setText(s)
        layout.addWidget(label)
        about.setLayout(layout)
        about.show()
        about.exec_()


import os
if not os.path.exists('./save'):
    os.makedirs('./save')

ek = EmeraldKnight()
ek.app.exec_()
