import "./app.css"
import {
    chapterName,
    sceneText,
    sceneChoices,
    changePara,
    getPara,
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
let scene = "end-1"

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
        return sceneChoices(configData, scene, paras)
    }
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

function battleStatus (configData, paras, hero, enemy) { }

function battleText (configData, round, hero, enemy) {
    if (round == 0) {
    }
}
