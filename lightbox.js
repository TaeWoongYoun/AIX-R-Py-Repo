// 이미지 클릭 확대 (라이트박스) — base.css의 .lightbox-* 스타일과 함께 동작
(function () {
    function init() {
        var overlay = document.createElement('div');
        overlay.className = 'lightbox-overlay';
        overlay.innerHTML = '<button class="lightbox-close" aria-label="닫기">&times;</button><img alt="">';
        document.body.appendChild(overlay);

        var big = overlay.querySelector('img');

        function open(src, alt) {
            big.src = src;
            big.alt = alt || '';
            overlay.classList.add('open');
            document.body.style.overflow = 'hidden';
        }
        function close() {
            overlay.classList.remove('open');
            document.body.style.overflow = '';
        }

        // .shot-item 안의 이미지(스크린샷·결과·데모)에 확대 기능 부여
        var imgs = document.querySelectorAll('.shot-item img');
        imgs.forEach(function (im) {
            im.addEventListener('click', function () {
                open(im.currentSrc || im.src, im.alt);
            });
        });

        overlay.addEventListener('click', close);
        document.addEventListener('keydown', function (e) {
            if (e.key === 'Escape') close();
        });
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
})();
