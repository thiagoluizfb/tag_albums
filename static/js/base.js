var images = [];
var outputs = [];
var output = 0;

$(function () {
  $('[data-toggle="tooltip"]').tooltip();
})

var loadFile = function(event) {
    $(".upload-photo-btn").html("Add more");
    $(".image-container").css("display", "none");
    $(".addtags-wrapper").css("display", "block");
    var numFiles = $("#upload-photo")[0].files.length;
    for (i = 0; i < numFiles; i++) {
        imageName = event.target.files[i].name;
        if (images.indexOf(imageName)<0){
            images.push(imageName);
            outputs.push(output);
            console.log(images);
            console.log(outputs);
            idName = `output${output}`;
            $("#frame").append(`
            <div class="col-12 col-md-6 col-lg-3 text-center">
                <div class="frame-wrapper position-relative">
                    <img id="${idName}" class="upload-thumbnail" onmouseenter="showDelete(this)" onmouseleave="hideDelete(this)"/>
                    <span class="displaynone btn delete-thumbnail">
                        <strong>
                            <i class="far fa-times-circle" onclick="deleteImg(this)" data-toggle="tooltip" data-placement="top" title="Remove this file"></i>
                        </strong>
                    </span>
                </div>
                <div class="text-left position-relative">
                    <input type="text" class="tag-slot" placeholder="@tag this file only" onclick="addSymbol(this)">
                    <div class="tag-all-slot col-12"></div>
                </div>
            </div>`);
            var image = document.getElementById(idName);
            image.src = URL.createObjectURL(event.target.files[i]);
            output++;
        };
    };
    $("#upload-photo").val('');
}

function showDelete(btn){
    $(btn).siblings().removeClass("displaynone");
}

function hideDelete(btn){
    $(btn).siblings().addClass("displaynone");
}

function deleteImg(btn){
    image = $(btn).parent().parent().siblings().attr("id");
    imageId = parseInt(image.slice(6,10));
    index = outputs.indexOf(imageId);
    console.log("Output Index:" + index);
    imageName = images[index];
    console.log("Image name:" + imageName);
    images.splice(index,1);
    outputs.splice(index,1);
    console.log("Images: " + images);
    console.log("Outputs: " + outputs)
    $(btn).parent().parent().parent().parent().remove();
}

function addtags() {
    allTags = $("#tag-all-files").val();
    $("#tag-all-files").val(allTags);
    $(".tag-all-slot").html(`<strong>${allTags}</strong>`);
    $("#tag-all-files-btn").html("Update shared tags");
};

function addSymbol(input){
    console.log($(input).val()+"@");
    text = $(input).val();
    lastChar = text.slice(-1);
    console.log(lastChar);
    if(lastChar == "@"){
        $(input).val(text);
    }else{
        $(input).val(`${text}@`);
    };
}