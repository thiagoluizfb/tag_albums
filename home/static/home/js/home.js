var indexTag = 1;

$(document).ready(function() {
    $('#logo-text').focus();
});

function logoText() {
    $('#logo-text').focus();
    $(".logo-anime").css("font-size", "50px");
    text = $("#logo-text").val();
    if (event.keyCode == 13){
        if (indexTag == 4){
            indexTag = 1;
        }
        $(`.index-tag-${indexTag}`).html(`#${text}`);
        indexTag ++;
        text = "";
        $('#logo-text').val(text);
        $(".logo-anime").html(`@`);
    }else{
        $(".logo-anime").html(`@${text}`);
    }
}