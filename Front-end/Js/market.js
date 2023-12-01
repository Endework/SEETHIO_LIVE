var buckets = document.querySelectorAll('.bucket');
for(var i = 0; i < buckets.length; i++) {
  buckets[i].addEventListener('click', function() {
    this.innerHTML = 'Added to Bucketlist';
    this.style.backgroundColor = '#FABF00';
    this.style.color='#006167';
  });
};