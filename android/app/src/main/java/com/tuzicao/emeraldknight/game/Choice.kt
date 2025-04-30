package com.tuzicao.emeraldknight.game

import org.json.JSONObject


abstract class Choice(data: JSONObject) {

    companion object {
        fun getById(choiceId: String): Choice {
            return StoryChoice(GameLogic.choiceMap[choiceId]!!)
        }
    }

    val id: String = data.getString("id")

    open fun getText(): String = ""

    open fun isShow(): Boolean = true

    open fun beChosen() {}
}

