from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from profiles.models import UserProfile
from django.conf import settings

from .models import Tiers
from .forms import SnackForm

import stripe


def buy(request):
    """ A view to choose how many snacks to buy """

    price = settings.SNACK_PRICE
    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        status = Tiers.objects.get(user=profile)
        tier = status.tier
    else:
        tier = False
        profile = UserProfile.objects.get(id=6)

    if request.method == "POST":
        qty = request.POST.get('qty')
        return redirect('buy_snack', qty)

    context = {
        'tier': tier,
        'profile': profile,
        'price': price,
    }

    return render(request, "subscription/buy.html", context)


def buy_snack(request, qty):
    """ A view to confirm snack donation"""
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    price = settings.SNACK_PRICE
    total = qty*price

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        status = Tiers.objects.get(user=profile)
        tier = status.tier
    else:
        tier = False
        profile = UserProfile.objects.get(id=6)

    if request.method == 'POST':

        email = request.POST['email']
        form_data = {
            'f_name': request.POST['f_name'],
            'l_name': request.POST['l_name'],
            'email': email,
            'country': request.POST['country'],
            'county': request.POST['county'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'postcode': request.POST['postcode'],
            'snack_qty': qty,
            'total': total,
        }
        snack_form = SnackForm(form_data)

        if snack_form.is_valid():
            setattr(snack_form, 'total', total)
            snack_form.save()
            if User.objects.filter(email=email):
                profile = User.objects.get(email=email)
                user = Tiers.objects.get(
                    user=UserProfile.objects.get(user=profile))
                setattr(user, 'tier', True)
                user.save()

            return redirect(reverse('success'))

    else:
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=qty*price*100,
            currency=settings.STRIPE_CURRENCY,
        )
        snack_form = SnackForm()

    context = {
        'tier': tier,
        'profile': profile,
        'snack_form': snack_form,
        'stripe_public_key': stripe_public_key,
        'qty': qty,
        'total': total,
        'client_secret': intent.client_secret,
    }

    return render(request, "subscription/buy_snack.html", context)


def success(request):

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        status = Tiers.objects.get(user=profile)
        tier = status.tier
    else:
        tier = False
        profile = UserProfile.objects.get(id=6)

    context = {
        'tier': tier,
        'profile': profile,
    }

    return render(request, "subscription/buy_snack_success.html", context)
