$('.studentlife-btn').click(function() {
    console.log("clicked");
    $('.studentlife').toggleClass("show"); 
    $('.first').toggleClass("rotate");
});

$('.scholar-btn').click(function() {
    console.log("clicked");
    $('.scholar-show').toggleClass("show2"); 
    $('.side-nav ul .second').toggleClass("rotate");
});

$('.jobplace-btn').click(function() {
    console.log("clicked");
    $('.jobplace-show').toggleClass("show3"); 
    $('.side-nav ul .third').toggleClass("rotate");
});

$('.student_disc-btn').click(function() {
    console.log("clicked");
    $('.student_disc-show').toggleClass("show4"); 
    $('.side-nav ul .fourth').toggleClass("rotate");
});

$('.guide-btn').click(function() {
    $('.guide-show').toggleClass("show5"); 
    $('.side-nav ul .fifth').toggleClass("rotate");
});

$('.alumni-btn').click(function() {
    $('.alumni-show').toggleClass("show6"); 
    $('.side-nav ul .sixth').toggleClass("rotate");
});

$('.community-btn').click(function() {
    $('.community-show').toggleClass("show7"); 
    $('.side-nav ul .seventh').toggleClass("rotate");
});

$('.student_org-btn').click(function() {
    $('.student_org-show').toggleClass("show8"); 
    $('.side-nav ul .eight').toggleClass("rotate");
});

$('.medical-btn').click(function() {
    $('.medical-show').toggleClass("show9"); 
    $('.side-nav ul .ninth').toggleClass("rotate");
});


    // Toggle dropdown on click
    var dropdownLink = document.querySelector('.dropdown-link');
    var dropdown = dropdownLink.closest('.dropdown');
    dropdownLink.addEventListener('click', function(event) {
        event.preventDefault();
        dropdown.classList.toggle('show');
    });

    // Close the dropdown if the user clicks outside of it
    window.onclick = function(event) {
        if (!event.target.matches('.dropdown-link')) {
            var dropdowns = document.getElementsByClassName("dropdown");
            for (var i = 0; i < dropdowns.length; i++) {
                var openDropdown = dropdowns[i];
                if (openDropdown.classList.contains('show')) {
                    openDropdown.classList.remove('show');
                }
            }
        }
    }
