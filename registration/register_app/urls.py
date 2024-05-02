from django.urls import path
from register_app.views import *

urlpatterns = [
    path('home_page/',home_page,name = "home_page"),
    path('signup_page/',signup_page,name = 'signup'),
    path('login_page/',login_page,name = 'login_page'),
    path('logout/',logout_page,name="logout")
]
