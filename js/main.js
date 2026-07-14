// Mobile menu functionality
document.addEventListener('DOMContentLoaded', function() {
    const mobileMenuButton = document.getElementById('mobile-menu-button');
    const mobileMenu = document.getElementById('mobile-menu');
    const header = document.getElementById('main-header');
    const profile = document.querySelector('.shrink-profile');
    const name = document.querySelector('.shrink-name');
    const title = document.querySelector('.shrink-title');
    const links = document.querySelector('.shrink-links');
    const headerProfile = document.getElementById('header-profile');

    mobileMenuButton.addEventListener('click', function() {
        mobileMenu.classList.toggle('hidden');
    });

    // Close mobile menu when clicking outside
    document.addEventListener('click', function(event) {
        if (!mobileMenuButton.contains(event.target) && !mobileMenu.contains(event.target)) {
            mobileMenu.classList.add('hidden');
        }
    });

    // Close mobile menu when window is resized to desktop size
    window.addEventListener('resize', function() {
        if (window.innerWidth >= 768) { // 768px is the md breakpoint in Tailwind
            mobileMenu.classList.add('hidden');
        }
    });

    // Shrinking header on scroll
    window.addEventListener('scroll', function() {
        if (window.scrollY > 40) {
            header.classList.add('minimized');
            if (profile) profile.classList.add('minimized-profile');
            if (name) name.classList.add('minimized-name');
            if (title) title.classList.add('minimized-title');
            if (links) links.classList.add('minimized-links');
            if (headerProfile) headerProfile.classList.add('minimized-header-profile');
        } else {
            header.classList.remove('minimized');
            if (profile) profile.classList.remove('minimized-profile');
            if (name) name.classList.remove('minimized-name');
            if (title) title.classList.remove('minimized-title');
            if (links) links.classList.remove('minimized-links');
            if (headerProfile) headerProfile.classList.remove('minimized-header-profile');
        }
    });

    // Intersection Observer for scroll animations
    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.1
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate-fade-in');
                observer.unobserve(entry.target); // Stop observing once animated
            }
        });
    }, observerOptions);

    // Animate portfolio cards on scroll-in
    document.querySelectorAll('.portfolio-card').forEach((card) => {
        observer.observe(card);
    });

    // Add typing effect to the introduction
    const introText = document.querySelector('.text-xl.text-gray-600.mb-6');
    if (introText) {
        const text = introText.textContent;
        introText.textContent = '';
        let i = 0;
        
        function typeWriter() {
            if (i < text.length) {
                introText.textContent += text.charAt(i);
                i++;
                setTimeout(typeWriter, 50);
            }
        }
        
        // Start typing effect after a short delay
        setTimeout(typeWriter, 1000);
    }
});

// Intersection Observer callback for cards
const cardObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.remove('opacity-0', 'translate-y-8');
            entry.target.classList.add('opacity-100', 'translate-y-0', 'transition-all', 'duration-700');
            cardObserver.unobserve(entry.target);
        }
    });
}, { threshold: 0.15 });
document.querySelectorAll('.portfolio-card').forEach(card => {
    cardObserver.observe(card);
});

