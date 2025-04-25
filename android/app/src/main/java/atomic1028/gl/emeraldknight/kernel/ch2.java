package atomic1028.gl.emeraldknight.kernel;

import java.util.LinkedList;

class c2_1_1 extends abstract_choice {
    public c2_1_1() {
        super("2-4");
    }

    @Override
    public boolean show() {
        return Constant.kernel.getPara(Constant.TEMPORARY) % 2 == 0;
    }

    @Override
    public void chosen() {
        Constant.kernel.offsetPara(Constant.KNOWLEDGE, 1);
        Constant.kernel.offsetPara(Constant.TEMPORARY, 1);
        super.chosen();
    }
}

class c2_1_2 extends abstract_choice {
    public c2_1_2() {
        super("2-5");
    }

    @Override
    public boolean show() {
        return (Constant.kernel.getPara(Constant.TEMPORARY) >> 1) % 2 == 0;
    }

    @Override
    public void chosen() {
        Constant.kernel.offsetPara(Constant.KNOWLEDGE, 1);
        Constant.kernel.offsetPara(Constant.TEMPORARY, 2);
        super.chosen();
    }
}

class c2_1_3 extends abstract_choice {
    public c2_1_3() {
        super("2-6");
    }

    @Override
    public boolean show() {
        return (Constant.kernel.getPara(Constant.TEMPORARY) >> 2) % 2 == 0;
    }

    @Override
    public void chosen() {
        Constant.kernel.offsetPara(Constant.KNOWLEDGE, 1);
        Constant.kernel.offsetPara(Constant.TEMPORARY, 4);
        super.chosen();
    }
}

class c2_1_4 extends abstract_choice {
    public c2_1_4() {
        super("2-7");
    }

    @Override
    public boolean show() {
        return Constant.kernel.getPara(Constant.TEMPORARY) == 7;
    }

    @Override
    public void chosen() {
        Constant.kernel.offsetPara(Constant.KNOWLEDGE, 1);
        Constant.kernel.setPara(Constant.TEMPORARY, 0);
        super.chosen();
    }
}

class c2_2_1 extends abstract_choice {
    public c2_2_1() {
        super("2-8");
    }

    @Override
    public boolean show() {
        return Constant.kernel.getPara(Constant.TEAMMATE) == Constant.OLIVER_CODE;
    }
}

class c2_2_2 extends abstract_choice {
    public c2_2_2() {
        super("2-9");
    }

    @Override
    public boolean show() {
        return Constant.kernel.getPara(Constant.TEAMMATE) != Constant.OLIVER_CODE;
    }
}

class c2_3_1 extends abstract_choice {
    public c2_3_1() {
        super("2-24");
    }

    @Override
    public boolean show() {
        return Constant.kernel.getPara(Constant.SWORD_HOT_TIME) == 3;
    }

    @Override
    public void chosen() {
        Constant.kernel.offsetPara(Constant.SWORD_HOT_TIME, 1);
        super.chosen();
    }
}

class c2_3_2 extends abstract_choice {
    public c2_3_2() {
        super("2-25");
    }

    @Override
    public boolean show() {
        return Constant.kernel.getPara(Constant.SWORD_HOT_TIME) == 1;
    }
}

class c2_3_3 extends abstract_choice {
    public c2_3_3() {
        super("7-1");
    }

    @Override
    public boolean show() {
        return Constant.kernel.readPara("end-10") == 1;
    }
}

class c2_7_1 extends abstract_choice {
    public c2_7_1() {
        super("3-2");
    }
}

class c2_8_1 extends abstract_choice {
    public c2_8_1() {
        super("2-10");
    }
}

class c2_8_2 extends abstract_choice {
    public c2_8_2() {
        super("2-11");
    }
}

class c2_8_3 extends abstract_choice {
    public c2_8_3() {
        super("2-12");
    }

    @Override
    public void chosen() {
        Constant.kernel.offsetPara(Constant.OLIVER_LOVE, 3);
        super.chosen();
    }
}

class c2_9_1 extends abstract_choice {
    public c2_9_1() {
        super("2-20");
    }

