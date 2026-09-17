// Site interactions: mobile menu + scroll-in animations
document.addEventListener('DOMContentLoaded', function () {
    var btn = document.getElementById('mobile-menu-button');
    var menu = document.getElementById('mobile-menu');

    if (btn && menu) {
        btn.addEventListener('click', function () {
            menu.classList.toggle('hidden');
        });
        document.addEventListener('click', function (event) {
            if (!btn.contains(event.target) && !menu.contains(event.target)) {
                menu.classList.add('hidden');
            }
        });
        window.addEventListener('resize', function () {
            if (window.innerWidth >= 768) {
                menu.classList.add('hidden');
            }
        });
    }

    // Fade sections in as they scroll into view (skip when reduced motion is set)
    if (!window.matchMedia('(prefers-reduced-motion: reduce)').matches && 'IntersectionObserver' in window) {
        var observer = new IntersectionObserver(function (entries) {
            entries.forEach(function (entry) {
                if (entry.isIntersecting) {
                    entry.target.classList.add('animate-fade-in');
                    observer.unobserve(entry.target);
                }
            });
        }, { threshold: 0.1 });
        document.querySelectorAll('main section').forEach(function (el) {
            observer.observe(el);
        });
    }
});
