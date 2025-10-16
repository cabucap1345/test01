//
document.addEventListener('DOMContentLoaded', () => {

    const loginForm = document.getElementById('login-form');
    const protectedDataButton = document.getElementById('get-protected-data');
    const messageDiv = document.getElementById('message');

    // Function to handle the login process
    async function handleLogin(event) {
        event.preventDefault(); // Prevent the form from submitting normally

        const username = loginForm.username.value;
        const password = loginForm.password.value;

        try {
            // Send the login request to the backend
            const response = await fetch('/api/login', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ username, password })
            });

            if (!response.ok) {
                // If the response is not ok, throw an error
                const errorData = await response.json();
                throw new Error(errorData.message || 'Login failed');
            }

            // Get the JWT from the response
            const data = await response.json();
            const token = data.token;

            // Store the token securely (e.g., in localStorage)
            // Note: localStorage is not the most secure place for tokens.
            localStorage.setItem('authToken', token);

            showMessage('Login successful! Token stored.', 'success');
        } catch (error) {
            showMessage(`Error: ${error.message}`, 'error');
        }
    }

    // Function to fetch protected data using the stored token
    async function getProtectedData() {
        const token = localStorage.getItem('authToken');

        if (!token) {
            showMessage('No token found. Please log in first.', 'error');
            return;
        }

        try {
            // Send the request with the JWT in the Authorization header
            const response = await fetch('/api/data', {
                method: 'GET',
                headers: {
                    'Authorization': `Bearer ${token}`
                }
            });

            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.message || 'Failed to fetch protected data');
            }

            const data = await response.json();
            showMessage(`Protected data fetched successfully: ${JSON.stringify(data)}`, 'success');
        } catch (error) {
            showMessage(`Error: ${error.message}`, 'error');
            // If the token is invalid, you might want to remove it
            if (error.message.includes('invalid token')) {
                localStorage.removeItem('authToken');
            }
        }
    }

    // A simple function to display messages to the user
    function showMessage(message, type) {
        messageDiv.textContent = message;
        messageDiv.className = type; // 'success' or 'error'
    }

    // Attach event listeners to the form and button
    if (loginForm) {
        loginForm.addEventListener('submit', handleLogin);
    }
    if (protectedDataButton) {
        protectedDataButton.addEventListener('click', getProtectedData);
    }
});