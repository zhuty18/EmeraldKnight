package atomic1028.gl.emeraldknight.kernel;

import java.util.LinkedList;

class c3_1_1 extends abstract_choice {
    public c3_1_1() {
        super("3-5");
    }

    @Override
    public void chosen() {
        Constant.kernel.offsetPara(Constant.SINESTRO_TAME, 1);
        super.chosen();
    }
}

class c3_1_2 extends abstract_choice {
    public c3_1_2() {
        super("3-30");
    }
}

class c3_2_1 extends abstract_choice {
    public c3_2_1() {
        super("3-31");
    }

    @Override
    public void chosen() {
        Constant.kernel.offsetPara(Constant.KNOWLEDGE, 3);
        super.chosen();
    }
}

class c3_2_2 extends abstract_choice {
    public c3_2_2() {
        super("3-41");
    }
}

class c3_3_1 extends abstract_choice {
    public c3_3_1() {
        super("3-43");
    }

    @Override
    public void chosen() {
        Constant.kernel.offsetPara(Constant.TEMPORARY, 1);
        super.chosen();
    }
}

class c3_4_1 extends abstract_choice {
    public c3_4_1() {
        super("3-50");
    }

    @Override
    public void chosen() {
        Constant.kernel.offsetPara(Constant.KNOWLEDGE, 1);
        super.chosen();
    }
}

class c3_4_2 extends abstract_choice {
    public c3_4_2() {
        super("3-51");
    }
}

class c3_4_3 extends abstract_choice {
    public c3_4_3() {
        super("3-52");
    }
}

class c3_5_1 extends abstract_choice {
    public c3_5_1() {
        super("3-6");
    }
}

class c3_5_2 extends abstract_choice {
    public c3_5_2() {
        super("3-7");
    }
}

class c3_6_1 extends abstract_choice {
    public c3_6_1() {
        super("3-8");
    }
}

class c3_6_2 extends abstract_choice {
    public c3_6_2() {
        super("3-9");
    }
}

class c3_8_1 extends abstract_choice {
    public c3_8_1() {
        super("3-10");
    }
}

class c3_8_2 extends abstract_choice {
    public c3_8_2() {
        super("3-11");
    }
}

class c3_10_1 extends abstract_choice {
    public c3_10_1() {
        super("3-12");
    }
}

class c3_10_2 extends abstract_choice {
    public c3_10_2() {
        super("3-13");
    }
}

class c3_12_1 extends abstract_choice {
    public c3_12_1() {
        super("3-14");
    }

    @Override
    public void chosen() {
        Constant.kernel.offsetPara(Constant.SINESTRO_TAME, 2);
        super.chosen();
    }
}

class c3_12_2 extends abstract_choice {
    public c3_12_2() {
        super("3-15");
    }
}

class c3_14_1 extends abstract_choice {
    public c3_14_1() {
        super("3-16");
    }
}

class c3_16_1 extends abstract_choice {
    public c3_16_1() {
        super("3-17");
    }
}

class c3_16_2 extends abstract_choice {
    public c3_16_2() {
        super("end-5");
    }

    @Override
    public String text() {
        return "直接跳";
    }
}

class c3_17_1 extends abstract_choice {
    public c3_17_1() {
        super("3-18");
    }
}

class c3_18_1 extends abstract_choice {
    public c3_18_1() {
        super("3-19");
    }
}

class c3_18_2 extends abstract_choice {
    public c3_18_2() {
        super("3-20");
    }
}

class c3_18_3 extends abstract_choice {
    public c3_18_3() {
        super("3-21");
    }

    @Override
    public void chosen() {
        Constant.kernel.offsetPara(Constant.SINESTRO_LOVE, 1);
        super.chosen();
    }
}

class c3_19_1 extends abstract_choice {
    public c3_19_1() {
        super("3-27");
    }

    @Override
    public String text() {
        return "我捡到了他的信";
    }
}

class c3_19_2 extends abstract_choice {
    public c3_19_2() {
        super("3-22");
    }

    @Override
    public String text() {
        return "我以为他会在山上";
    }
}

class c3_20_1 extends abstract_choice {
    public c3_20_1() {
        super("3-22");
    }

