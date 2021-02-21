var indexTag = 1
var keyCode = 0
var images = [];

$(function () {
  $('[data-toggle="tooltip"]').tooltip();
})

$('.carousel').carousel()

function loadFile(event) {
    $(".image-container").addClass("hidden");
    $(".upload-photo").removeClass("hidden");
    imageName = event.target.files[0].name;
    images.push(imageName);
    $(".frame-wrapper").html(`
        <img id="img-upload" class="thumbnail"/>`);
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
            indexTag ++;
            text = "";
            $('#logo-text').val(text);
            $(".logo-anime").html(`@`);
        }else{
            $(".logo-anime").html(`@${text}`);
        }
    }
};