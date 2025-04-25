package atomic1028.gl.emeraldknight.kernel;

import java.util.LinkedList;
import java.util.Random;

class Entry {
    int number;
    String text;

    public Entry(int i, String s) {
        number = i;
        text = s;
    }
}

class Character {
    int attack;
    int max_life;
    int speed;
    int life;
    int blood;

    public Character(int atk, int spd, int mlf) {
        attack = atk;
        max_life = mlf;
        life = mlf;
        speed = spd;
        blood = 0;
    }

    boolean isDead() {
        return life <= 0;
    }

    static Entry move(Character src, Character tar, double multiplier) {
        int dodge = src.speed - tar.speed + 50;
        Random random = new Random();
        if (random.nextInt(500) < dodge) {
            return new Entry(0, "被躲开了！");
        } else {
            double atk = src.attack;
            atk *= 0.8 + 0.4 * random.nextFloat();
            int r = (int) (atk * multiplier);
            return new Entry(r, "造成了" + r + "点伤害！");
        }
    }
}

class Sinestro extends Character {
    public Sinestro() {
        super(100 - Constant.kernel.getPara(Constant.SINESTRO_LOVE) * 5, 100 - Constant.kernel.getPara(Constant.SINESTRO_TAME) * 2, 500);
    }

    String plain_attack(Character hal) {
        Entry e = Character.move(this, hal, 0.1);
        hal.life -= e.number;
        return "魔王向你发动进攻，" + e.text;
    }

    String special_attack(Character hal) {
        Entry e = Character.move(this, hal, 0.25);
        hal.life -= e.number;
        return "魔王对你使用了魔法，" + e.text;
    }

    String treat(Character hal) {
        int tmp = new Random().nextInt(60) + 120;
        life += tmp;
        blood += 1;
        return "魔王身上黑雾攒动，回复了" + tmp + "点体力！";
    }

    String take_act(Character hal) {
        if (((blood == 0) && (life < 250)) || ((blood == 1) && (life < 100))) {
            return treat(hal);
        } else if (new Random().nextDouble() < 0.67) {
            return plain_attack(hal);
        } else {
            return special_attack(hal);
        }
    }
}

class battle_choice extends abstract_choice {
    String des;
    int move;
    BattleHandler tar;

    public battle_choice(String s, int m, BattleHandler target) {
        des = s;
        move = m;
        tar = target;
    }

    @Override
    public String text() {
        return des;
    }

    @Override
    public void chosen() {
        tar.battle_text = tar.hal.move(tar.sinestro, move);
    }
}

class Hal extends Character {
    boolean fly;

    public Hal() {
        super(
                100 + (Constant.kernel.getPara(Constant.BRUCE_LOVE) + Constant.kernel.getPara(Constant.INTELLIGENCE)) * 2 + Constant.kernel.getPara(Constant.DRAGON_EGG) * 10,
                100 + Constant.kernel.getPara(Constant.KNOWLEDGE) + Constant.kernel.getPara(Constant.PEGASUS) * 20,
                100 + (Constant.kernel.getPara(Constant.OLIVER_LOVE) + Constant.kernel.getPara(Constant.BARRY_LOVE)) * 10
        );
        fly = Constant.kernel.getPara(Constant.PEGASUS) == 1;
    }


    LinkedList<Entry> moves() {
        LinkedList<Entry> res = new LinkedList<Entry>() {{
            add(new Entry(0, "普通攻击"));
        }};
        if (fly) {
            res.add(new Entry(1, "突袭"));
        }
        res.add(new Entry(2, "特殊攻击"));
        if (blood < 10) {
            res.add(new Entry(3, "治疗"));
        }
        res.add(new Entry(100, "开挂"));
        return res;
    }

    String move(Character sinestro, int i) {
        if (i == 0) {
            return plain_attack(sinestro);
        } else if (i == 1) {
            return special_attack(sinestro);
        } else if (i == 2) {
            return sword_attack(sinestro);
        } else if (i == 3) {
            return treat(sinestro);
        } else {
            return cheat(sinestro);
        }
    }

    String plain_attack(Character sinestro) {
        Entry e = Character.move(this, sinestro, 0.15);
        sinestro.life -= e.number;
        return "你向魔王发动进攻，" + e.text;
    }

    String special_attack(Character sinestro) {
        Entry e = Character.move(this, sinestro, 0.30);
        sinestro.life -= e.number;
        return "你借助飞马对魔王发起奇袭，" + e.text;
    }

    String sword_attack(Character sinestro) {
        Entry e = Character.move(this, sinestro, 0.50);
        sinestro.life -= e.number;
        int tmp = new Random().nextInt(10) + 5;
        life -= tmp;
        return "翡翠剑面对魔王放出强光，消耗了你的" + tmp + "点体力，" + e.text;
    }

    String treat(Character sinestro) {
        int tmp = new Random().nextInt(20) + 40;
        blood += 1;
        if (life + tmp > max_life) {
            tmp = max_life - life;
        }
        life += tmp;
        return "你吃下一颗雷电小球，回复了" + tmp + "点体力！";
    }

    String cheat(Character sinestro) {
        sinestro.life = 0;
        return "你开挂绝杀！";
    }
}

public class BattleHandler {
    Sinestro sinestro;
    Hal hal;
    String battle_text;
    boolean just_start;

    public BattleHandler() {
        sinestro = new Sinestro();
        hal = new Hal();
        just_start = true;
    }

    LinkedList<abstract_choice> choices() {
        if (sinestro.isDead()) {
            return new end_scene().load();
        } else if (hal.isDead()) {
            return new LinkedList<abstract_choice>() {{
                add(new fail_choice());
            }};
        } else {
            LinkedList<Entry> entry_list = hal.moves();
            LinkedList<abstract_choice> res = new LinkedList<abstract_choice>();
            for (int i = 0; i < entry_list.size(); i++) {
                Entry e = entry_list.get(i);
                res.add(new battle_choice(e.text, e.number, this));
            }
            return res;
        }
    }

    String status() {
        StringBuilder sb = new StringBuilder();
        sb.append("魔王\nHP: ").append(sinestro.life).append(" / ").append(sinestro.max_life).append("\n");
        sb.append("\n\n");
        for (int i = 0; i < 46; i++) {
            sb.append(" ");
        }
        sb.append("你\n");
        String t = "HP: " + hal.life + " / " + hal.max_life;
        for (int i = 0; i < 48 - t.length(); i++) {
            sb.append(" ");
        }
        sb.append(t).append("\n");
        sb.append("\n\n");
        return sb.toString();
    }

    String first_round() {
        just_start = false;
        return status() + "这场决定大陆未来的战斗，开始了！";
    }

    public String round() {
        if (just_start) {
            return first_round();
        } else {
            StringBuilder sb = new StringBuilder();
            if (sinestro.isDead()) {
                sb.append(status());
                sb.append(battle_text).append("\n");
                sb.append("魔王倒下了！");
            } else {
                String t=sinestro.take_act(hal);
                sb.append(status());
                sb.append(battle_text).append("\n");
                sb.append(t);
                if (hal.isDead()) {
                    sb.append("\n你被打败了！");
                }
            }
            return sb.toString();
        }
    }
}
