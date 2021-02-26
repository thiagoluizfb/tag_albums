var stripe_public_key = $('#id_stripe_public_key').text().slice(1, -1);
var client_secret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripe_public_key);
var elements = stripe.elements();
var style = {
    base: {
        padding: '0',
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
    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            cardNumberElement: cardNumberElement,
            cardExpiryElement: cardExpiryElement,
            cardCvcElement: cardCvcElement,
        }
    }).then(function(result) {
        if (result.error) {
            var errorDiv = document.getElementById('card-errors');
            // var html = `
            //     <span class="icon" role="alert">
            //     <i class="fas fa-times"></i>
            //     </span>
            //     <span>${result.error.message}</span>`;
            $(errorDiv).html(html);
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
});