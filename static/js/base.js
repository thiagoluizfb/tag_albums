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
                    <input type="text" class="tag-slot" placeholder="@tag this file only" onclick="addSymbol(this)" data-toggle="modal" data-target="#edit-file-tag-modal">
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
    imageName = images[index];
    images.splice(index,1);
    outputs.splice(index,1);
    $(btn).parent().parent().parent().parent().remove();
}

function addtags() {
    allTags = $("#tag-all-files").val();
    $("#tag-all-files").val(allTags);
    $(".tag-all-slot").html(`<strong>${allTags}</strong>`);
    $("#tag-all-files-btn").html("Update shared tags");
};

function addSymbol(input){
    text = $(input).val();
    lastChar = text.slice(-1);
    image = $(input).parent().siblings().children().first().attr("id");
    if(lastChar == "@"){
        //$(input).val(text);
        $(".modal-body").children().first().val(text);
        $("#output-file").html(image);
        
    }else{
        //$(input).val(`${text}@`);
        $(".modal-body").children().first().val(`${text}@`);
        $("#output-file").html(image);
    };
}

function editTagFile(){
    editedTag = $(".modal-body").children().first().val();
    image = $("#output-file").html();
    $(`#${image}`).parent().siblings().children().first().val(editedTag);
}