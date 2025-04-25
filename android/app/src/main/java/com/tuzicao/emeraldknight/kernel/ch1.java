package com.tuzicao.emeraldknight.kernel;

import java.util.LinkedList;

class c1_1_1 extends abstract_choice {
    public c1_1_1() {
        super("1-2");
    }

    @Override
    public void chosen() {
        Constant.kernel.offsetPara(Constant.SWORD_HOT_TIME, 1);
        super.chosen();
    }
}

class c1_1_2 extends abstract_choice {
    public c1_1_2() {
        super("1-3");
    }
}

class c1_1_3 extends abstract_choice {
    public c1_1_3() {
        super("1-4");
    }
}

class c1_2_1 extends abstract_choice {
    public c1_2_1() {
        super("1-5");
    }

    @Override
    public void chosen() {
        Constant.kernel.offsetPara(Constant.SWORD_HOT_TIME, 1);
        super.chosen();
    }
}

class c1_3_1 extends abstract_choice {
    public c1_3_1() {
        super("1-6");
    }
}

class c1_3_2 extends abstract_choice {
    public c1_3_2() {
        super("1-7");
    }
}

class c1_3_3 extends abstract_choice {
    public c1_3_3() {
        super("1-8");
    }
}

class c1_4_1 extends abstract_choice {
    public c1_4_1() {
        super("1-9");
    }

    @Override
    public void chosen() {
        Constant.kernel.offsetPara(Constant.SINESTRO_TAME, -1);
        super.chosen();
    }
}

class c1_4_2 extends abstract_choice {
    public c1_4_2() {
        super("1-10");
    }

    @Override
    public void chosen() {
        Constant.kernel.offsetPara(Constant.SINESTRO_LOVE, 1);
        super.chosen();
    }
}

class c1_4_3 extends abstract_choice {
    public c1_4_3() {
        super("1-11");
    }
}

class c1_5_1 extends abstract_choice {
    public c1_5_1() {
        super("1-12");
    }
}

class c1_5_2 extends abstract_choice {
    public c1_5_2() {
        super("1-13");
    }

    @Override
    public void chosen() {
        Constant.kernel.offsetPara(Constant.KNOWLEDGE, 1);
        super.chosen();
    }
}

class c1_6_1 extends abstract_choice {
    public c1_6_1() {
        super("1-52");
    }
}

class c1_6_2 extends abstract_choice {
    public c1_6_2() {
        super("1-18");
    }

    @Override
    public void chosen() {
        Constant.kernel.offsetPara(Constant.KNOWLEDGE, 3);
        super.chosen();
    }
}

class c1_7_1 extends abstract_choice {
    public c1_7_1() {
        super("1-14");
    }

    @Override
    public void chosen() {
        Constant.kernel.offsetPara(Constant.KNOWLEDGE, 2);
        super.chosen();
    }
}

class c1_7_2 extends abstract_choice {
    public c1_7_2() {
        super("1-17");
    }
}

class c1_8_1 extends abstract_choice {
    public c1_8_1() {
        super("1-16");
    }

    @Override
    public String text() {
        return "找人带路去龙骨雪山";
    }
}

class c1_11_1 extends abstract_choice {
    public c1_11_1() {
        super("1-55");
    }

    @Override
    public void chosen() {
        Constant.kernel.offsetPara(Constant.SINESTRO_LOVE, -1);
        super.chosen();
    }
}

class c1_11_2 extends abstract_choice {
    public c1_11_2() {
        super("1-56");
    }
}

class c1_11_3 extends abstract_choice {
    public c1_11_3() {
        super("1-57");
    }

    @Override
    public void chosen() {
        Constant.kernel.offsetPara(Constant.SINESTRO_TAME, 1);
        super.chosen();
    }
}

class c1_11_4 extends abstract_choice {
    public c1_11_4() {
        super("1-58");
    }
}

class c1_12_0 extends abstract_choice {
    public c1_12_0() {
        super("1-24");
    }
}

