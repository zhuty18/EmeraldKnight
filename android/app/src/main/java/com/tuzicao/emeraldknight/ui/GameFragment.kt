package com.tuzicao.emeraldknight.ui

import android.content.Context
import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Button
import android.widget.LinearLayout
import android.widget.TextView
import androidx.fragment.app.Fragment
import com.tuzicao.emeraldknight.R
import com.tuzicao.emeraldknight.game.Choice
import java.util.LinkedList

class GameFragment(
    private val sceneText: String,
    private val choicesList: LinkedList<Choice>
) : Fragment() {

    var listener: GameFragmentListener? = null

    interface GameFragmentListener {
        fun choose(i: Int)
    }

    override fun onAttach(context: Context) {
        super.onAttach(context)
        if (context is GameFragmentListener) {
            listener = context
        } else {
            throw RuntimeException("$context must implement GameFragmentListener")
        }
    }

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?, savedInstanceState: Bundle?
    ): View? {
        return inflater.inflate(R.layout.game_fragment, container, false)
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)

        val tv: TextView = requireView().findViewById(R.id.game_text)
        tv.text = sceneText

        val layout: LinearLayout = requireView().findViewById(R.id.game_choice_layout)
        layout.removeAllViews()

        for (i in choicesList.indices) {
            val choice = choicesList[i]
            val btn = Button(layout.context).apply {
                text = choice.getText()
                setOnClickListener {
                    listener?.choose(i)
                }
            }
            layout.addView(btn)
        }
    }
}
