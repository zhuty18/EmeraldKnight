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
import com.tuzicao.emeraldknight.game.Kernel
import org.json.JSONException
import org.json.JSONObject
import java.io.File
import java.io.IOException
import java.io.InputStreamReader
import java.nio.charset.StandardCharsets
import java.text.SimpleDateFormat
import java.util.*

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

    private fun saveName(fileName: String): String {
        try {
            val fis = context?.openFileInput(fileName)
            val isr = InputStreamReader(fis, StandardCharsets.UTF_8)
            val input = CharArray(fis?.available() ?: 0)
            isr.read(input)
            isr.close()
            fis?.close()
            val text = String(input)
            val json = JSONObject(text)
            val date = Date(json.getLong("time"))
            val ft = SimpleDateFormat("MM.dd HH:mm")
            return json.getString("title") + "\n" + ft.format(date)
        } catch (e: IOException) {
            e.printStackTrace()
        } catch (e: JSONException) {
            e.printStackTrace()
        }
        return ""
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        val tv: TextView = requireView().findViewById(R.id.save_title_text)
        if (isSaving) {
            tv.setText(R.string.menu_save)
            val layout: LinearLayout = requireView().findViewById(R.id.save_button_layout)
            layout.removeAllViews()
            for (i in 0 until Kernel.MaxSave) {
                val index = i + 1
                val saveName = "$index.eks"
                if (saveExist(saveName)) {
                    val btn = Button(layout.context).apply {
                        text = saveName(saveName)
                        setOnClickListener {
                            listener?.saveGame(index)
                        }
                    }
                    layout.addView(btn)
                } else {
                    val btn = Button(layout.context).apply {
                        text = getString(R.string.empty_save)
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
            for (i in 0 until Kernel.MaxSave) {
                val index = i + 1
                val saveName = "$index.eks"
                if (saveExist(saveName)) {
                    val btn = Button(layout.context).apply {
                        text = saveName(saveName)
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
