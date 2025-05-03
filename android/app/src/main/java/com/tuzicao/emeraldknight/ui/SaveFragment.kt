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
import com.tuzicao.emeraldknight.game.GameLogic
import com.tuzicao.emeraldknight.game.Kernel
import java.io.File

class SaveFragment(private val isSaving: Boolean) : Fragment() {

    private var listener: SaveFragmentListener? = null

    interface SaveFragmentListener {
        fun saveGame(i: Int)
        fun loadGame(i: Int)
    }

    override fun onAttach(context: Context) {
        super.onAttach(context)
        if (context is SaveFragmentListener) {
            listener = context
        } else {
            throw RuntimeException("$context must implement SaveFragmentListener")
        }
    }

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?, savedInstanceState: Bundle?
    ): View? {
        return inflater.inflate(R.layout.save_fragment, container, false)
    }

    private fun saveExist(fileName: String): Boolean {
        val file = File(context?.filesDir, fileName)
        return file.exists()
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        val tv: TextView = requireView().findViewById(R.id.save_title_text)
        if (isSaving) {
            tv.setText(R.string.menu_save)
            val layout: LinearLayout = requireView().findViewById(R.id.save_button_layout)
            layout.removeAllViews()
            for (i in 0 until Kernel.MAX_SAVE) {
                val index = i + 1
                val saveName = "$index.eks"
                val saveInfo = GameLogic.getSaveInfo(requireContext(), index)
                if (saveExist(saveName)) {
                    val btn = Button(layout.context).apply {
                        text = saveInfo
                        setOnClickListener {
                            listener?.saveGame(index)
                        }
                    }
                    layout.addView(btn)
                } else {
                    val btn = Button(layout.context).apply {
                        text = GameLogic.getEmptySave()
                        setOnClickListener {
                            listener?.saveGame(index)
                        }
                    }
                    layout.addView(btn)
                    break
                }
            }
        } else {
            tv.setText(R.string.menu_load)
            val layout: LinearLayout = requireView().findViewById(R.id.save_button_layout)
            layout.removeAllViews()
            for (i in 0 until Kernel.MAX_SAVE) {
                val index = i + 1
                val saveName = "$index.eks"
                val saveInfo = GameLogic.getSaveInfo(requireContext(), index)
                if (saveExist(saveName)) {
                    val btn = Button(layout.context).apply {
                        text = saveInfo
                        setOnClickListener {
                            listener?.loadGame(index)
                        }
                    }
                    layout.addView(btn)
                } else {
                    break
                }
            }
        }
    }
}
