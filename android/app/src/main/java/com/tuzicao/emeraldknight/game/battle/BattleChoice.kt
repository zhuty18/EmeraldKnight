package com.tuzicao.emeraldknight.game.battle

import com.tuzicao.emeraldknight.game.Choice

class BattleChoice(private val battleScene: BattleScene, private val move: Action) : Choice("BattleChoice") {

    override fun getText(): String = move.name!!
    override fun isShow(): Boolean = move.isAvailable()
    override fun beChosen() {
        battleScene.hero.setText(
            move.execute(battleScene.enemy)
        )
        battleScene.nextRound()
    }
}