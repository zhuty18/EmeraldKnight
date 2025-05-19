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
let scene = "1-1"

function initPara (configData) {
    for (var key in configData.para_map) {
        paras[key] = configData.para_map[key].default_value
    }
}

function toScene (target) {
    scene = target
    refreshStory()
}

function chooseChoice (choice_id) {
    if (scene === configData.const_map.START_OVER) {
        toScene(configData.const_map.START_SCENE)
        initPara()
    } else {
        if (configData.choice_map[choice_id].choose) {
            configData.choice_map[choice_id].choose.forEach((action) =>
                changePara(configData, scene, paras, action)
            )
        }
        toScene(configData.choice_map[choice_id].target)
    }
}

function currentChoices (configData, scene, paras) {
    if (scene === configData.const_map.START_OVER) {
        return [
            {
                id: "default_id",
                text: "开始游戏",
            },
        ]
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
    story.insertAdjacentHTML(
        "afterbegin",
        debugInfo() + sceneText(configData, scene)
    )
    let choice_list = document.getElementById("choice_list")
    clearNode(choice_list)
    let choice = currentChoices(configData, scene, paras)
    for (var i = 0; i < choice.length; i++) {
        let btn = document.createElement("button")
        btn.textContent = choice[i].text
        btn.classList = ["btn btn-primary w-full shadow-lg"]
        btn.id = choice[i].id
        btn.onclick = function () {
            chooseChoice(this.id)
        }
        choice_list.appendChild(btn)
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
