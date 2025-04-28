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
import com.tuzicao.emeraldknight.game.Kernel
import org.json.JSONException
import org.json.JSONObject
import java.io.IOException
import java.nio.charset.StandardCharsets

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
        val sbtn = view.findViewById<Button>(R.id.start_button)
        sbtn.setOnClickListener {
            listener.startGame()
        }

        val layout = view.findViewById<LinearLayout>(R.id.history_layout)
        layout.removeAllViews()

        try {
            val fis = requireContext().openFileInput("0.eks")
            val input = fis.readBytes()
            fis.close()
            val text = String(input, StandardCharsets.UTF_8)
            val json = JSONObject(text)

            for (i in 0 until Kernel.MaxEnd) {
                val index = i + 1
                val endName = "end-$index"
                val btn = Button(context)
                if (json.optInt(endName, 0) == 1) {
                    btn.text = "结局$index ${Kernel.getSceneName(endName)}"
                    btn.setOnClickListener {
                        listener.loadEnd(index)
                    }
                } else {
                    btn.text = "结局$index 未解锁"
                }
                layout.addView(btn)
            }
        } catch (e: IOException) {
            e.printStackTrace()
        } catch (e: JSONException) {
            e.printStackTrace()
        }
    }
}
