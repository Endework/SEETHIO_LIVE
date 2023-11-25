// For #imageCard
var images = document.querySelectorAll('#imageCard img');
var currentImage = 0;
var hoverInterval;
var imageCard = document.querySelector('#imageCard');
var lastMousePosition = { x: 0, y: 0 };
var mouseSpeed = 0;
var isMouseOver = false;

imageCard.addEventListener('mousemove', function(e) {
    if (!isMouseOver) return;

    var rect = e.target.getBoundingClientRect();
    var x = e.clientX - rect.left;
    var y = e.clientY - rect.top;

    mouseSpeed = Math.sqrt(Math.pow(x - lastMousePosition.x, 2) + Math.pow(y - lastMousePosition.y, 2));
    var direction = x > lastMousePosition.x ? 'right' : 'left';
    lastMousePosition = { x: x, y: y };

    changeImage(direction);
});

imageCard.addEventListener('mouseover', function(e) {
    isMouseOver = true;

    hoverInterval = setInterval(function() {
        var transitionTime = 1000 / mouseSpeed;
        changeImage('right');
    }, 1000);
});

imageCard.addEventListener('mouseout', function() {
    isMouseOver = false;
    clearInterval(hoverInterval);
});

function changeImage(direction) {
    images[currentImage].classList.remove('active');
    if (direction === 'right') {
        currentImage = (currentImage + 1) % images.length;
    } else if (direction === 'left') {
        currentImage = (currentImage - 1 + images.length) % images.length;
    }
    images[currentImage].classList.add('active');
}

// For #imageCard1
var images1 = document.querySelectorAll('#imageCard1 img');
var currentImage1 = 0;
var hoverInterval1;
var imageCard1 = document.querySelector('#imageCard1');
var lastMousePosition1 = { x: 0, y: 0 };
var mouseSpeed1 = 0;
var isMouseOver1 = false;

imageCard1.addEventListener('mousemove', function(e) {
    if (!isMouseOver1) return;

    var rect = e.target.getBoundingClientRect();
    var x = e.clientX - rect.left;
    var y = e.clientY - rect.top;

    mouseSpeed1 = Math.sqrt(Math.pow(x - lastMousePosition1.x, 2) + Math.pow(y - lastMousePosition1.y, 2));
    var direction = x > lastMousePosition1.x ? 'right' : 'left';
    lastMousePosition1 = { x: x, y: y };

    changeImage1(direction);
});

imageCard1.addEventListener('mouseover', function(e) {
    isMouseOver1 = true;

    hoverInterval1 = setInterval(function() {
        var transitionTime = 1000 / mouseSpeed1;
        changeImage1('right');
    }, 1000);
});

imageCard1.addEventListener('mouseout', function() {
    isMouseOver1 = false;
    clearInterval(hoverInterval1);
});

function changeImage1(direction) {
    images1[currentImage1].classList.remove('active1');
    if (direction === 'right') {
        currentImage1 = (currentImage1 + 1) % images1.length;
    } else if (direction === 'left') {
        currentImage1 = (currentImage1 - 1 + images1.length) % images1.length;
    }
    images1[currentImage1].classList.add('active1');
}

// For #imageCard2
var images2 = document.querySelectorAll('#imageCard2 img');
var currentImage2 = 0;
var hoverInterval2;
var imageCard2 = document.querySelector('#imageCard2');
var lastMousePosition2 = { x: 0, y: 0 };
var mouseSpeed2 = 0;
var isMouseOver2 = false;

imageCard2.addEventListener('mousemove', function(e) {
    if (!isMouseOver2) return;

    var rect = e.target.getBoundingClientRect();
    var x = e.clientX - rect.left;
    var y = e.clientY - rect.top;

    mouseSpeed2 = Math.sqrt(Math.pow(x - lastMousePosition2.x, 2) + Math.pow(y - lastMousePosition2.y, 2));
    var direction = x > lastMousePosition2.x ? 'right' : 'left';
    lastMousePosition2 = { x: x, y: y };

    changeImage2(direction);
});

imageCard2.addEventListener('mouseover', function(e) {
    isMouseOver2 = true;

    hoverInterval2 = setInterval(function() {
        var transitionTime = 1000 / mouseSpeed2;
        changeImage2('right');
    }, 1000);
});

imageCard2.addEventListener('mouseout', function() {
    isMouseOver2 = false;
    clearInterval(hoverInterval2);
});

function changeImage2(direction) {
    images2[currentImage2].classList.remove('active2');
    if (direction === 'right') {
        currentImage2 = (currentImage2 + 1) % images2.length;
    } else if (direction === 'left') {
        currentImage2 = (currentImage2 - 1 + images2.length) % images2.length;
    }
    images2[currentImage2].classList.add('active2');
}
