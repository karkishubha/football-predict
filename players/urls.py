from django.urls import path
from . import views

urlpatterns = [
    path('', views.player_list, name='player_list'), 
    path('<int:pk>/', views.player_detail, name='player_detail'),
]
