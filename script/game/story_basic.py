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
        self._text = data.get("text") or Logic.get_scene_name(self._target)

        self._show = data.get("show")
        self._choose = data.get("choose")

    def text(self):
        return self._text

    def show(self):
        if not self._show:
            return True
        return Logic.get_kernel().check_is(self._show)

    def choose(self):
        kernel = Logic.get_kernel()
        if self._choose:
            for action in self._choose:
                kernel.change_para(action)
        kernel.to_scene(self._target)


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
            choices = [Choice.get_existence(x) for x in (options or [])]
        return [c for c in choices if c.show()]


class StoryScene(Scene):
    """故事场景"""

    def __init__(self, data):
        self._id = data["id"]
        self._options = data["options"]
        self._require = data.get("require")

    def get_text(self):
        scene_text = Logic.get_scene_text(self._id)
        if not scene_text:
            scene_text = ""
        if self._id.startswith(Logic.END_MARK):
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
    if str(scene_id).startswith(Logic.END_MARK):
        Logic.mark_end(scene_id)
        return StoryScene(
            {
                "id": scene_id,
                "options": Logic.SCENE_MAP[Logic.START_OVER]["options"],
            }
        )
    return StoryScene(Logic.SCENE_MAP[scene_id])


Scene.add_get_functions(get_story_scene)
