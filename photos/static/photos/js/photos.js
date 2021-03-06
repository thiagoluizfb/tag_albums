var images = [];

$('.carousel').carousel();

function loadFile(event) {
    $(".image-container").addClass("hidden");
    $(".upload-photo").removeClass("hidden");
    var imageName = event.target.files[0].name;
    images.push(imageName);
    $(".frame-wrapper").html(`
        <img id="img-upload" class="thumbnail" alt="${imageName}"/>`);
    var image = document.getElementById("img-upload");
    image.src = URL.createObjectURL(event.target.files[0]);
    $("#img-src").val(image.src);
    $('#edit-file-tag').select();
}

function showIcon(btn){
    $(btn).siblings().removeClass("hidden");
    return;
}

function hideIcon(btn){
    $(btn).siblings().addClass("hidden");
    return;
}
