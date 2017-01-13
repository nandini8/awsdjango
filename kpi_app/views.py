
from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.views import login
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import logout as auth_logout
from kpi_app.models import User, Company, Dimension, DimensionValue, Role, UserRole
from django.core.exceptions import ObjectDoesNotExist
from kpi_app.forms import CompanyForm, UserForm, DimensionValueForm, DimensionForm
from django.core.context_processors import csrf
from .forms import UploadFileForm




# Create your views here.

def login_page(request):
	context_dict = {}
	return render(request, "kpi_app/login.html", context_dict)

def home(request):
	if request.user.is_authenticated():
		email = request.user.email
		user_obj = User.objects.get(email=email)
		print(UserRole.objects.get(id=user_obj.id).id)
		role = Role.objects.filter(id=UserRole.objects.get(user_id=user_obj.id).role_id_id)
		try:
			if user_obj:
				context_dict_1 = getData(user_obj)
				#context_dict_2 = AllDegrees()
				print(role)
				return render(request,"kpi_app/home.html", {'context_dict1' : context_dict_1, 'role': role })
		except ObjectDoesNotExist:
			logout(request)
			return redirect('/')
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
		role = Role.objects.filter(id=UserRole.objects.get(id=user_obj.id).id)
		try:
			context_dict1=getData(user_obj)
			if user_obj:
				return render(request,"kpi_app/charts.html", {'context_dict1': context_dict1, 'role':role})
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


def uploadFile(request):
	email = request.user.email
	user_obj = User.objects.get(email=email)
	context_dict_1 = getData(user_obj)
	role = Role.objects.filter(id=UserRole.objects.get(id=user_obj.id).id)
	if request.method == 'POST':
		form = UploadFileForm(request.POST, request.FILES)
		if form.is_valid():
			handle_uploaded_file(request.FILES['file'])
			return render(request, 'kpi_app/uploadData.html', {'form': form, 'context_dict1': context_dict_1, 'role': role, 'success': True})
		else:
			return render(request, 'kpi_app/uploadData.html', {'form': form, 'context_dict1': context_dict_1, 'role': role, 'success': False})
	else:
		form = UploadFileForm()
	return render(request, 'kpi_app/uploadData.html', {'form': form, 'context_dict1': context_dict_1, 'role': role})


def handle_uploaded_file(f):
	with open('templates/kpi_app/a.txt', 'wb') as destination:
		for chunk in f.chunks():
			destination.write(chunk)



def getData(user_obj):
	company_obj = Company.objects.get(id=user_obj.company_name.id)
	context_dict = {'filter1': company_obj.filter1_dimValue, 'filter2': company_obj.filter2_dimValue,
					 'filter3': company_obj.filter3_dimValue, 'tab3': company_obj.tab3_name,
					  'tab4': company_obj.tab4_name}
	return context_dict

'''
def AllSems():
	print('{:>4} {:<15} {:>10} {:>15} {:>15}'.format("Num","Sem","Marks","Max","Percentage"))

	sem_list = Dimension.objects.raw('select id from rango_dimension where id in (select parent_id from rango_dimension where id in (select dim_1_id from rango_metricdata group by dim_1_id))')
	for sem in sem_list:
		m_list = MetricData.objects.raw('select  id, sum(numerator) as numerator , sum(denominator) as denominator,sum(numerator) * 100 / sum(denominator) as percentage from rango_metricdata where dim_1_id in (select id from rango_dimension where parent_id =' + str(sem.id) + ')')
		id = 0
		for m in m_list:
			id += 1
			print('{:>4} {:<15} {:>10} {:>15} {:13.2f}'.format(id, sem.dim_name, m.numerator, m.denominator , m.percentage))
def AllDegrees():
	degree_list = DimensionValue.objects.raw('select id from kpi_app_')
	for degree in degree_list:
		#query
		return

def userAuthentication(request):
	if request.user.is_authenticated():
		email = request.user.email
		user_obj = User.objects.get(email=email)
		return user_obj
	else:
		return redirect('/')
'''






#select  id, sum(numerator) as numerator , sum(denominator) as denominator,sum(numerator) * 100 / sum(denominator) as percentage from kpi_app_metricdata where dim_1_id in (select id from kpi_app_dimensionvalue where parent_id in (select id from ))
