from django.urls import path 
from .views import *

urlpatterns = [
	path('', home, name='home'),
	# path('practitioner/dashboard', practitioner_dashboard, name='practitioner_dashboard'),
	

]