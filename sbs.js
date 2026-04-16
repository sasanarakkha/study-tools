/**
 * SBS identity JS
 * Makes the site title in the header a link to the homepage
 * Exact logic from dpd-pali-courses/identity/footnotes.js
 */
document.addEventListener("DOMContentLoaded", function() {
    // Make site title in header a link to the homepage
    // We look for the logo link, which is present in the DOM even if hidden by CSS
    const logoLink = document.querySelector("a.md-header__button.md-logo");
    const titleEllipsis = document.querySelector(".md-header__title .md-ellipsis");
    
    if (titleEllipsis && logoLink) {
        const link = document.createElement("a");
        link.href = logoLink.href;
        link.style.cssText = "color:inherit;text-decoration:none;cursor:pointer;display:flex;align-items:center;height:100%;";
        
        // Match DPD's exact approach: replace titleEllipsis with the link, 
        // then put titleEllipsis inside the link.
        titleEllipsis.parentNode.replaceChild(link, titleEllipsis);
        link.appendChild(titleEllipsis);
    }
});
