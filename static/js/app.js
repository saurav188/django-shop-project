
const ham=document.querySelector('.bars');
const links=document.querySelector('.links');
const link=document.getElementsByClassName('link');
const nav=document.querySelector('.nav');
// click to get big nav
ham.addEventListener('click',function(){
    nav.classList.toggle('ham-nav');
})
