from django.urls import path
from register_app.views import *

urlpatterns = [
    path('home_page/',home_page),
    path('signup_page/',signup_page),
    path('login_page/',login_page),
]
