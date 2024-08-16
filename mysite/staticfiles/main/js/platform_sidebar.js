document.addEventListener("DOMContentLoaded", function() {
    toggleContent();
    document.getElementById("musinsa").addEventListener("click", function() {
        document.getElementById("musinsa").style.textDecoration = "underline";
        document.getElementById("29cm").style.textDecoration = "none";
        document.getElementById("zigzag").style.textDecoration = "none";
    });
});
document.addEventListener("DOMContentLoaded", function() {
    toggleContent();
    document.getElementById("29cm").addEventListener("click", function() {
        document.getElementById("musinsa").style.textDecoration = "none";
        document.getElementById("29cm").style.textDecoration = "underline";
        document.getElementById("zigzag").style.textDecoration = "none";
    });
});
document.addEventListener("DOMContentLoaded", function() {
    toggleContent();
    document.getElementById("zigzag").addEventListener("click", function() {
        document.getElementById("musinsa").style.textDecoration = "none";
        document.getElementById("29cm").style.textDecoration = "none";
        document.getElementById("zigzag").style.textDecoration = "underline";
    });
});

function toggleContent() {
    var womenContent = document.getElementById("women-content");
    var menContent = document.getElementById("men-content");

    if (womenContent) {  // women-content가 존재할 경우
        document.getElementById("home").style.display = "none";
        womenContent.style.display = "flex";
    } else if (menContent) {  // men-content가 존재할 경우
        document.getElementById("home").style.display = "none";
        menContent.style.display = "flex";
    }
}

// 페이지 로드 시 toggleContent 함수 실행
window.onload = function() {
    toggleContent();
}