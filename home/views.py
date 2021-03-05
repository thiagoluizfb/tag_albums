from django.shortcuts import render, redirect, reverse, get_object_or_404
from photos.views import Tags
from subscription.models import Snack, Tiers
from profiles.models import UserProfile
from preview_photos.models import PhotosPreview
from django.conf import settings

import os
import boto3


def index(request):
    """ A view to delete photos uploaded w/o login and return the index page"""

    preview = request.session.get('preview', {})

    for photo in preview:
        location = settings.MEDIA_URL
        image = preview[photo]['image']
        if location[0] == '/':
            location = location[1:10000000]
            os.remove(f'{location}{image}')
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

    tags = Tags.objects.all()
    if tags:
        for tag in tags:
            if not tag.tag_photos.all():
                todelete = Tags.objects.filter(tag_name=tag)
                todelete.delete()

    if request.user.is_authenticated:
        upload = 'upload'
        profile = get_object_or_404(UserProfile, user=request.user)
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