class c1_12_1 extends abstract_choice {
    public c1_12_1() {
        super("1-20");
    }

    @Override
    public String text() {
        return "带有火焰纹路的红晶石";
    }

    @Override
    public void chosen() {
        Constant.kernel.setPara(Constant.PROPS, 1);
        super.chosen();
    }
}

class c1_12_2 extends abstract_choice {
    public c1_12_2() {
        super("1-21");
    }

    @Override
    public String text() {
        return "带有雪花纹路的蓝晶石";
    }

    @Override
    public void chosen() {
        Constant.kernel.setPara(Constant.PROPS, 2);
        super.chosen();
    }
}

class c1_12_3 extends abstract_choice {
    public c1_12_3() {
        super("1-22");
    }

    @Override
    public String text() {
        return "带有漩涡纹路的紫晶石";
    }

    @Override
    public void chosen() {
        Constant.kernel.setPara(Constant.PROPS, 3);
        super.chosen();
    }
}

class c1_12_4 extends abstract_choice {
    public c1_12_4() {
        super("1-23");
    }

    @Override
    public String text() {
        return "带有草叶纹路的绿晶石";
    }

    @Override
    public void chosen() {
        Constant.kernel.setPara(Constant.PROPS, 4);
        super.chosen();
    }
}

class c1_14_1 extends abstract_choice {
    public c1_14_1() {
        super("1-47");
    }
}

class c1_14_2 extends abstract_choice {
    public c1_14_2() {
        super("1-48");
    }

    @Override
    public void chosen() {
        Constant.kernel.offsetPara(Constant.BARRY_LOVE, 5);
        super.chosen();
    }
}

class c1_14_3 extends abstract_choice {
    public c1_14_3() {
        super("1-49");
    }
}

class c1_15_1 extends abstract_choice {
    public c1_15_1() {
        super("1-19");
    }

    @Override
    public String text() {
        return "重选";
    }
}

class c1_16_1 extends abstract_choice {
    public c1_16_1() {
        super("2-1");
    }
}

class c1_16_2 extends abstract_choice {
    public c1_16_2() {
        super("2-2");
    }
}

class c1_16_3 extends abstract_choice {
    public c1_16_3() {
        super("2-3");
    }
}

class c1_17_1 extends abstract_choice {
    public c1_17_1() {
        super("end-1");
    }

    @Override
    public String text() {
        return "不了";
    }
}

class c1_17_2 extends abstract_choice {
    public c1_17_2() {
        super("1-19");
    }
}

class c1_19_1 extends abstract_choice {
    public c1_19_1() {
        super("1-15");
    }
}

class c1_24_0 extends abstract_choice {
    public c1_24_0() {
        super("1-29");
    }
}

class c1_24_1 extends abstract_choice {
    public c1_24_1() {
        super("1-25");
    }

    @Override
    public String text() {
        return "看看书架";
    }

    @Override
    public void chosen() {
        Constant.kernel.offsetPara(Constant.PROPS, 8);
        super.chosen();
    }
}

class c1_24_2 extends abstract_choice {
    public c1_24_2() {
        super("1-26");
    }

    @Override
    public String text() {
        return "看看卷轴";
    }

    @Override
    public void chosen() {
        Constant.kernel.offsetPara(Constant.PROPS, 16);
        super.chosen();
    }
}

class c1_24_3 extends abstract_choice {
    public c1_24_3() {
        super("1-27");
    }

    @Override
    public String text() {
        return "看看挂毯";
    }

    @Override
    public void chosen() {
        Constant.kernel.offsetPara(Constant.PROPS, 24);
        super.chosen();
    }
}

class c1_24_4 extends abstract_choice {
    public c1_24_4() {
        super("1-28");
    }

    @Override
    public String text() {
        return "看看徽章";
    }

    @Override
    public void chosen() {
        Constant.kernel.offsetPara(Constant.PROPS, 32);
        super.chosen();
    }
}

