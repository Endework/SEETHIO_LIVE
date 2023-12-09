var images = document.querySelectorAll('#imageCard img');
var currentImage = 0;
var hoverInterval;
var imageCard = document.querySelector('#imageCard');
var lastMousePosition = { x: 0, y: 0 };
var mouseSpeed = 0;
var isMouseOver = false; // Add this flag

function changeImage(direction) {
    images[currentImage].classList.remove('active7');
    if (direction === 'right') {
        currentImage = (currentImage + 1) % images.length;
    } else if (direction === 'left') {
        currentImage = (currentImage - 1 + images.length) % images.length;
    }
    images[currentImage].classList.add('active7');
}

imageCard.addEventListener('mousemove', function(e) {
    if (!isMouseOver) return; // Add this line

    var rect = e.target.getBoundingClientRect();
    var x = e.clientX - rect.left; //x position within the element.
    var y = e.clientY - rect.top;  //y position within the element.

    // Calculate mouse speed and direction
    mouseSpeed = Math.sqrt(Math.pow(x - lastMousePosition.x, 2) + Math.pow(y - lastMousePosition.y, 2));
    var direction = x > lastMousePosition.x ? 'right' : 'left';
    lastMousePosition = { x: x, y: y };

    // Change image based on mouse direction
    changeImage(direction);
});

imageCard.addEventListener('mouseover', function(e) {
    isMouseOver = true; // Set the flag to true

    hoverInterval = setInterval(function() {
        var transitionTime = 1000 / mouseSpeed; // Change transition time based on mouse speed
        changeImage('right'); // Default direction
    }, 1000);
});

imageCard.addEventListener('mouseout', function() {
    isMouseOver = false; // Set the flag to false
    clearInterval(hoverInterval);
});

// for card 2

var images1 = document.querySelectorAll('#imageCard1 img');
var currentImage1 = 0;
var hoverInterval1;
var imageCard1 = document.querySelector('#imageCard1');
var lastMousePosition1 = { x: 0, y: 0 };
var mouseSpeed1 = 0;
var isMouseOver1 = false; // Add this flag

function changeImage1(direction) {
    images1[currentImage1].classList.remove('active8');
    if (direction === 'right') {
        currentImage1 = (currentImage1 + 1) % images1.length;
    } else if (direction === 'left') {
        currentImage1 = (currentImage1 - 1 + images1.length) % images1.length;
    }
    images1[currentImage1].classList.add('active8');
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
    changeImage1(direction);
});

imageCard1.addEventListener('mouseover', function(e) {
    isMouseOver1 = true; // Set the flag to true

    hoverInterval1 = setInterval(function() {
        var transitionTime = 1000 / mouseSpeed1; // Change transition time based on mouse speed
        changeImage1('right'); // Default direction
    }, 1000);
});

imageCard1.addEventListener('mouseout', function() {
    isMouseOver1 = false; // Set the flag to false
    clearInterval(hoverInterval1);
});

// for card 3
var images2 = document.querySelectorAll('#imageCard2 img');
var currentImage2 = 0;
var hoverInterval2;
var imageCard2 = document.querySelector('#imageCard2');
var lastMousePosition2 = { x: 0, y: 0 };
var mouseSpeed2 = 0;
var isMouseOver2 = false; // Add this flag

function changeImage(direction) {
    images2[currentImage2].classList.remove('active9');
    if (direction === 'right') {
        currentImage2 = (currentImage2 + 1) % images2.length;
    } else if (direction === 'left') {
        currentImage2 = (currentImage2 - 1 + images2.length) % images2.length;
    }
    images2[currentImage2].classList.add('active3');
}

imageCard2.addEventListener('mousemove', function(e) {
    if (!isMouseOver2) return; // Add this line

    var rect = e.target.getBoundingClientRect();
    var x = e.clientX - rect.left; //x position within the element.
    var y = e.clientY - rect.top;  //y position within the element.

    // Calculate mouse speed and direction
    mouseSpeed2 = Math.sqrt(Math.pow(x - lastMousePosition.x, 2) + Math.pow(y - lastMousePosition.y, 2));
    var direction = x > lastMousePosition.x ? 'right' : 'left';
    lastMousePosition = { x: x, y: y };

    // Change image based on mouse direction
    changeImage(direction);
});

imageCard2.addEventListener('mouseover', function(e) {
    isMouseOver2 = true; // Set the flag to true

    hoverInterval2 = setInterval(function() {
        var transitionTime = 1000 / mouseSpeed; // Change transition time based on mouse speed
        changeImage('right'); // Default direction
    }, 1000);
});

imageCard2.addEventListener('mouseout', function() {
    isMouseOver2 = false; // Set the flag to false
    clearInterval(hoverInterval2);
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