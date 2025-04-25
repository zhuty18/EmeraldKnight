package com.tuzicao.emeraldknight.kernel;

import java.util.LinkedList;

public class abstract_scene {
    LinkedList<abstract_choice> option;

    public abstract_scene() {
        option = new LinkedList<abstract_choice>();
    }

    public abstract_scene(LinkedList<abstract_choice> l) {
        option = l;
    }

    LinkedList<abstract_choice> load() {
        LinkedList<abstract_choice> tmp = new LinkedList<>();
        for (int i = 0; i < option.size(); i++) {
            if (option.get(i).show()) {
                tmp.add(option.get((i)));
            }
        }
        return tmp;
    }
}
