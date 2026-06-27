let lastScroll = 0;

window.addEventListener("scroll", () => {

    const navbar = document.querySelector(".navbar");

    const currentScroll = window.pageYOffset;

    if(currentScroll > lastScroll && currentScroll > 80){

        navbar.classList.add("hide-navbar");

    }else{

        navbar.classList.remove("hide-navbar");

    }

    lastScroll = currentScroll;
});