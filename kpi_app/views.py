
from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.views import login
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import logout as auth_logout
from kpi_app.models import User
from django.core.exceptions import ObjectDoesNotExist



# Create your views here.

def login_page(request):
	context_dict = {}
	return render(request, "kpi_app/login.html", context_dict)

def home(request):
	if request.user.is_authenticated():
		email = request.user.email
		try:
			if User.objects.get(email=email):
				return render(request,"kpi_app/home.html")
		except ObjectDoesNotExist:
			logout(request)
			return redirect('/')
	else:
		return redirect('/')


def logout(request):
    auth_logout(request)
    return redirect('/')
