document.addEventListener("DOMContentLoaded", function() {
    let searchBox = document.getElementById("searchBox");
    let rows = document.querySelectorAll("table tr");

    searchBox.addEventListener("keyup", function() {
        let query = searchBox.value.toLowerCase();

        rows.forEach((row, index) => {
            if (index === 0) return;  // Skip table header
            let title = row.cells[0].textContent.toLowerCase();
            row.style.display = title.includes(query) ? "" : "none";
        });
    });
});
