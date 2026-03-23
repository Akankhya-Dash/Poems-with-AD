// Smooth scroll
function scrollToSection(id) {
    document.getElementById(id).scrollIntoView({
        behavior: "smooth"
    });
}

// Dark mode
function toggleTheme() {
    const html = document.documentElement;
    const current = html.getAttribute("data-theme");
    html.setAttribute("data-theme", current === "dark" ? "light" : "dark");
}

// Cursor hide
let timeout;
document.addEventListener("mousemove", () => {
    document.body.style.cursor = "default";
    clearTimeout(timeout);
    timeout = setTimeout(() => {
        document.body.style.cursor = "none";
    }, 2000);
});