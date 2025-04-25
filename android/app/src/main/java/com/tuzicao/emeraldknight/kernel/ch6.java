package com.tuzicao.emeraldknight.kernel;
class c6_1_1 extends abstract_choice {
    public c6_1_1() {
        super("6-2");
    }
}

class c6_2_1 extends abstract_choice {
    public c6_2_1() {
        super("6-3");
    }
}

class c6_3_1 extends abstract_choice {
    public c6_3_1() {
        super("6-4");
    }
}

class c6_4_1 extends abstract_choice {
    public c6_4_1() {
        super("6-5");
    }
}

class c6_5_1 extends abstract_choice {
    public c6_5_1() {
        super(Constant.FINAL_BATTLE);
    }

    @Override
    public String text() {
        return "决战";
    }

    @Override
    public void chosen() {
        Constant.kernel.startBattle();
        super.chosen();
    }
}