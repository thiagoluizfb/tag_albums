from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import Snack, Tiers
from profiles.models import UserProfile
from django.conf import settings

import time


class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """
        intent = event.data.object
        pid = intent.id

        billing_details = intent.charges.data[0].billing_details
        total = round(intent.charges.data[0].amount / 100, 2)
        snack_data = intent.metadata.snack_data

        snack_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                snack_order = Snack.objects.get(
                    f_name__iexact=billing_details.name,
                    email__iexact=billing_details.email,
                    country__iexact=billing_details.address.country,
                    town_or_city__iexact=billing_details.address.city,
                    street_address1__iexact=billing_details.address.line1,
                    street_address2__iexact=billing_details.address.line2,
                    county__iexact=billing_details.address.state,
                    total=total,
                    snack_data=snack_data,
                    stripe_pid=pid,
                )
                snack_exists = True
                break
            except Snack.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if snack_exists:
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: \
                    Verified order already in database',
                status=200)
        else:
            snack_order = None
            try:
                snack_order = Snack.objects.create(
                    f_name=billing_details.name,
                    email=billing_details.email,
                    country=billing_details.address.country,
                    town_or_city=billing_details.address.city,
                    street_address1=billing_details.address.line1,
                    street_address2=billing_details.address.line2,
                    county=billing_details.address.state,
                    total=total,
                    snack_data=snack_data,
                    stripe_pid=pid,
                )
                email = billing_details.email
                if User.objects.filter(email=email):
                    profile = User.objects.get(email=email)
                    user = Tiers.objects.get(
                        user=UserProfile.objects.get(user=profile))
                    setattr(user, 'tier', True)
                    user.save()
            except Exception as e:
                if snack_order:
                    snack_order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)
        return HttpResponse(
            content=f'Webhook received: {event["type"]} | \
                SUCCESS: Created order in webhook',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
