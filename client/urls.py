from django.urls import path
from .views import *

urlpatterns = [
	path('signup', signup, name='client_signup'),
	path('login', login, name='client_login'),
    path('logout', log_out_view, name='client_logout'),
	path('home', client_home, name='client_home'),
]