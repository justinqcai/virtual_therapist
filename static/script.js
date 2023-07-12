document.addEventListener("DOMContentLoaded", function() {
  const userInputElement = document.getElementById("user_input");
  const chatContainer = document.getElementById("chat_container");
  const loadingIndicator = document.getElementById("loading_indicator");

  function scrollToBottom() {
    chatContainer.scrollTop = chatContainer.scrollHeight;
  }

  function appendMessage(containerClass, message) {
    const messageContainer = document.createElement("div");
    messageContainer.classList.add("message-container", containerClass);
    messageContainer.innerHTML = `<p>${message}</p>`;
    chatContainer.appendChild(messageContainer);
    scrollToBottom();
  }

  document.querySelector(".send-button").addEventListener("click", function() {
    const userInput = userInputElement.value.trim();
    if (userInput !== "") {
      userInputElement.value = ""; // Clear the input field

      // Append user input to the chat container
      appendMessage("user-input", userInput);

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
          // Remove loading indicator
          loadingIndicator.innerHTML = "";

          // Append bot response to the chat container
          appendMessage("bot-response", data.bot_response);
        })
        .catch(error => {
          console.error("Error:", error);
        });
    }
  });
});
