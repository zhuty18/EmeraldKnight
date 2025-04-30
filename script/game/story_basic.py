# coding = utf-8

"""基本故事类"""

from abc import abstractmethod

from game_logic import Logic
from logic_basic import BasicLogic


class Choice(BasicLogic):
    """选项"""

    @classmethod
    def get_existence(cls, para_1=None, para_2=None):
        """
        获取选项实例

        参数:
            para_1: 选项id
            para_2: None
        """
        return super().get_existence(para_1, para_2)

    @abstractmethod
    def text(self):
        """选项文本"""

    @abstractmethod
    def show(self):
        """是否显示"""

    @abstractmethod
    def choose(self):
        """选择"""


class StoryChoice(Choice):
    """故事选项"""

    def __init__(self, data):
        self._id = data["id"]
        self._target = data["target"]
        self._text = (
            data["text"]
            if "text" in data
            else Logic.get_scene_name(self._target)
        )

        self._show = data["show"] if "show" in data else None
        self._choose = data["choose"] if "choose" in data else None

    def text(self):
        return self._text

    def show(self):
        if not self._show:
            return True
        return Logic.get_kernel().check_is(
            self._show["op"], self._show["condition"]
        )

    def choose(self):
        if self._choose:
            for action in self._choose:
                Logic.get_kernel().change_para(action)
        Logic.get_kernel().to_scene(self._target)


def get_story_choice(choice_id, _):
    """获取故事选项"""
    return StoryChoice(Logic.CHOICE_MAP[choice_id])


Choice.add_get_functions(get_story_choice)


class Scene(BasicLogic):
    """场景基类"""

    @classmethod
    def get_existence(cls, para_1=None, para_2=None):
        """
        获取场景实例

        参数:
            para_1: 场景id
            para_2: None
        """
        return super().get_existence(para_1, para_2)

    @abstractmethod
    def get_text(self):
        """获取文本"""

    def get_options(self, options=None, choices=None):
        """获取选项"""
        if not choices:
            choices = [Choice.get_existence(x) for x in options]
        res = []
        for c in choices:
            if c.show():
                res.append(c)
        return res


class StoryScene(Scene):
    """故事场景"""

    def __init__(self, data):
        self._id = data["id"]
        self._scene = data["scene"] if "scene" in data else None
        self._options = data["options"]
        self._require = data["require"] if "require" in data else None

    def get_text(self):
        s_id = self._scene if self._scene else self._id
        scene_text = Logic.get_scene_text(s_id)
        if "end" in self._id:
            scene_text += Logic.STORY_END + Logic.get_end_name(self._id)
        scene_text = "    " + scene_text
        scene_text = scene_text.replace("\n", "\n    ")
        return scene_text

    def get_options(self, options=None, choices=None):
        option_list = self._options
        if self._require:
            if Logic.get_kernel().check_is(self._require):
                option_list = self._require["match_options"]
        return super().get_options(options=option_list)


def get_story_scene(scene_id, _):
    """获取故事场景"""
    if "end" in str(scene_id):
        Logic.mark_end(scene_id)
        return StoryScene(
            {
                "id": scene_id,
                "options": Logic.SCENE_MAP[Logic.START_OVER]["options"],
            }
        )
    return StoryScene(Logic.SCENE_MAP[scene_id])


Scene.add_get_functions(get_story_scene)
