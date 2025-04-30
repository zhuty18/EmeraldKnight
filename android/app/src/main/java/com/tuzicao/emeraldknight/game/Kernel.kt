package com.tuzicao.emeraldknight.game

import android.content.Context
import org.json.JSONObject
import java.util.LinkedList


class Kernel(context: Context) {

    companion object {
        const val MAX_SAVE = 100

        fun getSceneName(id: String): String {
            return GameLogic.getSceneName(id)
        }
    }

    private var paraMap: HashMap<String, Int> = HashMap()

    init {
        GameLogic.initData(context, this)
    }

    fun getPara(paraId: String): Int {
        return 0
    }

    fun setPara(para_id: String, value: Int) {

    }

    fun checkIs(toCheck: JSONObject): Boolean {
        return true
    }

    fun changeAs(action: JSONObject) {
        val act: String = action.getString("change")
        if (act == "CONDITION") {
            if (checkIs(action.getJSONObject("para"))) {
                val change = action.getJSONArray("value")
                for (i in 0 until change.length()) {
                    changeAs(change.getJSONObject(i))
                }
            }
        } else {
            var value = action.get("value")
            if (value is String) {
                value = GameLogic.defaultCodes[action.getString("value")]!!
            } else if (value !is Int) {
                value = 0
            }
            val paraName: String = action.getString("para")
            when (action.getString("change")) {
                "ADD" -> setPara(paraName, getPara(paraName) + value)
                "SET" -> setPara(paraName, value)
            }
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
