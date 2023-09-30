from django.urls import path
from . import views

urlpatterns = [

    path('', views.homepage, name='homepage'),
    path('Movie_list', views.Movie_list, name='Movie list'),
    path('Movie_detail', views.Movie_detail, name='Moive detail'),
    path('attend_list/', views.attend_list, name='attend_list'),
    path('attend_detail/<int:attn_number>/', views.attend_detail, name='attend_detail'),
]