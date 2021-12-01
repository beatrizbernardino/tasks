from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path("tasks/<int:pk>", views.delete_detail, name="task"),
    path("tasks/", views.details_task, name="all_task"),


]