class c1_24_5 extends abstract_choice {
    public c1_24_5() {
        super("1-29");
    }

    @Override
    public void chosen() {
        Constant.kernel.offsetPara(Constant.INTELLIGENCE, -2);
        super.chosen();
    }
}

class c1_29_1 extends abstract_choice {
    public c1_29_1() {
        super("1-30");
    }
}

class c1_29_2 extends abstract_choice {
    public c1_29_2() {
        super("1-34");
    }

    @Override
    public boolean show() {
        return Constant.kernel.getPara(Constant.PROPS) >> 3 == 1;
    }

    @Override
    public void chosen() {
        Constant.kernel.setPara(Constant.BRUCE_SHOW_UP, 1);
        super.chosen();
    }
}

class c1_31_1 extends abstract_choice {
    public c1_31_1() {
        super("1-32");
    }

    @Override
    public boolean show() {
        return Constant.kernel.getPara(Constant.BRUCE_LOVE) >= 0;
    }
}

class c1_31_2 extends abstract_choice {
    public c1_31_2() {
        super("1-33");
    }

    @Override
    public void chosen() {
        Constant.kernel.setPara(Constant.PROPS, 0);
        super.chosen();
    }
}

class c1_34_1 extends abstract_choice {
    public c1_34_1() {
        super("1-35");
    }

    @Override
    public String text() {
        return "这是什么地方？";
    }

    @Override
    public boolean show() {
        return Constant.kernel.getPara(Constant.TEMPORARY) < 2;
    }

    @Override
    public void chosen() {
        Constant.kernel.offsetPara(Constant.TEMPORARY, 1);
        super.chosen();
    }
}

class c1_34_2 extends abstract_choice {
    public c1_34_2() {
        super("1-36");
    }

    @Override
    public boolean show() {
        return Constant.kernel.getPara(Constant.TEMPORARY) < 2;
    }

    @Override
    public void chosen() {
        Constant.kernel.offsetPara(Constant.TEMPORARY, 1);
        super.chosen();
    }
}

class c1_34_3 extends abstract_choice {
    public c1_34_3() {
        super("1-37");
    }

    @Override
    public boolean show() {
        return Constant.kernel.getPara(Constant.TEMPORARY) == 2;
    }

    @Override
    public void chosen() {
        Constant.kernel.setPara(Constant.TEMPORARY, 0);
        super.chosen();
    }
}

class c1_37_1 extends abstract_choice {
    public c1_37_1() {
        super("1-38");
    }

    @Override
    public void chosen() {
        Constant.kernel.offsetPara(Constant.BRUCE_LOVE, -5);
        super.chosen();
    }
}

class c1_37_2 extends abstract_choice {
    public c1_37_2() {
        super("1-39");
    }

    @Override
    public void chosen() {
        Constant.kernel.offsetPara(Constant.BRUCE_LOVE, 1);
        super.chosen();
    }
}

class c1_38_1 extends abstract_choice {
    public c1_38_1() {
        super("1-31");
    }

    @Override
    public String text() {
        return "四处走走";
    }
}

class c1_39_1 extends abstract_choice {
    public c1_39_1() {
        super("1-40");
    }

    @Override
    public String text() {
        return "四处走走";
    }

    @Override
    public boolean show() {
        return Constant.kernel.getPara(Constant.KNOWLEDGE) >= 1;
    }
}

class c1_39_2 extends abstract_choice {
    public c1_39_2() {
        super("1-31");
    }

    @Override
    public String text() {
        return "四处走走";
    }

    @Override
    public boolean show() {
        return Constant.kernel.getPara(Constant.KNOWLEDGE) < 1;
    }
}

class c1_40_1 extends abstract_choice {
    public c1_40_1() {
        super("1-41");
    }

    @Override
    public String text() {
        return "仔细看看";
    }

    @Override
    public void chosen() {
        Constant.kernel.offsetPara(Constant.SWORD_HOT_TIME, 1);
        super.chosen();
    }
}

