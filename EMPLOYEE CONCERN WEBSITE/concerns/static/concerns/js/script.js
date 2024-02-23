// script.js

// Function to confirm the deletion of a concern
function confirmDelete() {
    return confirm("Are you sure you want to delete this concern?");
  }
  
  // Example of adding event listener to a button
  document.addEventListener("DOMContentLoaded", function() {
    // Get the delete buttons
    var deleteButtons = document.querySelectorAll(".delete-btn");
  
    // Add event listener to each delete button
    deleteButtons.forEach(function(button) {
      button.addEventListener("click", function(event) {
        // Prevent the default form submission
        event.preventDefault();
  
        // Confirm the deletion
        if (confirmDelete()) {
          // Submit the form for deletion
          event.target.closest("form").submit();
        }
      });
    });
  });
  