// Configuração do Tailwind
tailwind.config = {
  theme: {
    extend: {
      animation: {
        'gradient-x': 'gradient-x 6s ease-in-out infinite',
      },
      keyframes: {
        'gradient-x': {
          '0%, 100%': { 'background-position': '0% 50%' },
          '50%': { 'background-position': '100% 50%' },
        },
      },
    }
  }
};

// Fade-in suave nas seções ao rolar
function initFadeSections() {
  const fadeSections = document.querySelectorAll('.fade-section');
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.remove('opacity-0', 'translate-y-8');
      }
    });
  }, { threshold: 0.15 });
  
  fadeSections.forEach(section => observer.observe(section));
}

// Menu mobile
function initMobileMenu() {
  const menuToggle = document.getElementById('menu-toggle');
  const mobileMenu = document.getElementById('mobile-menu');
  const menuClose = document.getElementById('menu-close');
  
  if (menuToggle && mobileMenu) {
    menuToggle.addEventListener('click', function() {
      mobileMenu.classList.toggle('hidden');
    });
    
    if (menuClose) {
      menuClose.addEventListener('click', function() {
        mobileMenu.classList.add('hidden');
      });
    }
  }
}

// Formulário de horóscopo
function initHoroscopeForm() {
  const form = document.getElementById('horoscopoForm');
  if (!form) return;

  form.addEventListener('submit', async function(e) {
    e.preventDefault();
    const signo = document.getElementById('signo').value;
    const resultado = document.getElementById('resultado-horoscopo');
    resultado.innerHTML = '';
    
    if (!signo) {
      resultado.innerHTML = `
        <div class="text-center">
          <div class="text-4xl mb-4">🔮</div>
          <p class="text-gray-300 text-lg">Selecione um signo para ver a previsão.</p>
        </div>
      `;
      return;
    }
    
    resultado.innerHTML = `
      <div class="text-center">
        <div class="text-4xl mb-4 floating">✨</div>
        <p class="text-gray-300 text-lg">Consultando horóscopo...</p>
      </div>
    `;
    
    try {
      const resp = await fetch('/horoscopo', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({signo})
      });
      const data = await resp.json();
      
      if (data.horoscopo_diario) {
        resultado.innerHTML = `
          <div class="crystal-bg rounded-xl p-6 text-center">
            <div class="text-4xl mb-4">🔮</div>
            <h3 class="text-xl font-bold mystic-text mb-4">Horóscopo Diário para ${signo.charAt(0).toUpperCase() + signo.slice(1)}:</h3>
            <p class="text-gray-200 leading-relaxed">${data.horoscopo_diario}</p>
          </div>
        `;
      } else {
        resultado.innerHTML = `
          <div class="text-center">
            <div class="text-4xl mb-4">🔮</div>
            <p class="text-gray-300 text-lg">Não foi possível obter o horóscopo.</p>
          </div>
        `;
      }
    } catch (err) {
      resultado.innerHTML = `
        <div class="text-center">
          <div class="text-4xl mb-4">⚠️</div>
          <p class="text-red-400 text-lg">Erro ao consultar horóscopo.</p>
        </div>
      `;
    }
  });
}

// Partículas místicas
function createMysticParticles() {
  const container = document.getElementById('particles-bg');
  if (!container) return;
  container.innerHTML = '';
  
  const shapes = [
    // Sol estilizado
    `<svg width="38" height="38" viewBox="0 0 38 38" fill="none" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <radialGradient id="solGradient" cx="50%" cy="50%" r="50%">
          <stop offset="0%" stop-color="#fffbe6"/>
          <stop offset="100%" stop-color="#FFD700"/>
        </radialGradient>
      </defs>
      <circle cx="19" cy="19" r="12" fill="url(#solGradient)"/>
      <g stroke="#FFD700" stroke-width="2">
        <line x1="19" y1="2" x2="19" y2="10"/>
        <line x1="19" y1="28" x2="19" y2="36"/>
        <line x1="2" y1="19" x2="10" y2="19"/>
        <line x1="28" y1="19" x2="36" y2="19"/>
        <line x1="7" y1="7" x2="13" y2="13"/>
        <line x1="25" y1="25" x2="31" y2="31"/>
        <line x1="7" y1="31" x2="13" y2="25"/>
        <line x1="25" y1="13" x2="31" y2="7"/>
      </g>
    </svg>`,
    // Lua estilizada
    `<svg width="36" height="36" viewBox="0 0 36 36" fill="none" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <radialGradient id="luaGradient" cx="50%" cy="50%" r="50%">
          <stop offset="0%" stop-color="#e0e7ff"/>
          <stop offset="100%" stop-color="#6b7cff"/>
        </radialGradient>
      </defs>
      <path d="M28 18c0 6.627-5.373 12-12 12a12 12 0 0 1 0-24c.5 0 1 .03 1.5.09A10 10 0 1 0 28 18z" fill="url(#luaGradient)"/>
    </svg>`,
    // Estrela estilizada
    `<svg width="32" height="32" viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <radialGradient id="estrelaGradient" cx="50%" cy="50%" r="50%">
          <stop offset="0%" stop-color="#fffbe6"/>
          <stop offset="100%" stop-color="#ffe066"/>
        </radialGradient>
      </defs>
      <polygon points="16,3 20,12 30,12.5 22,19 25,29 16,23.5 7,29 10,19 2,12.5 12,12" fill="url(#estrelaGradient)" stroke="#ffe066" stroke-width="1.5"/>
    </svg>`
  ];
  
  const num = 22;
  for (let i = 0; i < num; i++) {
    const el = document.createElement('div');
    el.className = 'particle-mystic';
    el.dataset.left = Math.random() * 100;
    el.dataset.top = Math.random() * 100;
    el.style.left = el.dataset.left + 'vw';
    el.style.top = el.dataset.top + 'vh';
    const size = 28 + Math.random() * 36;
    el.style.width = el.style.height = size + 'px';
    el.style.opacity = 0.13 + Math.random() * 0.18;
    el.innerHTML = shapes[Math.floor(Math.random() * shapes.length)];
    el.dataset.dx = (Math.random() - 0.5) * 0.08;
    el.dataset.dy = (Math.random() - 0.5) * 0.08;
    container.appendChild(el);
  }
}

function animateMysticParticles() {
  const particles = document.querySelectorAll('.particle-mystic');
  particles.forEach(el => {
    let left = parseFloat(el.dataset.left);
    let top = parseFloat(el.dataset.top);
    let dx = parseFloat(el.dataset.dx);
    let dy = parseFloat(el.dataset.dy);
    left += dx;
    top += dy;
    if (left < 0 || left > 100) el.dataset.dx = (-dx).toString();
    if (top < 0 || top > 100) el.dataset.dy = (-dy).toString();
    el.dataset.left = left;
    el.dataset.top = top;
    el.style.left = left + 'vw';
    el.style.top = top + 'vh';
  });
  requestAnimationFrame(animateMysticParticles);
}

// Inicialização quando o DOM estiver pronto
document.addEventListener('DOMContentLoaded', () => {
  initFadeSections();
  initMobileMenu();
  initHoroscopeForm();
  createMysticParticles();
  animateMysticParticles();
  
  // Recriar partículas quando a janela for redimensionada
  window.addEventListener('resize', createMysticParticles);
}); 