class c1_40_2 extends abstract_choice {
    public c1_40_2() {
        super("1-45");
    }

    @Override
    public void chosen() {
        Constant.kernel.offsetPara(Constant.BRUCE_LOVE, 2);
        super.chosen();
    }
}

class c1_40_3 extends abstract_choice {
    public c1_40_3() {
        super("1-31");
    }

    @Override
    public String text() {
        return "起身走开";
    }
}

class c1_41_1 extends abstract_choice {
    public c1_41_1() {
        super("1-42");
    }

    @Override
    public void chosen() {
        Constant.kernel.offsetPara(Constant.KNOWLEDGE, 5);
        super.chosen();
    }
}

class c1_41_2 extends abstract_choice {
    public c1_41_2() {
        super("1-43");
    }

    @Override
    public void chosen() {
        Constant.kernel.setPara(Constant.PROPS, 0);
        super.chosen();
    }
}

class c1_41_3 extends abstract_choice {
    public c1_41_3() {
        super("1-44");
    }

    @Override
    public boolean show() {
        return Constant.kernel.getPara(Constant.BRUCE_SHOW_UP) == 0;
    }

    @Override
    public void chosen() {
        Constant.kernel.offsetPara(Constant.BRUCE_LOVE, 4);
        super.chosen();
    }
}

class c1_41_4 extends abstract_choice {
    public c1_41_4() {
        super("1-46");
    }

    @Override
    public String text() {
        return "那个人呢？";
    }

    @Override
    public boolean show() {
        return Constant.kernel.getPara(Constant.BRUCE_SHOW_UP) == 1;
    }

    @Override
    public void chosen() {
        Constant.kernel.offsetPara(Constant.BRUCE_LOVE, 10);
        Constant.kernel.setPara(Constant.BRUCE_INTRODUCE, 1);
        super.chosen();
    }
}

class c1_49_1 extends abstract_choice {
    public c1_49_1() {
        super("end-1");
    }

    @Override
    public String text() {
        return "我还不够强";
    }
}

class c1_49_2 extends abstract_choice {
    public c1_49_2() {
        super("1-50");
    }

    @Override
    public String text() {
        return "知道的太少";
    }

    @Override
    public boolean show() {
        return Constant.kernel.getPara(Constant.SWORD_HOT_TIME) >= 1;
    }
}

class c1_49_3 extends abstract_choice {
    public c1_49_3() {
        super("1-51");
    }

    @Override
    public void chosen() {
        Constant.kernel.offsetPara(Constant.KNOWLEDGE, 1);
        super.chosen();
    }
}

class c1_52_1 extends abstract_choice {
    public c1_52_1() {
        super("1-53");
    }

    @Override
    public void chosen() {
        Constant.kernel.offsetPara(Constant.KNOWLEDGE, 1);
        super.chosen();
    }
}

class c1_52_2 extends abstract_choice {
    public c1_52_2() {
        super("1-54");
    }

    @Override
    public void chosen() {
        Constant.kernel.setPara(Constant.TEAMMATE, Constant.OLIVER_CODE);
        super.chosen();
    }
}

class c1_58_1 extends abstract_choice {
    public c1_58_1() {
        super("1-59");
    }

    @Override
    public String text() {
        return "你就这么在野外点火的？";
    }

    @Override
    public boolean show() {
        return Constant.kernel.getPara(Constant.SINESTRO_TAME) >= 0;
    }

    @Override
    public void chosen() {
        Constant.kernel.offsetPara(Constant.SINESTRO_TAME, 2);
        super.chosen();
    }
}

class c1_58_2 extends abstract_choice {
    public c1_58_2() {
        super("1-60");
    }

    @Override
    public void chosen() {
        Constant.kernel.offsetPara(Constant.SINESTRO_TAME, -1);
        super.chosen();
    }
}

class c1_58_3 extends abstract_choice {
    public c1_58_3() {
        super("1-61");
    }

    @Override
    public boolean show() {
        return Constant.kernel.getPara(Constant.SINESTRO_LOVE) >= 0;
    }

