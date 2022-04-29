from django.urls import path, include
import allauth.urls
from .views import *

urlpatterns = [
	path('accounts/', include('allauth.urls')),
	path('dashboard/', dashboard, name='dashboard'),
	path('welcome', verification_welcome, name='verification_welcome'),
	path('schedule/appointments', schedule_appointments, name='schedule_appointments'),
	path('talk/to/clients', talk_to_clients, name='talk_to_clients'),
	path('take/notes', take_notes, name='take_notes'),

]