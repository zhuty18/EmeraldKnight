package com.tuzicao.emeraldknight.game

import android.annotation.SuppressLint
import android.content.Context
import org.json.JSONArray
import org.json.JSONObject

class GameLogic {
    companion object {
        lateinit var defaultParas: HashMap<String, JSONObject>
        lateinit var defaultFunctionParas: HashMap<String, String>
        lateinit var defaultCodes: HashMap<String, Int>
        lateinit var constMap: HashMap<String, String>

        lateinit var choiceMap: HashMap<String, JSONObject>
        lateinit var sceneMap: HashMap<String, JSONObject>
        lateinit var endNameMap: HashMap<String, String>
        lateinit var chapterNameMap: HashMap<String, String>

        lateinit var characterMap: HashMap<String, JSONObject>

        lateinit var battleStory: JSONObject
        lateinit var endChoice: JSONObject
        lateinit var endScene: JSONObject

        @SuppressLint("StaticFieldLeak")
        lateinit var gameKernel: Kernel

        fun initData(context: Context, kernel: Kernel) {
            gameKernel = kernel
            val consts = JSONObject(readJSON(context, "consts.json"))
            for (key in consts.keys()){
                consts.get
            }

            val choices = JSONArray(readJSON(context, "choices.json"))
            for (i in 0 until choices.length()) {
                val item = choices.getJSONObject(i)
                choiceMap[item.getString("id")] = item
            }
            val scenes = JSONArray(readJSON(context, "scenes.json"))
            for (i in 0 until scenes.length()) {
                val item = scenes.getJSONObject(i)
                sceneMap[item.getString("id")] = item
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