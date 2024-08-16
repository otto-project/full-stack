const slide = document.querySelector('.slider-wrapper');
let slideWidth = slide.clientWidth;

const prevButton = document.querySelector('.prev-slide');
const nextButton = document.querySelector('.next-slide');
// 현재 슬라이드 위치가 슬라이드 개수를 넘기지 않게 하기 위한 변수
const slides = document.querySelectorAll('.slide');
const maxSlide = slides.length;

let currSlide = 1;
const slideInterval = 5000; // 슬라이드 간격 시간 (밀리초 단위)

// 페이지네이션 생성
const pagination = document.querySelector(".slide_pagination");

for (let i = 0; i < maxSlide; i++) {
    if (i === 0) pagination.innerHTML += `<li class="active">•</li>`;
    else pagination.innerHTML += `<li>•</li>`;
}

const paginationItems = document.querySelectorAll(".slide_pagination > li");

// 첫 번째 슬라이드와 마지막 슬라이드를 복사하여 무한 루프 구현
const firstClone = slides[0].cloneNode(true);
const lastClone = slides[slides.length - 1].cloneNode(true);

slide.appendChild(firstClone); // 첫 번째 슬라이드 복사본을 마지막에 추가
slide.insertBefore(lastClone, slides[0]); // 마지막 슬라이드 복사본을 첫 번째로 추가

const slideItems = document.querySelectorAll('.slide'); // 복제된 슬라이드 포함

let offset = -currSlide * 100;
slide.style.transform = `translateX(${offset}%)`;

nextButton.addEventListener('click', () => {
    moveToNextSlide();
    resetAutoSlide(); // 버튼 클릭 시 자동 슬라이드 리셋
});

prevButton.addEventListener('click', () => {
    moveToPreviousSlide();
    resetAutoSlide(); // 버튼 클릭 시 자동 슬라이드 리셋
});

// 각 페이지네이션 클릭 시 해당 슬라이드로 이동하기
for (let i = 0; i < maxSlide; i++) {
    paginationItems[i].addEventListener("click", () => {
        // 클릭한 페이지네이션에 따라 현재 슬라이드 변경해주기(currSlide는 시작 위치가 1이기 때문에 + 1)
        currSlide = i + 1;
        const offset = -currSlide * 100;
        slide.style.transform = `translateX(${offset}%)`;
        updatePagenation();
    });
}

// 브라우저 화면이 조정될 때 마다 slideWidth를 변경하기 위해
window.addEventListener("resize", () => {
    slideWidth = slide.clientWidth;
});

function moveToNextSlide() {
    currSlide += 1;
    if (currSlide <= maxSlide) {
        currSlide = currSlide % slideItems.length;
        const offset = -currSlide * 100;
        slide.style.transform = `translateX(${offset}%)`;
    }
    else {
        currSlide = 0;
        let offset = -currSlide * 100;
        slide.style.transition = 'transform 0s';
        slide.style.transform = `translateX(${offset}%)`;
        currSlide += 1;
        offset = -currSlide * 100;
        setTimeout(() => {
            slide.style.transition = 'transform 0.5s ease';
            slide.style.transform = `translateX(${offset}%)`;
        }, 0);
    }   
    updatePagenation();
}

function moveToPreviousSlide() {
    currSlide -= 1;
    if (currSlide > 0) {
        currSlide = (currSlide + slideItems.length) % slideItems.length;
        const offset = -currSlide * 100;
        slide.style.transform = `translateX(${offset}%)`;
    }
    else {
        currSlide = maxSlide + 1;
        let offset = -currSlide * 100;
        slide.style.transition = 'transform 0s';
        slide.style.transform = `translateX(${offset}%)`;
        currSlide -= 1;
        offset = -currSlide * 100;
        setTimeout(() => {
            slide.style.transition = 'transform 0.5s ease';
            slide.style.transform = `translateX(${offset}%)`;
        }, 0);
    }   
    updatePagenation();
}

function updatePagenation() {
    // 슬라이드 이동 시 현재 활성화된 pagination 변경
    paginationItems.forEach((i) => i.classList.remove("active"));
    paginationItems[currSlide - 1].classList.add("active");
}

function startAutoSlide() {
    return setInterval(moveToNextSlide, slideInterval);
}   

function resetAutoSlide() {
    clearInterval(autoSlide); // 기존의 자동 슬라이드를 멈추고
    autoSlide = startAutoSlide(); // 새로운 자동 슬라이드를 시작
}

let autoSlide = startAutoSlide(); // 페이지 로드 시 자동 슬라이드 시작
