window.addEventListener("scroll", function() {
    if (window.scrollY >= 250) {
        document.getElementById('page_nav').classList.add("show");
        document.getElementById('page_nav').classList.remove("hide");
    } else {
        document.getElementById('page_nav').classList.remove("show");
        document.getElementById('page_nav').classList.add("hide");
    }
});

document.getElementById('op1').addEventListener("mousedown", function(){
    document.getElementById('page_view1').style.display = "block";
    document.getElementById('page_view2').style.display = "none";
    document.getElementById('page_view3').style.display = "none";
    document.getElementById('op1').classList.add('navselected');
    document.getElementById('op2').classList.remove('navselected');
    document.getElementById('op3').classList.remove('navselected');
    document.getElementById('page').innerHTML = variableLongText;
    document.getElementById('page').scrollTop = 0;
})

document.getElementById('op2').addEventListener("mousedown", function(){
    document.getElementById('page_view1').style.display = "none";
    document.getElementById('page_view2').style.display = "block";
    document.getElementById('page_view3').style.display = "none";
    document.getElementById('op1').classList.remove('navselected');
    document.getElementById('op2').classList.add('navselected');
    document.getElementById('op3').classList.remove('navselected');
    document.getElementById('page').innerHTML = variableLongText;
    document.getElementById('page').scrollTop = 0;
})

document.getElementById('op3').addEventListener("mousedown", function(){
    document.getElementById('page_view1').style.display = "none";
    document.getElementById('page_view2').style.display = "none";
    document.getElementById('page_view3').style.display = "block";
    document.getElementById('op1').classList.remove('navselected');
    document.getElementById('op2').classList.remove('navselected');
    document.getElementById('op3').classList.add('navselected');
    document.getElementById('page').innerHTML = variableLongText;
    document.getElementById('page').scrollTop = 0;
})

