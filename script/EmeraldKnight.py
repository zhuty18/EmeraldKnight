from functools import partial

import PySide6.QtCore as core
import PySide6.QtGui as gui
import PySide6.QtWidgets as qt
from game_kernel import Kernel


class EmeraldKnight:
    """游戏类"""

    def __init__(self):
        Kernel()
        self.gk = Kernel.KERNEL
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
        self.app.exec_()

    def set_menu(self):
        """初始化工具栏"""
        self.icon = gui.QIcon(Kernel.res_path("", "icon.ico"))
        self.main.setWindowIcon(self.icon)
        self.main.setWindowTitle("翡翠骑士 v" + Kernel.VERSION)
        menu_bar = self.main.menuBar()
        new_btn = menu_bar.addAction("新的游戏")
        new_btn.triggered.connect(self.new_game)
        # save_btn = menu_bar.addAction("保存进度")
        # save_btn.triggered.connect(self.save_game)
        # load_btn = menu_bar.addAction("读取存档")
        # load_btn.triggered.connect(self.load_game)
        # exit_btn = menu_bar.addAction("退出游戏")
        # exit_btn.triggered.connect(self.exit_game)
        if Kernel.DEBUG:
            debug_btn = menu_bar.addAction("打印变量")
            debug_btn.triggered.connect(self.debug_game)
        # about_btn = menu_bar.addAction("关于")
        # about_btn.triggered.connect(self.about_game)

    def update(self, layout):
        """刷新"""
        game = qt.QWidget(self.main)
        game.setLayout(layout)
        self.main.setCentralWidget(game)
        self.main.update()

    def load_scene(self):
        """加载场景"""
        print(self.gk.get_scene_id() == self.gk.START_OVER)
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
            "</font><font size=2>v" + Kernel.VERSION + "<br><br></font>"
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
        self.load_game(0)

    def load_game(self, save_id):
        """从存档加载游戏"""
        self.gk.load_save(save_id)
        self.load_scene()

    def choose(self, choice):
        """选择选项"""
        choice.chosen()
        self.load_scene()

    def debug_game(self):
        """调试"""
        self.gk.print_debug()


if __name__ == "__main__":
    ek = EmeraldKnight()
    ek.run()
