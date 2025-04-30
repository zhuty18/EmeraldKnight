package com.tuzicao.emeraldknight.game

import org.json.JSONArray
import org.json.JSONObject

class StoryChoice(data: JSONObject) : Choice(data) {
    private val target: String = data.getString("target")
    private val text: String =
        if (data.has("text")) data.getString("text") else GameLogic.getSceneName(target)
    private val show: JSONObject? = if (data.has("show")) data.getJSONObject("show") else null
    private val choose: JSONArray? = if (data.has("choose")) data.getJSONArray("choose") else null

    override fun getText(): String = text
    override fun isShow(): Boolean {
        return show?.let {
            GameLogic.gameKernel.checkIs(show)
        } ?: true
    }

    override fun beChosen() {
        choose?.let {
            for (i in 0 until choose.length()) {
                GameLogic.gameKernel.changeAs(choose.getJSONObject(i))
            }
        }
        GameLogic.gameKernel.toScene(target)
    }
}