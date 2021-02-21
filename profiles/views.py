from django.shortcuts import render, redirect, reverse
from .models import UserProfile


def profile(request):
    """ A view to view user profile """

    profile = UserProfile.objects.all()

    context = {
        'profile': profile,
    }

    return render(request, "profiles/profile.html", context)
