document.addEventListener('DOMContentLoaded', function () {
    // Handle sanction form submission
    const sanctionForm = document.getElementById('sanction-form');
    const sanctionSubmitButton = document.querySelector('.sanction-submit-btn');

    sanctionSubmitButton.addEventListener('click', function () {
        sanctionForm.submit();
    });

    // Handle case record deletion with confirmation
    const deleteButtons = document.querySelectorAll('.delete-btn');
    deleteButtons.forEach(button => {
        button.addEventListener('click', function (event) {
            event.preventDefault();
            const caseId = this.getAttribute('data-id');
            Swal.fire({
                title: "Are you sure?",
                text: "You won't be able to revert this!",
                icon: "warning",
                showCancelButton: true,
                confirmButtonColor: "#3085d6",
                cancelButtonColor: "#d33",
                confirmButtonText: "Yes, delete it!"
            }).then((result) => {
                if (result.isConfirmed) {
                    fetch(`/DeleteCaseRecord/${caseId}/`, {
                        method: 'DELETE',
                        headers: {
                            'X-CSRFToken': getCookie('csrftoken'),
                            'Content-Type': 'application/json'
                        }
                    }).then(response => {
                        if (response.ok) {
                            Swal.fire({
                                title: "Deleted!",
                                text: "The record has been deleted.",
                                icon: "success"
                            }).then(() => {
                                location.reload();
                            });
                        } else {
                            Swal.fire({
                                title: "Error!",
                                text: "An error occurred while deleting the record.",
                                icon: "error"
                            });
                        }
                    });
                }
            });
        });
    });

    // Handle search form validation and submission
    const searchInput = document.getElementById('search');
    const searchForm = document.querySelector('.search-container form');
    searchForm.addEventListener('submit', function (event) {
        const inputValue = searchInput.value.trim();
        if (!inputValue) {
            event.preventDefault();
            Swal.fire({
                title: "Error!",
                text: "Student ID must be provided.",
                icon: "error"
            });
        } else if (!/^\d+$/.test(inputValue)) {
            event.preventDefault();
            Swal.fire({
                title: "Error!",
                text: "Student ID must be a number.",
                icon: "error"
            });
        }
    });
});

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}