document.addEventListener("DOMContentLoaded", function() {
  const carousels = document.querySelectorAll(".carousel");

  carousels.forEach((carousel) => {
    let currentIndex = 0;

    setInterval(() => {
      currentIndex = (currentIndex + 1) % carousel.children.length;
      const transformValue = -currentIndex * 500; // Adjust for image width
      carousel.style.transform = `translateX(${transformValue}px)`;
    }, 3000);
  });
});