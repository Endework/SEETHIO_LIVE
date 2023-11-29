// for the bucketlist
var buckets = document.querySelectorAll('#bucket');
for(var i = 0; i < buckets.length; i++) {
  buckets[i].addEventListener('click', function() {
    this.innerHTML = 'Added to Bucketlist';
    this.style.backgroundColor = '#FABF00';
    this.style.color='#006167';
  });
};


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