    @Override
    public void chosen() {
        Constant.kernel.offsetPara(Constant.SINESTRO_LOVE, -1);
        super.chosen();
    }
}

class c1_58_4 extends abstract_choice {
    public c1_58_4() {
        super("1-62");
    }
}

class c1_62_1 extends abstract_choice {
    public c1_62_1() {
        super("1-63");
    }

    @Override
    public String text() {
        return "把他捆上";
    }
}

class c1_62_2 extends abstract_choice {
    public c1_62_2() {
        super("1-64");
    }
}

class c1_63_1 extends abstract_choice {
    public c1_63_1() {
        super("1-72");
    }
}

class c1_63_2 extends abstract_choice {
    public c1_63_2() {
        super("end-3");
    }

    @Override
    public String text() {
        return "拒绝";
    }
}

class c1_64_1 extends abstract_choice {
    public c1_64_1() {
        super("1-65");
    }

    @Override
    public void chosen() {
        Constant.kernel.setPara(Constant.TEMPORARY, 1);
        super.chosen();
    }
}

class c1_64_2 extends abstract_choice {
    public c1_64_2() {
        super("1-66");
    }
}

class c1_66_1 extends abstract_choice {
    public c1_66_1() {
        super("1-67");
    }

    @Override
    public String text() {
        return "质问他是否与失踪有关";
    }

    @Override
    public boolean show() {
        return Constant.kernel.getPara(Constant.TEMPORARY) == 1;
    }

    @Override
    public void chosen() {
        Constant.kernel.setPara(Constant.TEMPORARY, 0);
        super.chosen();
    }
}

class c1_66_2 extends abstract_choice {
    public c1_66_2() {
        super("1-68");
    }
}

class c1_67_1 extends abstract_choice {
    public c1_67_1() {
        super("1-69");
    }

    @Override
    public boolean show() {
        return Constant.kernel.getPara(Constant.TEMPORARY) < 2;
    }

    @Override
    public void chosen() {
        Constant.kernel.offsetPara(Constant.TEMPORARY, 1);
        super.chosen();
    }
}

class c1_67_2 extends abstract_choice {
    public c1_67_2() {
        super("1-70");
    }

    @Override
    public boolean show() {
        return Constant.kernel.getPara(Constant.TEMPORARY) < 2;
    }

    @Override
    public void chosen() {
        Constant.kernel.offsetPara(Constant.TEMPORARY, 1);
        super.chosen();
    }
}

class c1_67_3 extends abstract_choice {
    public c1_67_3() {
        super("1-71");
    }

    @Override
    public boolean show() {
        return Constant.kernel.getPara(Constant.TEMPORARY) == 2;
    }

    @Override
    public void chosen() {
        Constant.kernel.setPara(Constant.TEMPORARY, 0);
        super.chosen();
    }
}

class c1_71_1 extends abstract_choice {
    public c1_71_1() {
        super("end-2");
    }

    @Override
    public String text() {
        return "杀了他";
    }
}

class c1_72_1 extends abstract_choice {
    public c1_72_1() {
        super("1-73");
    }

    @Override
    public String text() {
        return "吻他";
    }
}

class c1_72_2 extends abstract_choice {
    public c1_72_2() {
        super("1-73");
    }

    @Override
    public String text() {
        return "摸他";
    }

    @Override
    public void chosen() {
        Constant.kernel.offsetPara(Constant.TEMPORARY, 2);
        super.chosen();
    }
}

class c1_73_1 extends abstract_choice {
    public c1_73_1() {
        super("1-74");
    }

    @Override
    public String text() {
        return "地上";
    }

    @Override
    public void chosen() {
        Constant.kernel.offsetPara(Constant.TEMPORARY, 3);
        super.chosen();
    }
}

class c1_73_2 extends abstract_choice {
    public c1_73_2() {
        super("1-74");
    }

    @Override
    public String text() {
        return "墙上";
    }
}

