from django.urls import  path
from . import views

# see https://docs.djangoproject.com/en/5.2/intro/tutorial03/
# Namespacing for URL names
app_name = "todo"

'''
urlpatterns = [ 
    path('', views.index, name="index" ),
    path('del/<str:item_id>', views.remove, name="del"),
]

'''

urlpatterns = [ 
    path('', views.IndexView.as_view(), name="index" ),
    path('del/<str:item_id>', views.remove, name="del"),
]
