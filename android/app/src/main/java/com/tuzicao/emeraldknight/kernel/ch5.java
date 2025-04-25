package com.tuzicao.emeraldknight.kernel;

import java.util.LinkedList;

class c5_1_1 extends abstract_choice {
    public c5_1_1() {
        super("5-26");
    }
}

class c5_1_2 extends abstract_choice {
    public c5_1_2() {
        super("5-2");
    }

    @Override
    public void chosen() {
        Constant.kernel.setPara(Constant.TEMPORARY, 0);
        super.chosen();
    }
}

class c5_1_3 extends abstract_choice {
    public c5_1_3() {
        super("5-27");
    }
}

class c5_2_1 extends abstract_choice {
    public c5_2_1() {
        super("5-5");
    }
}

class c5_2_2 extends abstract_choice {
    public c5_2_2() {
        super("5-6");
    }
}

class c5_2_3 extends abstract_choice {
    public c5_2_3() {
        super("5-7");
    }
}

class c5_2_4 extends abstract_choice {
    public c5_2_4() {
        super("5-8");
    }
}

class c5_3_1 extends abstract_choice {
    public c5_3_1() {
        super("5-13");
    }
}

class c5_4_1 extends abstract_choice {
    public c5_4_1() {
        super("5-9");
    }
}

class c5_4_2 extends abstract_choice {
    public c5_4_2() {
        super("5-10");
    }
}

class c5_4_3 extends abstract_choice {
    public c5_4_3() {
        super("5-12");
    }
}

class c5_8_1 extends abstract_choice {
    public c5_8_1() {
        super("5-3");
    }

    @Override
    public String text() {
        return "走吧";
    }
}

class c5_10_1 extends abstract_choice {
    public c5_10_1() {
        super("5-11");
    }
}

class c5_13_1 extends abstract_choice {
    public c5_13_1() {
        super("5-14");
    }
}

class c5_14_1 extends abstract_choice {
    public c5_14_1() {
        super("5-15");
    }
}

class c5_15_1 extends abstract_choice {
    @Override
    public String text() {
        return "主建筑";
    }

    @Override
    public void chosen() {
        Constant.kernel.setPosition(1);
    }
}

class c5_15_1_1 extends abstract_choice {
    public c5_15_1_1() {
        super("5-16");
    }

    @Override
    public void chosen() {
        Constant.kernel.setPosition(0);
        super.chosen();
    }
}

class c5_15_1_2 extends abstract_choice {
    public c5_15_1_2() {
        super("5-18");
    }

    @Override
    public void chosen() {
        Constant.kernel.setPosition(0);
        super.chosen();
    }
}

class c5_15_1_3 extends abstract_choice {
    public c5_15_1_3() {
        super("5-19");
    }

    @Override
    public void chosen() {
        Constant.kernel.setPosition(0);
        super.chosen();
    }
}

class c5_15_2 extends abstract_choice {
    @Override
    public String text() {
        return "东塔楼";
    }

    @Override
    public void chosen() {
        Constant.kernel.setPosition(2);
    }
}

class c5_15_2_1 extends abstract_choice {
    public c5_15_2_1() {
        super("5-20");
    }

    @Override
    public void chosen() {
        Constant.kernel.setPosition(0);
        super.chosen();
    }
}

class c5_15_2_2 extends abstract_choice {
    public c5_15_2_2() {
        super("5-21");
    }

    @Override
    public void chosen() {
        Constant.kernel.setPosition(0);
        if (Constant.kernel.getPara(Constant.TEMPORARY) % 2 == 0) {
            Constant.kernel.offsetPara(Constant.TEMPORARY, 1);
            Constant.kernel.offsetPara(Constant.KNOWLEDGE, 1);
        }
        super.chosen();
    }
}

class c5_15_3 extends abstract_choice {
    @Override
    public String text() {
        return "西塔楼";
    }

    @Override
    public void chosen() {
        Constant.kernel.setPosition(3);
    }
}

class c5_15_3_1 extends abstract_choice {
    public c5_15_3_1() {
        super("5-22");
    }

    @Override
    public void chosen() {
        Constant.kernel.setPosition(0);
        if ((Constant.kernel.getPara(Constant.TEMPORARY) >> 1) % 2 == 0) {
            Constant.kernel.offsetPara(Constant.TEMPORARY, 2);
            Constant.kernel.offsetPara(Constant.KNOWLEDGE, 2);
        }
        super.chosen();
    }
}

class c5_15_3_2 extends abstract_choice {
    public c5_15_3_2() {
        super("5-23");
    }

