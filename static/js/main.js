// Smooth scrolling for navigation links
if (document.querySelectorAll('a[href^="#"]').length) {
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
            // Fecha o menu mobile ao clicar em um link
            const mobileMenu = document.getElementById('mobile-menu');
            if(mobileMenu && !mobileMenu.classList.contains('max-h-0')){
                mobileMenu.classList.add('max-h-0');
                mobileMenu.classList.remove('menu-open');
            }
        });
    });
}

// Header background on scroll
window.addEventListener('scroll', function() {
    const header = document.querySelector('header');
    if (window.scrollY > 100) {
        header.classList.add('bg-primary');
    } else {
        header.classList.remove('bg-primary');
    }
});

// Navbar mobile responsiva no estilo WATech
const menuToggle = document.getElementById('menu-toggle');
const mobileMenu = document.getElementById('mobile-menu');

if (menuToggle && mobileMenu) {
    menuToggle.addEventListener('click', function() {
        if (mobileMenu.classList.contains('max-h-0')) {
            mobileMenu.classList.remove('max-h-0');
            mobileMenu.classList.add('menu-open');
        } else {
            mobileMenu.classList.add('max-h-0');
            mobileMenu.classList.remove('menu-open');
        }
    });
}

// Floating particles (decorativo)
function createParticles() {
    const container = document.getElementById('particles-container');
    if (container) {
        for (let i = 0; i < 18; i++) {
            const p = document.createElement('div');
            p.className = 'particle';
            p.style.width = p.style.height = `${Math.random() * 16 + 8}px`;
            p.style.left = `${Math.random() * 100}%`;
            p.style.top = `${Math.random() * 100}%`;
            p.style.opacity = Math.random() * 0.4 + 0.2;
            p.style.animation = `float ${Math.random() * 4 + 4}s ease-in-out infinite alternate`;
            container.appendChild(p);
        }
    }
}
createParticles();

// Mobile player
const audioMobile = document.getElementById('audioPlayerMobile');
const btnMobile = document.getElementById('playPauseBtnMobile');
const iconMobile = document.getElementById('playPauseIconMobile');
if(btnMobile && audioMobile && iconMobile) {
    btnMobile.addEventListener('click', () => {
        if (audioMobile.paused) {
            audioMobile.play();
        } else {
            audioMobile.pause();
        }
    });
    audioMobile.addEventListener('play', () => {
        iconMobile.classList.remove('fa-play');
        iconMobile.classList.add('fa-pause');
    });
    audioMobile.addEventListener('pause', () => {
        iconMobile.classList.remove('fa-pause');
        iconMobile.classList.add('fa-play');
    });
    audioMobile.addEventListener('ended', () => {
        iconMobile.classList.remove('fa-pause');
        iconMobile.classList.add('fa-play');
    });
}

// Desktop player
const audioDesktop = document.getElementById('audioPlayerDesktop');
const btnDesktop = document.getElementById('playPauseBtnDesktop');
const iconDesktop = document.getElementById('playPauseIconDesktop');
if(btnDesktop && audioDesktop && iconDesktop) {
    btnDesktop.addEventListener('click', () => {
        if (audioDesktop.paused) {
            audioDesktop.play();
        } else {
            audioDesktop.pause();
        }
    });
    audioDesktop.addEventListener('play', () => {
        iconDesktop.classList.remove('fa-play');
        iconDesktop.classList.add('fa-pause');
    });
    audioDesktop.addEventListener('pause', () => {
        iconDesktop.classList.remove('fa-pause');
        iconDesktop.classList.add('fa-play');
    });
    audioDesktop.addEventListener('ended', () => {
        iconDesktop.classList.remove('fa-pause');
        iconDesktop.classList.add('fa-play');
    });
}

// Rolagem suave para âncoras
if ('scrollBehavior' in document.documentElement.style) {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                e.preventDefault();
                target.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        });
    });
}

// Horóscopo API alternativa
const btnHoroscopo = document.getElementById('buscar-horoscopo');
if (btnHoroscopo) {
    const signoMap = {
        aries: 'aries',
        taurus: 'taurus',
        gemini: 'gemini',
        cancer: 'cancer',
        leo: 'leo',
        virgo: 'virgo',
        libra: 'libra',
        scorpio: 'scorpio',
        sagittarius: 'sagittarius',
        capricorn: 'capricorn',
        aquarius: 'aquarius',
        pisces: 'pisces'
    };
    btnHoroscopo.addEventListener('click', async function() {
        const signo = document.getElementById('signo-select').value;
        const resultado = document.getElementById('resultado-horoscopo');
        if (!signo) {
            resultado.textContent = 'Por favor, selecione um signo.';
            return;
        }
        resultado.textContent = 'Buscando horóscopo...';
        try {
            const response = await fetch(`/api/horoscopo?signo=${signo}`);
            if (!response.ok) throw new Error('Erro ao buscar horóscopo.');
            const data = await response.json();
            if (data.horoscopo) {
                resultado.innerHTML = `<div><span class='text-mystic-gold font-bold'>${signo.charAt(0).toUpperCase() + signo.slice(1)}</span><br><span class='block mt-2'>${data.horoscopo}</span></div>`;
            } else {
                resultado.textContent = 'Horóscopo não encontrado.';
            }
        } catch (e) {
            resultado.textContent = 'Não foi possível obter o horóscopo. Tente novamente mais tarde.';
        }
    });
} 