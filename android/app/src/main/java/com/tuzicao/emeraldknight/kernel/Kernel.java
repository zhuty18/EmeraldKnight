package com.tuzicao.emeraldknight.kernel;


import android.content.Context;
import android.util.Log;

import org.json.JSONException;
import org.json.JSONObject;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.nio.charset.StandardCharsets;
import java.util.Date;
import java.util.HashMap;
import java.util.Iterator;
import java.util.LinkedList;
import java.util.Random;

public class Kernel {
    public static String key = "Emerald Knight";
    public static int MaxSave = 100;
    public static int MaxEnd=21;
    private String scene;
    private HashMap<String, Integer> paras;
    private int position;
    private BattleHandler battle;
    private final Context context;

    public static Kernel getKernel(Context ct) {
        Constant.kernel = new Kernel(ct);
        return Constant.kernel;
    }

    public Kernel(Context ct) {
        context = ct;
        reset();
        init_save();
    }

    public void init() {
        scene = "1-1";
        paras = Constant.default_para();
    }

    public void reset() {
        scene = Constant.GAME_OVER;
        paras = null;
        position = 0;
    }

    public void setScene(String s) {
        scene = s;
    }

    public String getScene() {
        return scene;
    }

    static public String getSceneName(String name){
        return Constant.scene_name.get(name);
    }

    public int getPara(String key) {
        return paras.get(key);
    }

    public void setPara(String key, int value) {
        paras.put(key, value);
    }

    public void offsetPara(String key, int offset) {
        paras.put(key, paras.get(key) + offset);
    }

    public String getSceneText() {
        if (scene.equals(Constant.FINAL_BATTLE)) {
            return battle.round();
        } else {
            return context.getResources().getString(Constant.getSceneTextId(scene));
        }
    }

    public LinkedList<abstract_choice> getChoices() {
        if (scene.equals(Constant.FINAL_BATTLE)) {
            return battle.choices();
        } else {
            return Constant.getChoices(scene);
        }
    }

    public void save(int i) {
        try {
            JSONObject json = new JSONObject();
            json.put("scene", scene);
            json.put("paras", new JSONObject(paras));
            json.put("time", new Date().getTime());
            json.put("title", Constant.getTitle(scene));
            Log.d(key, json.toString());
            String file_name = i + ".eks";
            FileOutputStream fos = context.openFileOutput(file_name, Context.MODE_PRIVATE);
            OutputStreamWriter osw = new OutputStreamWriter(fos, "UTF-8");
            osw.write(json.toString());
            osw.flush();
            fos.flush();
            osw.close();
            fos.close();
        } catch (IOException | JSONException e) {
            e.printStackTrace();
        }
    }

    void init_save() {
        String file_name = "0.eks";
        File f = new File(context.getFilesDir(), file_name);
        if (!f.exists()) {
            try {
                JSONObject json=new JSONObject();
                for(int i=1;i<MaxEnd+1;i++){
                    json.put("end-"+i,0);
                }
                String text = json.toString();
                FileOutputStream fos = context.openFileOutput(file_name, Context.MODE_PRIVATE);
                OutputStreamWriter osw = new OutputStreamWriter(fos, "UTF-8");
                osw.write(text);
                osw.flush();
                fos.flush();
                osw.close();
                fos.close();
            } catch (IOException | JSONException e) {
                e.printStackTrace();
            }
        }
    }

    public int readPara(String key) {
        try {
            FileInputStream fis = context.openFileInput("0.eks");
            InputStreamReader isr = new InputStreamReader(fis, StandardCharsets.UTF_8);
            char[] input = new char[fis.available()];
            isr.read(input);
            isr.close();
            fis.close();
            String text = new String(input);
            JSONObject json = new JSONObject(text);
            return json.getInt(key);
        } catch (IOException | JSONException e) {
            e.printStackTrace();
        }
        return 0;
    }

    public void openPara(String key) {
        try {
            FileInputStream fis = context.openFileInput("0.eks");
            InputStreamReader isr = new InputStreamReader(fis, StandardCharsets.UTF_8);
            char[] input = new char[fis.available()];
            isr.read(input);
            isr.close();
            fis.close();
            String text = new String(input);
            JSONObject json = new JSONObject(text);
            json.put(key, 1);

            FileOutputStream fos = context.openFileOutput("0.eks", Context.MODE_PRIVATE);
            OutputStreamWriter osw = new OutputStreamWriter(fos, "UTF-8");
            osw.write(json.toString());
            osw.flush();
            fos.flush();
            osw.close();
            fos.close();
        } catch (IOException | JSONException e) {
            e.printStackTrace();
        }
    }

    public void load(int i) {
        String file_name = i + ".eks";
        try {
            FileInputStream fis = context.openFileInput(file_name);
            InputStreamReader isr = new InputStreamReader(fis, StandardCharsets.UTF_8);
            char[] input = new char[fis.available()];
            isr.read(input);
            isr.close();
            fis.close();
            String text = new String(input);
            JSONObject json = new JSONObject(text);
            scene = json.getString("scene");
            JSONObject tmp = json.getJSONObject("paras");
            paras = new HashMap<String, Integer>();
            for (Iterator<String> it = tmp.keys(); it.hasNext(); ) {
                String key = it.next();
                int value = tmp.getInt(key);
                paras.put(key, value);
            }
        } catch (IOException | JSONException e) {
            e.printStackTrace();
        }
    }

    public boolean fight() {
        int hp = paras.get(Constant.TEMPORARY);
        hp += 3 * paras.get(Constant.INTELLIGENCE);
        hp += paras.get(Constant.KNOWLEDGE);
        hp += 5 * paras.get(Constant.BRUCE_LOVE);
        hp += 5 * (paras.get(Constant.SINESTRO_LOVE) + paras.get(Constant.SINESTRO_TAME));
        if (paras.get(Constant.TEAMMATE) != 0) {
            hp += 20;
        }
        Random random = new Random();
        for (int i = 0; i < 10; i++) {
            hp -= random.nextInt(16);
        }
        return hp > 0;
    }

    public void setPosition(int position) {
        this.position = position;
    }

    public int getPosition() {
        return position;
    }

    public boolean isOn() {
        return !scene.equals(Constant.GAME_OVER);
    }

    public void startBattle() {
        battle = new BattleHandler();
    }
    public boolean inBattle(){
        return scene.equals(Constant.FINAL_BATTLE);
    }
    public void loadEnd(int i){
        setScene("end-"+i);
    }
}
