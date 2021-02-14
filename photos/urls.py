from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload, name='photos'),
    path('albums/', views.albums, name='albums'),
    path('<album>/', views.photos, name='photos'),
    path('uploaded', views.uploaded, name='uploaded')
]
