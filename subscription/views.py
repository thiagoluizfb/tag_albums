from django.shortcuts import render
from django.conf import settings
import stripe


def subscribe(request):
    """ A view to view user profile """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    profile = ""
    # get_object_or_404(UserProfile, user=request.user)

    # if request.method == 'POST':
    #     form = UserProfileForm(request.POST, instance=profile)
    #     if form.is_valid():
    #         form.save()
    # else:
    #     form = UserProfileForm(instance=profile)

    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount="200",
        currency=settings.STRIPE_CURRENCY,
    )

    print(intent)

    context = {
        'profile': profile,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, "subscription/subscribe.html", context)
