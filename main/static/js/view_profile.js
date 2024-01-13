function showSection(sectionId) {
  var sectionIds = ['info', 'posts', 'upvotes', 'downvotes'];

  // Hide all sections
  for (var i = 0; i < sectionIds.length; i++) {
    var currentSection = document.getElementById(sectionIds[i]);
    if (currentSection) {
      currentSection.style.display = 'none';
    }
  }

  // Show the selected section
  var selectedSection = document.getElementById(sectionId);
  if (selectedSection) {
    selectedSection.style.display = 'block';
  }
}

function feedbackForm() {
  alert("Thank you for giving us your feedback! We are glad to have you here!")
}