    @Override
    public void chosen() {
        Constant.kernel.setPosition(0);
        if ((Constant.kernel.getPara(Constant.TEMPORARY) >> 2) % 2 == 0) {
            Constant.kernel.offsetPara(Constant.TEMPORARY, 4);
            Constant.kernel.offsetPara(Constant.INTELLIGENCE, 1);
        }
        super.chosen();
    }
}

class c5_15_4 extends abstract_choice {
    public c5_15_4() {
        super("5-24");
    }

    @Override
    public boolean show() {
        return Constant.kernel.getPara(Constant.DRAGON_EGG) == 0;
    }

    @Override
    public void chosen() {
        Constant.kernel.setPara(Constant.DRAGON_EGG, 1);
        Constant.kernel.offsetPara(Constant.KNOWLEDGE, 3);
        super.chosen();
    }
}

class c5_15_5 extends abstract_choice {
    public c5_15_5() {
        super("5-25");
    }

    @Override
    public boolean show() {
        return Constant.kernel.getPara(Constant.DRAGON_EGG) == 1;
    }
}

class c5_16_1 extends abstract_choice {
    public c5_16_1() {
        super("5-17");
    }
}

class c5_18_1 extends abstract_choice {
    public c5_18_1() {
        super("5-28");
    }

    @Override
    public void chosen() {
        Constant.kernel.setPara(Constant.TEMPORARY, 0);
        super.chosen();
    }
}

class c5_28_1 extends abstract_choice {
    public c5_28_1() {
        super("5-29");
    }

    @Override
    public boolean show() {
        return (Constant.kernel.getPara(Constant.INTELLIGENCE) > 2) && (Constant.kernel.getPara(Constant.BRUCE_LOVE) > 8);
    }
}

class c5_28_2 extends abstract_choice {
    public c5_28_2() {
        super("5-30");
    }

    @Override
    public boolean show() {
        return (Constant.kernel.getPara(Constant.INTELLIGENCE) > 2) && (Constant.kernel.getPara(Constant.BRUCE_LOVE) <= 8);
    }
}

class c5_28_3 extends abstract_choice {
    public c5_28_3() {
        super("5-31");
    }
}

class c5_29_1 extends abstract_choice {
    public c5_29_1() {
        super("5-32");
    }
}

class c5_29_2 extends abstract_choice {
    public c5_29_2() {
        super("end-13");
    }

    @Override
    public String text() {
        return "让布鲁斯去操心";
    }
}

class c5_31_1 extends abstract_choice {
    public c5_31_1() {
        super("end-13");
    }

    @Override
    public String text() {
        return "不再管了";
    }
}

class c5_32_1 extends abstract_choice {
    public c5_32_1() {
        super("5-33");
    }
}

class c5_32_2 extends abstract_choice {
    public c5_32_2() {
        super("5-40");
    }

    @Override
    public boolean show() {
        return Constant.kernel.getPara(Constant.TEMPORARY) % 2 == 0;
    }

    @Override
    public void chosen() {
        Constant.kernel.offsetPara(Constant.TEMPORARY, 1);
        super.chosen();
    }
}

class c5_32_3 extends abstract_choice {
    public c5_32_3() {
        super("5-41");
    }

    @Override
    public boolean show() {
        return Constant.kernel.getPara(Constant.TEMPORARY) % 2 == 1;
    }
}

class c5_32_4 extends abstract_choice {
    public c5_32_4() {
        super("5-44");
    }
}

class c5_32_5 extends abstract_choice {
    public c5_32_5() {
        super("5-46");
    }

    @Override
    public boolean show() {
        return Constant.kernel.getPara(Constant.TEMPORARY) % 2 == 0;
    }

    @Override
    public void chosen() {
        Constant.kernel.offsetPara(Constant.TEMPORARY, 1);
        super.chosen();
    }
}

class c5_32_6 extends abstract_choice {
    public c5_32_6() {
        super("5-47");
    }

    @Override
    public boolean show() {
        return Constant.kernel.getPara(Constant.TEMPORARY) % 2 == 1;
    }
}

class c5_32_7 extends abstract_choice {
    public c5_32_7() {
        super("5-51");
    }

    @Override
    public boolean show() {
        return (Constant.kernel.getPara(Constant.DRAGON_EGG) == 1) && (Constant.kernel.getScene().equals("5-32"));
    }

    @Override
    public void chosen() {
        Constant.kernel.offsetPara(Constant.BRUCE_LOVE, 4);
        super.chosen();
    }
}

