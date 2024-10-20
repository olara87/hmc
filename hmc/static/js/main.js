const mobileCta = document.getElementById('mobile-menu-open');
const mobileExit = document.getElementById('mobile-menu-close');
const nav = document.querySelector('nav');

// Open the mobile menu
mobileCta.addEventListener('click', () => {
    nav.classList.add('open');
});

// Close the mobile menu
mobileExit.addEventListener('click', () => {
    nav.classList.remove('open');
});