document.getElementById("musinsa").addEventListener("click", function() {
    document.getElementById("musinsa").style.textDecoration = "underline";
    document.getElementById("29cm").style.textDecoration = "none";
    document.getElementById("zigzag").style.textDecoration = "none";
});

document.getElementById("29cm").addEventListener("click", function() {
    document.getElementById("musinsa").style.textDecoration = "none";
    document.getElementById("29cm").style.textDecoration = "underline";
    document.getElementById("zigzag").style.textDecoration = "none";
});

document.getElementById("zigzag").addEventListener("click", function() {
    document.getElementById("musinsa").style.textDecoration = "none";
    document.getElementById("29cm").style.textDecoration = "none";
    document.getElementById("zigzag").style.textDecoration = "underline";
});