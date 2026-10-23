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

    var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    // Fade sections in as they scroll into view (skip when reduced motion is set).
    // Sections already on screen when the page loads are left alone (animating them
    // made the page flash: visible, then hidden, then fading back in). Sections below
    // the fold are hidden right away and fade in when they're scrolled to.
    // Sections marked data-reveal="gsap" are animated by GSAP below instead.
    if (!reduceMotion && 'IntersectionObserver' in window) {
        var firstPass = true;
        var observer = new IntersectionObserver(function (entries) {
            entries.forEach(function (entry) {
                var el = entry.target;
                if (firstPass) {
                    if (entry.isIntersecting) {
                        observer.unobserve(el);
                    } else {
                        el.classList.add('pre-reveal');
                    }
                } else if (entry.isIntersecting) {
                    el.classList.remove('pre-reveal');
                    el.classList.add('animate-fade-in');
                    observer.unobserve(el);
                }
            });
            firstPass = false;
        }, { threshold: 0.1 });
        document.querySelectorAll('main section:not([data-reveal])').forEach(function (el) {
            observer.observe(el);
        });
    }

    // Work page cards ("More of what I build"): each row of cards slides up and fades in
    // as it scrolls into view. Cards start hidden only once GSAP has loaded.
    if (!reduceMotion && window.gsap && window.ScrollTrigger) {
        gsap.registerPlugin(ScrollTrigger);
        var cards = document.querySelectorAll('[data-reveal="gsap"] .reveal-cards > *');
        if (cards.length) {
            gsap.set(cards, { opacity: 0, y: 24 });
            ScrollTrigger.batch(cards, {
                start: 'top 88%',
                once: true,
                onEnter: function (batch) {
                    gsap.to(batch, { opacity: 1, y: 0, duration: 0.6, ease: 'power2.out', stagger: 0.1 });
                }
            });
        }
    }

    // Client list (Work page): each group's heading and names slide up and fade in
    // as the group scrolls into view. Content stays visible if GSAP doesn't load.
    if (!reduceMotion && window.gsap && window.ScrollTrigger) {
        gsap.registerPlugin(ScrollTrigger);
        document.querySelectorAll('[data-reveal="gsap"] .client-group').forEach(function (group) {
            gsap.from(group.querySelectorAll('h3, li'), {
                opacity: 0,
                y: 18,
                duration: 0.55,
                ease: 'power2.out',
                stagger: 0.03,
                scrollTrigger: { trigger: group, start: 'top 85%', once: true }
            });
        });
    }
});
