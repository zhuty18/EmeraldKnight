import "./app.css"
import {
    chapterName,
    sceneText,
    sceneOptions,
    changePara,
    getPara,
    choiceFromOption,
} from "./story"
import { markEnd, checkEnd, saveAt, loadAt } from "./save"
import {
    useAttack,
    useCheat,
    useHeal,
    initBattle,
    battleText,
    battleChoices,
} from "./battle"

let configData = {}

await fetch("data/config.json")
    .then((res) => res.json())
    .then((data) => {
        configData = data
    })

let paras = {}
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
    } else if (choice_id === configData.const_map.END_CHOICE.id) {
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
    refreshStory()
}

function saveGame (index) {
    saveAt(
        {
            scene: scene,
            paras: paras,
        },
        index
    )
    console.log("save game at " + index)
}

function loadGame (index) {
    let saveData = loadAt(index)
    if (saveData && saveData.scene && saveData.paras) {
        scene = saveData.scene
        paras = saveData.paras
    } else {
        scene = configData.const_map.START_OVER
        initPara(configData)
    }
    refreshStory()
}

function clearNode (parent) {
    while (parent.firstChild) {
        parent.removeChild(parent.firstChild)
    }
}

function refreshStory () {
    // if (
    //     scene !== configData.const_map.FINAL_BATTLE
    // ) {
    //     saveGame(0)
    // }

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
        let blank = document.createElement("div")
        blank.style.height = "5em"
        choice_list.appendChild(blank)
        for (var i in configData.end_map) {
            let endBtn = document.createElement("button")
            endBtn.classList = "btn w-full btn-soft"
            endBtn.id = i
            if (checkEnd(i)) {
                endBtn.textContent =
                    configData.chap_map.end +
                    i.replace("end-", "") +
                    configData.end_map[i]
                endBtn.classList += " btn-success"
                endBtn.onclick = function () {
                    toScene(this.id)
                }
            } else {
                endBtn.innerHTML =
                    configData.chap_map.end +
                    i.replace("end-", "") +
                    "&nbsp;&nbsp;&nbsp;未解锁"
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

loadGame(0)
// document.getElementById("start_alarm").showModal()

document.getElementById("restart_btn").onclick = startOver
function startOver () {
    loadGame(-1)
}

document.getElementById("save_btn").onclick = function () {
    showSave(true)
}
document.getElementById("load_btn").onclick = function () {
    showSave(false)
}
function showSave (saving) { }

function debugInfo () {
    let res = "<div>"
    res += "<p>scene: " + scene + "</p><p>"
    for (var i in configData.para_map) {
        res += i + ": " + getPara(configData, paras, i) + "；"
    }
    res += "</p></div>"
    return res
}
