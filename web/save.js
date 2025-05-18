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

function mark_end (end_id) {
    setCookie(end_id, "true")
}

function check_end (end_id) {
    return getCookie(end_id) === "true"
}

export { mark_end, check_end }
