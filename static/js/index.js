
const active = document.querySelector("aside").getAttribute("data-active")
document.querySelector(`.${active}`).classList.add("active")
