import "./app.css"
import { chapter_name, scene_text, choice_text } from "./story"
import { mark_end, check_end } from "./save"

let config_data = {}

await fetch("data/config.json")
    .then((res) => res.json())
    .then((data) => {
        config_data = data
    })

let paras = {}

// let scene = config_data.const_map.START_OVER
let scene = "1-1"

function init_para () {
    for (var key in config_data.para_map) {
        paras[key] = config_data.para_map[key].default_value
    }
}

function to_scene (target) {
    scene = target
    refresh_story()
}

function choose (choice_id) {
    if (scene === config_data.const_map.START_OVER) {
        to_scene(config_data.const_map.START_SCENE)
        init_para()
    }
    to_scene(config_data.choice_map[choice_id].target)
}

function check_condition (paras, condition) {
    if (condition.check === "CONDITION") {
        return check_is(paras, condition.para) == check.value
    }
    let value_a = 1
    let value_b = check.value
    return true
}

function check_is (paras, check) {
    if (check.op === "AND") {
        return check.map((x) => check_condition(paras, x)).reduce((a, b) => a && b)
    } else if (check.op === "OR") {
        return check.map((x) => check_condition(paras, x)).reduce((a, b) => a || b)
    }
}

function choice_show (paras, choice_id) {
    let choice = config_data.choice_map[choice_id]
    if (choice.show) {
        return check_is(paras, choice.show)
    }
    return true
}

function current_choices (scene, paras) {
    if (scene === config_data.const_map.START_OVER) {
        return [
            {
                id: "default_id",
                text: "开始游戏",
            },
        ]
    }
    {
        let options = config_data.scene_map[scene].options
        let res = []
        for (var i = 0; i < options.length; i++) {
            if (choice_show(paras, options[i])) {
                res.push({
                    id: options[i],
                    text: choice_text(options[i]),
                })
            }
        }
        return res
    }
}

function clear_node (parent) {
    while (parent.firstChild) {
        parent.removeChild(parent.firstChild)
    }
}

function refresh_story () {
    document.getElementById("scene_title").textContent = chapter_name(scene)
    let story = document.getElementById("story")
    clear_node(story)
    story.insertAdjacentHTML("afterbegin", scene_text(scene))
    let choice_list = document.getElementById("choice_list")
    clear_node(choice_list)
    let choice = current_choices(scene, paras)
    for (var i = 0; i < choice.length; i++) {
        let btn = document.createElement("button")
        btn.textContent = choice[i].text
        btn.classList = ["btn btn-primary w-full shadow-lg"]
        btn.id = choice[i].id
        btn.onclick = function () {
            choose(this.id)
        }
        choice_list.appendChild(btn)
    }
}

refresh_story()
