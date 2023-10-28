from django.contrib import admin
from django.urls import path
from . import views  # assuming this urls.py is in the same folder as views.py

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', views.list_users, name='list_users'),
    path('exercises/', views.list_exercises, name='list_exercises'),
    path('workplans/', views.list_workplans, name='list_workplans'),
    path('', views.home, name='home'),
]
