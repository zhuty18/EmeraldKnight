from functools import partial
import json, time, os
import PySide2.QtWidgets as qt
import PySide2.QtCore as core
import PySide2.QtGui as gui

from kernel import kernel, VERSION, gk
from constant import GAME_OVER, res_path, DEBUG


class EmeraldKnight:
    def __init__(self):
        gk.init()
        self.kernel = kernel()
        self.choices = []
        self.loading = False
        self.saving = True
        self.app = qt.QApplication()
        self.main = qt.QMainWindow()
        self.main.resize(400, 640)
        self.setMenu()
        self.font = gui.QFont()
        self.font.setPixelSize(14)
        self.font.setFamily("宋体")
        self.main.show()
        self.hello()
        # self.tips()

    def setMenu(self):
        self.icon = gui.QIcon(res_path("icon.ico"))
        self.main.setWindowIcon(self.icon)
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
        if DEBUG:
            exit = menu.addAction("打印变量")
            exit.triggered.connect(self.debug)
        exit = menu.addAction("关于")
        exit.triggered.connect(self.about)

    def update(self, layout):
        self.game = qt.QWidget(self.main)
        self.game.setLayout(layout)
        self.main.setCentralWidget(self.game)
        self.main.update()

    def hello(self):
        #1afa29
        hello_str = "<font size=7 face='华文隶书' color='#25ee79'>翡翠骑士<br>"
        hello_str += "</font><font size=2>v" + VERSION + "<br><br></font>"
        hello_str += "<font size=3 face='华文仿宋'>"
        hello_str += "雪山之巅&nbsp;&nbsp;英魂渐远<br>"
        hello_str += "危城影下&nbsp;&nbsp;一念不灭<br>"
        hello_str += "剑心重铸&nbsp;&nbsp;翡翠长明<br>"
        hello_str += "孤星陨灭&nbsp;&nbsp;万灵恸哭<br></font>"
        hello_str += "<font size=2><br><br>作者：兔子草</font>"
        hello_layout = qt.QVBoxLayout()
        hello_label = qt.QLabel()
        hello_label.setText(hello_str)
        f = gui.QFont()
        f.setPixelSize(20)
        hello_label.setFont(f)
        hello_label.setAlignment(core.Qt.AlignCenter)
        hello_layout.addWidget(hello_label)
        self.update(hello_layout)

    def newGame(self):
        self.startGame("0")

    def showSave(self):
        saves = qt.QDialog()
        saves.setWindowTitle("当前存档")
        self.dia = saves
        saves_layout = qt.QHBoxLayout()
        for l in range(0, 3):
            v_layout = qt.QVBoxLayout()
            for i in range(1, 11):
                k = i + l * 10
                btn = qt.QPushButton()
                fn = "save/" + str(k) + ".eks"
                fn = res_path(fn)
                try:
                    with open(fn, "r") as f:
                        j = json.loads(f.read())
                    sc = j['scene']
                    s = "存档" + str(k) + "\t"
                    try:
                        t = time.localtime(j['time'])
                    except KeyError:
                        j['time'] = os.path.getmtime(fn)
                        t = time.localtime(j['time'])
                    s += time.strftime("%m.%d\t%H:%M", t)
                    s += "\n"
                    if DEBUG:
                        s += sc + "\t"
                    s += self.kernel.getChapter(sc)
                    btn.setText(s)
                    btn.clicked.connect(partial(self.pick, k))
                except FileNotFoundError:
                    s = "空存档"
                    btn.setText(s)
                    btn.clicked.connect(partial(self.pick, k))
                btn.setMinimumSize(140, 36)
                btn.setIcon(self.icon)
                v_layout.addWidget(btn)
            saves_layout.addLayout(v_layout)
        saves.setLayout(saves_layout)
        saves.show()
        saves.exec_()

    def pick(self, i):
        self.picked = i
        self.dia.close()
        if self.loading:
            try:
                fn = res_path("save/" + str(i) + ".eks")
                open(fn, "r")
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
        for i in range(1, 31):
            try:
                fn = res_path("save/" + str(i) + ".eks")
                open(fn, "r")
                havesave = True
                break
            except FileNotFoundError:
                pass
        if havesave:
            self.saving = False
            self.loading = True
            self.pickSave()
        else:
            m = qt.QMessageBox(self.main)
            m.critical(self.main, "警告！", "当前无可用存档！")

    def saveGame(self):
        if gk.scene == "0":
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
        st, self.choices = self.kernel.loadScene()
        if st == GAME_OVER:
            self.hello()
        else:
            game_layout = qt.QVBoxLayout()
            st = st.replace("  ", "&nbsp;")
            st = st.replace("\n", "<br>")
            st = "<p style='line-height:120%'>" + st + "</p>"
            text = qt.QLabel(st)
            text.setFont(self.font)
            text.setWordWrap(True)
            text.setAlignment(core.Qt.AlignTop)
            scroll = qt.QScrollArea()
            scroll.setWidgetResizable(True)
            scroll.setWidget(text)
            scroll.setFrameShape(qt.QScrollArea.NoFrame)
            game_layout.addWidget(scroll)
            for i in range(0, len(self.choices)):
                s = chr(i + ord('A')) + "\t" + self.choices[i].text()
                btn = qt.QPushButton(s)
                btn.setFont(self.font)
                btn.clicked.connect(partial(self.choose, i))
                game_layout.addWidget(btn)
            self.update(game_layout)

    def tips(self):
        m = qt.QMessageBox(self.main)
        m.information(self.main, "提示", "现在还处于开发阶段，游戏中可能有BUG。")

    def choose(self, c):
        self.choices[c].chosen()
        self.loadScene()

    def about(self):
        s = "作者：兔子草<br><br>"
        s += "联系方式：<br>"
        s += "QQ: 34409508988<br>"
        s += "邮箱：13718054285@163.com<br><br>"
        s += "游戏地址：<br>"
        s += "<a href=\"https://github.com/zhuty18/EmeraldKnight\">"
        s += "github.com/zhuty18/EmeraldKnight</a>"
        about = qt.QDialog()
        about.setWindowTitle("游戏信息")
        layout = qt.QVBoxLayout()
        label = qt.QLabel()
        label.setText(s)
        label.setOpenExternalLinks(True)
        layout.addWidget(label)
        about.setLayout(layout)
        about.show()
        about.exec_()

    def debug(self):
        print(gk.scene)
        print(gk.paras)

if __name__=="__main__":
    from sys import path
    path.append("./script")
    ek = EmeraldKnight()
    ek.app.exec_()