    @Override
    public String text() {
        return "我走了，去翻龙骨雪山";
    }
}

class c2_9_2 extends abstract_choice {
    public c2_9_2() {
        super("2-21");
    }
}

class c2_9_3 extends abstract_choice {
    public c2_9_3() {
        super("2-19");
    }
}

class c2_10_1 extends abstract_choice {
    public c2_10_1() {
        super("2-13");
    }
}

class c2_10_2 extends abstract_choice {
    public c2_10_2() {
        super("2-14");
    }

    @Override
    public void chosen() {
        Constant.kernel.offsetPara(Constant.KNOWLEDGE, 2);
        super.chosen();
    }
}

class c2_11_1 extends abstract_choice {
    public c2_11_1() {
        super("2-17");
    }

    @Override
    public boolean show() {
        return Constant.kernel.getPara(Constant.TEMPORARY) % 2 == 0;
    }

    @Override
    public void chosen() {
        Constant.kernel.offsetPara(Constant.TEMPORARY, 1);
        Constant.kernel.offsetPara(Constant.KNOWLEDGE, 1);
        super.chosen();
    }
}

class c2_11_2 extends abstract_choice {
    public c2_11_2() {
        super("2-18");
    }

    @Override
    public boolean show() {
        return (Constant.kernel.getPara(Constant.TEMPORARY) >> 1) % 2 == 0;
    }

    @Override
    public void chosen() {
        Constant.kernel.offsetPara(Constant.TEMPORARY, 2);
        super.chosen();
    }
}

class c2_11_3 extends abstract_choice {
    public c2_11_3() {
        super("2-10");
    }

    @Override
    public boolean show() {
        return Constant.kernel.getPara(Constant.TEMPORARY) == 3;
    }

    @Override
    public void chosen() {
        Constant.kernel.setPara(Constant.TEMPORARY, 0);
        super.chosen();
    }
}

class c2_14_1 extends abstract_choice {
    public c2_14_1() {
        super("2-15");
    }
}

class c2_14_2 extends abstract_choice {
    public c2_14_2() {
        super("2-33");
    }

    @Override
    public String text() {
        return "它是不是有什么不同寻常的地方";
    }

    @Override
    public boolean show() {
        return Constant.kernel.getPara(Constant.SWORD_HOT_TIME) > 0;
    }

    @Override
    public void chosen() {
        Constant.kernel.offsetPara(Constant.INTELLIGENCE, 2);
        super.chosen();
    }
}

class c2_15_1 extends abstract_choice {
    public c2_15_1() {
        super("2-16");
    }

    @Override
    public void chosen() {
        Constant.kernel.setPara(Constant.TEAMMATE, 0);
        super.chosen();
    }
}

class c2_16_1 extends abstract_choice {
    public c2_16_1() {
        super("3-3");
    }

    @Override
    public void chosen() {
        Constant.kernel.offsetPara(Constant.KNOWLEDGE, 2);
        super.chosen();
    }
}

class c2_20_1 extends abstract_choice {
    public c2_20_1() {
        super("2-22");
    }

    @Override
    public void chosen() {
        Constant.kernel.offsetPara(Constant.KNOWLEDGE, 3);
        super.chosen();
    }
}

class c2_20_2 extends abstract_choice {
    public c2_20_2() {
        super("2-23");
    }
}

class c2_24_1 extends abstract_choice {
    public c2_24_1() {
        super("2-26");
    }
}

class c2_24_2 extends abstract_choice {
    public c2_24_2() {
        super("2-27");
    }

    @Override
    public String text() {
        return "这下面是不是有黑暗力量？";
    }

    @Override
    public boolean show() {
        return Constant.kernel.getPara(Constant.KNOWLEDGE) > 5;
    }

    @Override
    public void chosen() {
        Constant.kernel.offsetPara(Constant.INTELLIGENCE, 2);
        super.chosen();
    }
}

class c2_25_1 extends abstract_choice {
    public c2_25_1() {
        super("2-28");
    }
}

class c2_28_1 extends abstract_choice {
    public c2_28_1() {
        super("2-29");
    }
}

