document.addEventListener("DOMContentLoaded", function () {
  const slides = document.querySelectorAll('.testimonial-slide');
  const dots = document.querySelectorAll('.testimonial-dots .dot');
  let current = 0;
  let timer;

  function showSlide(index) {
    slides.forEach((slide, i) => {
      slide.classList.remove('active', 'prev');
      if (i === current) slide.classList.add('prev'); // outgoing slide
      if (i === index) slide.classList.add('active');
      dots[i].classList.toggle('active', i === index);
    });
    current = index;
  }

  function nextSlide() {
    showSlide((current + 1) % slides.length);
  }

  function startAutoSlide() {
    timer = setInterval(nextSlide, 7000); // slower auto-advance
  }
  function stopAutoSlide() {
    clearInterval(timer);
  }

  dots.forEach((dot, idx) => {
    dot.addEventListener('click', () => {
      showSlide(idx);
      stopAutoSlide();
      startAutoSlide();
    });
  });

  showSlide(0);
  startAutoSlide();
});