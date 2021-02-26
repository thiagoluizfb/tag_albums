from django.shortcuts import render, get_object_or_404
from .models import UserProfile
from .forms import UserProfileForm
from subscription.models import Tiers


def profile(request):
    """ A view to view user profile """

    profile = get_object_or_404(UserProfile, user=request.user)

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        status = Tiers.objects.get(user=profile)
        tier = status.tier
    else:
        tier = False

    if request.method == 'POST':
        name = request.POST['display_name']
        form = UserProfileForm(request.POST, instance=profile)
        if name != profile.display_name:
            if form.is_valid():
                if not UserProfile.objects.filter(display_name=name):
                    form.save()
                    message = False
                else:
                    message = "This nickname is already in use, \
                        please chose a different one"
        else:
            message = False
    else:
        form = UserProfileForm(instance=profile)
        message = False

    context = {
        'message': message,
        'tier': tier,
        'profile': profile,
        'form': form,
    }

    return render(request, "profiles/profile.html", context)
