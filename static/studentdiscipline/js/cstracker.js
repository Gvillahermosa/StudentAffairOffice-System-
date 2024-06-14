document.addEventListener('DOMContentLoaded', (event) => {
    const dateInput = document.getElementById('id_date');

    // Retrieve stored values from local storage
    const storedDate = localStorage.getItem('service_date');


    if (storedDate) {
        dateInput.value = storedDate;
    } else {
        const today = new Date();
        const year = today.getFullYear();
        const month = String(today.getMonth() + 1).padStart(2, '0');
        const day = String(today.getDate()).padStart(2, '0');
        dateInput.value = `${year}-${month}-${day}`;
    }

    if (storedTimeIn) {
        dateTimeInput.value = storedTimeIn;
    } else {
        const today = new Date();
        const hours = String(today.getHours()).padStart(2, '0');
        const minutes = String(today.getMinutes()).padStart(2, '0');
        dateTimeInput.value = `${hours}:${minutes}`;
    }

    // Save values to local storage when the user leaves the page
    window.addEventListener('beforeunload', () => {
        localStorage.setItem('service_date', dateInput.value);
        localStorage.setItem('time_in', dateTimeInput.value);
    });

    // Clear local storage when the form is submitted
    document.getElementById('serviceForm').addEventListener('submit', () => {
        localStorage.removeItem('service_date');
        localStorage.removeItem('time_in');
    });

    // Add event listener to time_out input to reset time_in value
    timeOutInput.addEventListener('change', () => {
        if (timeOutInput.value !== "") {
            const today = new Date();
            const hours = String(today.getHours()).padStart(2, '0');
            const minutes = String(today.getMinutes()).padStart(2, '0');
            dateTimeInput.value = `${hours}:${minutes}`;
        }
    });
});

function addRow() {
    var table = document.getElementById("serviceTable").getElementsByTagName('tbody')[0];
    var row = table.insertRow(-1); // Insert row at the end
    var cell1 = row.insertCell(0);
    var cell2 = row.insertCell(1);
    var cell3 = row.insertCell(2);
    var cell4 = row.insertCell(3);
    var cell5 = row.insertCell(4);
    var cell6 = row.insertCell(5);
    cell1.innerHTML = document.getElementById("id_date").value;
    cell2.innerHTML = document.getElementById("id_time_in").value;
    cell3.innerHTML = document.getElementById("id_time_out").value;
    cell4.innerHTML = document.getElementById("id_hours_rendered").value;
    cell5.innerHTML = document.getElementById("id_student_signature").value;
    cell6.innerHTML = document.getElementById("id_remark").value;
    document.getElementById("serviceForm").reset(); // Reset form fields after adding row
}