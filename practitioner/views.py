from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
	return render(request, 'frontend/home.html')


def dashboard(request):
	return render(request, 'practitioner/dashboard.html')

@login_required(login_url='account_login')
def verification_welcome(request):
	return render(request, 'frontend/verification_welcome.html')

@login_required(login_url='account_login')
def schedule_appointments(request):
	return render(request, 'frontend/schedule_appointments.html')

@login_required(login_url='account_login')
def talk_to_clients(request):
	return render(request, 'frontend/talk_to_clients.html')

@login_required(login_url='account_login')
def take_notes(request):
	return render(request, 'frontend/take_notes.html')
