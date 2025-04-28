package com.tuzicao.emeraldknight.ui

import android.content.Context
import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Button
import androidx.fragment.app.Fragment
import com.tuzicao.emeraldknight.R

class AboutFragment : Fragment() {
    var listener: AboutFragmentListener? = null

    interface AboutFragmentListener {
        fun openCheat()
    }

    override fun onAttach(context: Context) {
        super.onAttach(context)
        if (context is AboutFragmentListener) {
            listener = context
        } else {
            throw RuntimeException("$context must implement AboutFragmentListener")
        }
    }

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?, savedInstanceState: Bundle?
    ): View? {
        return inflater.inflate(R.layout.about_fragment, container, false)
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)
        val btn: Button = view.findViewById(R.id.cheat_button)
        btn.setOnClickListener {
            listener?.openCheat()
        }
    }
}