class c1_74_1 extends abstract_choice {
    public c1_74_1() {
        super("1-75");
    }

    @Override
    public String text() {
        return "里面";
    }

    @Override
    public void chosen() {
        Constant.kernel.offsetPara(Constant.TEMPORARY, 5);
        super.chosen();
    }
}

class c1_74_2 extends abstract_choice {
    public c1_74_2() {
        super("1-75");
    }

    @Override
    public String text() {
        return "外面";
    }
}

class c1_75_1 extends abstract_choice {
    public c1_75_1() {
        super("1-76");
    }

    @Override
    public String text() {
        return "体验如何";
    }

    @Override
    public void chosen() {
        Constant.kernel.setPara(Constant.TEMPORARY, 0);
        Constant.kernel.offsetPara(Constant.SINESTRO_LOVE, 2);
        super.chosen();
    }
}

class c1_75_2 extends abstract_choice {
    public c1_75_2() {
        super("1-77");
    }

    @Override
    public String text() {
        return "体验如何";
    }

    @Override
    public void chosen() {
        Constant.kernel.setPara(Constant.TEMPORARY, 0);
        super.chosen();
    }
}

class c1_75_3 extends abstract_choice {
    public c1_75_3() {
        super("end-4");
    }

    @Override
    public String text() {
        return "体验如何";
    }
}

class c1_76_1 extends abstract_choice {
    public c1_76_1() {
        super("1-78");
    }

    @Override
    public void chosen() {
        Constant.kernel.offsetPara(Constant.SINESTRO_TAME, -1);
        super.chosen();
    }
}

class c1_76_2 extends abstract_choice {
    public c1_76_2() {
        super("1-79");
    }
}

class c1_76_3 extends abstract_choice {
    public c1_76_3() {
        super("1-80");
    }

    @Override
    public void chosen() {
        Constant.kernel.offsetPara(Constant.SINESTRO_TAME, 1);
        Constant.kernel.offsetPara(Constant.SINESTRO_LOVE, 1);
        super.chosen();
    }
}

class c1_76_4 extends abstract_choice {
    public c1_76_4() {
        super("1-81");
    }
}

class c1_81_1 extends abstract_choice {
    public c1_81_1() {
        super("3-1");
    }

}


class s1_1 extends abstract_scene {
    public s1_1() {
        super(new LinkedList<abstract_choice>() {{
            add(new c1_1_1());
            add(new c1_1_2());
            add(new c1_1_3());
        }});
    }
}

class s1_2 extends abstract_scene {
    public s1_2() {
        super(new LinkedList<abstract_choice>() {{
            add(new c1_2_1());
            add(new c1_1_2());
        }});
    }
}

class s1_3 extends abstract_scene {
    public s1_3() {
        super(new LinkedList<abstract_choice>() {{
            add(new c1_3_1());
            add(new c1_3_2());
            add(new c1_3_3());
        }});
    }
}

class s1_4 extends abstract_scene {
    public s1_4() {
        super(new LinkedList<abstract_choice>() {{
            add(new c1_4_1());
            add(new c1_4_2());
            add(new c1_4_3());
        }});
    }
}

class s1_5 extends abstract_scene {
    public s1_5() {
        super(new LinkedList<abstract_choice>() {{
            add(new c1_5_1());
            add(new c1_5_2());
        }});
    }
}

class s1_6 extends abstract_scene {
    public s1_6() {
        super(new LinkedList<abstract_choice>() {{
            add(new c1_6_1());
            add(new c1_6_2());
        }});
    }
}

class s1_7 extends abstract_scene {
    public s1_7() {
        super(new LinkedList<abstract_choice>() {{
            add(new c1_7_1());
            add(new c1_7_2());
        }});
    }
}

class s1_8 extends abstract_scene {
    public s1_8() {
        super(new LinkedList<abstract_choice>() {{
            add(new c1_6_1());
            add(new c1_8_1());
        }});
    }
}

