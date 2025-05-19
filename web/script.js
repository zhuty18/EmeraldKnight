import "./app.css"
import { chapterName, sceneText, choiceText } from "./story"
import { markEnd, checkEnd } from "./save"

let configData = {}

await fetch("data/config.json")
    .then((res) => res.json())
    .then((data) => {
        configData = data
    })

let paras = {}

// let scene = config_data.const_map.START_OVER
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
    }
    toScene(configData.choice_map[choice_id].target)
}

function currentChoices (configData, scene, paras) {
    if (scene === configData.const_map.START_OVER) {
        return [
            {
                id: "default_id",
                text: "开始游戏",
            },
        ]
    }
    {
        let options = configData.scene_map[scene].options
        let res = []
        for (var i = 0; i < options.length; i++) {
            if (choiceShow(configData, paras, options[i])) {
                res.push({
                    id: options[i],
                    text: choiceText(configData, options[i]),
                })
            }
        }
        return res
    }
}

function clearNode (parent) {
    while (parent.firstChild) {
        parent.removeChild(parent.firstChild)
    }
}

function refreshStory () {
    document.getElementById("scene_title").textContent = chapterName(configData, scene)
    let story = document.getElementById("story")
    clearNode(story)
    story.insertAdjacentHTML("afterbegin", sceneText(configData, scene))
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

function checkCondition (configData, paras, condition) {
    if (condition.check === "CONDITION") {
        return checkIs(paras, condition.para) == check.value
    }
    let value_a = 1
    let value_b = check.value
    return true
}

function checkIs (configData, paras, check) {
    if (check.op === "AND") {
        return check.map((x) => checkCondition(configData, paras, x)).reduce((a, b) => a && b)
    } else if (check.op === "OR") {
        return check.map((x) => checkCondition(configData, paras, x)).reduce((a, b) => a || b)
    }
}

function choiceShow (configData, paras, choice_id) {
    let choice = configData.choice_map[choice_id]
    if (choice.show) {
        return checkIs(paras, choice.show)
    }
    return true
}
