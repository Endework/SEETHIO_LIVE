var imageCards = ['imageCard', 'imageCard1', 'imageCard2'];
var images = [];
var currentImage = [];
var hoverInterval = [];
var lastMousePosition = [];
var mouseSpeed = [];
var isMouseOver = [];

for (let i = 0; i < imageCards.length; i++) {
    images[i] = document.querySelectorAll('#' + imageCards[i] + ' img');
    currentImage[i] = 0;
    lastMousePosition[i] = { x: 0, y: 0 };
    mouseSpeed[i] = 0;
    isMouseOver[i] = false;

    function changeImage(direction) {
        images[i][currentImage[i]].classList.remove('active2');
        if (direction === 'right') {
            currentImage[i] = (currentImage[i] + 1) % images[i].length;
        } else if (direction === 'left') {
            currentImage[i] = (currentImage[i] - 1 + images[i].length) % images[i].length;
        }
        images[i][currentImage[i]].classList.add('active2');
    }

    var imageCard = document.querySelector('#' + imageCards[i]);

    imageCard.addEventListener('mousemove', function(e) {
        if (!isMouseOver[i]) return;

        var rect = e.target.getBoundingClientRect();
        var x = e.clientX - rect.left;
        var y = e.clientY - rect.top;

        mouseSpeed[i] = Math.sqrt(Math.pow(x - lastMousePosition[i].x, 2) + Math.pow(y - lastMousePosition[i].y, 2));
        var direction = x > lastMousePosition[i].x ? 'right' : 'left';
        lastMousePosition[i] = { x: x, y: y };

        changeImage(direction);
    });

    imageCard.addEventListener('mouseover', function(e) {
        isMouseOver[i] = true;

        hoverInterval[i] = setInterval(function() {
            var transitionTime = 1000 / mouseSpeed[i];
            changeImage('right');
        }, 1000);
    });

    imageCard.addEventListener('mouseout', function() {
        isMouseOver[i] = false;
        clearInterval(hoverInterval[i]);
    });
}