class s1_11 extends abstract_scene {
    public s1_11() {
        super(new LinkedList<abstract_choice>() {{
            add(new c1_11_1());
            add(new c1_11_2());
            add(new c1_11_3());
        }});
    }
}

class s1_12 extends abstract_scene {
    public s1_12() {
        super(new LinkedList<abstract_choice>() {{
            add(new c1_12_1());
            add(new c1_12_2());
            add(new c1_12_3());
            add(new c1_12_4());
        }});
    }
}

class s1_14 extends abstract_scene {
    public s1_14() {
        super(new LinkedList<abstract_choice>() {{
            add(new c1_14_1());
            add(new c1_14_2());
            add(new c1_14_3());
        }});
    }
}

class s1_16 extends abstract_scene {
    public s1_16() {
        super(new LinkedList<abstract_choice>() {{
            add(new c1_16_1());
            add(new c1_16_2());
        }});
    }
}

class s1_17 extends abstract_scene {
    public s1_17() {
        super(new LinkedList<abstract_choice>() {{
            add(new c1_17_1());
            add(new c1_17_2());
        }});
    }
}

class s1_19 extends abstract_scene {
    public s1_19() {
        super(new LinkedList<abstract_choice>() {{
            add(new c1_8_1());
            add(new c1_19_1());
        }});
    }
}

class s1_24 extends abstract_scene {
    public s1_24() {
        super(new LinkedList<abstract_choice>() {{
            add(new c1_24_1());
            add(new c1_24_2());
            add(new c1_24_3());
            add(new c1_24_4());
            add(new c1_24_5());
        }});
    }
}

class s1_29 extends abstract_scene {
    public s1_29() {
        super(new LinkedList<abstract_choice>() {{
            add(new c1_29_1());
            add(new c1_29_2());
        }});
    }
}

class s1_31 extends abstract_scene {
    public s1_31() {
        super(new LinkedList<abstract_choice>() {{
            add(new c1_31_1());
            add(new c1_31_2());
        }});
    }
}

class s1_34 extends abstract_scene {
    public s1_34() {
        super(new LinkedList<abstract_choice>() {{
            add(new c1_34_1());
            add(new c1_34_2());
        }});
    }
}

class s1_35 extends abstract_scene {
    public s1_35() {
        super(new LinkedList<abstract_choice>() {{
            add(new c1_34_2());
            add(new c1_34_3());
        }});
    }
}

class s1_36 extends abstract_scene {
    public s1_36() {
        super(new LinkedList<abstract_choice>() {{
            add(new c1_34_1());
            add(new c1_34_3());
        }});
    }
}

class s1_37 extends abstract_scene {
    public s1_37() {
        super(new LinkedList<abstract_choice>() {{
            add(new c1_37_1());
            add(new c1_37_2());
        }});
    }
}

class s1_39 extends abstract_scene {
    public s1_39() {
        super(new LinkedList<abstract_choice>() {{
            add(new c1_39_1());
            add(new c1_39_2());
        }});
    }
}

class s1_40 extends abstract_scene {
    @Override
    LinkedList<abstract_choice> load() {
        if (Constant.kernel.getPara(Constant.PROPS) % 8 == 4) {
            return new LinkedList<abstract_choice>() {{
                add(new c1_40_1());
            }};
        } else if (Constant.kernel.getPara(Constant.BRUCE_SHOW_UP) == 1) {
            return new LinkedList<abstract_choice>() {{
                add(new c1_40_2());
            }};
        } else {
            return new LinkedList<abstract_choice>() {{
                add(new c1_40_3());
            }};
        }
    }

}

class s1_41 extends abstract_scene {
    public s1_41() {
        super(new LinkedList<abstract_choice>() {{
            add(new c1_41_4());
            add(new c1_41_3());
        }});
    }
}

class s1_46 extends abstract_scene {
    public s1_46() {
        super(new LinkedList<abstract_choice>() {{
            add(new c1_41_1());
            add(new c1_41_2());
        }});
    }
}

