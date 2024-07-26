document.getElementById("home-display").addEventListener("click", function() {
    document.getElementById("home").style.display = "flex";
    document.getElementById("women-content").style.display = "none";
    document.getElementById("men-content").style.display = "none";
    document.getElementById("women-link").style.textDecoration = "none";
    document.getElementById("men-link").style.textDecoration = "none";
});

document.getElementById("women-link").addEventListener("click", function() {
    document.getElementById("home").style.display = "none";
    document.getElementById("women-content").style.display = "flex";
    document.getElementById("women-link").style.textDecoration = "underline";
    document.getElementById("men-content").style.display = "none";
    document.getElementById("men-link").style.textDecoration = "none";
});

document.getElementById("men-link").addEventListener("click", function() {
    document.getElementById("home").style.display = "none";
    document.getElementById("women-content").style.display = "none";
    document.getElementById("women-link").style.textDecoration = "none";
    document.getElementById("men-content").style.display = "flex";
    document.getElementById("men-link").style.textDecoration = "underline";
});

// document.getElementsByClassName("login-button").addEventListener("click", function() {
//     document.getElementById("home").style.display = "none";
//     document.getElementById("women-content").style.display = "none";
//     document.getElementById("women-link").style.textDecoration = "none";
//     document.getElementById("men-content").style.display = "flex";
//     document.getElementById("men-link").style.textDecoration = "underline";
// });