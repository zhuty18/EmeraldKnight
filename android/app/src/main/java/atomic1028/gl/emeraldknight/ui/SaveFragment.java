package atomic1028.gl.emeraldknight.ui;

import android.content.Context;
import android.os.Bundle;
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

import org.json.JSONException;
import org.json.JSONObject;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.Reader;
import java.io.UnsupportedEncodingException;
import java.nio.charset.StandardCharsets;
import java.text.SimpleDateFormat;
import java.util.Date;

import atomic1028.gl.emeraldknight.R;
import atomic1028.gl.emeraldknight.kernel.Kernel;

public class SaveFragment extends Fragment {
    private boolean isSave;
    public SaveFragmentListener listener;

    public SaveFragment(boolean save) {
        isSave = save;
    }

    public static interface SaveFragmentListener {
        void saveGame(int i);

        void loadGame(int i);
    }

    @Override
    public void onAttach(Context context) {
        super.onAttach(context);
        if (context instanceof SaveFragmentListener) {
            listener = (SaveFragmentListener) context;
        } else {
            throw new RuntimeException(context.toString()
                    + " must implement OnFragmentInteractionListener");
        }
    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {
        View view = inflater.inflate(R.layout.save_fragment, container, false);
        return view;
    }

    boolean saveExist(String file_name) {
        File f = new File(getContext().getFilesDir(), file_name);
        if (!f.exists()) {
            return false;
        } else {
            return true;
        }
    }

    String saveName(String file_name) {
        try {
            FileInputStream fis = getContext().openFileInput(file_name);
            InputStreamReader isr = new InputStreamReader(fis, StandardCharsets.UTF_8);
            char[] input = new char[fis.available()];
            isr.read(input);
            isr.close();
            fis.close();
            String text = new String(input);
            JSONObject json = new JSONObject(text);
            Date date = new Date(json.getLong("time"));
            SimpleDateFormat ft = new SimpleDateFormat("MM.dd HH:mm");
            return json.getString("title") + "\n" + ft.format(date);
        } catch (IOException | JSONException e) {
            e.printStackTrace();
        }
        return "";
    }

    @Override
    public void onViewCreated(@NonNull View view, @Nullable Bundle savedInstanceState) {
        TextView tv = getView().findViewById(R.id.save_title_text);
        if (isSave) {
            tv.setText(R.string.menu_save);
            LinearLayout layout = getView().findViewById(R.id.save_button_layout);
            layout.removeAllViews();
            for (int i = 0; i < Kernel.MaxSave; i++) {
                int index = i + 1;
                String save_name = index + ".eks";
                if (saveExist(save_name)) {
                    Button btn = new Button(layout.getContext());
                    btn.setText(saveName(save_name));
                    btn.setOnClickListener(new View.OnClickListener() {
                        @Override
                        public void onClick(View v) {
                            listener.saveGame(index);
                        }
                    });
                    layout.addView(btn);
                } else {
                    Button btn = new Button(layout.getContext());
                    btn.setText(R.string.empty_save);
                    btn.setOnClickListener(new View.OnClickListener() {
                        @Override
                        public void onClick(View v) {
                            listener.saveGame(index);
                        }
                    });
                    layout.addView(btn);
                    break;
                }
            }
        } else {
            tv.setText(R.string.menu_load);
            LinearLayout layout = getView().findViewById(R.id.save_button_layout);
            layout.removeAllViews();
            for (int i = 0; i < Kernel.MaxSave; i++) {
                int index = i + 1;
                String save_name = index + ".eks";
                if (saveExist(save_name)) {
                    Button btn = new Button(layout.getContext());
                    btn.setText(saveName(save_name));
                    btn.setOnClickListener(new View.OnClickListener() {
                        @Override
                        public void onClick(View v) {
                            listener.loadGame(index);
                        }
                    });
                    layout.addView(btn);
                } else {
                    break;
                }
            }
        }
    }
}
