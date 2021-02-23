import datetime
from django.shortcuts import render, redirect, reverse, get_object_or_404
from photos.views import Photos, Tags
from profiles.models import UserProfile


def index(request):
    """ A view to delete photos uploaded w/o login and return the index page"""

    if Photos.objects.all():
        for photos in Photos.objects.all():
            if not photos.owner:
                photos.delete()

    tags = Tags.objects.all()
    if tags:
        for tag in tags:
            if not tag.tag_photos.all():
                todelete = Tags.objects.filter(tag_name=tag)
                todelete.delete()
        tags.delete()

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
    else:
        profile = ""

    context = {
        'profile': profile,
    }

    return render(request, "home/index.html", context)


def upload(request):
    """ A view to return the upload page"""

    if request.method == 'POST':

        images = request.FILES.get('upload-photo')
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
        print(tosave)
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

    return redirect(reverse('all_photos'))
