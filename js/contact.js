// Contact form: posts to the Apps Script web app (Practice Hub → Leads tab + email to Tim).
// Without JavaScript the form still posts normally and the script shows a simple thank-you page.
(function () {
    var form = document.getElementById('contact-form');
    if (!form) return;

    var thanks = document.getElementById('form-thanks');
    var status = document.getElementById('form-status');
    var button = form.querySelector('button[type="submit"]');
    var label = button.querySelector('span');
    var FALLBACK = 'Please email <a class="font-semibold underline" href="mailto:timgut@gmail.com?subject=Project%20inquiry">timgut@gmail.com</a> instead.';

    form.elements.started.value = String(Date.now());
    form.elements.page.value = document.referrer || window.location.href;

    function say(html, isError) {
        status.innerHTML = html;
        status.className = 'text-sm ' + (isError ? 'text-red-700' : 'text-gray-600');
    }

    form.addEventListener('submit', function (event) {
        event.preventDefault();
        if (!form.reportValidity()) return;

        var endpoint = form.getAttribute('action') || '';
        if (endpoint.indexOf('https://script.google.com/') !== 0) {
            say('The form isn&rsquo;t connected yet. ' + FALLBACK, true);
            return;
        }

        var data = new URLSearchParams(new FormData(form));
        data.set('js', '1');
        button.disabled = true;
        label.textContent = 'Sending…';
        say('', false);

        fetch(endpoint, { method: 'POST', body: data })
            .then(function (response) { return response.json(); })
            .then(function (result) {
                if (result && result.ok) {
                    form.classList.add('hidden');
                    thanks.classList.remove('hidden');
                    thanks.focus();
                } else {
                    say((result && result.error) || ('Something went wrong. ' + FALLBACK), true);
                }
            })
            .catch(function () {
                say('Your message didn&rsquo;t go through. ' + FALLBACK, true);
            })
            .then(function () {
                button.disabled = false;
                label.textContent = 'Send';
            });
    });
})();
