// Products Carousel functionality
(function() {
    function initCarousel() {
        let currentIndex = 0;
        const track = document.getElementById('carouselTrack');
        const items = document.querySelectorAll('.carousel-item');
        const dotsContainer = document.getElementById('carouselDots');
        let autoplayInterval;
        
        if (!track || !items.length || !dotsContainer) return;
        
        // Calcular items visíveis baseado na largura da tela
        function getVisibleItems() {
            if (window.innerWidth <= 768) return 1;
            if (window.innerWidth <= 1024) return 2;
            return 3;
        }

        function getTotalSlides() {
            return Math.max(1, items.length - getVisibleItems() + 1);
        }

        // Criar dots
        function createDots() {
            dotsContainer.innerHTML = '';
            const totalSlides = getTotalSlides();
            for (let i = 0; i < totalSlides; i++) {
                const dot = document.createElement('div');
                dot.className = i === 0 ? 'dot active' : 'dot';
                dot.onclick = () => goToSlide(i);
                dotsContainer.appendChild(dot);
            }
        }

        function updateCarousel() {
            if (items.length === 0) return;
            
            const itemWidth = items[0].offsetWidth + 20; // width + margin
            track.style.transform = `translateX(-${currentIndex * itemWidth}px)`;
            
            // Update dots
            const dots = document.querySelectorAll('.dot');
            dots.forEach((dot, index) => {
                dot.classList.toggle('active', index === currentIndex);
            });
        }

        window.moveCarousel = function(direction) {
            const totalSlides = getTotalSlides();
            currentIndex += direction;
            
            if (currentIndex < 0) {
                currentIndex = 0;
            } else if (currentIndex >= totalSlides) {
                currentIndex = totalSlides - 1;
            }
            
            updateCarousel();
        }

        function goToSlide(index) {
            currentIndex = index;
            updateCarousel();
        }

        function startAutoplay() {
            autoplayInterval = setInterval(() => {
                const totalSlides = getTotalSlides();
                if (currentIndex >= totalSlides - 1) {
                    currentIndex = 0;
                } else {
                    currentIndex++;
                }
                updateCarousel();
            }, 5000);
        }

        function stopAutoplay() {
            clearInterval(autoplayInterval);
        }

        // Auto-play
        startAutoplay();

        // Pausar autoplay ao passar o mouse
        const container = document.querySelector('.carousel-container');
        if (container) {
            container.addEventListener('mouseenter', stopAutoplay);
            container.addEventListener('mouseleave', startAutoplay);
        }

        // Recalcular ao redimensionar
        window.addEventListener('resize', () => {
            createDots();
            updateCarousel();
        });

        // Inicializar
        createDots();
        updateCarousel();
    }

    // Inicializar quando o DOM estiver pronto
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initCarousel);
    } else {
        // DOM já está pronto
        initCarousel();
    }
})();
