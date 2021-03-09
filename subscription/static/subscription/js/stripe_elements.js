var stripePublicKey  = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
var qty = $('#id_qty').text();
var total = $('#id_total').text();
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();
var style = {
    base: {
        color: '#bebebe',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '14px',
        '::placeholder': {
            color: '#bebebe'
        },
        ':-webkit-autofill': {
        color: '#bebebe',
      }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};

var cardNumberElement = elements.create('cardNumber', {style: style});
var cardExpiryElement = elements.create('cardExpiry', {style: style});
var cardCvcElement = elements.create('cardCvc', {style: style});

cardNumberElement.mount('#card-number-element');
cardExpiryElement.mount('#card-expiry-element');
cardCvcElement.mount('#card-cvc-element');

// Form submit
var form = document.getElementById('payment-form');

form.addEventListener('submit', function(ev) {
    ev.preventDefault();
    cardNumberElement.update({ 'disabled': true});
    cardExpiryElement.update({ 'disabled': true});
    cardCvcElement.update({ 'disabled': true});
    $('#submit-button').attr('disabled', true);
    $('#payment-form').fadeToggle(100);
    $('#loading-overlay').fadeToggle(100);

    // From using {% csrf_token %} in the form
    var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
    var postData = {
        'csrfmiddlewaretoken': csrfToken,
        'client_secret': clientSecret,
        'qty': qty,
        'total': total,
    };
    var url = '/buy/cache_buy_snacks/';

    $.post(url, postData).done(function () {
        stripe.confirmCardPayment(clientSecret, {
            payment_method: {
                card: cardNumberElement,
                billing_details: {
                    name: $.trim(form.f_name.value),
                    email: $.trim(form.email.value),
                    address:{
                        line1: $.trim(form.street_address1.value),
                        line2: $.trim(form.street_address2.value),
                        city: $.trim(form.town_or_city.value),
                        country: $.trim(form.country.value),
                        state: $.trim(form.county.value),
                    }
                },
            }
        }).then(function(result) {
            if (result.error) {
                var errorDiv = document.getElementById('card-errors');
                var html = `
                    <span class="icon" role="alert">
                    <i class="fas fa-times"></i>
                    </span>
                    <span>Something went wrong, please try again</span>`;
                $(errorDiv).html(html);
                $('#payment-form').fadeToggle(100);
                $('#loading-overlay').fadeToggle(100);
                cardNumberElement.update({ 'disabled': false});
                cardExpiryElement.update({ 'disabled': false});
                cardCvcElement.update({ 'disabled': false});
                $('#submit-button').attr('disabled', false);
            } else {
                if (result.paymentIntent.status === 'succeeded') {
                    form.submit();
                }
            }
        });
        }).fail(function () {
            location.reload();
            var errorDiv = document.getElementById('card-errors');
            var html = `
                <span class="icon" role="alert">
                <i class="fas fa-sad-cry"></i>
                </span>
                <span>'Sorry, your payment cannot be \
                processed right now. No snacks were bought. Please try again later.'</span>`;
            $(errorDiv).html(html);
        });
});