class s1_49 extends abstract_scene {
    public s1_49() {
        super(new LinkedList<abstract_choice>() {{
            add(new c1_49_1());
            add(new c1_49_2());
            add(new c1_49_3());
        }});
    }
}

class s1_52 extends abstract_scene {
    @Override
    LinkedList<abstract_choice> load() {
        if (Constant.kernel.getPara(Constant.KNOWLEDGE) > 0) {
            return new LinkedList<abstract_choice>() {{
                add(new c1_52_1());
            }};
        } else {
            return new LinkedList<abstract_choice>() {{
                add(new c1_52_2());
            }};
        }
    }
}

class s1_58 extends abstract_scene {
    public s1_58() {
        super(new LinkedList<abstract_choice>() {{
            add(new c1_58_1());
            add(new c1_58_2());
            add(new c1_58_3());
        }});
    }
}

class s1_62 extends abstract_scene {
    @Override
    LinkedList<abstract_choice> load() {
        if ((Constant.kernel.getPara(Constant.SINESTRO_LOVE) > 0) || (Constant.kernel.getPara(Constant.SINESTRO_TAME) > 0)) {
            return new LinkedList<abstract_choice>() {{
                add(new c1_62_1());
            }};
        } else {
            return new LinkedList<abstract_choice>() {{
                add(new c1_62_2());
            }};
        }
    }
}

class s1_63 extends abstract_scene {
    public s1_63() {
        super(new LinkedList<abstract_choice>() {{
            add(new c1_63_1());
            add(new c1_63_2());
        }});
    }
}

class s1_64 extends abstract_scene {
    public s1_64() {
        super(new LinkedList<abstract_choice>() {{
            add(new c1_64_1());
            add(new c1_64_2());
        }});
    }
}

class s1_66 extends abstract_scene {
    public s1_66() {
        super(new LinkedList<abstract_choice>() {{
            add(new c1_66_1());
            add(new c1_66_2());
        }});
    }
}

class s1_67 extends abstract_scene {
    public s1_67() {
        super(new LinkedList<abstract_choice>() {{
            add(new c1_67_1());
            add(new c1_67_2());
        }});
    }
}

class s1_69 extends abstract_scene {
    public s1_69() {
        super(new LinkedList<abstract_choice>() {{
            add(new c1_67_2());
            add(new c1_67_3());
        }});
    }
}

class s1_70 extends abstract_scene {
    public s1_70() {
        super(new LinkedList<abstract_choice>() {{
            add(new c1_67_1());
            add(new c1_67_3());
        }});
    }
}

class s1_72 extends abstract_scene {
    public s1_72() {
        super(new LinkedList<abstract_choice>() {{
            add(new c1_72_1());
            add(new c1_72_2());
        }});
    }
}

class s1_73 extends abstract_scene {
    public s1_73() {
        super(new LinkedList<abstract_choice>() {{
            add(new c1_73_1());
            add(new c1_73_2());
        }});
    }
}

class s1_74 extends abstract_scene {
    public s1_74() {
        super(new LinkedList<abstract_choice>() {{
            add(new c1_74_1());
            add(new c1_74_2());
        }});
    }
}

class s1_75 extends abstract_scene {
    @Override
    LinkedList<abstract_choice> load() {
        if (Constant.kernel.getPara(Constant.TEMPORARY) == 10) {
            return new LinkedList<abstract_choice>() {{
                add(new c1_75_1());
            }};
        } else if (Constant.kernel.getPara(Constant.TEMPORARY) >= 5) {
            return new LinkedList<abstract_choice>() {{
                add(new c1_75_2());
            }};
        } else {
            return new LinkedList<abstract_choice>() {{
                add(new c1_75_3());
            }};
        }
    }
}

class s1_76 extends abstract_scene {
    public s1_76() {
        super(new LinkedList<abstract_choice>() {{
            add(new c1_76_1());
            add(new c1_76_2());
            add(new c1_76_3());
        }});
    }
}

