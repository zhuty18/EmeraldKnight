package com.tuzicao.emeraldknight.game.battle

import com.tuzicao.emeraldknight.game.GameLogic
import org.json.JSONObject

class Sinestro(data: JSONObject) : Enemy(data) {
    override val attack: Int = 100 - GameLogic.gameKernel.getPara("SINESTRO_LOVE") * 5
    override val speed: Int = 100 - GameLogic.gameKernel.getPara("SINESTRO_TAME") * 2
    override val lifeMax: Int = data.getInt("max_life")

    init {
        set()
    }
}