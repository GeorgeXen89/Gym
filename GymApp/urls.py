from django.contrib import admin
from django.urls import path
from WorkoutApp import views  # Import views from WorkoutApp

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', views.list_users, name='list_users'),
    path('exercises/', views.list_exercises, name='list_exercises'),
    path('workplans/', views.list_workplans, name='list_workplans'),
    path('', views.home, name='home'),
]
