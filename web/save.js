function setCookie (cname, cvalue) {
    document.cookie = cname + "=" + cvalue + ";"
}

function getCookie (cname) {
    var name = cname + "="
    var ca = document.cookie.split(";")
    for (var i = 0; i < ca.length; i++) {
        var c = ca[i].trim()
        if (c.indexOf(name) == 0) return c.substring(name.length, c.length)
    }
    return ""
}

function markEnd (end_id) {
    setCookie(end_id, "true")
}

function checkEnd (end_id) {
    return getCookie(end_id) === "true"
}

function saveAt (saveData, index) {
    setCookie("save" + index, JSON.stringify(saveData))
}

function loadAt (index) {
    let saveData = getCookie("save" + index)
    if (saveData === "") {
        return null
    }
    return JSON.parse(saveData)
}

export { markEnd, checkEnd, saveAt, loadAt }
