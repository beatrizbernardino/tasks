from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path("tasks/<int:pk>", views.task_detail, name="task"),
    path("tasks/", views.get_task, name="all_task"),


]
