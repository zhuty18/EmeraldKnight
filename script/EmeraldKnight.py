# coding = utf-8

"""翡翠骑士游戏 v2.0"""

import sys
from functools import partial

import PySide6.QtCore as core
import PySide6.QtGui as gui
import PySide6.QtWidgets as qt
from EmeraldKnightCMD import EmeraldKnightCMD
from game_kernel import Kernel


class EmeraldKnight:
    """游戏类"""

    def __init__(self):
        self.gk = Kernel()
        self.app = qt.QApplication()
        self.main = qt.QMainWindow()
        self.main.resize(400, 640)
        self.set_menu()
        self.font = gui.QFont()
        self.font.setPixelSize(14)
        self.font.setFamily("宋体")
        self.main.show()
        self.hello_page()

    def run(self):
        """运行游戏"""
        self.app.exec()

    def set_menu(self):
        """初始化工具栏"""
        self.icon = gui.QIcon(self.gk.res_path("", "icon.ico"))
        self.main.setWindowIcon(self.icon)
        self.main.setWindowTitle("翡翠骑士 v" + self.gk.VERSION)
        menu_bar = self.main.menuBar()
        new_btn = menu_bar.addAction("新的游戏")
        new_btn.triggered.connect(self.new_game)
        save_btn = menu_bar.addAction("保存进度")
        save_btn.triggered.connect(self.save_game)
        load_btn = menu_bar.addAction("读取存档")
        load_btn.triggered.connect(self.load_game)
        exit_btn = menu_bar.addAction("退出游戏")
        exit_btn.triggered.connect(self.exit_game)
        if self.gk.DEBUG:
            debug_btn = menu_bar.addAction("打印变量")
            debug_btn.triggered.connect(self.debug_game)
        about_btn = menu_bar.addAction("关于")
        about_btn.triggered.connect(self.about_game)

    def update(self, layout):
        """刷新"""
        game = qt.QWidget(self.main)
        game.setLayout(layout)
        self.main.setCentralWidget(game)
        self.main.update()

    def load_scene(self):
        """加载场景"""
        if self.gk.get_scene_id() == self.gk.START_OVER:
            self.hello_page()
            return
        scene_text = self.gk.get_scene_text()
        choices = self.gk.get_choices()
        game_layout = qt.QVBoxLayout()
        scene_text = scene_text.replace("  ", "&nbsp;")
        scene_text = scene_text.replace("\n", "<br>")
        scene_text = "<p style='line-height:120%'>" + scene_text + "</p>"
        text = qt.QLabel(scene_text)
        text.setFont(self.font)
        text.setWordWrap(True)
        text.setAlignment(core.Qt.AlignTop)
        scroll = qt.QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setWidget(text)
        scroll.setFrameShape(qt.QScrollArea.NoFrame)
        game_layout.addWidget(scroll)
        for index, choice in enumerate(choices):
            btn = qt.QPushButton(f"{chr(index + ord('A'))}: {choice.text()}")
            btn.setFont(self.font)
            btn.clicked.connect(partial(self.choose, choice))
            game_layout.addWidget(btn)
        self.update(game_layout)

    def hello_page(self):
        """开始页"""
        # 1afa29
        hello_str = "<font size=7 face='华文隶书' color='#25ee79'>翡翠骑士<br>"
        hello_str += (
            "</font><font size=2>v" + self.gk.VERSION + "<br><br></font>"
        )
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

    def new_game(self):
        """开始新游戏"""
        self.load_at(0)

    def load_at(self, save_id, save_window=None):
        """从存档加载游戏"""
        if save_id != 0:
            if self.gk.get_save_info(save_id) == self.gk.EMPTY_SAVE:
                m = qt.QMessageBox(self.main)
                m.critical(self.main, "警告！", "不可读取空存档！")
                return
            if save_window:
                save_window.close()
        self.gk.load_at(save_id)
        self.load_scene()

    def save_at(self, save_id, save_window):
        """保存游戏"""
        save_window.close()
        self.gk.save_at(save_id)

    def choose(self, choice):
        """选择选项"""
        choice.chosen()
        self.load_scene()

    def show_save(self, is_saving=True):
        """显示存档界面"""
        saves = qt.QDialog()
        saves.setWindowTitle("当前存档")
        saves_layout = qt.QHBoxLayout()
        for l in range(3):
            v_layout = qt.QVBoxLayout()
            for i in range(10):
                save_id = i + l * 10 + 1
                btn = qt.QPushButton()
                info = self.gk.get_save_info(save_id)
                btn.setText(info)
                if is_saving:
                    btn.clicked.connect(partial(self.save_at, save_id, saves))
                else:
                    btn.clicked.connect(partial(self.load_at, save_id, saves))
                btn.setMinimumSize(140, 36)
                btn.setIcon(self.icon)
                v_layout.addWidget(btn)
            saves_layout.addLayout(v_layout)
        saves.setLayout(saves_layout)
        saves.show()
        saves.exec()

    def save_game(self):
        """存档"""
        if self.gk.get_scene_id() == self.gk.START_OVER:
            m = qt.QMessageBox(self.main)
            m.critical(self.main, "警告！", "还没有进入游戏！")
        else:
            self.show_save()

    def load_game(self):
        """读档"""
        self.show_save(False)

    def debug_game(self):
        """调试"""
        self.gk.print_debug()

    def exit_game(self):
        """退出游戏"""
        self.app.exit()

    def about_game(self):
        """介绍页"""
        s = "作者：兔子草<br><br>"
        s += "联系方式：<br>"
        s += "QQ: 34409508988<br>"
        s += "邮箱：13718054285@163.com<br><br>"
        s += "游戏地址：<br>"
        s += '<a href="https://github.com/zhuty18/EmeraldKnight">'
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
        about.exec()


if __name__ == "__main__":
    if len(sys.argv) == 1:
        ek = EmeraldKnight()
    else:
        ek = EmeraldKnightCMD()
    ek.run()
