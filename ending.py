from abstract import choice_abstract, scene_abstract


class end_choice(choice_abstract):
    def text(self):
        return "战斗结束了"


class fail_choice(end_choice):
    target = ""


class end_16(end_choice):
    target = "end-16"

    def chosen(self):
        print("chosen " + self.target)
        return super().chosen()


class end_scene(scene_abstract):
    options = [end_choice]
