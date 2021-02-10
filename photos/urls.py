from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload, name='photos'),
    path('uploaded_photos/', views.uploaded_photos, name='uploaded_photos')
]
