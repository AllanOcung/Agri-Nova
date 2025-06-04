document.addEventListener("DOMContentLoaded", function () {
  const images = [
    "/static/core/images/1.jpg",
    "/static/core/images/2.jpg",
    "/static/core/images/3.jpg",
  ];
  let idx = 0;
  const banner = document.querySelector('.hero-banner');
  if (!banner) return;
  setInterval(() => {
    idx = (idx + 1) % images.length;
    banner.style.backgroundImage = `url('${images[idx]}')`;
  }, 4000);
});