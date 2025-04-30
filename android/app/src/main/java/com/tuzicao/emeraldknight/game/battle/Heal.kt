package com.tuzicao.emeraldknight.game.battle

import com.tuzicao.emeraldknight.game.GameLogic
import org.json.JSONObject
import java.util.Random

class Heal(data: JSONObject, owner: Character) : Action(data, owner) {
    val healMin: Int = data.getInt("min")
    val healMax: Int = data.getInt("max")
    val time: Int = data.getInt("time")
    var used = 0

    override fun execute(target: Character?): String {
        used += 1
        val healValue: Int = healMin + (Random().nextDouble() * (healMax - healMin)).toInt()
        owner.heal(healValue)
        return text + GameLogic.getBattleOf("Heal")
            .replace(GameLogic.getBattleOf("BLANK"), healValue.toString())
    }

    override fun isAvailable(): Boolean = used < time

}