let storyEl = document.getElementById("story");
let inputEl = document.getElementById("playerInput");

function handleInput () {
    const choice = inputEl.value.trim().toLowerCase();
    inputEl.value = "";

    if (choice === "进入") {
        storyEl.textContent = "你迈入森林，四周变得昏暗。远处传来狼嚎...";
    } else if (choice === "离开") {
        storyEl.textContent = "你转身离开，但心中有些许遗憾。也许，这是个错误的决定。";
    } else {
        storyEl.textContent = `你说了“${choice}”，但风似乎没有回应。试试别的？`;
    }
}