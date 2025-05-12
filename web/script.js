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

import "./app.css";

let paras = {};
let scene = "";

fetch("data/paras.json")
    .then((res) => res.json())
    .then((data) => {
        for (let i = 0; i < data.para_list.length; i++) {
            paras[data.para_list[i].name] = data.para_list[i].default_value;
        }
    });

function chapter_id(scene) {
    return scene.split("-")[0];
}

function chapter_name(scene) {
    fetch("data/names.json")
        .then((res) => res.json())
        .then((data) => {
            if (data.chapter_names.includes(chapter_id(scene))) {
                return data.chapter_names[chapter_id(scene)];
            }
        });
    return scene + "章名";
}

function refresh_story() {
    document.getElementById("scene_title").textContent = chapter_name(scene);
}

refresh_story();
