document.addEventListener("DOMContentLoaded", function () {
  const header = document.querySelector('.header-container');
  window.addEventListener('scroll', function () {
    if (window.scrollY > 40) {
      header.classList.add('scrolled');
    } else {
      header.classList.remove('scrolled');
    }
  });
});