from django.urls import path
from .views import IndexView

urlpatterns = [
    path('',IndexView.as_view(), name ='index'), # the path for our index view
] 