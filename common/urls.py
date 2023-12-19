from django.urls import path
from common import views\

app_name='common'

urlpatterns = [
    path('',views.home, name='home'),
    path('register',views.register, name='register'),
    path('login',views.login, name='login'),
    
]
