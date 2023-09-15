// script.js
function validateForm() {
    var username = document.getElementById("username").value;
    var email = document.getElementById("email").value;
    var password = document.getElementById("password").value;
    var confirmPassword = document.getElementById("confirm-password").value;
    var isValid = true;
  
    // Reset error messages
    document.getElementById("username-error").textContent = "";
    document.getElementById("email-error").textContent = "";
    document.getElementById("password-error").textContent = "";
    document.getElementById("confirm-password-error").textContent = "";
  
    if (username.length < 3) {
      document.getElementById("username-error").textContent =
        "Username must be at least 3 characters";
      isValid = false;
    }
  
    // Simple email validation (you can enhance it)
    if (!email.includes("@")) {
      document.getElementById("email-error").textContent =
        "Invalid email format";
      isValid = false;
    }
  
    if (password.length < 6) {
      document.getElementById("password-error").textContent =
        "Password must be at least 6 characters";
      isValid = false;
    }
  
    if (password !== confirmPassword) {
      document.getElementById("confirm-password-error").textContent =
        "Passwords do not match";
      isValid = false;
    }
  
    return isValid;
  }
  