from django.urls import path
from . import views

app_name = 'gallery'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('', views.product_list, name ='product_list'),
]

