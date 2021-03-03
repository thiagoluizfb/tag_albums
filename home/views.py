import os
import boto3

from django.shortcuts import render, redirect, reverse, get_object_or_404
from photos.views import Photos, Tags
from subscription.models import Snack, Tiers
from profiles.models import UserProfile
from preview_photos.models import PhotosPreview
from django.contrib.auth.models import User
from django.conf import settings


def index(request):
    """ A view to delete photos uploaded w/o login and return the index page"""

    preview = request.session.get('preview', {})
    location = settings.MEDIA_URL

    for photo in preview:
        image = preview[photo]['image']
        if location[0] == '/':
            location = location[1:10000000]
            os.remove(f'{location}preview/{image}')
        else:
            # Credits https://www.edureka.co/community/31903/how-to-delete-a /
            #   -file-from-s3-bucket-using-boto3#:~:text=You%20can%20delete%20the%20file,delete().
            s3 = boto3.resource("s3")
            bucket_name = 'tag-albums'
            location = 'media/'
            obj = s3.Object(bucket_name, f'{location}preview/{image}')
            obj.delete()

        image_id = preview[photo]['image_id']
        deleteimage = PhotosPreview.objects.filter(image_name=image_id)
        deleteimage.delete()

    request.session['preview'] = {}

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
