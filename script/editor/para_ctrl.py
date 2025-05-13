# coding = utf-8

"""参数管理器"""

import json
import os
import sys
from functools import partial

import PySide6.QtWidgets as qt

sys.path.append(".")
sys.path.append("./script")
sys.path.append("./script/game")

from editor_setting import FILE_PARAS, PATH, PATH_DATA
from utils import sort_data, write_data

from script.game.game_logic import Logic


class ParaGui:
    """参数gui"""

    def __init__(self, main_window, screen):
        """设置参数相关窗口"""
        self._para_window = qt.QMainWindow(main_window)
        self._para_window.resize(
            screen.width() * 1 / 3, screen.height() * 1 / 2
        )

        self._para_edit = qt.QDialog(main_window)

        self._id_input = qt.QLineEdit()
        self._des_input = qt.QLineEdit()
        self._name_input = qt.QLineEdit()
        self._value_input = qt.QLineEdit()

    def minium_btn(self, name):
        """生成最小按键"""
        btn = qt.QPushButton(name)
        btn.setSizePolicy(
            qt.QSizePolicy.Policy.Fixed, qt.QSizePolicy.Policy.Fixed
        )
        return btn

    def add_label(self, layout, value):
        """增加标签"""
        layout.addWidget(qt.QLabel(value))

    def edit_layout(self, name, edit, value):
        """编辑布局"""
        edit.setText(value)
        layout = qt.QHBoxLayout()
        layout.addWidget(qt.QLabel(name))
        layout.addWidget(edit)
        return layout


