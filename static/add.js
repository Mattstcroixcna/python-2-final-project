const $ = selector => document.querySelector(selector);

document.addEventListener("DOMContentLoaded", () => {  
    $("#submit").addEventListener("click", validateForm);
    
})

function submit() {
    validateForm();

}

function validateForm() {
    let x = document.forms["form"]["name"].value;
    if (x == "") {
        alert("Name must be filled out");
        return false;
    }
    let y = document.forms["form"]["year"].value;
    if (y == "") {
        alert("Release Year must be filled out");
        return false;
    }
    let z = document.forms["form"]["rate"].value;
    if (z == "") {
        alert("Rating must be filled out");
        return false; 
    }
}