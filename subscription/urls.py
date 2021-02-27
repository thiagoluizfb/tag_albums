from django.urls import path
from . import views
from .webhooks import webhook

urlpatterns = [
    path('', views.buy, name='buy'),
    path('buy_snacks/<int:qty>', views.buy_snack, name='buy_snack'),
    path('success/', views.success, name='success'),
    path('cache_buy_snacks/', views.cache_buy_snacks, name='cache_buy_snacks'),
    path('wh/', webhook, name='webhook'),
]
