
from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.views import login
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import logout as auth_logout
from kpi_app.models import User, Company
from django.core.exceptions import ObjectDoesNotExist
from kpi_app.forms import CompanyForm, UserForm, DimensionValueForm, DimensionForm
from django.core.context_processors import csrf




# Create your views here.

def login_page(request):
	context_dict = {}
	return render(request, "kpi_app/login.html", context_dict)

def home(request):
	if request.user.is_active:
		print(request.user.email)
	'''if request.user.is_authenticated():
		email = request.user.email
		user_obj = User.objects.get(email=email)
		try:
			if user_obj:
				context_dict = getData(user_obj)
				return render(request,"kpi_app/home.html", context_dict)
		except ObjectDoesNotExist:
			logout(request)
			return redirect('/')
	'''
	else:
		logout(request)
		return redirect('/')


def logout(request):
    auth_logout(request)
    return redirect('/')


def charts(request):
	if request.user.is_authenticated():
		email = request.user.email
		user_obj = User.objects.get(email=email)
		try:
			context_dict=getData(user_obj)
			if user_obj:
				return render(request,"kpi_app/charts.html",context_dict)
		except ObjectDoesNotExist:
			logout(request)
			return redirect('/')
	else:
		logout(request)
		return redirect('/')



def companyCrud(request):
	if request.user.is_authenticated():
		email = request.user.email
		user_obj = User.objects.get(email=email)

		if request.method == 'POST':
			form = CompanyForm(request.POST, request.FILES)
			if form.is_valid():
				form.save()
				return HttpResponse('Data Saved')
		else:
			form = CompanyForm()
		args = {}
		args.update(csrf(request))
		args['form'] = form
		return render_to_response('kpi_app/company.html', args)

	else:
		logout(request)
		return redirect('/')
	

def userCrud(request):
	if request.user.is_authenticated():
		email = request.user.email
		user_obj = User.objects.get(email=email)


		if request.method == 'POST':
			form = UserForm(request.POST, request.FILES)
			if form.is_valid():
				form.save()
				return HttpResponse('Data Saved')
		else:
			form = UserForm()
		args = {}
		args.update(csrf(request))
		args['form'] = form
		return render_to_response('kpi_app/user.html', args)

	else:
		logout(request)
		return redirect('/')


def dimensionValueCrud(request):
	if request.user.is_authenticated():
		email = request.user.email
		user_obj = User.objects.get(email=email)

		if request.method == 'POST':
			form = DimensionValueForm(request.POST, request.FILES)
			if form.is_valid():
				form.save()
				return HttpResponse('Data Saved')
		else:
			form = DimensionValueForm()
		args = {}
		args.update(csrf(request))
		args['form'] = form
		return render_to_response('kpi_app/dimensionValue.html', args)


	else:
		logout(request)
		return redirect('/')


def dimensionCrud(request):
	if request.user.is_authenticated():
		email = request.user.email
		user_obj = User.objects.get(email=email)

		if request.method == 'POST':
			form = DimensionForm(request.POST, request.FILES)
			if form.is_valid():
				form.save()
				return HttpResponse('Data Saved')
		else:
			form = DimensionForm()
		args = {}
		args.update(csrf(request))
		args['form'] = form
		return render_to_response('kpi_app/dimension.html', args)


	else:
		logout(request)
		return redirect('/')







def getData(user_obj):
	company_obj = Company.objects.get(id=user_obj.company_name.id)
	context_dict = {'filter1': company_obj.filter1_dimValue, 'filter2': company_obj.filter2_dimValue,
					 'filter3': company_obj.filter3_dimValue, 'tab3': company_obj.tab3_name,
					  'tab4': company_obj.tab4_name}
	return context_dict

'''def userAuthentication(request):
	if request.user.is_authenticated():
		email = request.user.email
		user_obj = User.objects.get(email=email)
		return user_obj
	else:
		return redirect('/')
'''
