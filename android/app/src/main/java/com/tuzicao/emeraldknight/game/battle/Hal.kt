package com.tuzicao.emeraldknight.game.battle

import com.tuzicao.emeraldknight.game.GameLogic
import org.json.JSONObject

class Hal(data: JSONObject) : Hero(data) {
    override val attack: Int =
        100 + GameLogic.gameKernel.getPara("BRUCE_LOVE") * 2 + GameLogic.gameKernel.getPara("INTELLIGENCE") * 2 + GameLogic.gameKernel.getPara(
            "DRAGON_EGG"
        ) * 10
    override val speed: Int =
        100 + GameLogic.gameKernel.getPara("KNOWLEDGE") + GameLogic.gameKernel.getPara("PEGASUS") * 20
    override val lifeMax: Int =
        100 + GameLogic.gameKernel.getPara("OLIVER_LOVE") * 10 + GameLogic.gameKernel.getPara("BARRY_LOVE") * 10

    init {
        set()
    }
}