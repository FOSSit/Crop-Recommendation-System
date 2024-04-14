document.addEventListener('DOMContentLoaded', function() {
    var form = document.getElementById('contactForm');
    form.addEventListener('submit', function(event) {
        event.preventDefault();
        var name = document.getElementById('name').value;
        var email = document.getElementById('email').value;
        var message = document.getElementById('message').value;
        
        // Perform client-side validation
        if (!name || !message) {
            alert('Please fill in all required fields.');
            return;
        }
        
        // Optional: Perform email format validation
        if (email && !isValidEmail(email)) {
            alert('Please enter a valid email address.');
            return;
        }
        
        // Optional: Perform additional validation as needed
        
        // Submit the form data
        submitFormData(name, email, message);
    });
});

function isValidEmail(email) {
    // Basic email format validation using regex
    var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
}

function submitFormData(name, email, message) {
    // Implement AJAX request to submit form data to backend
    // Example using Fetch API:
    fetch('/submit_contact_form', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            name: name,
            email: email,
            message: message
        })
    })
    .then(response => {
        if (response.ok) {
            alert('Message sent successfully!');
            // Optionally clear form fields after successful submission
            document.getElementById('name').value = '';
            document.getElementById('email').value = '';
            document.getElementById('message').value = '';
        } else {
            throw new Error('Failed to send message.');
        }
    })
    .catch(error => {
        alert('An error occurred: ' + error.message);
    });
}
