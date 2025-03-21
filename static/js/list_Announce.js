document.addEventListener("DOMContentLoaded", function() {
    const searchInput = document.getElementById("searchInput");
    const categoryFilter = document.getElementById("categoryFilter");
    const annonceCards = document.querySelectorAll(".annonce-card");

    if (searchInput) {
        searchInput.addEventListener("keyup", function() {
            let filter = searchInput.value.toLowerCase();
            annonceCards.forEach(card => {
                let title = card.querySelector(".card-title").innerText.toLowerCase();
                card.style.display = title.includes(filter) ? "block" : "none";
            });
        });
    }

    if (categoryFilter) {
        categoryFilter.addEventListener("change", function() {
            let selectedCategory = categoryFilter.value;
            annonceCards.forEach(card => {
                card.style.display = (selectedCategory === "" || card.getAttribute("data-category") === selectedCategory) ? "block" : "none";
            });
        });
    }

    // Add hover effect on annonce cards
    annonceCards.forEach(card => {
        card.addEventListener("mouseenter", () => {
            card.classList.add("shadow-lg");
            card.style.transform = "scale(1.05)";
            card.style.transition = "transform 0.3s ease-in-out";
        });

        card.addEventListener("mouseleave", () => {
            card.classList.remove("shadow-lg");
            card.style.transform = "scale(1)";
        });
    });
});