// Modal logic
function openModal(imgSrc) {
    const modal = document.getElementById('project-modal');
    const modalImg = document.getElementById('modal-img');
    const modalContent = document.getElementById('modal-content');
    const modalHeadline = document.getElementById('modal-headline');
    // Show correct modal content for each project
    if (imgSrc.includes('amps-modal.png') || imgSrc.includes('amps-thumb.png')) {
        modalImg.src = 'img/portfolio/amps-modal.png';
        modalHeadline.textContent = 'AMPS Content Management System';
        modalContent.innerHTML = `
            <h3 id="modal-headline" class="text-2xl md:text-3xl font-bold text-tg-blue text-center mt-6 mb-8 tracking-tight">AMPS Content Management System</h3>
            <div class="grid md:grid-cols-2 gap-8 p-8">
                <div>
                    <h4 class="text-xl font-bold mb-2 flex items-center">
                      <span class="inline-block w-1.5 h-6 bg-tg-yellow mr-3 rounded"></span>
                      <i class="fas fa-info-circle text-tg-blue mr-2"></i>
                      <span class="tracking-widest uppercase text-tg-blue">Overview</span>
                    </h4>
                    <p class="text-gray-700 mb-4">The AMPS content management system (the acronym was a reference to the former name of the company) is an enterprise-scale CMS on par with WordPress or Drupal, but customized for internal design staff and clients for rapid site creation and deployment. Built in Ruby on Rails and utilizing mutliple front-end displays (a React-based UI was added to the original in 2020), it has been used to build and host more than 800 websites in more than a decade of service. Permission levels allow novice clients to do basic posting or tech-savvy ones to write their own page templates. The entire architecture is maintained at Amazon Web Sevices, and is easily configurable with Cloudfront and S3.</p>
                </div>
                <div>
                    <h4 class="text-xl font-bold mb-2 flex items-center">
                      <span class="inline-block w-1.5 h-6 bg-tg-yellow mr-3 rounded"></span>
                      <i class="fas fa-tools text-tg-blue mr-2"></i>
                      <span class="tracking-widest uppercase text-tg-blue">Tech Stack</span>
                    </h4>
                    <ul class="list-disc list-inside text-gray-700 text-base mb-4 pl-4">
                        <li>Ruby on Rails</li>
                        <li>MySQL</li>
                        <li>React</li>
                        <li>SASS</li>
                        <li>Webpacker</li>
                        <li>RubyGems</li>
                        <li>Amazon Web Services
                          <ul class="list-disc list-inside text-gray-700 text-sm ml-6 mt-1">
                            <li>Cloudfront</li>
                            <li>RDS</li>
                            <li>Elastic Load Balancer</li>
                            <li>EC2</li>
                          </ul>
                        </li>
                        <li>Let's Encrypt</li>
                    </ul>
                </div>
            </div>
        `;
    } else if (imgSrc.includes('asana-modal.png') || imgSrc.includes('asana-thumb.png')) {
        modalImg.src = 'img/portfolio/asana-modal.png';
        modalHeadline.textContent = 'Asana API';
        modalContent.innerHTML = `
            <h3 id="modal-headline" class="text-2xl md:text-3xl font-bold text-tg-blue text-center mt-6 mb-8 tracking-tight">Asana API</h3>
            <div class="grid md:grid-cols-2 gap-8 p-8">
                <div>
                    <h4 class="text-xl font-bold mb-2 flex items-center">
                      <span class="inline-block w-1.5 h-6 bg-tg-yellow mr-3 rounded"></span>
                      <i class="fas fa-info-circle text-tg-blue mr-2"></i>
                      <span class="tracking-widest uppercase text-tg-blue">Overview</span>
                    </h4>
                    <p class="text-gray-700 mb-4">Multiple internal teams rely heavily on Asana for project management. The problem is that each team has specific needs in term of project requests, inputs, and timing, whether that was a design request for an ad, a writing request for a proposal, or trafficking details for a paid media plan. The solution was to build an internal app which collected required information for each job type, assigned responsibility, tracked time spent to Harvest (a timetracker tool) and utilized Asana's API to create the ticket on an Asana job board, driving efficiency and streamlining workflows.</p>
                </div>
                <div>
                    <h4 class="text-xl font-bold mb-2 flex items-center">
                      <span class="inline-block w-1.5 h-6 bg-tg-yellow mr-3 rounded"></span>
                      <i class="fas fa-tools text-tg-blue mr-2"></i>
                      <span class="tracking-widest uppercase text-tg-blue">Tech Stack</span>
                    </h4>
                    <ul class="list-disc list-inside text-gray-700 text-base mb-4 pl-4">
                        <li>Rails</li>
                        <li>React</li>
                        <li>Webpacker</li>
                        <li>REST APIs</li>
                        <li>AWS</li>
                    </ul>
                </div>
            </div>
        `;
    } else {
        modalImg.src = imgSrc;
        modalHeadline.textContent = '';
        modalContent.innerHTML = '';
    }
    modal.classList.remove('hidden');
}

document.querySelectorAll('.see-more-btn').forEach(btn => {
    btn.addEventListener('click', function(e) {
        e.preventDefault();
        openModal(btn.getAttribute('data-modal-img'));
    });
});
document.querySelectorAll('.portfolio-card img[data-modal-img]').forEach(img => {
    img.addEventListener('click', function(e) {
        openModal(img.getAttribute('data-modal-img'));
    });
});
/*function closeModal() {
    const modal = document.getElementById('project-modal');
    modal.classList.add('hidden');
}
document.getElementById('close-modal').addEventListener('click', closeModal);
document.getElementById('project-modal').addEventListener('click', function(e) {
    if (e.target === this) {
        closeModal();
    }
}); */