class c2_28_2 extends abstract_choice {
    public c2_28_2() {
        super("2-30");
    }

    @Override
    public void chosen() {
        Constant.kernel.offsetPara(Constant.INTELLIGENCE, 1);
        super.chosen();
    }
}

class c2_30_1 extends abstract_choice {
    public c2_30_1() {
        super("2-31");
    }
}

class c2_30_2 extends abstract_choice {
    public c2_30_2() {
        super("2-32");
    }

    @Override
    public void chosen() {
        Constant.kernel.offsetPara(Constant.INTELLIGENCE, -1);
        super.chosen();
    }
}

class c2_31_1 extends abstract_choice {
    public c2_31_1() {
        super("3-4");
    }
}

class s2_1 extends abstract_scene {
    public s2_1() {
        super(new LinkedList<abstract_choice>() {{
            add(new c2_1_1());
            add(new c2_1_2());
            add(new c2_1_3());
            add(new c2_1_4());
        }});
    }
}

class s2_2 extends abstract_scene {
    public s2_2() {
        super(new LinkedList<abstract_choice>() {{
            add(new c2_2_1());
            add(new c2_2_2());
        }});
    }
}

class s2_3 extends abstract_scene {
    public s2_3() {
        super(new LinkedList<abstract_choice>() {{
            add(new c2_3_1());
            add(new c2_3_2());
            add(new c2_3_3());
        }});
    }
}

class s2_7 extends abstract_scene {
    public s2_7() {
        super(new LinkedList<abstract_choice>() {{
            add(new c2_7_1());
        }});
    }
}

class s2_8 extends abstract_scene {
    public s2_8() {
        super(new LinkedList<abstract_choice>() {{
            add(new c2_8_1());
            add(new c2_8_2());
        }});
    }

    @Override
    LinkedList<abstract_choice> load() {
        if ((Constant.kernel.getPara(Constant.KNOWLEDGE) == 4) && (!Constant.kernel.getScene().equals("2-12"))) {
            return new LinkedList<abstract_choice>() {{
                add(new c2_8_3());
            }};
        } else {
            return super.load();
        }
    }
}

class s2_9 extends abstract_scene {
    public s2_9() {
        super(new LinkedList<abstract_choice>() {{
            add(new c2_9_1());
            add(new c2_9_2());
        }});
    }

    @Override
    LinkedList<abstract_choice> load() {
        if ((Constant.kernel.getPara(Constant.KNOWLEDGE)) == 1 && (Constant.kernel.getScene().equals("2-19"))) {
            return new LinkedList<abstract_choice>() {{
                add(new c2_9_3());
            }};
        } else {
            return super.load();
        }
    }
}

class s2_10 extends abstract_scene {
    public s2_10() {
        super(new LinkedList<abstract_choice>() {{
            add(new c2_10_1());
            add(new c2_10_2());
        }});
    }
}

class s2_11 extends abstract_scene {
    public s2_11() {
        super(new LinkedList<abstract_choice>() {{
            add(new c2_11_1());
            add(new c2_11_2());
            add(new c2_11_3());
        }});
    }
}

class s2_14 extends abstract_scene {
    public s2_14() {
        super(new LinkedList<abstract_choice>() {{
            add(new c2_14_1());
            add(new c2_14_2());
        }});
    }
}

class s2_20 extends abstract_scene {
    public s2_20() {
        super(new LinkedList<abstract_choice>() {{
            add(new c2_20_1());
            add(new c2_20_2());
        }});
    }
}

class s2_24 extends abstract_scene {
    public s2_24() {
        super(new LinkedList<abstract_choice>() {{
            add(new c2_24_1());
            add(new c2_24_2());
        }});
    }
}

class s2_28 extends abstract_scene {
    public s2_28() {
        super(new LinkedList<abstract_choice>() {{
            add(new c2_28_1());
            add(new c2_28_2());
        }});
    }
}

class s2_30 extends abstract_scene {
    public s2_30() {
        super(new LinkedList<abstract_choice>() {{
            add(new c2_30_1());
            add(new c2_30_2());
        }});
    }
}
