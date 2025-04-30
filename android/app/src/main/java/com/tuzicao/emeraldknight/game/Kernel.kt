package com.tuzicao.emeraldknight.game

import android.content.Context
import org.json.JSONObject
import java.io.File
import java.util.LinkedList
import java.util.Random


class Kernel(context: Context) {

    companion object {
        const val MAX_SAVE = 100

        fun getSceneName(id: String): String {
            return GameLogic.getSceneName(id)
        }
    }

    private var scene: Scene? = null
    private val paraMap: HashMap<String, Int> = HashMap()
    private val fightResult: HashMap<String, Int> = HashMap()

    init {
        GameLogic.initData(context, this)
        refreshParas()
    }

    fun getSceneId(): String {
        return scene?.let {
            scene!!.getId()
        } ?: GameLogic.getStartOver()
    }

    fun getSceneText(): String = scene!!.getText()


    fun getChoices(): LinkedList<Choice> = scene!!.getOptions()


    fun toScene(sceneId: String) {
        scene = Scene.getById(sceneId)
    }

    fun getPara(paraId: String): Int = paraMap[GameLogic.defaultParas[paraId]!!.getString("name")]!!

    fun setPara(paraId: String, value: Int) {
        paraMap[GameLogic.defaultParas[paraId]!!.getString("name")] = value
    }

    fun refreshParas() {
        for (item in GameLogic.defaultParas.values) {
            if (!paraMap.containsKey(item["name"])) {
                setPara(item.getString("id"), item.getInt("default_value"))
            }
        }
    }

    fun loadAt(context: Context, saveId: Int) {
        if (saveId == 0) {
            toScene(GameLogic.getStartScene())
            for (item in GameLogic.defaultParas.values) {
                paraMap.clear()
                setPara(item.getString("id"), item.getInt("default_value"))
            }
        } else {
            val save = JSONObject(File(context.filesDir, "$saveId.eks").readText())
            toScene(save.getString("scene"))
            paraMap.clear()
            val keys = save.getJSONObject("paras").keys()
            while (keys.hasNext()) {
                val key = keys.next()
                paraMap[key] = save.getJSONObject("paras").getInt(key)
            }
            refreshParas()
        }
    }

    fun saveAt(context: Context, saveId: Int) {
        if (scene!!.getId() == GameLogic.getFinalBattle()) {
            val saveFile = File(context.filesDir, "$saveId.eks")
            val saveInfo = JSONObject()
            saveInfo.put("scene", scene!!.getId())
            saveInfo.put("paras", JSONObject(paraMap as Map<*, *>))
            saveFile.writeText(saveInfo.toString())
        }
    }

    private fun fightNow(): Boolean {
        var hp: Double = getPara("TEMPORARY").toDouble()
        hp += 3 * getPara("INTELLIGENCE")
        hp += getPara("KNOWLEDGE")
        hp += 5 * getPara("BRUCE_LOVE")
        hp += 5 * getPara("SINESTRO_LOVE")
        hp += 5 * getPara("SINESTRO_TAME")
        hp += 20 * (if (getPara("TEAMMATE") != 0) 1 else 0)
        for (i in 0 until 10) {
            hp -= Random().nextDouble() * 16
        }
        return hp > 0
    }

    fun getFightResult(): Int {
        if (!fightResult.containsKey(scene!!.getId())) {
            fightResult[scene!!.getId()] = if (fightNow()) 1 else 0
        }
        return fightResult[scene!!.getId()]!!
    }

    fun checkCondition(toCheck: JSONObject): Boolean {
        val checkAct = toCheck.getString("check")
        if (checkAct == "CONDITION") {
            return (if (checkIs(toCheck.getJSONObject("para"))) 1 else 0) == toCheck.getInt("value")
        } else {
            val paraName = toCheck.getString("para")
            val checkValue: Any = when {
                GameLogic.defaultFuncs.contains(paraName) -> when (paraName) {
                    "SCENE" -> getSceneId()
                    "FIGHT" -> getFightResult()
                    "CHOICE" -> if (Choice.getById(toCheck.getString("value")).isShow()) 1 else 0
                    else -> paraName
                }

                paraName.contains("end") -> if (GameLogic.checkEnd(paraName)) 1 else 0
                else -> getPara(paraName)
            }
            val targetValue: Any = when {
                paraName == "CHOICE" -> 1
                toCheck.get("value") is String && GameLogic.defaultCodes.containsKey(
                    toCheck.getString(
                        "value"
                    )
                ) -> GameLogic.defaultCodes[toCheck.getString("value")]!!

                toCheck.get("value") is String -> toCheck.getString("value")
                else -> toCheck.getInt("value")
            }

            return when (checkAct) {
                "EQUAL" -> checkValue == targetValue
                "UNEQUAL" -> checkValue != targetValue
                "MORE" -> checkValue as Int > targetValue as Int
                "MORE_EQUAL" -> checkValue as Int >= targetValue as Int
                "LESS" -> (checkValue as Int) < targetValue as Int
                "LESS_EQUAL" -> checkValue as Int <= targetValue as Int
                "BINARY" -> ((checkValue as Int shr (targetValue as Int - 1)) and 1) == 1
                "NON_BINARY" -> ((checkValue as Int shr (targetValue as Int - 1)) and 1) == 0
                else -> false
            }
        }

    }

    fun checkIs(toCheck: JSONObject): Boolean {
        val checkOp = toCheck.getString("op")
        val checkItems = toCheck.getJSONArray("condition")

        val checks = (0 until checkItems.length()).map {
            checkCondition(checkItems.getJSONObject(it))
        }
        return when (checkOp) {
            "AND" -> checks.all { it }
            "OR" -> checks.any { it }
            else -> false
        }
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

    fun loadEnd(endId: Int) = toScene("end-$endId")

    fun isOn(): Boolean = (getSceneId() != GameLogic.getStartOver())
    fun isBattle(): Boolean = (getSceneId() == GameLogic.getFinalBattle())

}
