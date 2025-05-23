import { checkEnd } from "./save"

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
    let story = configData.story[scene_id].split("\n")
    let res = ""
    for (var i = 0; i < story.length; i++) {
        res += "<p>"
        res += story[i]
        res += "</p>"
    }
    return res
}

function choiceText (configData, choice_id) {
    if (configData.choice_map[choice_id].text) {
        return configData.choice_map[choice_id].text
    } else {
        return configData.scene_map[configData.choice_map[choice_id].target]
            .name
    }
}

function getPara (configData, paras, paraId) {
    return paras[configData.para_map[paraId].name] ?? 0
}

function setPara (configData, paras, paraId, value) {
    paras[configData.para_map[paraId].name] = value
}

let fightAt = {}

function fightRes (configData, paras) {
    let hp = getPara(configData, paras, "TEMPORARY")
    hp += 3 * getPara(configData, paras, "INTELLIGENCE")
    hp += getPara(configData, paras, "KNOWLEDGE")
    hp += 5 * getPara(configData, paras, "BRUCE_LOVE")
    hp += 5 * getPara(configData, paras, "SINESTRO_LOVE")
    hp += 5 * getPara(configData, paras, "SINESTRO_TAME")
    hp += 20 * (getPara(configData, paras, "TEAMMATE") !== 0 ? 1 : 0)
    for (let i = 0; i < 10; i++) {
        hp -= Math.random() * 16
    }
    return hp > 0
}

function fightResult (configData, scene, paras) {
    if (!(scene in fightAt)) {
        fightAt[scene] = fightRes(configData, paras) ? 1 : 0
    }
    return fightAt[scene]
}

function checkCondition (configData, scene, paras, condition) {
    if (condition.check === "CONDITION") {
        return checkIs(paras, condition.para) == condition.value
    }
    let value_a = null
    let value_b = null
    if (configData.func_list.includes(condition.para)) {
        switch (condition.para) {
            case "SCENE":
                value_a = scene
                break
            case "FIGHT":
                value_a = fightResult(configData, scene, paras)
                break
            case "CHOICE":
                value_a = choiceShow(configData, scene, paras, condition.value)
                    ? 1
                    : 0
                value_b = 1
                break
        }
    } else if (condition.para.includes("end")) {
        value_a = checkEnd(condition.para) ? 1 : 0
    } else {
        value_a = getPara(configData, paras, condition.para)
    }

    if (value_b === null) {
        if (
            typeof condition.value === "string" &&
            condition.value.includes("CODE")
        ) {
            value_b = configData.code_map[condition.value]
        } else {
            value_b = condition.value
        }
    }

    switch (condition.check) {
        case "EQUAL":
            return value_a === value_b
        case "UNEQUAL":
            return value_a !== value_b
        case "MORE":
            return value_a > value_b
        case "MORE_EQUAL":
            return value_a >= value_b
        case "LESS":
            return value_a < value_b
        case "LESS_EQUAL":
            return value_a <= value_b
        case "BINARY":
            return ((value_a >> (value_b - 1)) & 1) === 1
        case "NON_BINARY":
            return ((value_a >> (value_b - 1)) & 1) === 0
        default:
            return false
    }
}

function checkIs (configData, scene, paras, check) {
    let checks = check.condition.map((x) =>
        checkCondition(configData, scene, paras, x)
    )
    switch (check.op) {
        case "AND":
            return checks.reduce((a, b) => a && b)
        case "OR":
            return checks.reduce((a, b) => a || b)
    }
}

function choiceShow (configData, scene, paras, choice_id) {
    let choice = configData.choice_map[choice_id]
    if (choice.show) {
        return checkIs(configData, scene, paras, choice.show)
    }
    return true
}

function changePara (configData, scene, paras, action) {
    if (action.change === "CONDITION") {
        if (checkIs(configData, scene, paras, action.para)) {
            action.value.forEach((change) =>
                changePara(configData, scene, paras, change)
            )
        }
    } else {
        let value =
            typeof action.value === "string"
                ? configData.code_map[action.value]
                : action.value
        switch (action.change) {
            case "ADD":
                setPara(
                    configData,
                    paras,
                    action.para,
                    getPara(configData, paras, action.para) + value
                )
                break
            case "SET":
                setPara(configData, paras, action.para, value)
                break
        }
    }
}

function sceneOptions (configData, scene, paras) {
    if (configData.scene_map[scene].require) {
        if (
            checkIs(
                configData,
                scene,
                paras,
                configData.scene_map[scene].require
            )
        ) {
            return configData.scene_map[scene].require.match_options
        }
    }
    return configData.scene_map[scene].options
}

function choiceFromOption (configData, scene, paras, options) {
    let res = []
    for (var i = 0; i < options.length; i++) {
        if (choiceShow(configData, scene, paras, options[i])) {
            res.push({
                id: options[i],
                text: choiceText(configData, options[i]),
            })
        }
    }
    return res
}

export {
    sceneText,
    chapterName,
    sceneOptions,
    changePara,
    getPara,
    checkIs,
    choiceFromOption,
}