class c5_33_1 extends abstract_choice {
    public c5_33_1() {
        super("5-34");
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

class c5_33_2 extends abstract_choice {
    public c5_33_2() {
        super("5-35");
    }

    @Override
    public boolean show() {
        return (Constant.kernel.getPara(Constant.TEMPORARY) >> 2) % 2 == 0;
    }

    @Override
    public void chosen() {
        Constant.kernel.offsetPara(Constant.TEMPORARY, 4);
        super.chosen();
    }
}

class c5_33_3 extends abstract_choice {
    public c5_33_3() {
        super("5-36");
    }

    @Override
    public boolean show() {
        return Constant.kernel.getPara(Constant.PROPS) == 1;
    }

    @Override
    public void chosen() {
        if ((Constant.kernel.getPara(Constant.TEMPORARY) >> 3) % 2 == 0) {
            Constant.kernel.offsetPara(Constant.TEMPORARY, 8);
        }
        super.chosen();
    }
}

class c5_37_1 extends abstract_choice {
    public c5_37_1() {
        super("5-38");
    }

    @Override
    public boolean show() {
        return Constant.kernel.getPara(Constant.PROPS) == 0;
    }
}

class c5_37_2 extends abstract_choice {
    public c5_37_2() {
        super("5-39");
    }

    @Override
    public boolean show() {
        return Constant.kernel.getPara(Constant.PROPS) == 1;
    }

    @Override
    public void chosen() {
        Constant.kernel.setPara(Constant.TEMPORARY, 0);
        Constant.kernel.setPara(Constant.PROPS, 0);
        super.chosen();
    }
}

class c5_38_1 extends abstract_choice {
    public c5_38_1() {
        super("end-13");
    }

    @Override
    public String text() {
        return "专心备战";
    }
}

class c5_41_1 extends abstract_choice {
    public c5_41_1() {
        super("5-42");
    }

    @Override
    public boolean show() {
        return (Constant.kernel.getPara(Constant.TEMPORARY) >> 2) % 2 == 1;
    }
}

class c5_41_2 extends abstract_choice {
    public c5_41_2() {
        super("5-43");
    }

    @Override
    public boolean show() {
        return (Constant.kernel.getPara(Constant.TEMPORARY) >> 2) % 2 == 0;
    }
}

class c5_44_1 extends abstract_choice {
    public c5_44_1() {
        super("5-45");
    }

    @Override
    public boolean show() {
        return (Constant.kernel.getPara(Constant.TEMPORARY) >> 1) % 2 == 1;
    }

    @Override
    public void chosen() {
        if (Constant.kernel.getPara(Constant.TEMPORARY) % 2 == 0) {
            Constant.kernel.offsetPara(Constant.TEMPORARY, 1);
        }
        Constant.kernel.setPara(Constant.PROPS, 1);
        super.chosen();
    }
}

class c5_44_2 extends abstract_choice {
    public c5_44_2() {
        super("end-14");
    }

    @Override
    public String text() {
        return "跳下去";
    }

    @Override
    public boolean show() {
        return (Constant.kernel.getPara(Constant.TEMPORARY) >> 1) % 2 == 0;
    }
}

class c5_44_3 extends abstract_choice {
    public c5_44_3() {
        super("5-63");
    }
}

class c5_47_1 extends abstract_choice {
    public c5_47_1() {
        super("5-48");
    }

    @Override
    public boolean show() {
        return ((Constant.kernel.getPara(Constant.TEMPORARY) >> 3) % 2 == 1) && ((Constant.kernel.getPara(Constant.TEMPORARY) >> 2) % 2 == 1);
    }
}

class c5_47_2 extends abstract_choice {
    public c5_47_2() {
        super("5-49");
    }

    @Override
    public boolean show() {
        return (Constant.kernel.getPara(Constant.TEMPORARY) >> 2) % 2 == 1;
    }
}

class c5_47_3 extends abstract_choice {
    public c5_47_3() {
        super("5-50");
    }

    @Override
    public boolean show() {
        return (Constant.kernel.getPara(Constant.TEMPORARY) >> 3) % 2 == 0;
    }
}

class c5_47_4 extends abstract_choice {
    public c5_47_4() {
        super("5-64");
    }

    @Override
    public boolean show() {
        return ((Constant.kernel.getPara(Constant.TEMPORARY) >> 3) % 2 == 1) && ((Constant.kernel.getPara(Constant.TEMPORARY) >> 2) % 2 == 0);
    }
}

class c5_48_1 extends abstract_choice {
    public c5_48_1() {
        super("5-52");
    }

    @Override
    public void chosen() {
        Constant.kernel.setPara(Constant.TEMPORARY, 1);
        Constant.kernel.setPara(Constant.PROPS, 0);
        super.chosen();
    }
}

class c5_49_1 extends abstract_choice {
    public c5_49_1() {
        super("5-37");
    }
}

class c5_52_1 extends abstract_choice {
    public c5_52_1() {
        super("5-53");
    }
}

class c5_53_1 extends abstract_choice {
    public c5_53_1() {
        super("5-54");
    }
}

class c5_53_2 extends abstract_choice {
    public c5_53_2() {
        super("5-55");
    }
}

class c5_55_1 extends abstract_choice {
    public c5_55_1() {
        super("5-56");
    }

    @Override
    public void chosen() {
        Constant.kernel.setPara(Constant.TEMPORARY, 0);
        super.chosen();
    }
}

class c5_55_2 extends abstract_choice {
    public c5_55_2() {
        super("5-57");
    }
}

class c5_55_3 extends abstract_choice {
    public c5_55_3() {
        super("5-58");
    }

    @Override
    public void chosen() {
        Constant.kernel.setPara(Constant.TEMPORARY, 1);
        super.chosen();
    }
}

class c5_58_1 extends abstract_choice {
    public c5_58_1() {
        super("5-59");
    }
}

class c5_58_2 extends abstract_choice {
    public c5_58_2() {
        super("5-59");
    }

    @Override
    public String text() {
        return "西塔楼";
    }
}

class c5_58_3 extends abstract_choice {
    public c5_58_3() {
        super("5-59");
    }

    @Override
    public String text() {
        return "城堡一楼";
    }
}

class c5_58_4 extends abstract_choice {
    public c5_58_4() {
        super("5-60");
    }

    @Override
    public boolean show() {
        return Constant.kernel.getPara(Constant.DRAGON_EGG) == 1;
    }
}

class c5_58_5 extends abstract_choice {
    public c5_58_5() {
        super("5-61");
    }

    @Override
    public boolean show() {
        return Constant.kernel.getPara(Constant.DRAGON_EGG) == 0;
    }
}

class c5_59_1 extends abstract_choice {
    public c5_59_1() {
        super("6-1");
    }

    @Override
    public String text() {
        return "备战";
    }
}

class c5_60_1 extends abstract_choice {
    public c5_60_1() {
        super("5-62");
    }

    @Override
    public void chosen() {
        Constant.kernel.offsetPara(Constant.TEMPORARY, 1);
        super.chosen();
    }
}

class s5_1 extends abstract_scene {
    @Override
    LinkedList<abstract_choice> load() {
        if (Constant.kernel.getPara(Constant.TEAMMATE) == Constant.BRUCE_CODE) {
            return new LinkedList<abstract_choice>() {{
                add(new c5_1_3());
            }};
        } else if (Constant.kernel.getPara(Constant.TEMPORARY) == 1) {
            return new LinkedList<abstract_choice>() {{
                add(new c5_1_2());
            }};
        } else {
            return new LinkedList<abstract_choice>() {{
                add(new c5_1_1());
            }};
        }
    }
}

class s5_2 extends abstract_scene {
    @Override
    LinkedList<abstract_choice> load() {
        if (Constant.kernel.getPara(Constant.BRUCE_INTRODUCE) == 1) {
            return new LinkedList<abstract_choice>() {{
                add(new c5_2_1());
            }};
        } else if (Constant.kernel.getPara(Constant.BRUCE_SHOW_UP) == 1) {
            return new LinkedList<abstract_choice>() {{
                add(new c5_2_2());
            }};
        } else {
            return new LinkedList<abstract_choice>() {{
                add(new c5_2_3());
            }};
        }
    }
}

class s5_4 extends abstract_scene {
    @Override
    LinkedList<abstract_choice> load() {
        if (Constant.kernel.getPara(Constant.BRUCE_INTRODUCE) == 1) {
            return new LinkedList<abstract_choice>() {{
                add(new c5_4_1());
            }};
        } else {
            return new LinkedList<abstract_choice>() {{
                add(new c5_4_2());
            }};
        }
    }
}

class s5_10 extends abstract_scene {
    @Override
    LinkedList<abstract_choice> load() {
        if (Constant.kernel.getPara(Constant.BRUCE_SHOW_UP) == 1) {
            return new LinkedList<abstract_choice>() {{
                add(new c5_10_1());
            }};
        } else {
            return new LinkedList<abstract_choice>() {{
                add(new c5_4_3());
            }};
        }
    }
}

class s5_15 extends abstract_scene {
    public s5_15() {
        super(new LinkedList<abstract_choice>() {{
            add(new c5_15_1());
            add(new c5_15_2());
            add(new c5_15_3());
            add(new c5_15_4());
            add(new c5_15_5());
        }});
    }
}

class s5_15_1 extends abstract_scene {
    public s5_15_1() {
        super(new LinkedList<abstract_choice>() {{
            add(new c5_15_1_1());
            add(new c5_15_1_2());
            add(new c5_15_1_3());
        }});
    }
}

class s5_15_2 extends abstract_scene {
    public s5_15_2() {
        super(new LinkedList<abstract_choice>() {{
            add(new c5_15_2_1());
            add(new c5_15_2_2());
        }});
    }
}

class s5_15_3 extends abstract_scene {
    public s5_15_3() {
        super(new LinkedList<abstract_choice>() {{
            add(new c5_15_3_1());
            add(new c5_15_3_2());
        }});
    }
}

class s5_18 extends abstract_scene {
    public s5_18() {
        super(new LinkedList<abstract_choice>() {{
            add(new c5_18_1());
            add(new c5_16_1());
        }});
    }
}

class s5_28 extends abstract_scene {
    public s5_28() {
        super(new LinkedList<abstract_choice>() {{
            add(new c5_28_1());
            add(new c5_28_2());
            add(new c5_28_3());
        }});
    }
}

class s5_29 extends abstract_scene {
    public s5_29() {
        super(new LinkedList<abstract_choice>() {{
            add(new c5_29_1());
            add(new c5_29_2());
        }});
    }
}

class s5_32 extends abstract_scene {
    public s5_32() {
        super(new LinkedList<abstract_choice>() {{
            add(new c5_32_1());
            add(new c5_32_2());
            add(new c5_32_3());
            add(new c5_32_4());
            add(new c5_32_5());
            add(new c5_32_6());
            add(new c5_32_7());
        }});
    }
}

class s5_33 extends abstract_scene {
    public s5_33() {
        super(new LinkedList<abstract_choice>() {{
            add(new c5_33_1());
            add(new c5_33_2());
            add(new c5_33_3());
        }});
    }

    @Override
    public LinkedList<abstract_choice> load() {
        boolean isNone = true;
        for (int i = 0; i < option.size(); i++) {
            isNone = isNone && (!option.get(i).show());
        }
        if (isNone) {
            return new s5_32().load();
        } else {
            return super.load();
        }
    }
}

class s5_37 extends abstract_scene {
    public s5_37() {
        super(new LinkedList<abstract_choice>() {{
            add(new c5_37_1());
            add(new c5_37_2());
        }});
    }
}

class s5_41 extends abstract_scene {
    public s5_41() {
        super(new LinkedList<abstract_choice>() {{
            add(new c5_41_1());
            add(new c5_41_2());
        }});
    }
}

class s5_44 extends abstract_scene {
    public s5_44() {
        super(new LinkedList<abstract_choice>() {{
            add(new c5_44_1());
            add(new c5_44_2());
            add(new c5_44_3());
        }});
    }
}

class s5_47 extends abstract_scene {
    public s5_47() {
        super(new LinkedList<abstract_choice>() {{
            add(new c5_47_1());
            add(new c5_47_4());
            add(new c5_47_2());
            add(new c5_47_3());
        }});
    }
}

class s5_53 extends abstract_scene {
    @Override
    LinkedList<abstract_choice> load() {
        if (Constant.kernel.getPara(Constant.PEGASUS) == 1) {
            return new LinkedList<abstract_choice>() {{
                add(new c5_53_1());
            }};
        } else {
            return new LinkedList<abstract_choice>() {{
                add(new c5_53_2());
            }};
        }
    }
}

class s5_55 extends abstract_scene {
    @Override
    LinkedList<abstract_choice> load() {
        this.option = new LinkedList<abstract_choice>() {{
            add(new c5_55_1());
        }};
        if (Constant.kernel.getPara(Constant.TEMPORARY) == 1) {
            this.option.add(new c5_55_2());
        } else {
            this.option.add(new c5_55_3());
        }
        return super.load();
    }
}

class s5_57 extends abstract_scene {
    public s5_57() {
        super(new LinkedList<abstract_choice>() {{
            add(new c5_55_1());
            add(new c5_55_3());
        }});
    }
}

class s5_58 extends abstract_scene {
    public s5_58() {
        super(new LinkedList<abstract_choice>() {{
            add(new c5_58_1());
            add(new c5_58_2());
            add(new c5_58_3());
            add(new c5_58_4());
            add(new c5_58_5());
        }});
    }
}
