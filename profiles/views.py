from django.shortcuts import render, get_object_or_404
from .models import UserProfile
from .forms import UserProfileForm


def profile(request):
    """ A view to view user profile """

    profile = get_object_or_404(UserProfile, user=request.user)

    form = UserProfileForm(instance=profile)
    context = {
        'profile': profile,
        'form': form,
    }

    return render(request, "profiles/profile.html", context)
