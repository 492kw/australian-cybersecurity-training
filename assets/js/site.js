(() => {
  const toggle = document.querySelector('.nav-toggle');
  const nav = document.querySelector('#site-nav');
  if (!toggle || !nav) return;
  const close = () => { toggle.setAttribute('aria-expanded', 'false'); nav.dataset.open = 'false'; };
  toggle.addEventListener('click', () => {
    const open = toggle.getAttribute('aria-expanded') !== 'true';
    toggle.setAttribute('aria-expanded', String(open));
    nav.dataset.open = String(open);
  });
  nav.querySelectorAll('a').forEach(link => link.addEventListener('click', close));
  window.addEventListener('resize', () => { if (window.innerWidth > 820) close(); });
})();