class ParaController(ParaGui):
    """参数管理器"""

    def __init__(self, main_window, screen):
        super().__init__(main_window, screen)
        self._paras = {}
        self._func_paras = {}
        self._codes = {}
        self.load_paras()
        self.set_para_menu()

    # region 逻辑处理
    def load_paras(self):
        """读取参数"""
        if os.path.exists(os.path.join(PATH_DATA, FILE_PARAS)):
            with open(
                os.path.join(PATH_DATA, FILE_PARAS),
                "r",
                encoding="utf-8",
            ) as f:
                para = json.loads(f.read())
                self._paras = sort_data(para["para_list"])
                self._func_paras = sort_data(para["func_list"])
                self._codes = sort_data(para["code_list"])

    def save_paras(self):
        """保存参数"""
        if not os.path.exists(PATH):
            os.mkdir(PATH)
        if not os.path.exists(PATH_DATA):
            os.mkdir(PATH_DATA)
        para = {
            "para_list": self._paras,
            "func_list": self._func_paras,
            "code_list": self._codes,
        }
        write_data(para, os.path.join(PATH_DATA, FILE_PARAS))

    def import_paras(self):
        """导入参数设置"""
        if os.path.exists(os.path.join(Logic.PATH_DATA, Logic.FILE_PARAS)):
            with open(
                os.path.join(Logic.PATH_DATA, Logic.FILE_PARAS),
                "r",
                encoding="utf-8",
            ) as f:
                para = json.loads(f.read())
            for i in para["para_list"]:
                self.set_para(i["id"], i["name"], i["default_value"])
            for i in para["func_list"]:
                self.set_func_para(i)
            for i in para["code_list"]:
                self.set_code(i["id"], i["value"])

    def export_paras(self):
        """导出参数设置"""
        para = {
            "para_list": [
                {
                    "id": t["id"],
                    "name": t["name"],
                    "default_value": t["default_value"],
                }
                for t in self._paras.values()
            ],
            "func_list": list(self._func_paras.keys()),
            "code_list": [
                {"id": k, "value": v} for k, v in self._codes.items()
            ],
        }
        write_data(para, Logic.res_path(Logic.PATH_DATA, Logic.FILE_PARAS))

    def set_para(self, para_id, para_name, para_value, para_des=""):
        """设置参数"""
        self._paras[para_id] = {
            "id": para_id.upper(),
            "name": para_name,
            "default_value": para_value,
            "description": (
                para_des
                if para_des
                else (
                    self._paras[para_id]["description"]
                    if para_id in self._paras
                    else ""
                )
            ),
        }
        self.save_paras()

    def set_func_para(self, para_id, para_des=""):
        """设置功能参数"""
        self._func_paras[para_id] = {
            "id": para_id.upper(),
            "description": (
                para_des
                if para_des
                else (
                    self._func_paras[para_id]["description"]
                    if para_id in self._func_paras
                    else ""
                )
            ),
        }
        self.save_paras()

    def set_code(self, code_id, code_value, code_des=""):
        """设置代码"""
        self._codes[code_id] = {
            "id": code_id.upper(),
            "value": code_value,
            "description": (
                code_des
                if code_des
                else (
                    self._codes[code_id]["description"]
                    if code_id in self._codes
                    else ""
                )
            ),
        }
        self.save_paras()

    def del_para(self, para_id):
        """删除参数"""
        del self._paras[para_id]
        self.save_paras()

    def del_func_para(self, para_id):
        """删除功能参数"""
        del self._func_paras[para_id]
        self.save_paras()

    def del_code(self, code_id):
        """删除代码"""
        del self._codes[code_id]
        self.save_paras()

    def get_paras(self):
        """获取参数"""
        return self._paras

    def get_para_ids(self):
        """获取参数id"""
        return list(self._paras.keys())

    # region 窗口交互
    def set_para_menu(self):
        """设置参数菜单栏"""
        menu_bar = self._para_window.menuBar()
        menu_bar.setNativeMenuBar(False)
        new_para_btn = menu_bar.addAction("新建参数")
        new_para_btn.triggered.connect(
            partial(
                self.edit_para,
                {"id": "", "name": "", "default_value": 0, "description": ""},
            )
        )
        new_func_para_btn = menu_bar.addAction("新建功能参数")
        new_func_para_btn.triggered.connect(
            partial(
                self.edit_func_para,
                {"id": "", "description": ""},
            )
        )
        new_code_btn = menu_bar.addAction("新建代码")
        new_code_btn.triggered.connect(
            partial(
                self.edit_code,
                {"id": "", "value": "0", "description": ""},
            )
        )

    def open_para(self):
        """打开参数表"""
        self.refresh_para()
        self._para_window.show()

    def refresh_para(self):
        """刷新参数表"""
        layout_main = qt.QHBoxLayout()
        layout_left = qt.QVBoxLayout()
        for v in self._paras.values():
            layout_l1 = qt.QHBoxLayout()
            self.add_label(layout_l1, v["id"])
            self.add_label(layout_l1, v["description"])
            edit_btn = self.minium_btn("编辑")
            edit_btn.clicked.connect(partial(self.edit_para, v))
            layout_l1.addWidget(edit_btn)
            layout_left.addLayout(layout_l1)

            layout_l2 = qt.QHBoxLayout()
            self.add_label(layout_l2, str(v["default_value"]))
            del_btn = self.minium_btn("删除")
            del_btn.clicked.connect(partial(self.del_para, v["id"]))
            layout_l2.addWidget(del_btn)
            layout_left.addLayout(layout_l2)
        layout_main.addLayout(layout_left)

        layout_right = qt.QVBoxLayout()
        for v in self._func_paras.values():
            layout_l1 = qt.QHBoxLayout()
            self.add_label(layout_l1, v["id"])
            edit_btn = self.minium_btn("编辑")
            edit_btn.clicked.connect(partial(self.edit_func_para, v))
            layout_l1.addWidget(edit_btn)
            layout_right.addLayout(layout_l1)
            layout_l2 = qt.QHBoxLayout()
            self.add_label(layout_l2, v["description"])
            del_btn = self.minium_btn("删除")
            del_btn.clicked.connect(partial(self.del_func_para, v["id"]))
            layout_l2.addWidget(del_btn)
            layout_right.addLayout(layout_l2)
        for v in self._codes.values():
            layout_l1 = qt.QHBoxLayout()
            self.add_label(layout_l1, v["id"])
            self.add_label(layout_l1, str(v["value"]))
            edit_btn = self.minium_btn("编辑")
            edit_btn.clicked.connect(partial(self.edit_code, v))
            layout_l1.addWidget(edit_btn)
            layout_right.addLayout(layout_l1)
            layout_l2 = qt.QHBoxLayout()
            self.add_label(layout_l2, v["description"])
            del_btn = self.minium_btn("删除")
            del_btn.clicked.connect(partial(self.del_code, v["id"]))
            layout_l2.addWidget(del_btn)
            layout_right.addLayout(layout_l2)
        layout_main.addLayout(layout_right)

        widget_main = qt.QWidget()
        widget_main.setLayout(layout_main)
        scroll = qt.QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setWidget(widget_main)
        scroll.setFrameShape(qt.QScrollArea.NoFrame)
        self._para_window.setCentralWidget(scroll)

    def edit_para(self, para_data):
        """编辑参数"""
        layout_main = qt.QVBoxLayout()
        layout_main.addLayout(
            self.edit_layout("ID", self._id_input, para_data["id"])
        )
        layout_main.addLayout(
            self.edit_layout("描述", self._des_input, para_data["description"])
        )
        layout_main.addLayout(
            self.edit_layout("名称", self._name_input, para_data["name"])
        )
        layout_main.addLayout(
            self.edit_layout(
                "默认值", self._value_input, para_data["default_value"]
            )
        )

        btn_layout = qt.QHBoxLayout()
        btn = qt.QPushButton("确认")
        btn.clicked.connect(self.change_para)
        btn_layout.addWidget(btn)
        layout_main.addLayout(btn_layout)

        self._para_edit.setLayout(layout_main)
        self._para_edit.show()

    def change_para(self):
        """修改参数"""
        self.set_para(
            self._id_input.text(),
            self._name_input.text(),
            int(self._value_input.text()),
            self._des_input.text(),
        )
        self._para_edit.close()
        self.refresh_para()

    def edit_func_para(self, para_data):
        """编辑功能参数"""
        layout_main = qt.QVBoxLayout()
        layout_main.addLayout(
            self.edit_layout("ID", self._id_input, para_data["id"])
        )
        layout_main.addLayout(
            self.edit_layout("描述", self._des_input, para_data["description"])
        )

        btn_layout = qt.QHBoxLayout()
        btn = qt.QPushButton("确认")
        btn.clicked.connect(self.change_func_para)
        btn_layout.addWidget(btn)
        layout_main.addLayout(btn_layout)

        self._para_edit.setLayout(layout_main)
        self._para_edit.show()

    def change_func_para(self):
        """修改功能参数"""
        self.set_func_para(
            self._id_input.text(),
            self._des_input.text(),
        )
        self._para_edit.close()
        self.refresh_para()

    def edit_code(self, para_data):
        """编辑代码"""
        layout_main = qt.QVBoxLayout()
        layout_main.addLayout(
            self.edit_layout("ID", self._id_input, para_data["id"])
        )
        layout_main.addLayout(
            self.edit_layout("描述", self._des_input, para_data["description"])
        )
        layout_main.addLayout(
            self.edit_layout("值", self._value_input.text, para_data["value"])
        )

        btn_layout = qt.QHBoxLayout()
        btn = qt.QPushButton("确认")
        btn.clicked.connect(self.change_code)
        btn_layout.addWidget(btn)
        layout_main.addLayout(btn_layout)

        self._para_edit.setLayout(layout_main)
        self._para_edit.show()

    def change_code(self):
        """修改代码"""
        self.set_code(
            self._id_input.text(),
            int(self._value_input.text()),
            self._des_input.text(),
        )
        self._para_edit.close()
        self.refresh_para()
