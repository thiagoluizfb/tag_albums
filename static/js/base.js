var indexTag = 1
var keyCode = 0
var uploadFiles = []
var images = [];
var allTags = "@";
var output = 0;
var uploaded = [];

$(function () {
  $('[data-toggle="tooltip"]').tooltip();
})

$('.carousel').carousel()

function loadFile(event) {
    $(".image-container").css("display", "none");
    imageName = event.target.files[0].name;
    uploadFiles.push(event.target.files[0]);
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
    $("#edit-file-tag").focus();
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

//credit: https://stackoverflow.com/users/2065039/guruprasad-j-rao
function preventComma() {
    if(event.keyCode === 44 ) {
        alert("comma not allowed");
        event.preventDefault();
    }
};
//at https://stackoverflow.com/questions/32096193/how-to-prevent-default-on-keypress-for-certain-event-but-then-bring-back-the-def

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