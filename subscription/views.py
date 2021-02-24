from django.shortcuts import render, get_object_or_404
from .models import UserProfile


def subscribe(request):
    """ A view to view user profile """

    profile = ""
    # get_object_or_404(UserProfile, user=request.user)

    # if request.method == 'POST':
    #     form = UserProfileForm(request.POST, instance=profile)
    #     if form.is_valid():
    #         form.save()
    # else:
    #     form = UserProfileForm(instance=profile)

    context = {
        'profile': profile,
    }

    return render(request, "subscription/subscribe.html", context)
