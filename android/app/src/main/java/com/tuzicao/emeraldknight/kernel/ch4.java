package com.tuzicao.emeraldknight.kernel;

import java.util.LinkedList;

class c4_1_1 extends abstract_choice {
    public c4_1_1() {
        super("4-3");
    }
}

class c4_3_1 extends abstract_choice {
    public c4_3_1() {
        super("4-4");
    }
}

class c4_3_2 extends abstract_choice {
    public c4_3_2() {
        super("4-5");
    }

    @Override
    public void chosen() {
        Constant.kernel.offsetPara(Constant.KNOWLEDGE, 5);
        super.chosen();
    }
}

class c4_3_3 extends abstract_choice {
    public c4_3_3() {
        super("4-6");
    }
}

class c4_4_1 extends abstract_choice {
    public c4_4_1() {
        super("end-6");
    }

    @Override
    public String text() {
        return "答应";
    }
}

class c4_4_2 extends abstract_choice {
    public c4_4_2() {
        super("4-7");
    }
}

class c4_5_1 extends abstract_choice {
    public c4_5_1() {
        super("4-7");
    }

    @Override
    public String text() {
        return "出发";
    }
}

class c4_6_1 extends abstract_choice {
    public c4_6_1() {
        super("4-8");
    }

    @Override
    public boolean show() {
        return Constant.kernel.getPara(Constant.PROPS) % 2 == 0;
    }

    @Override
    public void chosen() {
        Constant.kernel.offsetPara(Constant.PROPS, 1);
        super.chosen();
    }
}

class c4_6_2 extends abstract_choice {
    public c4_6_2() {
        super("4-9");
    }

    @Override
    public boolean show() {
        return (Constant.kernel.getPara(Constant.PROPS) >> 1) % 2 == 0;
    }

    @Override
    public void chosen() {
        Constant.kernel.offsetPara(Constant.PROPS, 2);
        super.chosen();
    }
}

class c4_6_3 extends abstract_choice {
    public c4_6_3() {
        super("4-10");
    }

    @Override
    public boolean show() {
        return (Constant.kernel.getPara(Constant.PROPS) >> 2) % 2 == 0;
    }

    @Override
    public void chosen() {
        Constant.kernel.offsetPara(Constant.PROPS, 4);
        super.chosen();
    }
}

class c4_6_4 extends abstract_choice {
    public c4_6_4() {
        super("4-11");
    }

    @Override
    public boolean show() {
        return Constant.kernel.getPara(Constant.PROPS) == 7;
    }

    @Override
    public void chosen() {
        Constant.kernel.setPara(Constant.PROPS, 0);
        Constant.kernel.setPara(Constant.TEAMMATE, Constant.BARRY_CODE);
        Constant.kernel.offsetPara(Constant.BARRY_LOVE, 1);
        super.chosen();
    }
}

class c4_7_1 extends abstract_choice {
    public c4_7_1() {
        super("end-7");
    }

    @Override
    public String text() {
        return "战斗";
    }

    @Override
    public boolean show() {
        return Constant.kernel.getPara(Constant.SINESTRO_LOVE) < 5;
    }

    @Override
    public void chosen() {
        Constant.kernel.setPara(Constant.TEMPORARY, 0);
        super.chosen();
    }
}

class c4_7_2 extends abstract_choice {
    public c4_7_2() {
        super("4-13");
    }

    @Override
    public String text() {
        return "战斗";
    }

    @Override
    public boolean show() {
        return Constant.kernel.getPara(Constant.SINESTRO_LOVE) >= 5;
    }

    @Override
    public void chosen() {
        Constant.kernel.setPara(Constant.TEMPORARY, 0);
        super.chosen();
    }
}

class c4_7_3 extends abstract_choice {
    public c4_7_3() {
        super("end-6");
    }

    @Override
    public String text() {
        return "战斗";
    }

