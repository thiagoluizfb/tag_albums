var indexTag = 1
var keyCode = 0
var images = [];

$(function () {
  $('[data-toggle="tooltip"]').tooltip();
})

$('.carousel').carousel()

function loadFile(event) {
    $(".image-container").css("display", "none");
    imageName = event.target.files[0].name;
    images.push(imageName);
    $(".frame-wrapper").append(`
        <img id="img-upload" class="thumbnail" onmouseenter="showDelete(this)" onmouseleave="hideDelete(this)"/>
        <span class="btn delete-thumbnail">
            <strong>
                <i class="far fa-times-circle" onclick="deleteImg(this)" data-toggle="tooltip" data-placement="top" title="Remove this file"></i>
            </strong>
        </span>`);
    image = document.getElementById("img-upload");
    image.src = URL.createObjectURL(event.target.files[0]);
}

function showDelete(btn){
    $(btn).siblings().removeClass("hidden");
    return;
}

function hideDelete(btn){
    $(btn).siblings().addClass("hidden");
    return;
}

function deleteImg(btn){
    $('.thumbnail').remove();
    $('.delete-thumbnail').remove();
    $(".image-container").css("display", "block");
    return;
}

$(document).ready(function() {
    $('#logo-text').focus();
});

function logoText() {
    keyCode ++;
    if (keyCode > 2){
        $('#logo-text').focus();
        $(".logo-anime").css("font-size", "50px")
        text = $("#logo-text").val();
        if (event.keyCode == 13){
            if (indexTag == 4){indexTag = 1}
            $(`.index-tag-${indexTag}`).html(`#${text}`);
            $(".logo-anime").html(`@`);
            indexTag ++;
        }
        $(".logo-anime").html(`@${text}`);
    }
};