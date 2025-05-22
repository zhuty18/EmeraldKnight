import { getPara, choiceFromOption, checkIs } from "./story"

function initBattle (configData, paras) {
    let hero = configData.char_map[configData.const_map.BATTLE_STORY.HERO]
    hero.attack = 100
    hero.attack += getPara(configData, paras, "BRUCE_LOVE") * 2
    hero.attack += getPara(configData, paras, "INTELLIGENCE") * 2
    hero.attack += getPara(configData, paras, "DRAGON_EGG") * 10
    hero.speed = 100
    hero.speed += getPara(configData, paras, "KNOWLEDGE")
    hero.speed += getPara(configData, paras, "PEGASUS") * 20
    hero.max_life = 100
    hero.max_life += getPara(configData, paras, "OLIVER_LOVE") * 10
    hero.max_life += getPara(configData, paras, "BARRY_LOVE") * 10
    hero.life = hero.max_life
    for (var i in hero.actions) {
        if (hero.actions[i].type === "HEAL") {
            hero.actions[i].used = 0
        }
    }

    let enemy = configData.char_map[configData.const_map.BATTLE_STORY.ENEMY]
    enemy.attack = 100
    enemy.attack -= getPara(configData, paras, "SINESTRO_LOVE") * 5
    enemy.speed = 100
    enemy.speed -= getPara(configData, paras, "SINESTRO_TAME") * 2
    enemy.life = enemy.max_life
    for (var i in enemy.actions) {
        if (enemy.actions[i].type === "HEAL") {
            enemy.actions[i].used = 0
        }
    }

    let battle = { hero: hero, enemy: enemy, round: 0 }
    return battle
}

function battleStatus (hero, enemy) {
    let res = "<p>" + enemy.name + "</p>"
    res += "<p>" + enemy.life + " / " + enemy.max_life + "</p>"
    res +=
        "<p class='text-right' style='margin-right:2em'>" + hero.name + "</p>"
    res +=
        "<p class='text-right' style='margin-right:2em'>" +
        hero.life +
        " / " +
        hero.max_life +
        "</p>"
    return res
}

function battleText (configData, battle) {
    if (battle.round == 0) {
        let res = "<p>" + configData.const_map.BATTLE_STORY.START + "</p>"
        return battleStatus(battle.hero, battle.enemy) + res
    } else {
        let res = battleStatus(battle.hero, battle.enemy)
        res += "<p>" + battle.hero_text
        if (battle.enemy.life == 0) {
            res +=
                configData.const_map.BATTLE_STORY.WIN.replace("\n", "</p><p>") +
                "</p>"
            return res
        }
        enemyMove(configData, battle)
        res = battleStatus(battle.hero, battle.enemy)
        res += "<p>" + battle.hero_text + "</p>"
        res += "<p>" + battle.enemy_text
        if (battle.hero.life == 0) {
            res +=
                configData.const_map.BATTLE_STORY.LOSE.replace(
                    "\n",
                    "</p><p>"
                ) + "</p>"
            return res
        }
        return res
    }
}

function battleChoices (configData, paras, hero, enemy) {
    let res = []
    if (enemy.life == 0) {
        let options =
            configData.scene_map[configData.const_map.FINAL_BATTLE].options_win
        return choiceFromOption(
            configData,
            configData.const_map.FINAL_BATTLE,
            paras,
            options
        )
    } else if (hero.life == 0) {
        let options =
            configData.scene_map[configData.const_map.FINAL_BATTLE].options_lose
        return choiceFromOption(
            configData,
            configData.const_map.FINAL_BATTLE,
            paras,
            options
        )
    } else {
        for (var i = 0; i < hero.actions.length; i++) {
            if (hero.actions[i].show) {
                if (
                    checkIs(
                        configData,
                        configData.const_map.FINAL_BATTLE,
                        paras,
                        hero.actions[i].show
                    )
                ) {
                    res.push({
                        id: hero.actions[i].id,
                        text: hero.actions[i].name,
                    })
                }
            } else if (hero.actions[i].type === "HEAL") {
                if (hero.actions[i].used < hero.actions[i].time) {
                    res.push({
                        id: hero.actions[i].id,
                        text: hero.actions[i].name,
                    })
                }
            } else {
                res.push({
                    id: hero.actions[i].id,
                    text: hero.actions[i].name,
                })
            }
        }
        return res
    }
}

function hurt (target, damage) {
    target.life = Math.max(target.life - damage, 0)
}

function heal (target, amount) {
    target.life = Math.min(target.life + amount, target.max_life)
}

function useAttack (configData, self, target, act) {
    let text = act.text
    if (act.self_hurt) {
        let self_hurt =
            Math.floor(
                Math.random() * (act.self_hurt.max - act.self_hurt.min)
            ) + act.self_hurt.min
        text += act.self_hurt.text.replace(
            configData.const_map.BATTLE_STORY.BLANK,
            self_hurt.toString()
        )
        hurt(self, self_hurt)
    }
    let dodge = 50 + self.speed - target.speed
    if (Math.random() * 500 < dodge) {
        text += configData.const_map.BATTLE_STORY.DODGE
    } else {
        let damage = Math.floor(
            self.attack * (0.8 + 0.4 * Math.random()) * act.strength
        )
        text += configData.const_map.BATTLE_STORY.HURT.replace(
            configData.const_map.BATTLE_STORY.BLANK,
            damage.toString()
        )
        hurt(target, damage)
    }
    return text
}

function useHeal (configData, self, act) {
    let text = act.text
    let amount = Math.floor(Math.random() * (act.max - act.min)) + act.min
    text += configData.const_map.BATTLE_STORY.HEAL.replace(
        configData.const_map.BATTLE_STORY.BLANK,
        amount.toString()
    )
    heal(self, amount)
    act.used += 1
    return text
}

function useCheat (target, act) {
    hurt(target, target.life)
    return act.text
}

function enemyMove (configData, battle) {
    let moveChance = []
    for (var i = 0; i < battle.enemy.actions.length; i++) {
        let act = battle.enemy.actions[i]
        if (act.type === "HEAL") {
            if (act.used == 0 && act.first) {
                if (battle.enemy.life < act.first) {
                    battle.enemy_text = useHeal(configData, battle.enemy, act)
                    return
                }
            } else {
                if (battle.enemy.life < act.trigger) {
                    battle.enemy_text = useHeal(configData, battle.enemy, act)
                    return
                }
            }
        } else {
            moveChance.push(act)
        }
    }
    let dice =
        moveChance.map((act) => act.chance).reduce((a, b) => a + b) *
        Math.random()
    for (var i = 0; i < moveChance.length; i++) {
        dice -= moveChance[i].chance
        if (dice <= 0) {
            battle.enemy_text = useAttack(
                configData,
                battle.enemy,
                battle.hero,
                moveChance[i]
            )
            return
        }
    }
}

export { initBattle, battleText, battleChoices, useAttack, useHeal, useCheat }
