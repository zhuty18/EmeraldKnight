package com.tuzicao.emeraldknight.game.battle

import org.json.JSONObject

class Cheat(data: JSONObject, owner: Character) : Action(data, owner) {
    override fun execute(target: Character?): String {
        target!!.hurt(target.life)
        return text
    }
}