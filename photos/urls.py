from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_photos, name='all_photos'),
    path('albums/', views.albums, name='albums'),
    path('<album>/', views.tag_album, name='tag_album'),
]
