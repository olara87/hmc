//navbar open and close
const menuButtons = document.querySelectorAll(".mobile-menu");
const nav = document.querySelector("nav");

menuButtons.forEach((menuButton) => {
    menuButton.addEventListener("click", () => {
        nav.classList.toggle("mobile-btn");
    });
});

//===============================================
//closing nav after about link clicked
const aboutBtn = document.querySelector("#about-section");

aboutBtn.addEventListener("click", () => {
    nav.classList.toggle("mobile-btn");
});

//===============================================
//This block of code works fine but it uses too many lines of code. Replaced by the code above
// const mobileBtn = document.getElementById("mobile-cta");
// const mobileBtnExit = document.getElementById("mobile-exit");

// mobileBtn.addEventListener("click", () => {
//     // nav.classList.add("mobile-btn");
//     nav.classList.toggle('mobile-btn')
// });
// mobileBtnExit.addEventListener("click", () => {
//     nav.classList.toggle('mobile-btn')
//     // nav.classList.remove("mobile-btn");
// });
//===============================================

//Modal
const openButtons = document.querySelectorAll(".order-cta");
const closeButton = document.querySelector("[data-close-modal]");
const modal = document.querySelector("[data-modal]");
//===============================================
//This block of code works fine. it does not work with the function "getElementsByClassName()".
openButtons.forEach((openButton) => {
    openButton.addEventListener("click", (e) => {
        console.log("inside openButton func");
        modal.showModal({ backdrop: "static" });
        if (nav.className === "mobile-btn") nav.classList.toggle("mobile-btn");
        e.preventDefault();
    });
});

closeButton.addEventListener("click", () => {
    console.log("inside closeButton func");
    modal.close();
});

//Removing P tag added by django
//===============================================
const main = document.querySelector("main");
const djMessage = document.querySelector(".dj-message");

// console.log(djMessage | null);

if (djMessage) {
    setTimeout(() => {
        djMessage.parentNode.removeChild(djMessage);
        console.log("inside settimeout");
    }, 5000);
}

//===============================================

//===============================================
//This block of code works fine but uses a for loop.
// for (const openButton of openButtons) {
//     openButton.addEventListener("click", () => {
//         console.log("inside openButton func");
//         modal.showModal();
//     });
// }
//===============================================

// moves to top of the page on refresh page.
history.scrollRestoration = "manual"
window.onbeforeunload = function () {
    window.scrollTo(0, 0);
};
