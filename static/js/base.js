var images = [];
var outputs = [];
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
            images.push(imageName);
            outputs.push(output);
            idName = `output${output}`;
            $("#frame").append(`
            <div class="col-12 col-md-6 col-lg-3 text-center">
                <div class="position-relative frame-wrapper">
                    <img id="${idName}" class="thumbnail" onmouseenter="showDelete(this)" onmouseleave="hideDelete(this)"/>
                    <span class="displaynone btn delete-thumbnail">
                        <strong>
                            <i class="far fa-times-circle" onclick="deleteImg(this)" data-toggle="tooltip" data-placement="top" title="Remove this file"></i>
                        </strong>
                    </span>
                </div>
                <div onclick="addSymbol(this)" data-toggle="modal" data-target="#edit-tag-modal">
                    <div type="text" class="tag-slot text-left">@tag this only</div>
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


function addSymbol(input){
    $(".modal-header").empty();
    $(input).css("font-size", "10px");
    text = $(input).children().html();
    if (text == "@tag this only" || text == "@tag all"){
        text = "";
    }
    lastChar = text.slice(-1);
    image = $(input).siblings().children().first().attr("id");
    src = $(input).siblings().children().first().attr("src");
    if(src){
        $(".modal-header").append(`
            <img class="thumbnail-edit" src="${src}"/>
        `)
    }else{
        $(".modal-header").append(`
            <h3>Tag all</h3>
        `)
    }
    if(lastChar == "@"){
        //$(input).val(text);
        $("#edit-file-tag").val(text);
        $("#output-file").html(image);
    }else{
        //$(input).val(`${text}@`);
        $("#edit-file-tag").val(`${text}@`);
        $("#output-file").html(image);
    };
    window.setTimeout (function(){ 
       $("#edit-file-tag").focus();
    },100);
}

function editTagFile(){
    $(".modal-header").empty();
    editedTag = $(".modal-body").children().first().val();
    image = $("#output-file").html();
    if (image){
        $(`#${image}`).parent().siblings().children().first().html(editedTag);
        $("#output-file").empty();
    }else{
        $(".tag-all-slot").children().html(editedTag);
    }
}