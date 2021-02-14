var files = []
var images = [];
var outputs = [];
var tags = [[],[]];
var allTags = null;
var output = 0;

$(function () {
  $('[data-toggle="tooltip"]').tooltip();
})

$('.carousel').carousel()

var loadFile = function(event) {
    $(".upload-photo-btn").html("Add more");
    $(".image-container").css("display", "none");
    $(".tag-all-slot").css("display", "block");
    var numFiles = $("#upload-photo")[0].files.length;
    for (i = 0; i < numFiles; i++) {
        imageName = event.target.files[i].name;
        if (images.indexOf(imageName)<0){
            files.push(event.target.files[i]);
            images.push(imageName);
            outputs.push(output);
            tags[0].push(`output${output}`);
            tags[1].push("@");
            idName = `output${output}`;
            $("#frame").append(`
            <div id="${idName}-container" class="col-12 col-md-6 col-lg-3 text-center">
                <div class="position-relative frame-wrapper">
                    <img id="${idName}" class="thumbnail" onmouseenter="showDelete(this)" onmouseleave="hideDelete(this)"/>
                    <span class="displaynone btn delete-thumbnail">
                        <strong>
                            <i id="${idName}-delete-img" class="far fa-times-circle" onclick="deleteImg(this)" data-toggle="tooltip" data-placement="top" title="Remove this file"></i>
                        </strong>
                    </span>
                </div>
                <div>
                    <div id="${idName}-tag-slot" class="tag-slot text-left" onclick="addSymbol(this)" data-toggle="modal" data-target="#edit-tag-modal">@tag this only</div>
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
    image = $(btn).attr("id").split("-");
    imageOutput = image[0];
    imageId = parseInt(imageOutput.slice(6,10));
    index = outputs.indexOf(imageId);
    imageName = images[index];
    images.splice(index,1);
    outputs.splice(index,1);
    tags[0].splice(index,1);
    tags[1].splice(index,1);
    $(`#${imageOutput}-container`).remove();
}


function addSymbol(input){
    $(".modal-header").empty();
    $(input).css("font-size", "10px");
    text = $(input).html();
    if (text == "@tag this only" || text == "@tag all"){
        text = "";
    }
    lastChar = text.slice(-1);
    image = $(input).attr("id").split("-");
    imageOutput = image[0];
    src = $(`#${imageOutput}`).attr("src");
    if(src){
        $(".modal-header").append(`
            <img class="thumbnail-edit" src="${src}"/>
        `)
    }else{
        $(".modal-header").append(`
            <h3>Tag all</h3>
        `)
        imageOutput = "";
    }
    if(lastChar == "@"){
        //$(input).val(text);
        $("#edit-file-tag").val(text);
        $("#output-file").html(imageOutput);
    }else{
        //$(input).val(`${text}@`);
        $("#edit-file-tag").val(`${text}@`);
        $("#output-file").html(imageOutput);
    };
    window.setTimeout (function(){ 
       $("#edit-file-tag").focus();
    },100);
}

function editTagFile(){
    $(".modal-header").empty();
    editedTag = $(".modal-body").children().first().val();
    image = $("#output-file").html();
    imageId = parseInt(image.slice(6,10));
    if (image){
        $(`#${image}-tag-slot`).html(editedTag);
        $("#output-file").empty();
        tags[1][tags[0].indexOf(image)] = editedTag;
    }else{
        $("#tag-all-slot").html(editedTag);
        allTags = editedTag;
    }
}