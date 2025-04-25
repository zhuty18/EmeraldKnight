package atomic1028.gl.emeraldknight.ui;

import android.content.Context;
import android.os.Bundle;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.LinearLayout;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.fragment.app.Fragment;

import org.json.JSONException;
import org.json.JSONObject;

import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.charset.StandardCharsets;

import atomic1028.gl.emeraldknight.R;
import atomic1028.gl.emeraldknight.kernel.Kernel;

public class HomeFragment extends Fragment {
    public FragmentListener listener;

    public static interface FragmentListener {
        void startGame();
        void loadEnd(int i);
    }

    @Override
    public void onAttach(Context context) {
        super.onAttach(context);
        if (context instanceof FragmentListener) {
            listener = (FragmentListener) context;
        } else {
            throw new RuntimeException(context.toString()
                    + " must implement OnFragmentInteractionListener");
        }
    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {
        View view = inflater.inflate(R.layout.home_fragment, container, false);
        return view;
    }

    @Override
    public void onViewCreated(@NonNull View view, @Nullable Bundle savedInstanceState) {
        Button sbtn = getView().findViewById(R.id.start_button);
        sbtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                listener.startGame();
            }
        });
        LinearLayout layout=getView().findViewById(R.id.history_layout);
        layout.removeAllViews();
        try {
            FileInputStream fis = getContext().openFileInput("0.eks");
            InputStreamReader isr = new InputStreamReader(fis, StandardCharsets.UTF_8);
            char[] input = new char[fis.available()];
            isr.read(input);
            isr.close();
            fis.close();
            String text = new String(input);
            JSONObject json = new JSONObject(text);
            for(int i=0;i< Kernel.MaxEnd;i++){
                int index=i+1;
                String end_name="end-"+index;
                Button btn=new Button(getContext());
                if (json.getInt(end_name)==1){
                    btn.setText("结局"+index+" "+Kernel.getSceneName(end_name));
                    btn.setOnClickListener(new View.OnClickListener() {
                        @Override
                        public void onClick(View v) {
                            listener.loadEnd(index);
                        }
                    });
                }else{
                    btn.setText("结局"+index+" 未解锁");
                }
                layout.addView(btn);
            }
        } catch (IOException | JSONException e) {
            e.printStackTrace();
        }
    }
}
