const $ = selector => document.querySelector(selector);

document.addEventListener("DOMContentLoaded", () => {
    const form = $("#game_info");

    form.addEventListener("submit", function (e) {
        if (!validateForm()) {
            e.preventDefault();
        }
    });
});

function validateForm() {
    let name = $("#name").value.trim();
    let year = $("#year").value.trim();
    let rate = $("#rate").value.trim();

    if (name === "") {
        alert("Name must be filled out");
        return false;
    }

    if (year === "") {
        alert("Release Year must be filled out");
        return false;
    }

    if (rate === "") {
        alert("Rating must be filled out");
        return false;
    }

    return true;
}
