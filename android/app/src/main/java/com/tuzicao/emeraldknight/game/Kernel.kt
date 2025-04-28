package com.tuzicao.emeraldknight.game

import java.util.LinkedList


class Kernel {

    companion object {
        const val MaxSave = 100
        const val MaxEnd = 21


        fun getSceneName(id: String): String {
            return ""
        }
    }

    fun isOn(): Boolean {
        return true
    }

    fun save(save_id: Int) {}

    fun new() {}
    fun load(save_id: Int) {}
    fun getSceneText(): String {
        return ""
    }

    fun getChoices(): LinkedList<Choice> {
        return LinkedList()
    }

    fun inBattle(): Boolean = true
    fun getScene(): String = ""
    fun loadEnd(end_id: Int) {}

}
