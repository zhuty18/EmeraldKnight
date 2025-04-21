# coding = utf-8

"""翡翠骑士游戏 v2 可运行基类"""

from game_kernel import Kernel
from game_logic import Logic


class EmeraldKnight:
    """游戏基类"""

    def __init__(self):
        self.gk = Kernel()

    def run(self):
        """运行游戏"""
        self.hello_page()

    def load_scene(self):
        """加载场景"""

    def hello_page(self):
        """开始页"""

    def new_game(self):
        """开始新游戏"""
        self.load_at(0)

    def load_at(self, save_id, _=None):
        """从存档加载游戏"""
        self.gk.load_at(save_id)
        self.load_scene()

    def save_at(self, save_id, _=None):
        """保存游戏"""
        self.gk.save_at(save_id)

    def choose(self, choice):
        """选择选项"""
        choice.chosen()
        self.load_scene()

    def show_save(self, _=True):
        """显示存档界面"""

    def save_game(self):
        """存档"""
        if (
            self.gk.get_scene_id() != Logic.START_OVER
            and self.gk.get_scene_id() != Logic.FINAL_BATTLE
        ):
            self.show_save()

    def load_game(self):
        """读档"""
        self.show_save(False)

    def debug_game(self):
        """调试"""
        self.gk.print_debug()

    def exit_game(self):
        """退出游戏"""

    def about_game(self):
        """介绍页"""

    def get_scene_id(self):
        return self.gk.get_scene_id()

    def get_paras(self):
        return self.gk.get_paras()

    def get_choices(self):
        return


if __name__ == "__main__":
    ek = EmeraldKnight()
    ek.run()
