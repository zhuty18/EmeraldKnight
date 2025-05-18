let config_data = {}

await fetch("data/config.json")
    .then((res) => res.json())
    .then((data) => {
        config_data = data
    })

function chapter_id (scene) {
    return scene.split("-")[0]
}

function chapter_name (scene) {
    if ("ch" + chapter_id(scene) in config_data.chap_map) {
        return config_data.chap_map["ch" + chapter_id(scene)]
    } else if (scene.includes("end")) {
        return config_data.chap_map.end + config_data.end_map[scene]
    } else if (scene === config_data.const_map.START_OVER) {
        return config_data.info.name_zh
    }
    return "无效章节"
}

function scene_text (scene_id) {
    if (scene_id === config_data.const_map.START_OVER) {
        let res = "<div style='text-align:center'>"
        for (var i = 0; i < config_data.info.poem.length; i++) {
            res += "<p>"
            res += config_data.info.poem[i].join("&nbsp;&nbsp;&nbsp;&nbsp;")
            res += "</p>"
        }
        res += "</div>"
        return res
    } else {
        let story = config_data.story[scene_id].split("\n")
        let res = ""
        for (var i = 0; i < story.length; i++) {
            res += "<p>"
            res += story[i]
            res += "</p>"
        }
        return res
    }
}

function choice_text (choice_id) {
    if (config_data.choice_map[choice_id].text) {
        return config_data.choice_map[choice_id].text
    } else {
        return config_data.scene_map[config_data.choice_map[choice_id].target].name
    }
}

export { scene_text, chapter_name, choice_text }
