package atomic1028.gl.emeraldknight.kernel;

import java.util.LinkedList;

class c7_1_1 extends abstract_choice {
    public c7_1_1() {
        super("end-19");
    }

    @Override
    public String text() {
        return "打断他";
    }
}

class c7_1_2 extends abstract_choice {
    public c7_1_2() {
        super("7-2");
    }
}

class c7_2_1 extends abstract_choice {
    public c7_2_1() {
        super("7-3");
    }
}

class c7_3_1 extends abstract_choice {
    public c7_3_1() {
        super("end-19");
    }

    @Override
    public String text() {
        return "瞎几把扯";
    }
}

class c7_3_2 extends abstract_choice {
    public c7_3_2() {
        super("7-5");
    }
}

class c7_3_3 extends abstract_choice {
    public c7_3_3() {
        super("7-4");
    }
}

class c7_5_1 extends abstract_choice {
    public c7_5_1() {
        super("7-6");
    }

    @Override
    public boolean show() {
        return Constant.kernel.getPara(Constant.KNOWLEDGE) >= 5;
    }
}

class c7_5_2 extends abstract_choice {
    public c7_5_2() {
        super("7-8");
    }

    @Override
    public boolean show() {
        return (Constant.kernel.getPara(Constant.BRUCE_INTRODUCE) == 1) && (Constant.kernel.getPara(Constant.KNOWLEDGE) < 5);
    }
}

class c7_5_3 extends abstract_choice {
    public c7_5_3() {
        super("7-9");
    }
}

class c7_6_1 extends abstract_choice {
    public c7_6_1() {
        super("end-20");
    }

    @Override
    public String text() {
        return "讨伐魔王";
    }
}

class c7_6_2 extends abstract_choice {
    public c7_6_2() {
        super("7-7");
    }
}

class c7_8_1 extends abstract_choice {
    public c7_8_1() {
        super("end-21");
    }

    @Override
    public String text() {
        return "你这样，来阻止我？";
    }
}

class s7_1 extends abstract_scene {
    public s7_1() {
        super(new LinkedList<abstract_choice>() {{
            add(new c7_1_1());
            add(new c7_1_2());
        }});
    }
}

class s7_2 extends abstract_scene {
    public s7_2() {
        super(new LinkedList<abstract_choice>() {{
            add(new c7_1_1());
            add(new c7_2_1());
        }});
    }
}

class s7_3 extends abstract_scene {
    public s7_3() {
        super(new LinkedList<abstract_choice>() {{
            add(new c7_3_1());
            add(new c7_3_2());
            add(new c7_3_3());
        }});
    }
}

class s7_5 extends abstract_scene {
    public s7_5() {
        super(new LinkedList<abstract_choice>() {{
            add(new c7_5_1());
            add(new c7_5_2());
            add(new c7_5_3());
        }});
    }
}

class s7_6 extends abstract_scene {
    public s7_6() {
        super(new LinkedList<abstract_choice>() {{
            add(new c7_6_1());
            add(new c7_6_2());
        }});
    }
}
