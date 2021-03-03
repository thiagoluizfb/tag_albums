import datetime, os
from django.shortcuts import render, redirect, reverse, get_object_or_404
from photos.views import Photos, Tags
from subscription.models import Snack, Tiers
from profiles.models import UserProfile
from django.contrib.auth.models import User


def index(request):
    """ A view to delete photos uploaded w/o login and return the index page"""

    if Photos.objects.all():
        profile = UserProfile.objects.get(id=6)
        for photos in profile.photos.all():
            photos.delete()

    tags = Tags.objects.all()
    if tags:
        for tag in tags:
            if not tag.tag_photos.all():
                todelete = Tags.objects.filter(tag_name=tag)
                todelete.delete()

    if request.user.is_authenticated:
        upload = 'upload'
        profile = UserProfile.objects.get(user=request.user)
        email = request.user.email
        if Snack.objects.filter(email=email):
            user = Tiers.objects.get(user=profile)
            setattr(user, 'tier', True)
            user.save()
            tier = user.tier
        else:
            tier = False
    else:
        profile = ""
        tier = False
        upload = 'upload_preview'

    context = {
        'profile': profile,
        'tier': tier,
        'upload': upload,
    }

    return render(request, "home/index.html", context)


def upload(request):
    """ A view to return the upload page"""

    # if request.method == 'POST':

    #     images = request.FILES.get('upload-photo')
    #     alltags = request.POST.get('edit-file-tag').split('@')
    #     if request.user.is_authenticated:
    #         tosave = Photos(
    #             owner=UserProfile.objects.get(user=request.user),
    #             upload_date=datetime.datetime.now(),
    #             image=images,
    #         )
    #     else:
    #         tosave = Photos(
    #             upload_date=datetime.datetime.now(),
    #             image=images,
    #         )
    #     tosave.save()
    #     for tag in alltags:
    #         if tag != "":
    #             if Tags.objects.filter(tag_name=tag):
    #                 savetag = Tags.objects.get(tag_name=tag)
    #                 savetag.tag_photos.add(tosave)
    #             else:
    #                 savetag = Tags(tag_name=tag)
    #                 savetag.save()
    #                 savetag.tag_photos.add(tosave)

    #     return redirect(reverse('all_photos'))

    return redirect(reverse('all_photos'))
