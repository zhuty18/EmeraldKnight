package com.tuzicao.emeraldknight.game

import android.annotation.SuppressLint
import android.content.Context
import org.json.JSONArray
import org.json.JSONObject
import java.io.File

class GameLogic {
    companion object {
        var defaultParas: HashMap<String, JSONObject> = HashMap()
        var defaultFuncs: HashMap<String, String> = HashMap()
        var defaultCodes: HashMap<String, Int> = HashMap()
        var constMap: HashMap<String, String> = HashMap()

        var choiceMap: HashMap<String, JSONObject> = HashMap()
        var sceneMap: HashMap<String, JSONObject> = HashMap()
        var endNameMap: HashMap<String, String> = HashMap()
        var chapterNameMap: HashMap<String, String> = HashMap()

        var characterMap: HashMap<String, JSONObject> = HashMap()

        lateinit var battleStory: JSONObject
        lateinit var endChoice: JSONObject
        lateinit var endScene: JSONObject

        @SuppressLint("StaticFieldLeak")
        lateinit var gameKernel: Kernel

        private fun <V> loadData(
            array: JSONArray,
            map: HashMap<String, V>,
            extractor: (JSONObject) -> V
        ) {
            for (i in 0 until array.length()) {
                val item = array.getJSONObject(i)
                val key = item.getString("id")
                map[key] = extractor(item)
            }
        }

        private fun loadIdValue(array: JSONArray, map: HashMap<String, String>) {
            for (i in 0 until array.length()) {
                val item = array.getJSONObject(i)
                map[item.getString("id")] = item.getString("value")
            }
        }

        fun initData(context: Context, kernel: Kernel) {
            gameKernel = kernel

            val consts = JSONArray(readJSON(context, "consts.json"))
            for (i in 0 until consts.length()) {
                val item = consts.getJSONObject(i)
                val id = item.getString("id")
                val value = item.get("value")
                if (value is String) {
                    constMap[id] = value
                } else {
                    val ob = value as JSONObject
                    when (id) {
                        "END_CHOICE" -> endChoice = ob
                        "END_SCENE" -> endScene = ob
                        "BATTLE_STORY" -> battleStory = ob
                    }
                }
            }

            val paras = JSONObject(readJSON(context, "paras.json"))
            loadData(paras.getJSONArray("para_list"), defaultParas) { it }
            loadData(paras.getJSONArray("code_list"), defaultCodes) { it.getInt("value") }
            loadData(paras.getJSONArray("func_list"), defaultFuncs) { it.getString("value") }

            loadData(JSONArray(readJSON(context, "choices.json")), choiceMap) { it }
            choiceMap[endChoice.getString("id")] = endChoice
            loadData(JSONArray(readJSON(context, "scenes.json")), sceneMap) { it }
            sceneMap[endScene.getString("id")] = endScene


            val names = JSONObject(readJSON(context, "names.json"))
            val endNames = names.getJSONArray("end_names")
            for (i in 0 until endNames.length()) {
                val item = endNames.getJSONObject(i)
                endNameMap[item.getString("id")] = item.getString("value")
            }
            val chapterNames = names.getJSONArray("chapter_names")
            for (i in 0 until chapterNames.length()) {
                val item = chapterNames.getJSONObject(i)
                chapterNameMap[item.getString("id")] = item.getString("value")
            }

            val characters = JSONArray(readJSON(context, "characters.json"))
            for (i in 0 until characters.length()) {
                val item = characters.getJSONObject(i)
            }

            val file = File(context.filesDir, "0.eks")
            if (!file.exists()) {
                file.writeText("{}")
            }
        }

        fun readJSON(context: Context, fileName: String): String {
            return context.assets.open(fileName).bufferedReader().use { it.readText() }
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

        fun getSceneName(sceneID: String): String {
            return sceneMap[sceneID]!!.getString("name")
        }

        fun getStartScene(): String = constMap["START_SCENE"]!!
        fun getStartOver(): String = constMap["START_OVER"]!!
        fun getFinalBattle(): String = constMap["FINAL_BATTLE"]!!
        fun getEmptySave(): String = constMap["EMPTY_SAVE"]!!
        fun getStoryEnd(): String = constMap["STORY_END"]!!
        fun getBattleStory(): JSONObject = battleStory
    }
}