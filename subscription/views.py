from django.shortcuts import render, redirect, reverse
from django.conf import settings
from .models import Snack
from .forms import SnackForm
import stripe


def subscribe(request):
    """ A view to choose how many snacks to buy """

    profile = ""

    context = {
        'profile': profile,
    }

    return render(request, "subscription/subscribe.html", context)


def buy_snack(request):
    """ A view to confirm snack donation"""
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    profile = ""

    stripe.api_key = stripe_secret_key
    # intent = stripe.PaymentIntent.create(
    #     amount="200",
    #     currency=settings.STRIPE_CURRENCY,
    # )

    snack_form = SnackForm()

    context = {
        'profile': profile,
        'snack_form': snack_form,
        'stripe_public_key': stripe_public_key,
        # 'client_secret': intent.client_secret,
    }

    return render(request, "subscription/buy_snack.html", context)
