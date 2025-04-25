package com.tuzicao.emeraldknight.kernel;

import java.util.LinkedList;

class end_choice extends abstract_choice {
    public end_choice(String s) {
        super(s);
    }

    @Override
    public String text() {
        return "战斗结束了";
    }
}

class fail_choice extends end_choice {
    public fail_choice() {
        super("end-15");
    }
}

class end_16 extends end_choice {
    public end_16() {
        super("end-16");
    }
}

class end_17 extends end_choice {
    public end_17() {
        super("end-17");
    }
}

class end_18 extends end_choice {
    public end_18() {
        super("end-18");
    }
}

class end_scene extends abstract_scene {
    @Override
    public LinkedList<abstract_choice> load() {
        if (Constant.kernel.getPara(Constant.TEMPORARY) == 2) {
            return new LinkedList<abstract_choice>() {{
                add(new end_16());
            }};
        } else if ((Constant.kernel.getPara(Constant.BRUCE_LOVE) == 20) && (Constant.kernel.getPara(Constant.TEMPORARY) == 0)) {
            return new LinkedList<abstract_choice>() {{
                add(new end_17());
            }};
        } else {
            return new LinkedList<abstract_choice>() {{
                add(new end_18());
            }};
        }
    }
}