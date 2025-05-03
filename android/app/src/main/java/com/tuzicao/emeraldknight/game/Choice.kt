package com.tuzicao.emeraldknight.game

import org.json.JSONObject


abstract class Choice(val id: String) {

    companion object {
        fun getById(choiceId: String): Choice {
            return StoryChoice(GameLogic.choiceMap[choiceId]!!)
        }
    }

    abstract fun getText(): String

    abstract fun isShow(): Boolean

    abstract fun beChosen()
}

