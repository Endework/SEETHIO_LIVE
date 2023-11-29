
//   var image = document.getElementById('mainimage');
// var zoom = document.getElementById('zoom');
// var cropper = new Cropper(image, {
// aspectRatio: 1,
// highlight: false,  // Add this line
// background:false,

// crop: function(event) {
//   console.log(event.detail.x);
//   console.log(event.detail.y);
//   console.log(event.detail.width);
//   console.log(event.detail.height);
//   console.log(event.detail.rotate);
//   console.log(event.detail.scaleX);
//   console.log(event.detail.scaleY);
// }
// });

// zoom.oninput = function() {
// cropper.zoomTo(this.value);
// }

var image = document.getElementById('mainimage');
var zoom = document.getElementById('zoom');
var rotateLeft = document.querySelector('.bottom-div svg:first-child');
var rotateRight = document.querySelector('.bottom-div svg:last-child');

var cropper = new Cropper(image, {
  aspectRatio: 1,
  highlight: false,
  background: false,
  crop: function(event) {
    console.log(event.detail.x);
    console.log(event.detail.y);
    console.log(event.detail.width);
    console.log(event.detail.height);
    console.log(event.detail.rotate);
    console.log(event.detail.scaleX);
    console.log(event.detail.scaleY);
  }
});

zoom.oninput = function() {
  cropper.zoomTo(this.value);
}

rotateLeft.addEventListener('click', function() {
  cropper.rotate(-45); // Rotate 45 degrees to the left
});

rotateRight.addEventListener('click', function() {
  cropper.rotate(45); // Rotate 45 degrees to the right
});

var saveButton = document.getElementById('save');
var doneButton = document.getElementById('done');

doneButton.addEventListener('click', function() {
  saveButton.style.display = 'block'; // Show the save button
});




saveButton.addEventListener('click', function() {
  var croppedCanvas = cropper.getCroppedCanvas();
  var croppedImage = document.createElement('img');
  croppedImage.src = croppedCanvas.toDataURL('image/png');
  
  // Replace the original image with the cropped one
  cropper.replace(croppedImage.src);
  
  // Destroy the cropper
  cropper.destroy();
});




