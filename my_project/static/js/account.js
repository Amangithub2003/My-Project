document.addEventListener('DOMContentLoaded', function() {
    const accountBtn = document.getElementById('accountBtn');
    const accountTab = document.getElementById('accountTab');

    // Event listener for "My Account" button
    accountBtn.addEventListener('click', function() {
        accountTab.classList.toggle('active');  // Toggle the active class to slide the tab
    });
});
