from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("prediction/<int:pk>/delete/", views.delete_prediction, name="delete_prediction"),
    path("prediction/<int:pk>/update/", views.update_prediction, name="update_prediction"),
]
