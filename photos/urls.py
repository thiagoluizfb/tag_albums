from django.urls import path
from . import views

urlpatterns = [
    path('albums/', views.albums, name='albums'),
    path('<album>/', views.photos, name='photos'),
]
