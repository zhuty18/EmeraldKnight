package com.tuzicao.emeraldknight.game.battle

import com.tuzicao.emeraldknight.game.CharacterType
import com.tuzicao.emeraldknight.game.EnemyId
import com.tuzicao.emeraldknight.game.GameLogic
import com.tuzicao.emeraldknight.game.HeroId
import org.json.JSONObject
import java.util.LinkedList
import kotlin.math.max
import kotlin.math.min

abstract class Character(data: JSONObject) {
    companion object {
        fun getById(characterId: String): Character {
            val data: JSONObject = GameLogic.characterMap[characterId]!!
            val type = CharacterType.valueOf(data.getString("type"))
            return when (type) {
                CharacterType.HERO -> when (HeroId.valueOf(data.getString("id"))) {
                    HeroId.HAL -> Hal(data)
                }

                CharacterType.ENEMY -> when (EnemyId.valueOf(data.getString("id"))) {
                    EnemyId.SINESTRO -> Sinestro(data)
                }
            }
        }
    }

    val id = data.getString("id")
    val name: String = data.getString("name")
    abstract val attack: Int
    abstract val speed: Int
    abstract val lifeMax: Int
    var life: Int = 0
    val actions: LinkedList<Action> = LinkedList(List(data.getJSONArray("actions").length()) {
        Action.build(data.getJSONArray("actions").getJSONObject(it), this)
    })
    var record: String = ""

    fun set() {
        life = lifeMax
    }

    open fun takeAct(target: Character? = null) = record

    fun hurt(damage: Int) {
        life = max(life - damage, 0)
    }

    fun heal(heal: Int) {
        life = min(life + heal, lifeMax)
    }

    fun isDead(): Boolean = (life == 0)

    fun setText(msg: String) {
        record = msg
    }

}