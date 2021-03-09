from django.conf import settings
from django.shortcuts import render, get_object_or_404

from subscription.models import Tiers
from profiles.models import UserProfile
from preview_photos.models import PhotosPreview

import boto3


def index(request):
    """ A view to delete photos uploaded w/o login and return the index page"""

    preview = request.session.get('preview', {})

    for photo in preview:
        location = settings.MEDIA_URL
        image = preview[photo]['image']
        image_id = preview[photo]['image_id']
        try:
            deleteimage = PhotosPreview.objects.filter(image_name=image_id)
            deleteimage.delete()
            # Credits https://www.edureka.co/community/31903/how-to-delete-a /
            #   -file-from-s3-bucket-using-boto3#:~:text=You%20can%20delete%20the%20file,delete().
            s3 = boto3.resource("s3")
            bucket_name = 'tag-albums'
            obj = s3.Object(bucket_name, f'{location}{image}')
            obj.delete()
        except Exception:
            pass

    request.session['preview'] = {}

    if request.user.is_authenticated:
        start = 'all_photos'
        profile = get_object_or_404(UserProfile, user=request.user)
        status = Tiers.objects.get(user=profile)
        tier = status.tier
    else:
        profile = ""
        tier = False
        start = 'upload_preview'

    context = {
        'profile': profile,
        'tier': tier,
        'start': start,
    }

    return render(request, "home/index.html", context)