    @Override
    public void chosen() {
        Constant.kernel.setPara(Constant.TEMPORARY, 0);
        super.chosen();
    }
}

class c4_11_1 extends abstract_choice {
    public c4_11_1() {
        super("4-12");
    }

    @Override
    public String text() {
        return "战斗";
    }

    @Override
    public void chosen() {
        Constant.kernel.setPara(Constant.TEMPORARY, 0);
        super.chosen();
    }
}

class c4_11_2 extends abstract_choice {
    public c4_11_2() {
        super("end-6");
    }

    @Override
    public String text() {
        return "战斗";
    }

    @Override
    public void chosen() {
        Constant.kernel.setPara(Constant.TEMPORARY, 0);
        super.chosen();
    }
}

class c4_12_1 extends abstract_choice {
    public c4_12_1() {
        super("5-4");
    }
}

class c4_13_1 extends abstract_choice {
    public c4_13_1() {
        super("4-14");
    }

    @Override
    public void chosen() {
        Constant.kernel.offsetPara(Constant.SINESTRO_LOVE, -1);
        super.chosen();
    }
}

class c4_13_2 extends abstract_choice {
    public c4_13_2() {
        super("4-15");
    }
}

class c4_13_3 extends abstract_choice {
    public c4_13_3() {
        super("4-16");
    }

    @Override
    public void chosen() {
        Constant.kernel.offsetPara(Constant.SINESTRO_TAME, 1);
        super.chosen();
    }
}

class c4_14_1 extends abstract_choice {
    public c4_14_1() {
        super("4-17");
    }

    @Override
    public void chosen() {
        Constant.kernel.offsetPara(Constant.SINESTRO_TAME, -1);
        super.chosen();
    }
}

class c4_14_2 extends abstract_choice {
    public c4_14_2() {
        super("4-18");
    }

    @Override
    public void chosen() {
        Constant.kernel.offsetPara(Constant.SINESTRO_LOVE, 1);
        super.chosen();
    }
}

class c4_14_3 extends abstract_choice {
    public c4_14_3() {
        super("4-19");
    }
}

class c4_14_4 extends abstract_choice {
    public c4_14_4() {
        super("4-20");
    }
}

class c4_20_1 extends abstract_choice {
    public c4_20_1() {
        super("4-29");
    }
}

class c4_20_2 extends abstract_choice {
    public c4_20_2() {
        super("4-22");
    }

    @Override
    public void chosen() {
        Constant.kernel.setPara(Constant.SINESTRO_TAME, 0);
        super.chosen();
    }
}

class c4_21_1 extends abstract_choice {
    public c4_21_1() {
        super("4-23");
    }
}

class c4_21_2 extends abstract_choice {
    public c4_21_2() {
        super("4-24");
    }

    @Override
    public void chosen() {
        Constant.kernel.setPara(Constant.SINESTRO_LOVE, 0);
        super.chosen();
    }
}

class c4_22_1 extends abstract_choice {
    public c4_22_1() {
        super("4-21");
    }
}

class c4_23_1 extends abstract_choice {
    public c4_23_1() {
        super("4-25");
    }
}

class c4_23_2 extends abstract_choice {
    public c4_23_2() {
        super("4-26");
    }
}

class c4_25_1 extends abstract_choice {
    public c4_25_1() {
        super("4-27");
    }

    @Override
    public boolean show() {
        return Constant.kernel.getPara(Constant.SINESTRO_TAME) == 8;
    }
}

class c4_25_2 extends abstract_choice {
    public c4_25_2() {
        super("4-28");
    }

    @Override
    public boolean show() {
        return Constant.kernel.getPara(Constant.SINESTRO_LOVE) < 8;
    }
}

class c4_25_3 extends abstract_choice {
    public c4_25_3() {
        super("end-10");
    }

    @Override
    public String text() {
        return "怎么了？";
    }
}

class c4_27_1 extends abstract_choice {
    public c4_27_1() {
        super("end-11");
    }

