from django.urls import path
from . import views

urlpatterns = [
    path('', views.subscribe, name='subscribe'),
    path('buy_snacks/', views.buy_snack, name='buy_snack'),
]
