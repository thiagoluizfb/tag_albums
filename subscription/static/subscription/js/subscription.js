$(".snack-choice").on("click", function(){
    qty = $(this).html();
    price = $("#price").html();
    total = qty*price;
    $(".snack-choice-input").val(qty);
    $(".snack-choice-input").html(qty);
    $("#snack-total").html(`Total: US$ ${total.toFixed(2)}`);
})

$(".snack-choice-input").on("change", function(){
    qty = $(this).val();
    price = $("#price").html();
    total = qty*price;
    $("#snack-total").html(`Total: US$ ${total.toFixed(2)}`);
})