function chapterId (scene) {
    return scene.split("-")[0]
}

function chapterName (configData, scene) {
    if ("ch" + chapterId(scene) in configData.chap_map) {
        return configData.chap_map["ch" + chapterId(scene)]
    } else if (scene.includes("end")) {
        return configData.chap_map.end + configData.end_map[scene]
    } else if (scene === configData.const_map.START_OVER) {
        return configData.info.name_zh
    }
    return "无效章节"
}

function sceneText (configData, scene_id) {
    if (scene_id === configData.const_map.START_OVER) {
        let res = "<div style='text-align:center'>"
        for (var i = 0; i < configData.info.poem.length; i++) {
            res += "<p>"
            res += configData.info.poem[i].join("&nbsp;&nbsp;&nbsp;&nbsp;")
            res += "</p>"
        }
        res += "</div>"
        return res
    } else {
        let story = configData.story[scene_id].split("\n")
        let res = ""
        for (var i = 0; i < story.length; i++) {
            res += "<p>"
            res += story[i]
            res += "</p>"
        }
        return res
    }
}

function choiceText (configData, choice_id) {
    if (configData.choice_map[choice_id].text) {
        return configData.choice_map[choice_id].text
    } else {
        return configData.scene_map[configData.choice_map[choice_id].target].name
    }
}

export { sceneText, chapterName, choiceText }
