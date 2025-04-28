package com.tuzicao.emeraldknight.game

import android.content.Context

abstract class Choice {
    companion object{
        fun getChoiceById(context: Context, c_id:String):Choice{
            var data=
            return StoryChoice(c_id)
        }
    }
    private val _id: String=""

    open fun getID(): String {
        return _id
    }

    open fun text(): String {
        return ""
    }

    open fun show(): Boolean {
        return true
    }

    open fun choose() {}
}

class StoryChoice(val _id: String,data:jsonObject):Choice(){

}