    @Override
    public String text() {
        return "瑟尔在这里吗";
    }
}

class c3_20_2 extends abstract_choice {
    public c3_20_2() {
        super("3-21");
    }

    @Override
    public String text() {
        return "阿琳是谁";
    }

    @Override
    public void chosen() {
        Constant.kernel.offsetPara(Constant.SINESTRO_LOVE, 1);
        super.chosen();
    }
}

class c3_21_1 extends abstract_choice {
    public c3_21_1() {
        super("3-27");
    }
}

class c3_21_2 extends abstract_choice {
    public c3_21_2() {
        super("3-28");
    }
}

class c3_22_1 extends abstract_choice {
    public c3_22_1() {
        super("3-23");
    }
}

class c3_22_2 extends abstract_choice {
    public c3_22_2() {
        super("3-24");
    }
}

class c3_22_3 extends abstract_choice {
    public c3_22_3() {
        super("3-27");
    }

    @Override
    public String text() {
        return "我还捡到了他的信";
    }
}

class c3_23_1 extends abstract_choice {
    public c3_23_1() {
        super("3-25");
    }
}

class c3_23_2 extends abstract_choice {
    public c3_23_2() {
        super("3-26");
    }

    @Override
    public boolean show() {
        return Constant.kernel.getPara(Constant.SINESTRO_TAME) == 7;
    }

    @Override
    public void chosen() {
        Constant.kernel.offsetPara(Constant.SINESTRO_LOVE, 2);
        super.chosen();
    }
}

class c3_24_1 extends abstract_choice {
    public c3_24_1() {
        super("3-23");
    }

    @Override
    public String text() {
        return "告诉他全过程";
    }
}

class c3_27_1 extends abstract_choice {
    public c3_27_1() {
        super("3-23");
    }

    @Override
    public String text() {
        return "信上的瑟尔又是谁？";
    }
}

class c3_28_1 extends abstract_choice {
    public c3_28_1() {
        super("3-29");
    }
}

class c3_29_1 extends abstract_choice {
    public c3_29_1() {
        super("4-1");
    }

    @Override
    public String text() {
        return "告辞离开";
    }

    @Override
    public void chosen() {
        Constant.kernel.setPara(Constant.TEMPORARY, 80);
        super.chosen();
    }
}

class c3_30_1 extends abstract_choice {
    public c3_30_1() {
        super("3-2");
    }
}

