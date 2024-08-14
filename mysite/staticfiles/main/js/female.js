document.getElementById("home-display").addEventListener("click", function() {
    document.getElementById("home").style.display = "flex";
    document.getElementById("women-content").style.display = "none";
    document.getElementById("women-link").style.textDecoration = "none";
});

document.getElementById("women-link").addEventListener("click", function() {
    document.getElementById("home").style.display = "none";
    document.getElementById("women-content").style.display = "flex";
    document.getElementById("women-link").style.textDecoration = "underline";
});

document.getElementsByClassName("brand-logo").addEventListener("click", function() {
    location.replace("main");
});