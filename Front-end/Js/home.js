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
function incrementValue()
{
    var value = parseInt(document.getElementById('number10').innerText, 10);
    value = isNaN(value) ? 0 : value;
    value++;
    document.getElementById('number10').innerText = value;
}

function decrementValue()
{
    var value = parseInt(document.getElementById('number10').innerText, 10);
    value = isNaN(value) ? 0 : value;
    value < 1 ? value = 1 : '';
    value--;
    document.getElementById('number10').innerText = value;
}
// This code is to switch between lodge and flight pages

var lodgeButton = document.getElementById('lodgeButton');
  var flightButton = document.getElementById('flightButton');
  
  lodgeButton.addEventListener('click', function() {
    document.getElementById('lodgecontainer').style.display = 'block';
    document.getElementById('flightcontainer').style.display = 'none';
    lodgeButton.classList.add('active');
    flightButton.classList.remove('active');
    document.querySelector('.description').innerHTML = '(Lodge API search results/Interface)';

  });
  
  flightButton.addEventListener('click', function() {
    document.getElementById('flightcontainer').style.display = 'block';
    document.getElementById('lodgecontainer').style.display = 'none';
    flightButton.classList.add('active');
    lodgeButton.classList.remove('active');
    document.querySelector('.description').innerHTML = '(Flight API search results/Interface)';

  });

// api pouup
document.querySelector('#copylink').addEventListener('click', function() {
  document.querySelector('.message').style.display = 'block';
});

// document.querySelector('#copylink1').addEventListener('click', function() {
//   document.querySelector('.message1').style.display = 'block';
// });


// for the bucketlist button
var buckets = document.getElementsByClassName('bucket');
for(var i = 0; i < buckets.length; i++) {
  buckets[i].addEventListener('click', function() {
    this.innerHTML = 'Added to Bucketlist';
    this.style.backgroundColor = '#FABF00';
    this.style.color='#006167';
  });
}


// lodge popup


// document.querySelector('.cancelButton').addEventListener('click', function() {
//   window.location.href = 'http://www.yourwebsite.com/otherpage#section';
// });


//   This code is for the calander display in the dd-mm-yyyy format for both lodge and flight


// flight section
// for Departure date
// $( function() {
//     var $datepicker = $( "#datepicker" );
//     $datepicker.datepicker({
//         dateFormat: "dd-mm-yy"
//     });

//     $( "#calendar-icon" ).click(function() {
//         if ($datepicker.datepicker('widget').is(':visible')) {
//             $datepicker.datepicker('hide');
//         } else {
//             $datepicker.datepicker('show');
//         }
//     });
// } );

// // for the return date
// $( function() {
//     var $datepicker1 = $( "#datepicker1" );
//     $datepicker1.datepicker({
//         dateFormat: "dd-mm-yy"
//     });

//     $( "#calendar-icon1" ).click(function() {
//         if ($datepicker1.datepicker('widget').is(':visible')) {
//             $datepicker1.datepicker('hide');
//         } else {
//             $datepicker1.datepicker('show');
//         }
//     });
// } );

// // check in
// $( function() {
//     var $datepicker2 = $( "#datepicker3" );
//     $datepicker2.datepicker({
//         dateFormat: "dd-mm-yy"
//     });

//     $( "#calendar-icon2" ).click(function() {
//         if ($datepicker2.datepicker('widget').is(':visible')) {
//             $datepicker2.datepicker('hide');
//         } else {
//             $datepicker2.datepicker('show');
//         }
//     });
// } );

// // checkout
// $( function() {
//     var $datepicker3 = $( "#datepicker4" );
//     $datepicker3.datepicker({
//         dateFormat: "dd-mm-yy"
//     });

//     $( "#calendar-icon3" ).click(function() {
//         if ($datepicker3.datepicker('widget').is(':visible')) {
//             $datepicker3.datepicker('hide');
//         } else {
//             $datepicker3.datepicker('show');
//         }
//     });
// } );





