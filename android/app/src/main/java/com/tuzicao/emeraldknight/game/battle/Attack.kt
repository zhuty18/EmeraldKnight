package com.tuzicao.emeraldknight.game.battle

import com.tuzicao.emeraldknight.game.GameLogic
import org.json.JSONObject
import java.util.Random

class Attack(data: JSONObject, owner: Character) : Action(data, owner) {
    val strength: Double = data.getDouble("strength")
    val selfHurt: JSONObject? = if (data.has("self_hurt")) data.getJSONObject("self_hurt") else null

    override fun execute(target: Character?): String {
        var exe_text = text
        selfHurt?.let {
            val selfHurtValue: Int =
                (Random().nextDouble() * (selfHurt.getInt("max") - selfHurt.getInt("min"))).toInt() + selfHurt.getInt(
                    "min"
                )
            owner.hurt(selfHurtValue)
            exe_text += selfHurt.getString("text")
                .replace(GameLogic.getBattleOf("BLANK"), selfHurtValue.toString())
        }
        val dodge: Int = 50 + owner.speed - target!!.speed
        if (Random().nextDouble() * 500 < dodge) {
            exe_text += GameLogic.getBattleOf("DODGE")
        } else {
            val damage: Int =
                (owner.attack * (0.8 + 0.4 * Random().nextDouble()) * strength).toInt()
            target.hurt(damage)
            exe_text += GameLogic.getBattleOf("HURT")
                .replace(GameLogic.getBattleOf("BLANK"), damage.toString())
        }
        return exe_text
    }
}