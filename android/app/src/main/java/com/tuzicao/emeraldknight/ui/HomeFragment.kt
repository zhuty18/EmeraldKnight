package com.tuzicao.emeraldknight.ui

import android.content.Context
import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Button
import android.widget.LinearLayout
import androidx.fragment.app.Fragment
import com.tuzicao.emeraldknight.R
import com.tuzicao.emeraldknight.game.GameLogic
import com.tuzicao.emeraldknight.game.Kernel

class HomeFragment : Fragment() {

    private lateinit var listener: FragmentListener

    interface FragmentListener {
        fun startGame()
        fun loadEnd(i: Int)
    }

    override fun onAttach(context: Context) {
        super.onAttach(context)
        if (context is FragmentListener) {
            listener = context
        } else {
            throw RuntimeException("$context must implement FragmentListener")
        }
    }

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View {
        return inflater.inflate(R.layout.home_fragment, container, false)
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        val startBtn = view.findViewById<Button>(R.id.start_button)
        startBtn.setOnClickListener {
            listener.startGame()
        }

        val layout = view.findViewById<LinearLayout>(R.id.history_layout)
        layout.removeAllViews()

        for (i in 0 until GameLogic.endNameMap.size) {
            val index = i + 1
            val endName = "end-$index"
            val btn = Button(context)
            if (GameLogic.checkEnd(endName)) {
                btn.text = "结局$index ${Kernel.getSceneName(endName)}"
                btn.setOnClickListener {
                    listener.loadEnd(index)
                }
            } else {
                btn.text = "结局$index 未解锁"
            }
            layout.addView(btn)
        }
    }
}
