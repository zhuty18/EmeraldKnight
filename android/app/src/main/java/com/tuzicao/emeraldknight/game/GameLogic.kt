package com.tuzicao.emeraldknight.game

import android.content.Context
import org.json.JSONArray
import org.json.JSONObject

class GameLogic {
    companion object {
        lateinit var ChoiceMap: HashMap<String, JSONObject>
        fun readJSON(context: Context, fileName: String): String {
            return context.assets.open(fileName).bufferedReader().use { it.readText() }
        }

        fun init(context: Context) {
            val choices = JSONArray(readJSON(context, "choices.json"))
            for (i in 0 until choices.length()) {
                val item = choices.getJSONObject(i)
                GameLogic.ChoiceMap[item.getString("id")] = item
            }
        }

        fun getSceneText(context: Context, sceneID: String): String {
            val sceneTexts = JSONArray(readJSON(context, "scene_text.json"))
            for (i in 0 until sceneTexts.length()) {
                val item = sceneTexts.getJSONObject(i)
                if (item.getString("id").equals(sceneID)) {
                    return item.getString("text")
                }
            }
            return ""
        }
    }
}