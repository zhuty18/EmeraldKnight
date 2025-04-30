package com.tuzicao.emeraldknight.game.battle

import com.tuzicao.emeraldknight.game.Choice
import com.tuzicao.emeraldknight.game.GameLogic
import com.tuzicao.emeraldknight.game.Scene
import org.json.JSONObject
import java.util.LinkedList

class BattleScene(data: JSONObject) : Scene(data) {
    private var round: Int = 0
    val enemy: Character = Character.getById(GameLogic.getBattleOf("ENEMY"))
    val hero: Character = Character.getById(GameLogic.getBattleOf("HERO"))
    private val optionLose: LinkedList<String> =
        LinkedList(List(data.getJSONArray("options_lose").length()) {
            data.getJSONArray("options_lose").getString(it)
        })
    private val optionWin: LinkedList<String> =
        LinkedList(List(data.getJSONArray("options_win").length()) {
            data.getJSONArray("options_win").getString(it)
        })

    private fun getBattleStatus(): String {
        var battleText = "${enemy.name}\n"
        battleText += "HP: ${enemy.life} / ${enemy.lifeMax}\n\n"
        val s = "HP: ${hero.life} / ${hero.lifeMax}"
        battleText += "${" ".repeat(46)}${hero.name}\n"
        battleText += "${" ".repeat(48 - s.length)}$s\n"
        battleText += "\n\n"
        return battleText
    }

    override fun getText(): String {
        return if (round == 0) {
            getBattleStatus() + GameLogic.getBattleOf("START")
        } else {
            var message = hero.takeAct()
            if (enemy.isDead()) {
                getBattleStatus() + message + GameLogic.getBattleOf("WIN")
            }
            message += enemy.takeAct(hero)
            if (hero.isDead()) {
                getBattleStatus() + message + GameLogic.getBattleOf("LOSE")
            }
            getBattleStatus() + message
        }
    }

    override fun getOptions(
        optionList: LinkedList<String>?,
        choices: LinkedList<Choice>?
    ): LinkedList<Choice> {
        return if (enemy.isDead()) {
            super.getOptions(optionWin, null)
        } else if (hero.isDead()) {
            super.getOptions(optionLose, null)
        } else {
            super.getOptions(
                null,
                LinkedList(List(hero.actions.size) { BattleChoice(this, hero.actions[it]) })
            )
        }
    }

    fun nextRound() {
        round += 1
    }
}