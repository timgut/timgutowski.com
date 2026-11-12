// Google Analytics 4 event tracking for timgutowski.com.
// Page views, scrolls, outbound links, and file downloads come from GA4's enhanced measurement.
// This file adds a few events GA4 doesn't collect on its own. No form contents or other personal data are sent.
(function () {
    function track(name, params) {
        if (typeof window.gtag === 'function') window.gtag('event', name, params || {});
    }
    window.tgTrack = track;

    // Where on the page a click happened: header, footer, or the nearest section with an id or heading.
    function where(el) {
        if (el.closest('header')) return 'header';
        if (el.closest('footer')) return 'footer';
        var section = el.closest('section');
        if (!section) return 'page';
        if (section.id) return section.id;
        var h = section.querySelector('h1, h2');
        return h ? h.textContent.trim().slice(0, 60) : 'section';
    }

    document.addEventListener('click', function (event) {
        var a = event.target.closest && event.target.closest('a[href]');
        if (!a) return;
        var href = a.getAttribute('href');
        var text = (a.textContent || '').replace(/\s+/g, ' ').trim().slice(0, 60);
        var info = { link_text: text, link_location: where(a), page_path: location.pathname };

        if (/(^|\/)contact\.html(#.*)?$/.test(href)) {
            track('start_project_click', info);
        } else if (href.indexOf('mailto:') === 0) {
            track('email_click', info);
        } else if (href.indexOf('linkedin.com') !== -1) {
            track('linkedin_click', info);
        } else if (/(^|\/)resume\.html$/.test(href)) {
            track('resume_click', info);
        }
    });
})();
