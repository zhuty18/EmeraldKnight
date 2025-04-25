package com.tuzicao.emeraldknight;

import androidx.appcompat.app.AppCompatActivity;
import androidx.fragment.app.Fragment;
import androidx.fragment.app.FragmentTransaction;

import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.Toast;

import java.util.LinkedList;

import com.tuzicao.emeraldknight.kernel.Kernel;
import com.tuzicao.emeraldknight.kernel.abstract_choice;
import com.tuzicao.emeraldknight.ui.AboutFragment;
import com.tuzicao.emeraldknight.ui.CheatFragment;
import com.tuzicao.emeraldknight.ui.GameFragment;
import com.tuzicao.emeraldknight.ui.HomeFragment;
import com.tuzicao.emeraldknight.ui.SaveFragment;

public class MainActivity extends AppCompatActivity implements HomeFragment.FragmentListener, GameFragment.GameFragmentListener, SaveFragment.SaveFragmentListener, AboutFragment.AboutFragmentListener {
    private Kernel gk;
    private LinkedList<abstract_choice> choices_list;
    private boolean atGame;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        gk = Kernel.getKernel(this);
        FragmentTransaction transaction = getSupportFragmentManager().beginTransaction();
        transaction.replace(R.id.main_layout, new HomeFragment()).commit();
        Button btn = findViewById(R.id.about_button);
        btn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                about();
            }
        });
        btn = findViewById(R.id.save_button);
        btn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                save();
            }
        });
        btn = findViewById(R.id.load_button);
        btn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                load();
            }
        });
        btn = findViewById(R.id.back_button);
        btn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                back();
            }
        });
        atGame = false;
    }


    void switchFragment(Fragment target) {
        FragmentTransaction transaction = getSupportFragmentManager().beginTransaction();
        transaction.replace(R.id.main_layout, target).commit();
        Button btn = findViewById(R.id.back_button);
        if (atGame) {
            btn.setText(R.string.menu_start);
        } else {
            btn.setText(R.string.menu_back);
        }
    }

    @Override
    public void startGame() {
        loadGame(0);
    }

    @Override
    public void saveGame(int i) {
        if (!gk.isOn()) {
            Toast.makeText(this, "不在游戏中，存储失败！", Toast.LENGTH_LONG).show();
        } else {
            gk.save(i);
            Toast.makeText(this, "存储成功！", Toast.LENGTH_SHORT).show();
            save();
        }
    }

    @Override
    public void loadGame(int i) {
        atGame = true;
        if (i == 0) {
            gk.init();
        } else {
            gk.load(i);
        }
        refreshGame();
    }

    void refreshGame() {
        if ((!atGame) || !(gk.isOn())) {
            switchFragment(new HomeFragment());
        } else {
            String scene_text = gk.getSceneText();
            choices_list = gk.getChoices();
            switchFragment(new GameFragment(scene_text, choices_list));
        }
    }

    @Override
    public void choose(int i) {
        Log.d(Kernel.key, "choose " + i);
        choices_list.get(i).chosen();
        refreshGame();
    }

    public void about() {
        atGame = false;
        switchFragment(new AboutFragment());
    }

    public void save() {
        if (gk.inBattle() || gk.getScene().startsWith("end")) {
            Toast.makeText(this, "当前无法保存！", Toast.LENGTH_SHORT).show();
        } else {
            atGame = false;
            switchFragment(new SaveFragment(true));
        }
    }

    public void load() {
        atGame = false;
        switchFragment(new SaveFragment(false));
    }

    public void back() {
        atGame = !atGame;
        refreshGame();
    }

    @Override
    public void loadEnd(int i) {
        atGame = true;
        gk.loadEnd(i);
        refreshGame();
    }

    @Override
    public void openCheat() {
        switchFragment(new CheatFragment());
    }
}