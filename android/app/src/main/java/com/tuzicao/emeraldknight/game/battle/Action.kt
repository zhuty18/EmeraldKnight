package com.tuzicao.emeraldknight.game.battle

import com.tuzicao.emeraldknight.game.ActionType
import com.tuzicao.emeraldknight.game.GameLogic
import org.json.JSONObject

abstract class Action(data: JSONObject, val owner: Character) {
    companion object {
        fun build(data: JSONObject, owner: Character): Action {
            val type = ActionType.valueOf(data.getString("type"))
            return when (type) {
                ActionType.ATTACK -> Attack(data, owner)
                ActionType.HEAL -> Heal(data, owner)
                ActionType.CHEAT -> Cheat(data, owner)
            }
        }
    }

    val id: String = data.getString("id")
    val text: String = data.getString("text")

    val show: JSONObject? = if (data.has("show")) data.getJSONObject("show") else null
    val name: String? = if (data.has("name")) data.getString("name") else null
    val condition: Int? =
        if (data.has("condition")) data.getInt("condition") else null
    val first: Int? = if (data.has("first")) data.getInt("first") else null
    val chance: Double? = if (data.has("chance")) data.getDouble("chance") else null

    abstract fun execute(target: Character? = null): String

    open fun isAvailable(): Boolean {
        return show?.let {
            GameLogic.gameKernel.checkIs(show)
        } ?: true
    }
}