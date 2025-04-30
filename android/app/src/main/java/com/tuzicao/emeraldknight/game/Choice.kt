package com.tuzicao.emeraldknight.game

import org.json.JSONObject

abstract class Choice(private val id: String, data: JSONObject) {

    companion object {
        fun getById(choiceId: String): Choice {
            return StoryChoice(choiceId, GameLogic.choiceMap[choiceId]!!)
        }
    }

    fun getId(): String = id

    open fun getText(): String = ""

    open fun isShow(): Boolean = true

    open fun beChosen() {}
}

