package com.tuzicao.emeraldknight.game.battle

import org.json.JSONObject
import java.util.HashMap
import java.util.Random

abstract class Enemy(data: JSONObject) : Character(data) {
    private fun needHeal(action: Heal): Boolean {
        action.first?.let {
            if (action.used == 0) {
                return life < it
            }
        }
        action.condition?.let {
            return life < it
        }
        return false
    }

    override fun takeAct(target: Character?): String {
        val chanceList = mutableListOf<Pair<Double, Action>>()
        for (act in actions) {
            if (act is Heal && needHeal(act) && act.isAvailable()) {
                return act.execute()
            }
            act.chance?.let {
                chanceList.add(it to act)
            }
        }
        var dice: Double = Random().nextDouble() * chanceList.sumOf { it.first }
        for ((c, a) in chanceList) {
            dice -= c
            if (dice <= 0) {
                return a.execute(target)
            }
        }

        return ""
    }
}