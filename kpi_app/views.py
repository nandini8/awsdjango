from django.shortcuts import render
from social.apps.django_app.default.models import UserSocialAuth

# Create your views here.

def login_page(request):
	context_dict = {}
	return render(request, "kpi_app/login.html", context_dict)

def home(request):
	context_dict = {}
	return render(request,"kpi_app/home.html", context_dict)
