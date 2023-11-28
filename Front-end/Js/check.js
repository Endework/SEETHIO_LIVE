var images1 = document.querySelectorAll('#imageCard1 img');
var currentImage1 = 0;
var hoverInterval1;
var imageCard1 = document.querySelector('#imageCard1');
var lastMousePosition1 = { x: 0, y: 0 };
var mouseSpeed1 = 0;
var isMouseOver1 = false; // Add this flag

function changeImage(direction) {
    images1[currentImage1].classList.remove('active2');
    if (direction === 'right') {
        currentImage1 = (currentImage1 + 1) % images1.length;
    } else if (direction === 'left') {
        currentImage1 = (currentImage1 - 1 + images1.length) % images1.length;
    }
    images1[currentImage1].classList.add('active2');
}

imageCard1.addEventListener('mousemove', function(e) {
    if (!isMouseOver1) return; // Add this line

    var rect = e.target.getBoundingClientRect();
    var x = e.clientX - rect.left; //x position within the element.
    var y = e.clientY - rect.top;  //y position within the element.

    // Calculate mouse speed and direction
    mouseSpeed1 = Math.sqrt(Math.pow(x - lastMousePosition1.x, 2) + Math.pow(y - lastMousePosition1.y, 2));
    var direction = x > lastMousePosition1.x ? 'right' : 'left';
    lastMousePosition1 = { x: x, y: y };

    // Change image based on mouse direction
    changeImage(direction);
});

imageCard1.addEventListener('mouseover', function(e) {
    isMouseOver1 = true; // Set the flag to true

    hoverInterval1 = setInterval(function() {
        var transitionTime = 1000 / mouseSpeed1; // Change transition time based on mouse speed
        changeImage('right'); // Default direction
    }, 1000);
});

imageCard1.addEventListener('mouseout', function() {
    isMouseOver1 = false; // Set the flag to false
    clearInterval(hoverInterval1);
});
