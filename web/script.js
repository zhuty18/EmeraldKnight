import "./app.css"
import {
    chapterName,
    sceneText,
    sceneOptions,
    changePara,
    getPara,
    checkIs,
    choiceFromOption,
} from "./story"
import { markEnd, checkEnd } from "./save"

let configData = {}

await fetch("data/config.json")
    .then((res) => res.json())
    .then((data) => {
        configData = data
    })

let paras = {}

// let scene = configData.const_map.START_OVER
let scene = "6-6"

let battle = null

function initPara (configData) {
    for (var key in configData.para_map) {
        paras[key] = configData.para_map[key].default_value
    }
}

function toScene (target) {
    scene = target
    if (target.includes("end-")) {
        markEnd(target)
    }
    refreshStory()
}

function chooseChoice (choice_id) {
    if (scene === configData.const_map.START_OVER) {
        toScene(configData.const_map.START_SCENE)
        initPara()
    } else if (choice_id === configData.const_map.END_CHOICE.id) {
        console.log(configData.const_map.START_OVER)
        toScene(configData.const_map.START_OVER)
    } else {
        if (configData.choice_map[choice_id].choose) {
            configData.choice_map[choice_id].choose.forEach((action) =>
                changePara(configData, scene, paras, action)
            )
        }
        toScene(configData.choice_map[choice_id].target)
    }
    document.documentElement.scrollTop = 0
}

function currentChoices (configData, scene, paras) {
    if (scene.includes("end")) {
        return [configData.const_map.END_CHOICE]
    } else {
        return choiceFromOption(
            configData,
            scene,
            paras,
            sceneOptions(configData, scene, paras)
        )
    }
}

function battleAct (actId) {
    battle.round += 1
    let act = null
    for (var i = 0; i < battle.hero.actions.length; i++) {
        if (battle.hero.actions[i].id === actId) {
            act = battle.hero.actions[i]
            break
        }
    }
    if (act === null) {
        return chooseChoice(actId)
    }
    let text = ""
    switch (act.type) {
        case "ATTACK":
            text = useAttack(configData, battle.hero, battle.enemy, act)
            break
        case "HEAL":
            text = useHeal(configData, battle.hero, act)
            break
        case "CHEAT":
            text = useCheat(battle.enemy, act)
            break
    }
    battle.hero_text = text
    console.log("hero_text: " + battle.hero_text)
    refreshStory()
}

function clearNode (parent) {
    while (parent.firstChild) {
        parent.removeChild(parent.firstChild)
    }
}

function refreshStory () {
    document.getElementById("scene_title").textContent = chapterName(
        configData,
        scene
    )
    let story = document.getElementById("story")
    clearNode(story)
    let choice_list = document.getElementById("choice_list")
    clearNode(choice_list)
    if (scene === configData.const_map.START_OVER) {
        let startText = "<div style='text-align:center'>"
        for (var i = 0; i < configData.info.poem.length; i++) {
            startText += "<p style='text-indent:0em'>"
            startText += configData.info.poem[i].join(
                "&nbsp;&nbsp;&nbsp;&nbsp;"
            )
            startText += "</p>"
        }
        startText += "</div>"
        story.insertAdjacentHTML("afterbegin", startText)
        let btn = document.createElement("button")
        btn.textContent = "开始游戏"
        btn.classList = ["btn btn-primary w-full shadow-lg"]
        btn.id = "start_game"
        btn.onclick = function () {
            chooseChoice(this.id)
        }
        choice_list.appendChild(btn)
        for (var i in configData.end_map) {
            let endBtn = document.createElement("button")
            endBtn.classList = "btn w-full btn-soft"
            endBtn.id = i
            if (checkEnd(i)) {
                endBtn.textContent =
                    configData.chap_map.end + configData.end_map[i]
                endBtn.className = " btn-success"
                endBtn.onclick = function () {
                    toScene(this.id)
                }
            } else {
                endBtn.textContent = configData.chap_map.end + "未解锁"
                endBtn.classList += " btn-disabled"
            }
            choice_list.appendChild(endBtn)
        }
    } else if (scene.includes("end")) {
        story.insertAdjacentHTML("afterbegin", sceneText(configData, scene))
        let btn = document.createElement("button")
        btn.classList = ["btn btn-primary w-full shadow-lg"]
        btn.id = configData.const_map.END_CHOICE.id
        btn.textContent = configData.const_map.END_CHOICE.text
        btn.onclick = function () {
            chooseChoice(this.id)
        }
        choice_list.appendChild(btn)
    } else if (scene === configData.const_map.FINAL_BATTLE) {
        if (battle === null) {
            battle = initBattle(configData, paras)
        }
        console.log(battle)

        story.insertAdjacentHTML("afterbegin", battleText(configData, battle))
        let choice = battleChoices(configData, paras, battle.hero, battle.enemy)
        for (var i = 0; i < choice.length; i++) {
            let btn = document.createElement("button")
            btn.textContent = choice[i].text
            btn.classList = "btn btn-primary w-full shadow-lg"
            btn.id = choice[i].id
            btn.onclick = function () {
                battleAct(this.id)
            }
            choice_list.appendChild(btn)
        }
    } else if (scene in configData.scene_map) {
        story.insertAdjacentHTML("afterbegin", sceneText(configData, scene))
        // story.insertAdjacentHTML("afterbegin", debugInfo())
        let choice = currentChoices(configData, scene, paras)
        for (var i = 0; i < choice.length; i++) {
            let btn = document.createElement("button")
            btn.textContent = choice[i].text
            btn.classList = "btn btn-primary w-full shadow-lg"
            btn.id = choice[i].id
            btn.onclick = function () {
                chooseChoice(this.id)
            }
            choice_list.appendChild(btn)
        }
    }
}

refreshStory()

function debugInfo () {
    let res = "<div>"
    res += "<p>scene: " + scene + "</p><p>"
    for (var i in configData.para_map) {
        res += i + ": " + getPara(configData, paras, i) + "；"
    }
    res += "</p></div>"
    return res
}

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

    let enemy = configData.char_map[configData.const_map.BATTLE_STORY.ENEMY]
    enemy.attack = 100
    enemy.attack -= getPara(configData, paras, "SINESTRO_LOVE") * 5
    enemy.speed = 100
    enemy.speed -= getPara(configData, paras, "SINESTRO_TAME") * 2
    enemy.life = enemy.max_life

    let battle = { hero: hero, enemy: enemy, round: 0 }
    return battle
}

function battleStatus (configData, paras, hero, enemy) {
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
    console.log(battle.round)

    if (battle.round == 0) {
        let res = "<p>" + configData.const_map.BATTLE_STORY.START + "</p>"
        return battleStatus(configData, paras, battle.hero, battle.enemy) + res
    } else {
        let res = battleStatus(configData, paras, battle.hero, battle.enemy)
        res += "<p>" + battle.hero_text + "</p>"
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
                    console.log(hero.actions[i].show)
                    res.push({
                        id: hero.actions[i].id,
                        text: hero.actions[i].name,
                    })
                }
            } else if (hero.actions[i].type === "HEAL") {
                if (!hero.actions[i].used) {
                    hero.actions[i].used = 0
                }
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
    let dodge = 50 + self.speed - target.speed
    if (Math.random() * 500 < dodge) {
        text += configData.const_map.BATTLE_STORY.DODGE
    } else {
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