class c3_31_1 extends abstract_choice {
    public c3_31_1() {
        super("3-32");
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

class c3_31_2 extends abstract_choice {
    public c3_31_2() {
        super("3-33");
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

class c3_31_3 extends abstract_choice {
    public c3_31_3() {
        super("3-34");
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

class c3_31_4 extends abstract_choice {
    public c3_31_4() {
        super("3-49");
    }

    @Override
    public boolean show() {
        return Constant.kernel.getPara(Constant.TEMPORARY) == 7;
    }

    @Override
    public void chosen() {
        Constant.kernel.setPara(Constant.TEMPORARY, 0);
        super.chosen();
    }
}

class c3_35_1 extends abstract_choice {
    public c3_35_1() {
        super("3-36");
    }

    @Override
    public String text() {
        return "处理羽毛";
    }

    @Override
    public boolean show() {
        return Constant.kernel.getPara(Constant.TEMPORARY) % 2 == 0;
    }

    @Override
    public void chosen() {
        Constant.kernel.setPara(Constant.PROPS, 1);
        Constant.kernel.offsetPara(Constant.TEMPORARY, 1);
        super.chosen();
    }
}

class c3_35_2 extends abstract_choice {
    public c3_35_2() {
        super("3-36");
    }

    @Override
    public String text() {
        return "处理金属";
    }

    @Override
    public boolean show() {
        return (Constant.kernel.getPara(Constant.TEMPORARY) >> 1) % 2 == 0;
    }

    @Override
    public void chosen() {
        Constant.kernel.setPara(Constant.PROPS, 2);
        Constant.kernel.offsetPara(Constant.TEMPORARY, 2);
        super.chosen();
    }
}

class c3_35_3 extends abstract_choice {
    public c3_35_3() {
        super("3-36");
    }

    @Override
    public String text() {
        return "处理骨头";
    }

    @Override
    public boolean show() {
        return (Constant.kernel.getPara(Constant.TEMPORARY) >> 2) % 2 == 0;
    }

    @Override
    public void chosen() {
        Constant.kernel.setPara(Constant.PROPS, 3);
        Constant.kernel.offsetPara(Constant.TEMPORARY, 4);
        super.chosen();
    }
}

class c3_35_4 extends abstract_choice {
    public c3_35_4() {
        super("3-37");
    }

    @Override
    public String text() {
        return "附魔翅膀";
    }

    @Override
    public boolean show() {
        return (Constant.kernel.getPara(Constant.TEMPORARY) >> 3) % 2 == 0;
    }

    @Override
    public void chosen() {
        Constant.kernel.setPara(Constant.PROPS, 4);
        Constant.kernel.offsetPara(Constant.TEMPORARY, 8);
        super.chosen();
    }
}

class c3_35_5 extends abstract_choice {
    public c3_35_5() {
        super("3-37");
    }

    @Override
    public String text() {
        return "附魔身体";
    }

    @Override
    public boolean show() {
        return (Constant.kernel.getPara(Constant.TEMPORARY) >> 4) % 2 == 0;
    }

    @Override
    public void chosen() {
        Constant.kernel.setPara(Constant.PROPS, 5);
        Constant.kernel.offsetPara(Constant.TEMPORARY, 16);
        super.chosen();
    }
}

class c3_35_6 extends abstract_choice {
    public c3_35_6() {
        super("3-38");
    }

    @Override
    public boolean show() {
        return ((Constant.kernel.getPara(Constant.TEMPORARY) == 31) && (Constant.kernel.getPara(Constant.PEGASUS) == 5));
    }

    @Override
    public void chosen() {
        Constant.kernel.setPara(Constant.PROPS, 0);
        Constant.kernel.setPara(Constant.TEMPORARY, 0);
        Constant.kernel.setPara(Constant.PEGASUS, 1);
        Constant.kernel.offsetPara(Constant.INTELLIGENCE, 3);
        super.chosen();
    }
}

class c3_35_7 extends abstract_choice {
    public c3_35_7() {
        super("3-39");
    }

    @Override
    public boolean show() {
        return ((Constant.kernel.getPara(Constant.TEMPORARY) == 31) && (Constant.kernel.getPara(Constant.PEGASUS) != 5));
    }

    @Override
    public void chosen() {
        Constant.kernel.setPara(Constant.PROPS, 0);
        Constant.kernel.setPara(Constant.TEMPORARY, 0);
        Constant.kernel.setPara(Constant.PEGASUS, 0);
        super.chosen();
    }
}

class c3_36_1 extends abstract_choice {
    public c3_36_1() {
        super("3-35");
    }

    @Override
    public String text() {
        return "清洁";
    }

    @Override
    public void chosen() {
        if (Constant.kernel.getPara(Constant.PROPS) == 1) {
            Constant.kernel.offsetPara(Constant.PEGASUS, 1);
        }
        super.chosen();
    }
}

class c3_36_2 extends abstract_choice {
    public c3_36_2() {
        super("3-35");
    }

    @Override
    public String text() {
        return "熔化";
    }

    @Override
    public void chosen() {
        if (Constant.kernel.getPara(Constant.PROPS) == 2) {
            Constant.kernel.offsetPara(Constant.PEGASUS, 1);
        }
        super.chosen();
    }
}

class c3_36_3 extends abstract_choice {
    public c3_36_3() {
        super("3-35");
    }

    @Override
    public String text() {
        return "粉碎";
    }

    @Override
    public void chosen() {
        if (Constant.kernel.getPara(Constant.PROPS) == 3) {
            Constant.kernel.offsetPara(Constant.PEGASUS, 1);
        }
        super.chosen();
    }
}

class c3_37_1 extends abstract_choice {
    public c3_37_1() {
        super("3-35");
    }

    @Override
    public String text() {
        return "水属性";
    }

    @Override
    public void chosen() {
        if (Constant.kernel.getPara(Constant.PROPS) == 5) {
            Constant.kernel.offsetPara(Constant.PEGASUS, 1);
        }
        super.chosen();
    }
}

class c3_37_2 extends abstract_choice {
    public c3_37_2() {
        super("3-35");
    }

    @Override
    public String text() {
        return "火属性";
    }
}

class c3_37_3 extends abstract_choice {
    public c3_37_3() {
        super("3-35");
    }

    @Override
    public String text() {
        return "风属性";
    }

    @Override
    public void chosen() {
        if (Constant.kernel.getPara(Constant.PROPS) == 4) {
            Constant.kernel.offsetPara(Constant.PEGASUS, 1);
        }
        super.chosen();
    }
}

class c3_37_4 extends abstract_choice {
    public c3_37_4() {
        super("3-35");
    }

    @Override
    public String text() {
        return "土属性";
    }
}

class c3_37_5 extends abstract_choice {
    public c3_37_5() {
        super("3-35");
    }

    @Override
    public String text() {
        return "雷属性";
    }
}

class c3_37_6 extends abstract_choice {
    public c3_37_6() {
        super("3-35");
    }

    @Override
    public String text() {
        return "空间属性";
    }
}

class c3_38_1 extends abstract_choice {
    public c3_38_1() {
        super("3-40");
    }
}

class c3_40_1 extends abstract_choice {
    public c3_40_1() {
        super("5-1");
    }

    @Override
    public void chosen() {
        Constant.kernel.setPara(Constant.TEMPORARY, 1);
        super.chosen();
    }
}

class c3_41_1 extends abstract_choice {
    public c3_41_1() {
        super("3-42");
    }

    @Override
    public void chosen() {
        Constant.kernel.offsetPara(Constant.TEMPORARY, 1);
        super.chosen();
    }
}

class c3_41_2 extends abstract_choice {
    public c3_41_2() {
        super("3-43");
    }

    @Override
    public String text() {
        return "不拿";
    }
}

class c3_42_1 extends abstract_choice {
    public c3_42_1() {
        super("3-43");
    }
}

class c3_43_1 extends abstract_choice {
    public c3_43_1() {
        super("3-44");
    }

    @Override
    public void chosen() {
        Constant.kernel.offsetPara(Constant.TEMPORARY, 2);
        super.chosen();
    }
}

class c3_43_2 extends abstract_choice {
    public c3_43_2() {
        super("3-45");
    }

    @Override
    public String text() {
        return "不进";
    }
}

class c3_44_1 extends abstract_choice {
    public c3_44_1() {
        super("3-45");
    }
}

class c3_45_1 extends abstract_choice {
    public c3_45_1() {
        super("3-46");
    }

    @Override
    public void chosen() {
        Constant.kernel.offsetPara(Constant.INTELLIGENCE, 1);
        super.chosen();
    }
}

class c3_45_2 extends abstract_choice {
    public c3_45_2() {
        super("3-47");
    }
}

class c3_45_3 extends abstract_choice {
    public c3_45_3() {
        super("3-48");
    }
}

class c3_46_1 extends abstract_choice {
    public c3_46_1() {
        super("5-1");
    }

    @Override
    public String text() {
        return "那座城";
    }

    @Override
    public void chosen() {
        Constant.kernel.setPara(Constant.TEMPORARY, 0);
        super.chosen();
    }
}

class c3_46_2 extends abstract_choice {
    public c3_46_2() {
        super("4-2");
    }

    @Override
    public void chosen() {
        Constant.kernel.setPara(Constant.TEMPORARY, 100);
        super.chosen();
    }
}

class c3_48_1 extends abstract_choice {
    public c3_48_1() {
        super("4-1");
    }

    @Override
    public String text() {
        return "继续前进";
    }

    @Override
    public void chosen() {
        Constant.kernel.setPara(Constant.TEMPORARY, 80);
        super.chosen();
    }
}

class c3_49_1 extends abstract_choice {
    public c3_49_1() {
        super("3-35");
    }
}

class c3_52_1 extends abstract_choice {
    public c3_52_1() {
        super("3-53");
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

class c3_52_2 extends abstract_choice {
    public c3_52_2() {
        super("3-54");
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

class c3_52_3 extends abstract_choice {
    public c3_52_3() {
        super("3-55");
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

class c3_52_4 extends abstract_choice {
    public c3_52_4() {
        super("3-56");
    }

    @Override
    public boolean show() {
        return (Constant.kernel.getPara(Constant.TEMPORARY) >> 3) % 2 == 0;
    }

    @Override
    public void chosen() {
        Constant.kernel.offsetPara(Constant.TEMPORARY, 8);
        super.chosen();
    }
}

class c3_52_5 extends abstract_choice {
    public c3_52_5() {
        super("3-57");
    }

    @Override
    public boolean show() {
        return (Constant.kernel.getPara(Constant.TEMPORARY) >> 4) % 2 == 0;
    }

    @Override
    public void chosen() {
        Constant.kernel.offsetPara(Constant.TEMPORARY, 16);
        Constant.kernel.offsetPara(Constant.KNOWLEDGE, 1);
        super.chosen();
    }
}

class c3_52_6 extends abstract_choice {
    public c3_52_6() {
        super("3-58");
    }

    @Override
    public boolean show() {
        return Constant.kernel.getPara(Constant.TEMPORARY) % 16 == 15;
    }

    @Override
    public void chosen() {
        Constant.kernel.setPara(Constant.TEMPORARY, 0);
        super.chosen();
    }
}

class c3_58_1 extends abstract_choice {
    public c3_58_1() {
        super("4-1");
    }

    @Override
    public String text() {
        return "讨伐魔王";
    }

    @Override
    public void chosen() {
        Constant.kernel.setPara(Constant.TEMPORARY, 80);
        super.chosen();
    }
}

class c3_58_2 extends abstract_choice {
    public c3_58_2() {
        super("3-60");
    }

    @Override
    public boolean show() {
        return Constant.kernel.getPara(Constant.BRUCE_INTRODUCE) == 0;
    }
}

class c3_58_3 extends abstract_choice {
    public c3_58_3() {
        super("3-61");
    }

    @Override
    public boolean show() {
        return Constant.kernel.getPara(Constant.BRUCE_INTRODUCE) == 1;
    }
}

class c3_59_1 extends abstract_choice {
    public c3_59_1() {
        super("4-1");
    }

    @Override
    public String text() {
        return "左边";
    }

    @Override
    public void chosen() {
        Constant.kernel.setPara(Constant.TEMPORARY, 80);
        super.chosen();
    }
}

class c3_59_2 extends abstract_choice {
    public c3_59_2() {
        super("3-41");
    }

    @Override
    public String text() {
        return "右边";
    }
}

class c3_60_1 extends abstract_choice {
    public c3_60_1() {
        super("3-62");
    }
}

class c3_60_2 extends abstract_choice {
    public c3_60_2() {
        super("3-63");
    }

    @Override
    public void chosen() {
        Constant.kernel.setPara(Constant.TEMPORARY, 1);
        super.chosen();
    }
}

class c3_62_3 extends abstract_choice {
    public c3_62_3() {
        super("3-63");
    }

    @Override
    public String text() {
        return "回头";
    }

    @Override
    public boolean show() {
        return Constant.kernel.getPara(Constant.TEMPORARY) == 0;
    }

    @Override
    public void chosen() {
        Constant.kernel.setPara(Constant.TEMPORARY, 1);
        super.chosen();
    }
}

class c3_61_1 extends abstract_choice {
    public c3_61_1() {
        super("3-68");
    }
}

class c3_61_2 extends abstract_choice {
    public c3_61_2() {
        super("3-69");
    }
}

class c3_62_1 extends abstract_choice {
    public c3_62_1() {
        super("3-64");
    }

    @Override
    public String text() {
        return "向左";
    }

    @Override
    public void chosen() {
        Constant.kernel.setPara(Constant.TEMPORARY, 0);
        super.chosen();
    }
}

class c3_62_2 extends abstract_choice {
    public c3_62_2() {
        super("3-65");
    }

    @Override
    public void chosen() {
        Constant.kernel.setPara(Constant.TEMPORARY, 0);
        super.chosen();
    }
}

class c3_63_1 extends abstract_choice {
    public c3_63_1() {
        super("3-62");
    }

    @Override
    public String text() {
        return "回头";
    }
}

class c3_64_1 extends abstract_choice {
    public c3_64_1() {
        super("5-1");
    }
}

class c3_65_1 extends abstract_choice {
    public c3_65_1() {
        super("3-66");
    }
}

class c3_65_2 extends abstract_choice {
    public c3_65_2() {
        super("3-64");
    }

    @Override
    public String text() {
        return "向下游";
    }
}

class c3_65_3 extends abstract_choice {
    public c3_65_3() {
        super("3-64");
    }

    @Override
    public String text() {
        return "涉水走对岸的路";
    }
}

class c3_66_1 extends abstract_choice {
    public c3_66_1() {
        super("3-64");
    }

    @Override
    public String text() {
        return "进森林";
    }
}

class c3_66_2 extends abstract_choice {
    public c3_66_2() {
        super("3-67");
    }
}

class c3_66_3 extends abstract_choice {
    public c3_66_3() {
        super("5-1");
    }

    @Override
    public String text() {
        return "右转";
    }

    @Override
    public void chosen() {
        Constant.kernel.offsetPara(Constant.INTELLIGENCE, 2);
        super.chosen();
    }
}

class c3_67_1 extends abstract_choice {
    public c3_67_1() {
        super("5-1");
    }

    @Override
    public String text() {
        return "回头";
    }
}

class c3_68_1 extends abstract_choice {
    public c3_68_1() {
        super("3-70");
    }

    @Override
    public boolean show() {
        return Constant.kernel.getPara(Constant.INTELLIGENCE) == 3;
    }

    @Override
    public void chosen() {
        Constant.kernel.offsetPara(Constant.BRUCE_LOVE, 2);
        super.chosen();
    }
}

class c3_68_2 extends abstract_choice {
    public c3_68_2() {
        super("3-71");
    }
}

class c3_68_3 extends abstract_choice {
    public c3_68_3() {
        super("3-72");
    }

    @Override
    public void chosen() {
        Constant.kernel.offsetPara(Constant.BRUCE_LOVE, -3);
        super.chosen();
    }
}

class c3_68_4 extends abstract_choice {
    public c3_68_4() {
        super("3-73");
    }
}

class c3_69_1 extends abstract_choice {
    public c3_69_1() {
        super("3-60");
    }
}

class c3_73_1 extends abstract_choice {
    public c3_73_1() {
        super("3-74");
    }

    @Override
    public void chosen() {
        Constant.kernel.offsetPara(Constant.KNOWLEDGE, 1);
        super.chosen();
    }
}

class c3_73_2 extends abstract_choice {
    public c3_73_2() {
        super("3-75");
    }
}

class c3_75_1 extends abstract_choice {
    public c3_75_1() {
        super("3-76");
    }

    @Override
    public void chosen() {
        Constant.kernel.offsetPara(Constant.BRUCE_LOVE, -1);
        super.chosen();
    }
}

class c3_75_2 extends abstract_choice {
    public c3_75_2() {
        super("3-77");
    }
}

class c3_75_3 extends abstract_choice {
    public c3_75_3() {
        super("3-77");
    }

    @Override
    public String text() {
        return "假装同意";
    }

    @Override
    public void chosen() {
        Constant.kernel.setPara(Constant.TEMPORARY, 1);
        super.chosen();
    }
}

class c3_75_4 extends abstract_choice {
    public c3_75_4() {
        super("3-78");
    }
}

class c3_78_1 extends abstract_choice {
    public c3_78_1() {
        super("3-79");
    }

    @Override
    public boolean show() {
        return Constant.kernel.getPara(Constant.TEMPORARY) == 1;
    }

    @Override
    public void chosen() {
        Constant.kernel.offsetPara(Constant.BRUCE_LOVE, 3);
        super.chosen();
    }
}

class c3_78_2 extends abstract_choice {
    public c3_78_2() {
        super("3-80");
    }
}

class c3_78_3 extends abstract_choice {
    public c3_78_3() {
        super("3-81");
    }

    @Override
    public void chosen() {
        Constant.kernel.offsetPara(Constant.BRUCE_LOVE, 1);
        super.chosen();
    }
}

class c3_78_4 extends abstract_choice {
    public c3_78_4() {
        super("5-1");
    }

    @Override
    public void chosen() {
        Constant.kernel.setPara(Constant.TEMPORARY, 0);
        Constant.kernel.setPara(Constant.TEAMMATE, Constant.BRUCE_CODE);
        super.chosen();
    }
}

class s3_1 extends abstract_scene {
    public s3_1() {
        super(new LinkedList<abstract_choice>() {{
            add(new c3_1_1());
            add(new c3_1_2());
        }});
    }
}

class s3_2 extends abstract_scene {
    public s3_2() {
        super(new LinkedList<abstract_choice>() {{
            add(new c3_2_1());
            add(new c3_2_2());
        }});
    }
}

class s3_4 extends abstract_scene {
    public s3_4() {
        super(new LinkedList<abstract_choice>() {{
            add(new c3_4_1());
            add(new c3_4_2());
        }});
    }
}

class s3_5 extends abstract_scene {
    public s3_5() {
        super(new LinkedList<abstract_choice>() {{
            add(new c3_5_1());
            add(new c3_5_2());
        }});
    }
}

class s3_6 extends abstract_scene {
    public s3_6() {
        super(new LinkedList<abstract_choice>() {{
            add(new c3_6_1());
            add(new c3_6_2());
        }});
    }
}

class s3_8 extends abstract_scene {
    public s3_8() {
        super(new LinkedList<abstract_choice>() {{
            add(new c3_8_1());
            add(new c3_8_2());
        }});
    }
}

class s3_10 extends abstract_scene {
    public s3_10() {
        super(new LinkedList<abstract_choice>() {{
            add(new c3_10_1());
            add(new c3_10_2());
        }});
    }
}

class s3_12 extends abstract_scene {
    public s3_12() {
        super(new LinkedList<abstract_choice>() {{
            add(new c3_12_1());
            add(new c3_12_2());
        }});
    }
}

class s3_16 extends abstract_scene {
    public s3_16() {
        super(new LinkedList<abstract_choice>() {{
            add(new c3_16_1());
            add(new c3_16_2());
        }});
    }
}

class s3_18 extends abstract_scene {
    public s3_18() {
        super(new LinkedList<abstract_choice>() {{
            add(new c3_18_1());
            add(new c3_18_2());
            add(new c3_18_3());
        }});
    }
}

class s3_19 extends abstract_scene {
    public s3_19() {
        super(new LinkedList<abstract_choice>() {{
            add(new c3_19_1());
            add(new c3_19_2());
        }});
    }
}

class s3_20 extends abstract_scene {
    public s3_20() {
        super(new LinkedList<abstract_choice>() {{
            add(new c3_20_1());
            add(new c3_20_2());
        }});
    }
}

class s3_21 extends abstract_scene {
    public s3_21() {
        super(new LinkedList<abstract_choice>() {{
            add(new c3_21_1());
            add(new c3_21_2());
        }});
    }
}

class s3_22 extends abstract_scene {
    public s3_22() {
        super(new LinkedList<abstract_choice>() {{
            add(new c3_22_1());
            add(new c3_22_2());
            add(new c3_22_3());
        }});
    }
}

class s3_23 extends abstract_scene {
    public s3_23() {
        super(new LinkedList<abstract_choice>() {{
            add(new c3_23_1());
            add(new c3_23_2());
        }});
    }
}

class s3_31 extends abstract_scene {
    public s3_31() {
        super(new LinkedList<abstract_choice>() {{
            add(new c3_31_1());
            add(new c3_31_2());
            add(new c3_31_3());
            add(new c3_31_4());
        }});
    }
}

class s3_35 extends abstract_scene {
    public s3_35() {
        super(new LinkedList<abstract_choice>() {{
            add(new c3_35_1());
            add(new c3_35_2());
            add(new c3_35_3());
            add(new c3_35_4());
            add(new c3_35_5());
            add(new c3_35_6());
            add(new c3_35_7());
        }});
    }
}

class s3_36 extends abstract_scene {
    public s3_36() {
        super(new LinkedList<abstract_choice>() {{
            add(new c3_36_1());
            add(new c3_36_2());
            add(new c3_36_3());
        }});
    }
}

class s3_37 extends abstract_scene {
    public s3_37() {
        super(new LinkedList<abstract_choice>() {{
            add(new c3_37_1());
            add(new c3_37_2());
            add(new c3_37_3());
            add(new c3_37_4());
            add(new c3_37_5());
            add(new c3_37_6());
        }});
    }
}

class s3_41 extends abstract_scene {
    public s3_41() {
        super(new LinkedList<abstract_choice>() {{
            add(new c3_41_1());
            add(new c3_41_2());
        }});
    }
}

class s3_43 extends abstract_scene {
    public s3_43() {
        super(new LinkedList<abstract_choice>() {{
            add(new c3_43_1());
            add(new c3_43_2());
        }});
    }
}

class s3_45 extends abstract_scene {
    @Override
    LinkedList<abstract_choice> load() {
        if (Constant.kernel.getPara(Constant.TEMPORARY) == 3) {
            return new LinkedList<abstract_choice>() {{
                add(new c3_45_1());
            }};
        } else if (Constant.kernel.getPara(Constant.TEMPORARY) == 2) {
            return new LinkedList<abstract_choice>() {{
                add(new c3_45_2());
            }};
        } else {
            return new LinkedList<abstract_choice>() {{
                add(new c3_45_3());
            }};
        }
    }
}

class s3_46 extends abstract_scene {
    public s3_46() {
        super(new LinkedList<abstract_choice>() {{
            add(new c3_46_1());
            add(new c3_46_2());
        }});
    }
}

class s3_52 extends abstract_scene {
    public s3_52() {
        super(new LinkedList<abstract_choice>() {{
            add(new c3_52_1());
            add(new c3_52_2());
            add(new c3_52_3());
            add(new c3_52_4());
            add(new c3_52_5());
            add(new c3_52_6());
        }});
    }
}

class s3_58 extends abstract_scene {
    public s3_58() {
        super(new LinkedList<abstract_choice>() {{
            add(new c3_58_1());
            add(new c3_58_2());
            add(new c3_58_3());
        }});
    }
}

class s3_59 extends abstract_scene {
    public s3_59() {
        super(new LinkedList<abstract_choice>() {{
            add(new c3_59_1());
            add(new c3_59_2());
        }});
    }
}

class s3_60 extends abstract_scene {
    public s3_60() {
        super(new LinkedList<abstract_choice>() {{
            add(new c3_60_1());
            add(new c3_60_2());
        }});
    }
}

class s3_61 extends abstract_scene {
    public s3_61() {
        super(new LinkedList<abstract_choice>() {{
            add(new c3_61_1());
            add(new c3_61_2());
        }});
    }
}

class s3_62 extends abstract_scene {
    public s3_62() {
        super(new LinkedList<abstract_choice>() {{
            add(new c3_62_1());
            add(new c3_62_2());
            add(new c3_62_3());
        }});
    }
}

class s3_65 extends abstract_scene {
    public s3_65() {
        super(new LinkedList<abstract_choice>() {{
            add(new c3_65_1());
            add(new c3_65_2());
            add(new c3_65_3());
        }});
    }
}

class s3_66 extends abstract_scene {
    public s3_66() {
        super(new LinkedList<abstract_choice>() {{
            add(new c3_66_1());
            add(new c3_66_2());
            add(new c3_66_3());
        }});
    }
}

class s3_68 extends abstract_scene {
    public s3_68() {
        super(new LinkedList<abstract_choice>() {{
            add(new c3_68_1());
            add(new c3_68_2());
            add(new c3_68_3());
        }});
    }
}

class s3_73 extends abstract_scene {
    public s3_73() {
        super(new LinkedList<abstract_choice>() {{
            add(new c3_73_1());
            add(new c3_73_2());
        }});
    }
}

class s3_75 extends abstract_scene {
    public s3_75() {
        super(new LinkedList<abstract_choice>() {{
            add(new c3_75_1());
            add(new c3_75_2());
            add(new c3_75_3());
        }});
    }
}

class s3_78 extends abstract_scene {
    public s3_78() {
        super(new LinkedList<abstract_choice>() {{
            add(new c3_78_1());
            add(new c3_78_2());
            add(new c3_78_3());
        }});
    }
}
