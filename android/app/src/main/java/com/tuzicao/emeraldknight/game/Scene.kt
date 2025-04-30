package com.tuzicao.emeraldknight.game

import org.json.JSONObject
import java.util.LinkedList

abstract class Scene(private val id: String, data: JSONObject) {
    companion object {
        fun getById(sceneId: String): Scene {
            return StoryScene(sceneId, GameLogic.sceneMap[sceneId]!!)
        }
    }

    fun getId(): String = id
    open fun getText(): String = ""
    open fun getOptions(): LinkedList<Choice> = LinkedList()
}
