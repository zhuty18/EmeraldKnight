package com.tuzicao.emeraldknight

import android.content.Intent
import android.net.Uri
import android.os.Bundle
import android.util.Log
import android.widget.Button
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import androidx.fragment.app.Fragment
import com.tuzicao.emeraldknight.game.Kernel
import com.tuzicao.emeraldknight.game.Choice
import com.tuzicao.emeraldknight.ui.*
import java.util.LinkedList
import androidx.core.net.toUri

class MainActivity : AppCompatActivity(),
    HomeFragment.FragmentListener,
    GameFragment.GameFragmentListener,
    SaveFragment.SaveFragmentListener,
    AboutFragment.AboutFragmentListener {

    private lateinit var kernel: Kernel
    private var choicesList = LinkedList<Choice>()
    private var atGame = false

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        kernel = Kernel(this.applicationContext)
        supportFragmentManager.beginTransaction()
            .replace(R.id.main_layout, HomeFragment())
            .commit()

        findViewById<Button>(R.id.about_button).setOnClickListener { about() }
        findViewById<Button>(R.id.save_button).setOnClickListener { save() }
        findViewById<Button>(R.id.load_button).setOnClickListener { load() }
        findViewById<Button>(R.id.back_button).setOnClickListener { back() }

        atGame = false
    }

    private fun switchFragment(target: Fragment) {
        supportFragmentManager.beginTransaction()
            .replace(R.id.main_layout, target)
            .commit()

        val btn = findViewById<Button>(R.id.back_button)
        if (atGame) {
            btn.setText(R.string.menu_start)
        } else {
            btn.setText(R.string.menu_back)
        }
    }

    override fun startGame() {
        loadGame(0)
    }

    override fun saveGame(i: Int) {
        if (!kernel.isOn()) {
            Toast.makeText(this, "不在游戏中，存储失败！", Toast.LENGTH_LONG).show()
        } else {
            kernel.saveAt(this, i)
            Toast.makeText(this, "存储成功！", Toast.LENGTH_SHORT).show()
            save()
        }
    }

    override fun loadGame(i: Int) {
        atGame = true
        kernel.loadAt(this, i)
        refreshGame()
    }

    private fun refreshGame() {
        if (!atGame || !kernel.isOn()) {
            switchFragment(HomeFragment())
        } else {
            if (kernel.getSceneId().contains("end")) {
                kernel.openEnd(this)
            }
            val sceneText = kernel.getSceneText()
            choicesList = kernel.getChoices()
            switchFragment(GameFragment(sceneText, choicesList))
        }
    }

    override fun choose(i: Int) {
        Log.d("Emerald Knight", "choose $i")
        choicesList[i].beChosen()
        refreshGame()
    }

    fun about() {
        atGame = false
        switchFragment(AboutFragment())
    }

    fun save() {
        if (kernel.isBattle() || kernel.getSceneId().startsWith("end")) {
            Toast.makeText(this, "当前无法保存！", Toast.LENGTH_SHORT).show()
        } else {
            atGame = false
            switchFragment(SaveFragment(true))
        }
    }

    fun load() {
        atGame = false
        switchFragment(SaveFragment(false))
    }

    fun back() {
        atGame = !atGame
        refreshGame()
    }

    override fun loadEnd(i: Int) {
        atGame = true
        kernel.loadEnd(i)
        refreshGame()
    }

    override fun openCheat() {
        switchFragment(CheatFragment())
    }

    override fun openProject() {
        val intent: Intent =
            Intent(Intent.ACTION_VIEW, this.getString(R.string.project_url).toUri())
        startActivity(intent)
    }
}
