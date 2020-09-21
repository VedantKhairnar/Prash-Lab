let x = document.getElementsByClassName('card_services');
let y = document.getElementsByClassName('adarsh');
let yx = document.getElementsByClassName('raturi');

function service_on_hover(i) {
    y[i].style.display = "inline-block";
    yx[i].style.display = "inline-block";
    y[i].style.width = "35%";
    yx[i].style.width = "60%";
    y[i].style.height = "100%";
    yx[i].style.height = "100%";
}

function service_on_mouseout(i2) {
    y[i2].style.display = "block";
    yx[i2].style.display = "block";
    y[i2].style.width = "100%";
    yx[i2].style.width = "100%";
    y[i2].style.height = "50%";
    yx[i2].style.height = "50%";
}
