// This is for image slider 
var index = 0;
var images = document.querySelectorAll('#carousel img');
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






// This is for the room section on the lodge section
// function incrementValue()
// {
//     var value = parseInt(document.getElementById('number10').innerText, 10);
//     value = isNaN(value) ? 0 : value;
//     value++;
//     document.getElementById('number10').innerText = value;
// }

// function decrementValue()
// {
//     var value = parseInt(document.getElementById('number10').innerText, 10);
//     value = isNaN(value) ? 0 : value;
//     value < 1 ? value = 1 : '';
//     value--;
//     document.getElementById('number10').innerText = value;
// }
// This code is to switch between lodge and flight pages

// var lodgeButton = document.getElementById('lodgeButton');
//   var flightButton = document.getElementById('flightButton');
  
//   lodgeButton.addEventListener('click', function() {
//     document.getElementById('lodgecontainer').style.display = 'block';
//     document.getElementById('flightcontainer').style.display = 'none';
//     lodgeButton.classList.add('active');
//     flightButton.classList.remove('active');
//     document.querySelector('.description').innerHTML = '(Lodge API search results/Interface)';

//   });
  
//   flightButton.addEventListener('click', function() {
//     document.getElementById('flightcontainer').style.display = 'block';
//     document.getElementById('lodgecontainer').style.display = 'none';
//     flightButton.classList.add('active');
//     lodgeButton.classList.remove('active');
//     document.querySelector('.description').innerHTML = '(Flight API search results/Interface)';

//   });
  var buckets = document.getElementsByClassName('bucket');
  for(var i = 0; i < buckets.length; i++) {
    buckets[i].addEventListener('click', function() {
      this.innerHTML = 'Added to Bucketlist';
      this.style.backgroundColor = '#FABF00';
      this.style.color='#006167';
    });
  }
  var description = document.querySelector('.description');
  document.querySelector('.search-btn').addEventListener('click', function(event){
      event.preventDefault();
      // description.innerHTML = 'Lodge API search results/Interface';
  });
  
// api pouup
// document.querySelector('#copylink').addEventListener('click', function() {
//   document.querySelector('.message').style.display = 'block';
// });

// document.querySelector('#copylink1').addEventListener('click', function() {
//   document.querySelector('.message1').style.display = 'block';
// });

