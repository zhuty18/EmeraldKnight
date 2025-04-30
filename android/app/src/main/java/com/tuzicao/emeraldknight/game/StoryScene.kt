package com.tuzicao.emeraldknight.game

import org.json.JSONObject
import java.util.LinkedList


class StoryScene(data: JSONObject) : Scene(data) {
    private val scene: String? = if (data.has("scene")) data.getString("scene") else null
    private val options: LinkedList<String> =
        LinkedList(List(data.getJSONArray("options").length()) {
            data.getJSONArray("options").getString(it)
        })
    private val require: JSONObject? =
        if (data.has("require")) data.getJSONObject("require") else null

    override fun getText(): String {
        var sceneText = GameLogic.getSceneText(scene ?: id)
        if (id.contains("end")) {
            sceneText += GameLogic.getStoryEnd() + GameLogic.getEndName(id)
        }
        sceneText = "    $sceneText"
        sceneText = sceneText.replace("\n", "\n    ")
        return sceneText
    }

    override fun getOptions(
        optionList: LinkedList<String>?,
        choices: LinkedList<Choice>?
    ): LinkedList<Choice> {
        require?.let {
            if (GameLogic.gameKernel.checkIs(require)) {
                val matchOption = LinkedList(List(require.getJSONArray("options").length()) {
                    require.getJSONArray("options").getString(it)
                })
                return super.getOptions(matchOption, null)
            }
        }
        return super.getOptions(options, null)
    }

}