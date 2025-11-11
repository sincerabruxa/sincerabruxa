document.addEventListener('DOMContentLoaded', () => {
  const mobileButton = document.getElementById('mobile-menu-button');
  const mobileMenu = document.getElementById('mobile-menu');
  const horoscopoSection = document.getElementById('horoscopo');
  const signoSelect = document.getElementById('signo');
  const whatsappForm = document.querySelector('[data-whatsapp-form]');

  if (signoSelect && horoscopoSection?.dataset.signoSelecionado === 'false') {
    signoSelect.selectedIndex = 0;
    signoSelect.value = '';
  }

  const backToTop = document.getElementById('back-to-top');
  if (backToTop) {
    const toggleBackToTop = () => {
      const scrollTop = window.scrollY || document.documentElement.scrollTop;
      const docHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight;
      const threshold = docHeight * 0.5;

      if (scrollTop > threshold) {
        backToTop.classList.remove('pointer-events-none', 'opacity-0', 'translate-y-3');
        backToTop.classList.add('pointer-events-auto');
      } else {
        backToTop.classList.add('pointer-events-none', 'opacity-0', 'translate-y-3');
        backToTop.classList.remove('pointer-events-auto');
      }
    };

    toggleBackToTop();
    window.addEventListener('scroll', toggleBackToTop, { passive: true });

    backToTop.addEventListener('click', () => {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }

  if (whatsappForm) {
    whatsappForm.addEventListener('submit', (event) => {
      event.preventDefault();
      const nome = whatsappForm.elements.namedItem('nome').value.trim();
      const tema = whatsappForm.elements.namedItem('tema').value.trim();
      const mensagem = whatsappForm.elements.namedItem('mensagem').value.trim();

      const partes = [
        nome && `Nome: ${nome}`,
        tema && `Tema: ${tema}`,
        mensagem && `Mensagem: ${mensagem}`,
      ].filter(Boolean);

      const texto = partes.join(' | ') || 'Olá, quero saber mais sobre as consultas.';
      const link = `https://wa.me/5522981735681?text=${encodeURIComponent(texto)}`;
      window.open(link, '_blank', 'noopener');
    });
  }

  if (mobileButton && mobileMenu) {
    const toggleMenu = () => {
      const isHidden = mobileMenu.classList.toggle('hidden');
      mobileButton.setAttribute('aria-expanded', String(!isHidden));
    };

    mobileButton.addEventListener('click', toggleMenu);

    const closeMenu = () => {
      if (!mobileMenu.classList.contains('hidden')) {
        mobileMenu.classList.add('hidden');
        mobileButton.setAttribute('aria-expanded', 'false');
      }
    };

    mobileMenu.querySelectorAll('a').forEach((link) => {
      link.addEventListener('click', closeMenu);
    });

    document.addEventListener('keydown', (event) => {
      if (event.key === 'Escape') {
        closeMenu();
      }
    });
  }
});

window.addEventListener('load', () => {
  const horoscopoSection = document.getElementById('horoscopo');
  const navigationEntry = performance.getEntriesByType('navigation')[0];
  const isReload = navigationEntry?.type === 'reload';
  if (horoscopoSection?.dataset.signoSelecionado === 'true' && !isReload) {
    requestAnimationFrame(() => {
      horoscopoSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
    });
  }
});
