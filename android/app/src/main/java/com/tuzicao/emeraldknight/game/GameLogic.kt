package com.tuzicao.emeraldknight.game

import android.content.Context
import org.json.JSONArray
import org.json.JSONObject
import java.io.File
import java.text.SimpleDateFormat
import java.util.LinkedList
import java.util.Locale

class GameLogic {
    companion object {
        private val constMap: HashMap<String, String> = HashMap()

        val defaultParas: HashMap<String, JSONObject> = HashMap()
        val defaultFuncs: LinkedList<String> = LinkedList()
        val defaultCodes: HashMap<String, Int> = HashMap()

        val choiceMap: HashMap<String, JSONObject> = HashMap()
        val sceneMap: HashMap<String, JSONObject> = HashMap()
        val sceneTextMap: HashMap<String, String> = HashMap()
        val endNameMap: HashMap<String, String> = HashMap()
        val chapterNameMap: HashMap<String, String> = HashMap()

        val characterMap: HashMap<String, JSONObject> = HashMap()

        val endStatusMap: HashMap<String, Int> = HashMap()

        lateinit var battleStory: JSONObject
        lateinit var endChoice: JSONObject
        lateinit var endScene: JSONObject

        lateinit var gameKernel: Kernel

        private fun readJSON(context: Context, fileName: String): String {
            return context.assets.open(fileName).bufferedReader().use { it.readText() }
        }

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
            for (i in 0 until paras.getJSONArray("func_list").length()) {
                defaultFuncs.add(paras.getJSONArray("func_list").getString(i))
            }

            loadData(JSONArray(readJSON(context, "choices.json")), choiceMap) { it }
            choiceMap[endChoice.getString("id")] = endChoice
            loadData(JSONArray(readJSON(context, "scenes.json")), sceneMap) { it }
            sceneMap[endScene.getString("id")] = endScene
            loadData(
                JSONArray(readJSON(context, "scene_text.json")),
                sceneTextMap
            ) { it.getString("value") }

            val names = JSONObject(readJSON(context, "names.json"))
            loadData(names.getJSONArray("end_names"), endNameMap) { it.getString("value") }
            loadData(names.getJSONArray("chapter_names"), chapterNameMap) { it.getString("value") }

            loadData(JSONArray(readJSON(context, "characters.json")), characterMap) { it }

            val file = File(context.filesDir, "0.eks")
            if (!file.exists()) {
                file.writeText("{}")
            }
            val endStatus = JSONObject(file.readText())
            val keys = endStatus.keys()
            while (keys.hasNext()) {
                val key = keys.next()
                endStatusMap[key] = endStatus.getInt(key)
            }


        }

        fun getStartScene(): String = constMap["START_SCENE"]!!
        fun getStartOver(): String = constMap["START_OVER"]!!
        fun getFinalBattle(): String = constMap["FINAL_BATTLE"]!!
        fun getEmptySave(): String = constMap["EMPTY_SAVE"]!!
        fun getStoryEnd(): String = constMap["STORY_END"]!!
        fun getBattleStory(): JSONObject = battleStory

        fun getSceneChapter(sceneId: String): String = sceneId.split("-")[0]

        fun getSceneText(sceneId: String): String = sceneTextMap[sceneId]!!

        fun getSceneName(sceneId: String): String = sceneMap[sceneId]!!.getString("name")
        fun getEndName(endId: String): String = endNameMap[endId]!!

        fun getChapterName(sceneId: String): String {
            if (getSceneChapter(sceneId) == "end") {
                return chapterNameMap["end"]!! + endNameMap[sceneId]!!
            }
            return chapterNameMap["ch${getSceneChapter(sceneId)}"]!!
        }

        fun markEnd(context: Context, endId: String) {
            endStatusMap[endId] = 1
            val file = File(context.filesDir, "0.eks")
            val endStatus = JSONObject(file.readText())
            endStatus.put(endId, 1)
            file.writeText(endStatus.toString())
        }

        fun checkEnd(endId: String): Boolean {
            return endStatusMap.getOrDefault(endId, 0) == 1
        }

        fun getSaveInfo(context: Context, saveId: Int): String {
            val file = File(context.filesDir, "$saveId.eks")
            if (file.exists()) {
                val saveInfo = JSONObject(file.readText())
                val formatter = SimpleDateFormat("MM.dd HH:mm", Locale.getDefault())
                val saveTime = formatter.format(file.lastModified())
                return getChapterName(saveInfo.getString("scene")) + "\n" + saveTime
            } else {
                return getEmptySave()
            }
        }
    }
}