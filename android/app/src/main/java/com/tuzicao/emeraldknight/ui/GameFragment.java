package com.tuzicao.emeraldknight.ui;

import android.content.Context;
import android.os.Bundle;
import android.text.Html;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.LinearLayout;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.fragment.app.Fragment;

import java.util.LinkedList;

import com.tuzicao.emeraldknight.R;
import com.tuzicao.emeraldknight.kernel.Kernel;
import com.tuzicao.emeraldknight.kernel.abstract_choice;

public class GameFragment extends Fragment {
    public GameFragmentListener listener;
    String scene_text;
    LinkedList<abstract_choice> choices_list;

    public static interface GameFragmentListener {
        void choose(int i);
    }

    @Override
    public void onAttach(Context context) {
        super.onAttach(context);
        if (context instanceof HomeFragment.FragmentListener) {
            listener = (GameFragmentListener) context;
        } else {
            throw new RuntimeException(context.toString()
                    + " must implement OnFragmentInteractionListener");
        }
    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {
        View view = inflater.inflate(R.layout.game_fragment, container, false);
        return view;
    }
    @Override
    public void onViewCreated(@NonNull View view, @Nullable Bundle savedInstanceState) {
        TextView tv = (TextView) getView().findViewById(R.id.game_text);
        tv.setText(scene_text);
        LinearLayout layout=(LinearLayout)getView().findViewById(R.id.game_choice_layout);
        layout.removeAllViews();
        for (int i = 0; i < choices_list.size(); i++) {
            abstract_choice choice=choices_list.get(i);
            Button btn=new Button(layout.getContext());
            btn.setText(choice.text());
            int index = i;
            btn.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View v) {
                    listener.choose(index);
                }
            });
            layout.addView(btn);
        }
    }

    public GameFragment(String scene_text, LinkedList<abstract_choice> choice_list) {
        this.scene_text="        "+scene_text.replace("\n","\n        ");
        this.choices_list=choice_list;
    }
}
