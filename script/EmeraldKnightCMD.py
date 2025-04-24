# coding = utf-8

"""翡翠骑士游戏 v2 命令行版本"""

import os
import sys

sys.path.append("./script")
sys.path.append("./script/game")

from game.emerald_knight import EmeraldKnight, Logic
from game.version import GAME_INFO


class EmeraldKnightCMD(EmeraldKnight):
    """命令行游戏"""

    def run(self):
        """运行游戏"""
        self.hello_page()

    def load_scene(self):
        """加载场景"""
        if self._kernel.get_scene_id() == Logic.START_OVER:
            self.hello_page()
            return
        scene_text = self._kernel.get_scene_text()
        choices = self._kernel.get_choices()
        print(scene_text)
        for index, c in enumerate(choices):
            print(f"{chr(index+ord('A'))}\t{c.text()}")
        while True:
            s = input().capitalize()
            try:
                t = ord(s[0]) - ord("A")
                if t >= 0 and t < len(choices):
                    # self.choose(choices[t])
                    choices[t].chosen()
                    break
                elif s == "S":
                    self.save_game()
                    break
                elif s == "L":
                    self.load_game()
                    break
                elif s == "Q":
                    self._kernel.print_debug()
                    quit()
                else:
                    raise TypeError
            except TypeError:
                print("请重新输入！")

    def hello_page(self):
        """开始页"""
        print("感谢你打开这个游戏！")
        print("=======================")
        print(f"{GAME_INFO["name"]}\n{GAME_INFO["name_en"]}")
        print("v" + Logic.VERSION)
        print()
        print(f"作者：{GAME_INFO["author"]}")
        print("-----------------------")
        for i in GAME_INFO["poem"]:
            print("\t".join(i))
        print("=======================")
        print()
        print("N\t新的游戏")
        print("L\t载入存档")
        print("Q\t退出游戏")
        print("\n（不区分大小写）")

        while True:
            t = input().capitalize()
            if t == "N":
                self.new_game()
                break
            elif t == "L":
                self.load_game()
                break
            elif t == "Q":
                break
            else:
                print("请重新输入")

    def new_game(self):
        """开始新游戏"""
        self.load_at(0)

    def load_at(self, save_id, _=None):
        """从存档加载游戏"""
        if save_id != 0 and Logic.get_save_info(save_id) == Logic.EMPTY_SAVE:
            print("存档不存在！")
            return
        self._kernel.load_at(save_id)
        while True:
            self.load_scene()

    def show_save(self, _=True):
        """显示存档"""
        has_save = False
        for i in range(30):
            if Logic.get_save_info(i + 1) != Logic.EMPTY_SAVE:
                print(
                    f"存档{i+1}\t{Logic.get_save_info(i+1).replace("\n","\t")}"
                )
                has_save = True
        return has_save

    def load_game(self):
        """读档"""
        has_save = self.show_save()
        if not has_save:
            print("没有存档！")
            print("N\t新的游戏\nB\t返回\nQ\t退出游戏\n")
            while True:
                t = input().capitalize()
                if t == "N":
                    self.new_game()
                    break
                elif t == "B":
                    if self._kernel.get_scene_id() == Logic.START_OVER:
                        self.hello_page()
                    else:
                        self.load_scene()
                    break
                elif t == "Q":
                    quit()
                else:
                    print("请重新输入！")
        else:
            print()
            s = int(input("你要载入的存档编号为："))
            while True:
                if os.path.exists(Logic.res_path(Logic.PATH_SAVE, f"{s}.eks")):
                    self.load_at(s)
                    break
                else:
                    print("存档不存在，请重新选择！")
                    s = int(input())

    def save_game(self):
        """保存游戏"""
        has_save = self.show_save()
        if has_save:
            print("\n以上是你的存档\n")
        print("请输入一个[1,30]内的整数来保存当前进度，输入B返回")
        while True:
            try:
                s = input().capitalize()
                if s == "B":
                    break
                index = int(s)
                if index > 0 and index <= 30:
                    self.save_at(index)
                    print("保存成功！")
                    break
                else:
                    raise TypeError
            except TypeError:
                print("请重新输入！")


if __name__ == "__main__":
    ek = EmeraldKnightCMD()
    ek.run()
