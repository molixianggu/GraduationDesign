
$(function(){
    $("#menu").menu();
    //$(".rb1").button();
    trend();
});

function trend(){
    if ($(window).width() < 1000){
        $("#trends").hide("slow");
        $("#selfinf").css("width", "100%");
    }
    else{
        $("#trends").show("slow");
        $("#selfinf").css("width", "65%");
    }
}

window.onresize = function () {
    trend();
}
