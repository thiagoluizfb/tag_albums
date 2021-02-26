var stripePublicKey  = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripePublicKey );
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
    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: cardNumberElement
        }
    }).then(function(result) {
        if (result.error) {
            var errorDiv = document.getElementById('card-errors');
            var html = `
                <span class="icon" role="alert">
                <i class="fas fa-times"></i>
                </span>
                <span>Something went wrong, please try again</span>`;
            $(errorDiv  ).html(html);
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