var carouselClasses = ['carousel1', 'carousel2', 'carousel3', 'carousel4', 'carousel5', 'carousel6' ,'carousel7', 'carousel8', 'carousel9'];

carouselClasses.forEach(function(carouselClass) {
    var carousel = document.querySelector('.' + carouselClass);
    var images = Array.from(carousel.querySelectorAll('.carousel-image'));
    var currentImageIndex = 0;
    var isHovering = false;

    carousel.addEventListener('mouseover', function() {
        isHovering = true;
        cycleImages();
    });

    carousel.addEventListener('mouseout', function() {
        isHovering = false;
    });

    carousel.addEventListener('mousemove', function(e) {
        var rect = carousel.getBoundingClientRect();
        var x = e.clientX - rect.left; // x position within the element
        var width = rect.right - rect.left; // width of the element
        var percentage = x / width; // percentage of the x position within the element
        var speed = 10 * (1 - percentage); // speed based on the x position

        images.forEach(function(image) {
            image.style.transition = 'opacity ' + speed + 's';
        });
    });

    function cycleImages() {
        if (!isHovering) return;

        images[currentImageIndex].style.opacity = 0;
        currentImageIndex = (currentImageIndex + 1) % images.length;
        images[currentImageIndex].style.opacity = 1;

        setTimeout(cycleImages, 2000);
    }
});

// for the popup2
document
.querySelector("#copylink")
.addEventListener("click", function () {
  document.querySelector(".message").style.display = "block";
});
document.querySelector(".close").addEventListener("click", function () {
document.querySelector(".message").style.display = "none";
});

// for the dropdown check boxes
document.querySelector(".checkbox-dropdown").addEventListener("click", function () {
    this.classList.toggle("is-active");
});

// Prevent the click event from propagating to the parent ul
document.querySelector(".checkbox-dropdown ul").addEventListener("click", function (e) {
    e.stopPropagation();
});