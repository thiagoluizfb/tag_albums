$(function () {
  $('[data-toggle="tooltip"]').tooltip();
})

$(document).ready(function(){
    if ($("#tier").html() == "True"){
       $("#tier").siblings().css("color", "#804800");
       $(".tier").css("color", "#804800");
    }

    setInterval(function(){
        $("#add-popup").removeClass("hidden");;
    }, 15000);
})

function showClose(btn){
    $(btn).children().last().removeClass("hidden");
    console.log($(btn).children().last())
    return;
}

function hideClose(btn){
    $(btn).children().last().addClass("hidden");
    return;
}

function closeAdd(){
    $("#add-popup").addClass("hidden");
    return;
}