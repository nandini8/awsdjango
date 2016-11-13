
from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.views import login
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import logout as auth_logout


# Create your views here.

def login_page(request):
	context_dict = {}
	return render(request, "kpi_app/login.html", context_dict)

def home(request):
	context_dict = {}
	return render(request,"kpi_app/home.html", context_dict)

def logout(request):
	auth_logout(request)
	return redirect('/')
	if request.user.is_authenticated():
		return render(request,"kpi_app/home.html", context_dict)
	else:
		return redirect('/')


def logout(request):
    auth_logout(request)
    return redirect('/')
