// Image slider data with descriptions
const sliderData = [
    {
        src: "images/fig1_timeseries_real.png",
        description: "이중 축 시계열 그래프 - ChatGPT 출시 이후 Stack Overflow 질문 수는 급감하고 GitHub AI 레포지토리는 급증하는 명확한 역전 현상"
    },
    {
        src: "images/fig2_before_after_real.png",
        description: "Before vs After 비교 - Stack Overflow는 51% 감소, GitHub AI는 141% 증가하여 개발자 행동 패턴의 극적인 변화를 보여줌"
    },
    {
        src: "images/fig3_yoy_real.png",
        description: "전년대비 변화율 - 2022년 11월 ChatGPT 출시 이후 Stack Overflow는 지속적으로 음수 성장률을 기록"
    },
    {
        src: "images/fig4_correlation_real.png",
        description: "상관관계 산점도 - Pearson 상관계수 r = -0.933으로 매우 강한 음의 상관관계 확인, ChatGPT 이후 패턴 변화가 뚜렷함"
    },
    {
        src: "images/fig5_normalized_trends.png",
        description: "정규화 추세 비교 - 두 플랫폼의 반대 방향 추세를 명확하게 시각화, AI 도구가 개발자 생태계에 미친 근본적 영향을 증명"
    }
];

// Slider state
let currentSlide = 0;
const totalSlides = sliderData.length;

// Initialize slider
function initSlider() {
    const sliderImages = document.getElementById('sliderImages');
    const sliderIndicators = document.getElementById('sliderIndicators');

    // Create slider items
    sliderData.forEach((data, index) => {
        // Create image container
        const item = document.createElement('div');
        item.className = 'slider-item';
        if (index === 0) item.classList.add('active');

        const img = document.createElement('img');
        img.src = data.src;
        img.alt = `Analysis Result ${index + 1}`;

        item.appendChild(img);
        sliderImages.appendChild(item);

        // Create indicator
        const indicator = document.createElement('div');
        indicator.className = 'indicator';
        if (index === 0) indicator.classList.add('active');
        indicator.addEventListener('click', () => goToSlide(index));
        sliderIndicators.appendChild(indicator);
    });

    updateDescription();
}

// Update description
function updateDescription() {
    const descElement = document.getElementById('sliderDesc');
    descElement.textContent = sliderData[currentSlide].description;
}

// Go to specific slide
function goToSlide(index) {
    // Remove active class from all items
    const items = document.querySelectorAll('.slider-item');
    const indicators = document.querySelectorAll('.indicator');

    items.forEach(item => item.classList.remove('active'));
    indicators.forEach(indicator => indicator.classList.remove('active'));

    // Set new active slide
    currentSlide = index;
    items[currentSlide].classList.add('active');
    indicators[currentSlide].classList.add('active');

    updateDescription();
}

// Navigate slider
function navigateSlider(direction) {
    if (direction === 'next') {
        currentSlide = (currentSlide + 1) % totalSlides;
    } else {
        currentSlide = (currentSlide - 1 + totalSlides) % totalSlides;
    }

    goToSlide(currentSlide);
}

// Event listeners
document.addEventListener('DOMContentLoaded', () => {
    initSlider();

    document.getElementById('nextBtn').addEventListener('click', () => {
        navigateSlider('next');
    });

    document.getElementById('prevBtn').addEventListener('click', () => {
        navigateSlider('prev');
    });

    // Keyboard navigation
    document.addEventListener('keydown', (e) => {
        if (e.key === 'ArrowRight') {
            navigateSlider('next');
        } else if (e.key === 'ArrowLeft') {
            navigateSlider('prev');
        }
    });

    // Auto-advance slider
    let autoAdvanceInterval = setInterval(() => {
        navigateSlider('next');
    }, 5000);

    // Pause auto-advance on hover
    const sliderContainer = document.querySelector('.slider-container');
    if (sliderContainer) {
        sliderContainer.addEventListener('mouseenter', () => {
            clearInterval(autoAdvanceInterval);
        });

        sliderContainer.addEventListener('mouseleave', () => {
            autoAdvanceInterval = setInterval(() => {
                navigateSlider('next');
            }, 5000);
        });
    }
});

// Smooth scroll for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// Add scroll animation for sections
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
        }
    });
}, observerOptions);

// Observe all sections for fade-in animation
document.addEventListener('DOMContentLoaded', () => {
    const sections = document.querySelectorAll('section');
    sections.forEach(section => {
        section.style.opacity = '0';
        section.style.transform = 'translateY(30px)';
        section.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        observer.observe(section);
    });
});
