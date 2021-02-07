  var images = [];
  var firstTag;

function addtags() {
    allTags = $("#tag-all-files").val();
    console.log(allTags[0]);
    if (allTags[0] != "@"){
        if (allTags == ""){
            allTags = "";
        }else{
            allTags = `@${allTags}`;
        };
    }
    $("#tag-all-files").val(allTags);
    $(".tag-all-slot").html(allTags);
    $("#tag-all-files-btn").html("Update shared tags");
};

  var loadFile = function(event) {
    $(".upload-photo-btn").html("Add more");
    $(".image-container").css("display", "none");
    $(".addtags-wrapper").css("display", "block");
    var numFiles = $("#upload-photo")[0].files.length;
    for (i = 0; i < numFiles; i++) {
      imageName = event.target.files[i].name;
      console.log(event.target.files[i]);
      //console.log(images.indexOf(image_name));
      if (images.indexOf(imageName)<0){
        images.push(imageName);
        var count = $("#frame").children().length/2;
        imageName = event.target.files[i].name;
        //date = event.target.files[i].lastModifiedDate;
        //var n = date.toLocaleDateString();
        //var x = n.split("/");
        //console.log(x);
        //console.log(n);
        idName = `output${count}`;
        $("#frame").append(`
        <div class="col-12 col-md-6 col-lg-3 text-center">
        	<div class="frame-wrapper">
            	<img id="${idName}" class="upload-thumbnail"/>
            </div>
        	<div class="text-left">
            	<input type="text" class="tag-slot" placeholder="@tag this file">
                <div class="tag-all-slot"></div>
            </div>
        </div>`);
        //id_name = `output`+count;
        var image = document.getElementById(idName);
        image.src = URL.createObjectURL(event.target.files[i]);
        var count = $("#frame").children().length/2;
      }
    }
  };
