from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'counter'  # name space 

urlpatterns= [
    path('counter', views.counter, name='counter')
]

