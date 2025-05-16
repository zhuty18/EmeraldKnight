// let storyEl = document.getElementById("story");
// let inputEl = document.getElementById("playerInput");

// function handleInput () {
//     const choice = inputEl.value.trim().toLowerCase();
//     inputEl.value = "";

//     if (choice === "进入") {
//         storyEl.textContent = "你迈入森林，四周变得昏暗。远处传来狼嚎...";
//     } else if (choice === "离开") {
//         storyEl.textContent = "你转身离开，但心中有些许遗憾。也许，这是个错误的决定。";
//     } else {
//         storyEl.textContent = `你说了“${choice}”，但风似乎没有回应。试试别的？`;
//     }
// }

import "./app.css"

let paras = {}
let scene = "end-1"
let config_data = {}

await fetch("data/config.json")
    .then((res) => res.json())
    .then((data) => {
        config_data = data
    })

function 配置初始化 () {
    for (let i = 0; i < config_data.para_list.length; i++) {
        paras[config_data.para_list[i].name] = config_data.para_list[i].default_value
    }
}

// 配置初始化();

function chapter_id (scene) {
    return scene.split("-")[0]
}

function chapter_name (scene) {
    if ("ch" + chapter_id(scene) in config_data.chap_map) {
        return config_data.chap_map["ch" + chapter_id(scene)]
    } else if (scene.includes("end")) {
        return config_data.chap_map.end + config_data.end_map[scene]
    }
    return "未知章节"
}

function refresh_story () {
    document.getElementById("scene_title").textContent = chapter_name(scene)
}

refresh_story()
