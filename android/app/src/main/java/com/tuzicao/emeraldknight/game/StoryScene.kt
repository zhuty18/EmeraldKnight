package com.tuzicao.emeraldknight.game

import org.json.JSONObject
import java.util.LinkedList


class StoryScene(data: JSONObject) : Scene(data) {
    private val options: LinkedList<String> =
        LinkedList(List(data.getJSONArray("options").length()) {
            data.getJSONArray("options").getString(it)
        })
    private val require: JSONObject? =
        if (data.has("require")) data.getJSONObject("require") else null

    override fun getText(): String {
        var sceneText = GameLogic.getSceneText(id)
        if (id.contains("end")) {
            sceneText += GameLogic.getStoryEnd() + GameLogic.getEndName(id)
        }
        return sceneText
    }

    override fun getOptions(
        optionList: LinkedList<String>?,
        choices: LinkedList<Choice>?
    ): LinkedList<Choice> {
        require?.let {
            if (GameLogic.gameKernel.checkIs(require)) {
                val matchOption = LinkedList(List(require.getJSONArray("match_options").length()) {
                    require.getJSONArray("match_options").getString(it)
                })
                return super.getOptions(matchOption, null)
            }
        }
        return super.getOptions(options, null)
    }

}