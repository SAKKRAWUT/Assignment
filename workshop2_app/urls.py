from django.urls import path
from . import views

urlpatterns = [

    path('', views.homepage, name='homepage'),
    path('Movie_list', views.Movie_list, name='Movie list'),
    path('Movie_detail', views.Movie_detail, name='Moive detail')
]