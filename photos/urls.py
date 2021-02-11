from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload, name='photos'),
    path('albums/', views.albums, name='photos'),
    path('<album>', views.photos, name='photos')
]
