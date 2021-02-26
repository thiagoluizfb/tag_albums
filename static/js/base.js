$(function () {
  $('[data-toggle="tooltip"]').tooltip();
})

$(document).ready(function(){
    if ($("#tier").html() == "True"){
       $("#tier").siblings().css("color", "#804800");
       $(".tier").css("color", "#804800");
    }
})