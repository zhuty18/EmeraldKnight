# coding = utf-8

"""游戏编辑器"""


import json
import os

# import PySide6.QtCore as core
# import PySide6.QtGui as gui
import PySide6.QtWidgets as qt
from editor_setting import FILE_CONFIG, PATH_DATA
from info_ctrl import InfoController
from para_ctrl import ParaController
from utils import write_data

from script.game.game_logic import Logic

# TODO: 章节管理器：结构&章、节名称
# TODO: 故事剧情编辑器
# TODO: 常量管理器
# TODO: 对应弹窗、机制


class GameEditor(ParaController, InfoController):
    """游戏编辑器"""

    def __init__(self):
        self._app = qt.QApplication()
        self._main_window = qt.QMainWindow()
        self.set_main_window()
        super().__init__(
            self._main_window,
            self._app.primaryScreen().geometry(),
        )
        self.load_data()

    def load_data(self):
        """加载数据"""
        para = {}
        para["para_list"] = self._paras
        para["func_list"] = self._func_paras
        para["code_list"] = self._codes
        with open(
            os.path.join(Logic.PATH_DATA, Logic.FILE_CHARACTERS),
            "r",
            encoding="utf-8",
        ) as f:
            para["char_list"] = json.loads(f.read())
        with open(
            os.path.join(Logic.PATH_DATA, Logic.FILE_CHOICES),
            "r",
            encoding="utf-8",
        ) as f:
            para["choice_list"] = json.loads(f.read())
        with open(
            os.path.join(Logic.PATH_DATA, Logic.FILE_CONSTS),
            "r",
            encoding="utf-8",
        ) as f:
            para["const_list"] = json.loads(f.read())
        with open(
            os.path.join(Logic.PATH_DATA, "info.json"),
            "r",
            encoding="utf-8",
        ) as f:
            para["info"] = json.loads(f.read())
        with open(
            os.path.join(Logic.PATH_DATA, Logic.FILE_SCENES),
            "r",
            encoding="utf-8",
        ) as f:
            para["scene_list"] = json.loads(f.read())
        with open(
            os.path.join(Logic.PATH_DATA, Logic.FILE_NAMES),
            "r",
            encoding="utf-8",
        ) as f:
            para["name_list"] = json.loads(f.read())
        with open(
            os.path.join(Logic.PATH_DATA, Logic.FILE_STORYS),
            "r",
            encoding="utf-8",
        ) as f:
            para["story"] = json.loads(f.read())
        write_data(para, os.path.join(PATH_DATA, FILE_CONFIG))

    def run(self):
        """开始运行"""
        self._main_window.show()
        self._app.exec()

    def set_main_window(self):
        """初始化主窗口"""
        self._main_window.setWindowTitle("游戏编辑器")
        screen = self._app.primaryScreen().geometry()
        self._main_window.resize(
            screen.width() * 2 / 3, screen.height() * 2 / 3
        )
        self.set_menu()

    def set_menu(self):
        """设置菜单栏"""
        menu_bar = self._main_window.menuBar()
        menu_bar.setNativeMenuBar(False)
        load_chapter_btn = menu_bar.addAction("打开章")
        load_chapter_btn.triggered.connect(self.ask_chapter)
        para_open_btn = menu_bar.addAction("打开参数")
        para_open_btn.triggered.connect(self.open_para)
        para_import_btn = menu_bar.addAction("导入参数")
        para_import_btn.triggered.connect(self.import_paras)
        para_export_btn = menu_bar.addAction("导出参数")
        para_export_btn.triggered.connect(self.export_paras)

    def ask_chapter(self):
        """选择加载章节"""
        # TODO: 弹窗，章节按钮

    def load_chapter(self, index):
        """加载章节"""
        # TODO: 根据对应章数据加载章节内容并显示


if __name__ == "__main__":
    GameEditor().run()