    @Override
    public boolean show() {
        return Constant.kernel.getPara(Constant.SINESTRO_LOVE) == 8;
    }

    @Override
    public String text() {
        return "再给他一次机会";
    }
}

class c4_27_2 extends abstract_choice {
    public c4_27_2() {
        super("end-12");
    }

    @Override
    public String text() {
        return "瑟尔早该死了";
    }
}

class c4_28_1 extends abstract_choice {
    public c4_28_1() {
        super("end-8");
    }

    @Override
    public String text() {
        return "你想怎样";
    }

    @Override
    public boolean show() {
        return Constant.kernel.getPara(Constant.SINESTRO_TAME) == 8;
    }
}

class c4_28_2 extends abstract_choice {
    public c4_28_2() {
        super("end-9");
    }

    @Override
    public String text() {
        return "你想怎样";
    }

    @Override
    public boolean show() {
        return Constant.kernel.getPara(Constant.SINESTRO_TAME) < 8;
    }
}

class s4_3 extends abstract_scene {
    public s4_3() {
        super(new LinkedList<abstract_choice>() {{
            add(new c4_3_1());
            add(new c4_3_2());
            add(new c4_3_3());
        }});
    }
}

class s4_4 extends abstract_scene {
    public s4_4() {
        super(new LinkedList<abstract_choice>() {{
            add(new c4_4_1());
            add(new c4_4_2());
        }});
    }
}

class s4_6 extends abstract_scene {
    public s4_6() {
        super(new LinkedList<abstract_choice>() {{
            add(new c4_6_1());
            add(new c4_6_2());
            add(new c4_6_3());
            add(new c4_6_4());
        }});
    }
}

class s4_7 extends abstract_scene {
    public s4_7() {
        super(new LinkedList<abstract_choice>() {{
            add(new c4_7_1());
            add(new c4_7_2());
        }});
    }

    @Override
    LinkedList<abstract_choice> load() {
        if (Constant.kernel.fight()) {
            return super.load();
        } else {
            return new LinkedList<abstract_choice>() {{
                add(new c4_7_3());
            }};
        }
    }
}


class s4_11 extends abstract_scene {
    @Override
    LinkedList<abstract_choice> load() {
        if (Constant.kernel.fight()) {
            return new LinkedList<abstract_choice>() {{
                add(new c4_11_1());
            }};
        } else {
            return new LinkedList<abstract_choice>() {{
                add(new c4_11_2());
            }};
        }
    }
}

class s4_13 extends abstract_scene {
    public s4_13() {
        super(new LinkedList<abstract_choice>() {{
            add(new c4_13_1());
            add(new c4_13_2());
            add(new c4_13_3());
        }});
    }
}

class s4_14 extends abstract_scene {
    public s4_14() {
        super(new LinkedList<abstract_choice>() {{
            add(new c4_14_1());
            add(new c4_14_2());
            add(new c4_14_3());
        }});
    }
}

class s4_20 extends abstract_scene {
    public s4_20() {
        super(new LinkedList<abstract_choice>() {{
            add(new c4_20_1());
            add(new c4_20_2());
        }});
    }
}

class s4_21 extends abstract_scene {
    public s4_21() {
        super(new LinkedList<abstract_choice>() {{
            add(new c4_21_1());
            add(new c4_21_2());
        }});
    }
}

class s4_25 extends abstract_scene {
    public s4_25() {
        super(new LinkedList<abstract_choice>() {{
            add(new c4_25_1());
            add(new c4_25_2());
            add(new c4_25_3());
        }});
    }
}

class s4_27 extends abstract_scene {
    public s4_27() {
        super(new LinkedList<abstract_choice>() {{
            add(new c4_27_1());
            add(new c4_27_2());
        }});
    }
}

class s4_28 extends abstract_scene {
    public s4_28() {
        super(new LinkedList<abstract_choice>() {{
            add(new c4_28_1());
            add(new c4_28_2());
        }});
    }
}
