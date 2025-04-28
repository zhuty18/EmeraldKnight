package com.tuzicao.emeraldknight.game

abstract class Choice {
    private lateinit var _id: String
    open fun getID(): String {
        return _id
    }

    open fun text(): String {
        return ""
    }

    open fun choose() {}
    open fun show(): Boolean {
        return true
    }
}