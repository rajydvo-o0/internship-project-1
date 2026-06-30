// Navbar Hide & Show

let lastScroll = 0;

window.addEventListener("scroll", () => {
    const navbar = document.querySelector(".navbar");
    const categoryBar = document.querySelector(".category-bar");
    if (!navbar) return;
    let currentScroll = window.pageYOffset;
    if (currentScroll > lastScroll) {
        navbar.classList.add("hide-navbar");
        if (categoryBar) {
            categoryBar.style.top = "0px";
        }}
            
        else {
            navbar.classList.remove("hide-navbar");
            if (categoryBar) {
                categoryBar.style.top = "85px";
            }
        }
    lastScroll = currentScroll;
});


// Toast Notification
function showToast() {
    let toast = document.getElementById("toast");
    if (!toast) return;
    toast.classList.add("show");
    setTimeout(() => {
        toast.classList.remove("show");
    }, 3000);
}


// Login Popup
function closePopup() {
    let popup = document.getElementById("loginPopup");
    if (popup) {
        popup.style.display = "none";
    }
}


// Cart Remove Confirmation
function confirmRemove() {
    return confirm("Are you sure you want to remove this product from the cart?");
}
