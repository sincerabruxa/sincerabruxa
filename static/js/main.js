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

  const whatsappBtn = document.getElementById('whatsapp-floating');
  const footer = document.querySelector('footer');
  if (whatsappBtn && footer) {
    const observer = new IntersectionObserver(([entry]) => {
      whatsappBtn.classList.toggle('opacity-0', entry.isIntersecting);
      whatsappBtn.classList.toggle('pointer-events-none', entry.isIntersecting);
    }, { threshold: 0.1 });

    observer.observe(footer);
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

      const texto = partes.join(' | ') || 'Olá, gostaria de saber mais sobre as consultas de tarot.';
      const link = `https://wa.me/5522981735681?text=${encodeURIComponent(texto)}`;
      window.open(link, '_blank', 'noopener');
    });
  }

  if (mobileButton && mobileMenu) {
    const toggleMenu = () => {
      const isHidden = mobileMenu.classList.toggle('hidden');
      mobileButton.classList.toggle('active', !isHidden);
      mobileButton.setAttribute('aria-expanded', String(!isHidden));
    };

    mobileButton.addEventListener('click', toggleMenu);

    const closeMenu = () => {
      if (!mobileMenu.classList.contains('hidden')) {
        mobileMenu.classList.add('hidden');
        mobileButton.classList.remove('active');
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
