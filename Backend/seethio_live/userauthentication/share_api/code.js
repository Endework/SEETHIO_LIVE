const shareDialog = document.querySelector('.share-dialog');
const closeButton = document.querySelector('.close-button');
let sharedUrl = ''; // Variable to store the shared URL

function shareOnFacebook() {
    // Replace with actual Facebook sharing logic
    console.log('Sharing on Facebook');
    // Assuming you dynamically get the URL here
    sharedUrl = window.location.href;
}

// ... (other share functions) ...

function copyLink() {
    if (!sharedUrl) {
        console.error('No URL to copy. Please share a platform first.');
        return;
    }

    // Create a temporary textarea element to facilitate copying
    const tempTextArea = document.createElement('textarea');
    tempTextArea.value = sharedUrl;
    
    // Append the textarea to the document
    document.body.appendChild(tempTextArea);
    
    // Select the text in the textarea
    tempTextArea.select();
    
    // Copy the selected text
    document.execCommand('copy');
    
    // Remove the temporary textarea
    document.body.removeChild(tempTextArea);

    console.log('Link copied to clipboard');
}

document.querySelector('.share-button').addEventListener('click', event => {
    if (navigator.share) { 
        navigator.share({
            title: 'WebShare API Demo',
            url: window.location.href // Dynamically get the current URL
        })
        .then(() => {
            console.log('Thanks for sharing!');
            // Assuming you dynamically get the URL after successful sharing
            sharedUrl = window.location.href;
        })
        .catch(error => {
            console.error('Error sharing:', error);
            shareDialog.classList.add('is-open'); // Open custom dialog on error
        });
    } else {
        shareDialog.classList.add('is-open');
    }
});

closeButton.addEventListener('click', event => {
    shareDialog.classList.remove('is-open');
});
