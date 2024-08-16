document.addEventListener("DOMContentLoaded", function() {
    toggleContent();

    const links = document.querySelectorAll(".sidebar ul li a");

    // 페이지 로드 시 저장된 상태를 확인하고 밑줄을 추가
    const activeLinkId = localStorage.getItem('activeLink');
    if (activeLinkId) {
        document.getElementById(activeLinkId).style.textDecoration = "underline";
    }

    links.forEach(function(link) {
        link.addEventListener("click", function() {
            // 모든 링크의 밑줄 제거
            links.forEach(function(link) {
                link.style.textDecoration = "none";
            });
            // 클릭한 링크에 밑줄 추가
            this.style.textDecoration = "underline";
            // 클릭한 링크의 ID를 localStorage에 저장
            localStorage.setItem('activeLink', this.id);
        });
    });
});

function toggleContent() {
    var womenContent = document.getElementById("women-content");
    var menContent = document.getElementById("men-content");

    if (womenContent) {
        document.getElementById("home").style.display = "none";
        womenContent.style.display = "flex";
    } else if (menContent) {
        document.getElementById("home").style.display = "none";
        menContent.style.display = "flex";
    }
}

window.onload = function() {
    toggleContent();
}