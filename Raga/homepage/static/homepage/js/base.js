function activateNavElement(NavElement){
    //Deactivate All the Elements 
    navbar = document.querySelector(".navigation");
    nav_els = navbar.querySelectorAll(".navEl");
    nav_els.forEach((nav_el)=>{
        nav_el.classList.remove("active");
    });
    // Activate the Element Selected
    NavElement.classList.add("active");
}
function performNavActions(){
    navbar = document.querySelector(".navigation");
    nav_els = navbar.querySelectorAll(".navEl");
     nav_els.forEach((nav_el)=>{
        nav_el.addEventListener("click", ()=>{
            activateNavElement(nav_el);
        });
    });
}

//All Start Homepage Function Calls Here 
performNavActions()