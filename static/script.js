document.addEventListener("DOMContentLoaded", function() {
  const userInputElement = document.getElementById("user_input");
  const responseContainer = document.getElementById("response_container");
  const loadingIndicator = document.getElementById("loading_indicator");

  document.querySelector(".send-button").addEventListener("click", function() {
    const userInput = userInputElement.value.trim();
    if (userInput !== "") {
      userInputElement.value = ""; // Clear the input field

      // Show loading indicator
      loadingIndicator.innerHTML = "Loading...";

      // Send user input to the server and fetch bot response
      fetch("/virtual-therapist", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ user_input: userInput })
      })
        .then(response => response.json())
        .then(data => {
          // Hide loading indicator
          loadingIndicator.innerHTML = "";

          // Append user input and bot response to the response container
          responseContainer.innerHTML += `
            <p class="user-input">${userInput}</p>
            <p class="bot-response">${data.bot_response}</p>
          `;
        })
        .catch(error => {
          console.error("Error:", error);
        });
    }
  });
});
