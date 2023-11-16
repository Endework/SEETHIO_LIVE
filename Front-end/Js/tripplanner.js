document
.querySelector("#copylink")
.addEventListener("click", function () {
  document.querySelector(".message").style.display = "block";
});
document.querySelector(".close").addEventListener("click", function () {
document.querySelector(".message").style.display = "none";
});

var btn = document.getElementById("addtobucket");

btn.addEventListener('mouseover', function() {
  btn.style.backgroundColor = '#FABF00';
  btn.style.color='#006167';
});
btn.addEventListener('mouseout', function() {
  btn.style.backgroundColor = '#006167'; // Reset the background color when the mouse is not over the button
  btn.style.color='#fff'
});
