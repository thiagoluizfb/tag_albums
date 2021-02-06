from django.shortcuts import render

# Create your views here.

def upload(request):
    """ A view to return the upload page"""

    return render(request, "upload.html")