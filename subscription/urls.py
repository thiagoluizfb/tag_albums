from django.urls import path
from . import views

urlpatterns = [
    path('', views.buy, name='buy'),
    path('buy_snacks/<int:qty>', views.buy_snack, name='buy_snack'),
    path('success', views.success, name='success'),
]
