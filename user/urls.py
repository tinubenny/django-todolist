from django.urls import path
from user import views

app_name='user'

urlpatterns = [
    path('',views.home, name='home'),
    path('add_task',views.add_task, name='add_task'),
    path('view_task',views.view_task, name='view_task'),
    path('profile',views.profile, name='profile'),
]
