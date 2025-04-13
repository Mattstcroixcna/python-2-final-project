document.addEventListener("DOMContentLoaded", () => {
	document.querySelector("#add").addEventListener("click", addGame);
});

function addGame() {
    let name = prompt("Name:");
    let year = prompt("Release Date:");
    let rating = prompt("Rating (1-10)");
}