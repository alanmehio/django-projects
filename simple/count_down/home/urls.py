from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.countdown_timer, name= 'countdown_timer'),
]