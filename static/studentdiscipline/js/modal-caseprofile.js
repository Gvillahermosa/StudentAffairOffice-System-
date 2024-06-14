document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('.case-form');
    const noStudentFound = document.getElementById('no-student-found');
    const missingQuery = document.getElementById('missing-query');

    // Show SweetAlert if no student found
    if (noStudentFound) {
        Swal.fire({
            icon: "error",
            title: "Oops...",
            text: "No student found with that ID."
        });
    }

    // Form submission validation
    if (form) {
        form.addEventListener('submit', function (event) {
            event.preventDefault();

            // Serialize form data
            const formData = new FormData(form);

            // Submit form data using AJAX
            fetch('', {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    // Show Sweet Alert on success
                    Swal.fire({
                        title: "Success!",
                        text: "Case saved successfully.",
                        icon: "success"
                    });

                    //form.reset();
                    form.closest('.case-container').remove();
                } else {
                    // Handle errors if any
                    Swal.fire({
                        title: "Error!",
                        text: "Failed to save case.",
                        icon: "error"
                    });
                }
            })
            .catch(error => {
                console.error('Error:', error);
                // Handle any network errors
                Swal.fire({
                    title: "Error!",
                    text: "Failed to save case due to a network error.",
                    icon: "error"
                });
            });
        });
    }

    // Validate student ID input on search form submission
    const studentIdInput = document.querySelector('input[name="q"]');
    const searchButton = document.querySelector('.search-container button'); // Adjust this selector as per your actual HTML

    if (studentIdInput && searchButton) {
        searchButton.addEventListener('click', function (event) {
            const studentId = studentIdInput.value.trim();

            // Check if the student ID is missing or not a number
            if (!studentId) {
                event.preventDefault();
                Swal.fire({
                    icon: "error",
                    title: "Oops...",
                    text: "Student ID must be provided."
                });
            } else if (isNaN(studentId)) {
                event.preventDefault();
                Swal.fire({
                    icon: "error",
                    title: "Oops...",
                    text: "Student ID must be a number."
                });
            }
        });
    }
});