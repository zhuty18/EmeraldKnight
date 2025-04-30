package com.tuzicao.emeraldknight.game

import org.json.JSONObject
import java.util.LinkedList

abstract class Scene(data: JSONObject) {
    companion object {
        fun getById(sceneId: String): Scene {
            return if (sceneId.contains("end")) {
                StoryScene(
                    JSONObject(
                        mapOf(
                            "id" to sceneId,
                            "options" to GameLogic.sceneMap[GameLogic.getStartOver()]!!.getJSONArray(
                                "options"
                            )
                        )
                    )
                )
            } else {
                StoryScene(GameLogic.sceneMap[sceneId]!!)
            }
        }
    }

    val id: String = data.getString("id")

    fun getId(): String = id
    open fun getText(): String = ""
    open fun getOptions(
        optionList: LinkedList<String>? = null,
        choices: LinkedList<Choice>? = null
    ): LinkedList<Choice> {
        val choiceList = choices ?: LinkedList()
        choices ?: {
            for (i in 0 until optionList!!.size) {
                choiceList.add(Choice.getById(optionList[i]))
            }
        }
        val res: LinkedList<Choice> = LinkedList()
        for (i in 0 until choiceList.size) {
            if (choiceList[i].isShow()) {
                res.add(choiceList[i])
            }
        }
        return res
    }
}
