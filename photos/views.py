import datetime
from django.shortcuts import render, redirect, reverse
from .models import Photos, Tags
from subscription.models import Tiers
from profiles.models import UserProfile
from django.conf import settings


def all_photos(request):
    """ A view to return the photos page"""

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        status = Tiers.objects.get(user=profile)
        tier = status.tier
    else:
        profile = UserProfile.objects.get(id=6)
        tier = False

    location = settings.MEDIA_URL
    photos = profile.photos.all()
    tags = Tags
    context = {
        'tier': tier,
        'photos': photos,
        'tags': tags,
        'profile': profile,
        'location': location,
    }

    return render(request, 'photos/all_photos.html', context)


def albums(request):
    """ A view to return the albums page"""

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        status = Tiers.objects.get(user=profile)
        tier = status.tier
    else:
        tier = False
        profile = UserProfile.objects.get(id=6)

    location = settings.MEDIA_URL
    photos = profile.photos.all()
    tags = list(Tags.objects.all())
    context = {
        'tier': tier,
        'photos': photos,
        'tags': tags,
        'profile': profile,
        'location': location,
    }

    return render(request, 'photos/albums.html', context)


def tag_album(request, album):
    """ A view to return the photos page"""

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        status = Tiers.objects.get(user=profile)
        tier = status.tier
    else:
        profile = UserProfile.objects.get(id=6)
        tier = False

    location = settings.MEDIA_URL
    photos = profile.photos.all()
    tags = list(Tags.objects.filter(tag_name=album))
    context = {
        'tier': tier,
        'photos': photos,
        'tags': tags,
        'profile': profile,
        'location': location,
    }

    return render(request, 'photos/tag_album.html', context)


def edit_tags(request, image_id):
    """ A view to edit photos' tags page"""

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        status = Tiers.objects.get(user=profile)
        tier = status.tier
    else:
        tier = False
        profile = UserProfile.objects.get(id=6)

    photo = Photos.objects.get(id=image_id)
    tags = Tags
    location = settings.MEDIA_URL
    context = {
        'tier': tier,
        'photo': photo,
        'tags': tags,
        'profile': profile,
        'location': location,
    }

    if request.method == 'POST':

        tags = request.POST.get('edit-file-tag').split('@')
        tosave = Photos.objects.get(id=image_id)
        tosave.tags_set.clear()
        for tag in tags:
            if tag != "":
                if Tags.objects.filter(tag_name=tag):
                    savetag = Tags.objects.get(tag_name=tag)
                    savetag.tag_photos.add(tosave)
                else:
                    savetag = Tags(tag_name=tag)
                    savetag.save()
                    savetag.tag_photos.add(tosave)

        tags = list(Tags.objects.all())
        for tag in tags:
            if not tag.tag_photos.all():
                todelete = Tags.objects.filter(tag_name=tag)
                todelete.delete()

        return redirect(reverse('all_photos'))

    else:
        return render(request, 'photos/edit_photos.html', context)


def upload(request):
    """ A view to return the upload page"""

    if request.method == 'POST':

        images = request.FILES.get('upload-photo')
        if Photos.objects.filter(image=images):
            count = Photos.objects.filter(image=images).count()
            image_name = images.name.split('.')
            images.name = f'{image_name[0]}_({count}).jpg'
        alltags = request.POST.get('edit-file-tag').split('@')
        if request.user.is_authenticated:
            tosave = Photos(
                owner=UserProfile.objects.get(user=request.user),
                upload_date=datetime.datetime.now(),
                image=images,
            )
        else:
            tosave = Photos(
                upload_date=datetime.datetime.now(),
                image=images,
            )
        tosave.save()
        for tag in alltags:
            if tag != "":
                if Tags.objects.filter(tag_name=tag):
                    savetag = Tags.objects.get(tag_name=tag)
                    savetag.tag_photos.add(tosave)
                else:
                    savetag = Tags(tag_name=tag)
                    savetag.save()
                    savetag.tag_photos.add(tosave)

        return redirect(reverse('all_photos'))

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

    return render(request, "photos/upload.html", context)


def delete_img(request, image_id):
    """ A view to delete photo"""

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        status = Tiers.objects.get(user=profile)
        tier = status.tier
    else:
        tier = False
        profile = UserProfile.objects.get(id=6)

    photo = Photos.objects.get(id=image_id)
    tags = Tags
    location = settings.MEDIA_URL
    context = {
        'tier': tier,
        'photo': photo,
        'tags': tags,
        'profile': profile,
        'location': location,
    }

    if request.method == 'POST':

        todelete = Photos.objects.get(id=image_id)
        todelete.delete()

        tags = list(Tags.objects.all())
        for tag in tags:
            if not tag.tag_photos.all():
                todelete = Tags.objects.filter(tag_name=tag)
                todelete.delete()

        return redirect(reverse('all_photos'))

    else:
        return render(request, 'photos/delete_photos.html', context)
