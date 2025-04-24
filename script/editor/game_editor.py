# coding = utf-8

"""游戏编辑器"""

# from functools import partial

# import PySide6.QtCore as core
# import PySide6.QtGui as gui
import PySide6.QtWidgets as qt
from para_ctrl import ParameterController


class GameEditor:
    """游戏编辑器"""

    def __init__(self):
        self._para_ctrl = ParameterController()
        self._app = qt.QApplication()
        self._main_window = qt.QMainWindow()
        self.set_main_window()
        self._para_window = qt.QMainWindow(self._main_window)

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
        self.set_menu_bar()

    def set_menu_bar(self):
        """设置菜单栏"""
        menu_bar = self._main_window.menuBar()
        menu_bar.setNativeMenuBar(False)
        paras_btn = menu_bar.addAction("打开参数")
        paras_btn.triggered.connect(self.open_paras)
        paras_export_btn = menu_bar.addAction("导出参数")
        paras_export_btn.triggered.connect(self._para_ctrl.export_paras)

    def open_paras(self):
        """打开参数表"""
        self.refresh_para_window()
        self._para_window.show()

    def refresh_para_window(self):
        """刷新参数表"""
        main_layout = qt.QVBoxLayout()
        para = self._para_ctrl.get_paras()
        for _, v in para.items():
            layout_1 = qt.QHBoxLayout()
            layout_1.addWidget(qt.QLabel(v["id"]))
            layout_1.addWidget(qt.QLabel(v["description"]))
            btn_1 = qt.QPushButton("编辑")
            btn_1.minimumSize()
            layout_1.addWidget(btn_1)
            main_layout.addLayout(layout_1)
            layout_2 = qt.QHBoxLayout()
            layout_2.addWidget(qt.QLabel(v["name"]))
            layout_2.addWidget(qt.QLabel(str(v["default_value"])))
            btn_2 = qt.QPushButton("删除")
            btn_2.minimumSize()
            layout_2.addWidget(btn_2)
            main_layout.addLayout(layout_2)
        widget = qt.QWidget()
        widget.setLayout(main_layout)
        scroll = qt.QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setWidget(widget)
        scroll.setFrameShape(qt.QScrollArea.NoFrame)
        self._para_window.setCentralWidget(scroll)


if __name__ == "__main__":
    GameEditor().run()
