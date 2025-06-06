document.addEventListener("DOMContentLoaded", function () {
  const slides = document.querySelectorAll('.slide-img');
  const dots = document.querySelectorAll('#slide-dots .dot');
  let current = 0;
  function showSlide(idx) {
    slides.forEach((img, i) => {
      img.classList.toggle('active', i === idx);
      dots[i].classList.toggle('active', i === idx);
    });
  }
  setInterval(() => {
    current = (current + 1) % slides.length;
    showSlide(current);
  }, 4000); // 4 seconds per slide (slow and smooth)
});