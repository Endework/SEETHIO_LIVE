var questions = document.getElementsByClassName("question");
for (var i = 0; i < questions.length; i++) {
questions[i].addEventListener("click", function() {
this.classList.toggle("active");
var answer = this.nextElementSibling;
var icon = this.getElementsByClassName("dropdown-icon")[0];
if (answer.style.display === "block") {
    answer.style.display = "none";
    icon.style.transform = "rotate(0deg)";
} else {
    answer.style.display = "block";
    icon.style.transform = "rotate(180deg)";
}
});
}
var index = 0;
var images = document.querySelectorAll('.carousel-image');  // Use the new class
var texts = document.querySelectorAll('#text p');

setInterval(function() {
// Remove the 'active' class from the current elements
images[index].classList.remove('active');
texts[index].classList.remove('active');

// Increment the index, and loop back to 0 if we've reached the end
index = (index + 1) % images.length;

// Add the 'active' class to the new elements
images[index].classList.add('active');
texts[index].classList.add('active');
}, 3000);  // Change every 3 seconds

