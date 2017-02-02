
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
from django.contrib.auth.decorators import login_required
import csv
from kpi_app import upload_data




# Create your views here.

def login_page(request):
	if request.user.is_authenticated():
		logout(request)
	return render(request, "kpi_app/login.html")

@login_required(login_url='/')	
def home(request):
	email = request.user.email
	user_obj = User.objects.get(email=email)
	role = Role.objects.filter(id=UserRole.objects.get(user_id=user_obj.id).role_id_id)
	try:
		if user_obj:
			context_dict_1 = getData(user_obj)
			print(context_dict_1)
			#context_dict_2 = AllDegrees()
			print(role)
			return render(request,"kpi_app/home.html", {'context_dict1' : context_dict_1, 'role': role })
	except ObjectDoesNotExist:
		print("a")
		logout(request)
		return redirect('/')

def logout(request):
    auth_logout(request)
    return redirect('/')

@login_required(login_url='/')	
def charts(request):
	email = request.user.email
	user_obj = User.objects.get(email=email)
	role = Role.objects.filter(id=UserRole.objects.get(user_id=user_obj.id).role_id_id)
	try:
		context_dict1=getData(user_obj)
		if user_obj:
			return render(request,"kpi_app/charts.html", {'context_dict1': context_dict1, 'role':role})
	except ObjectDoesNotExist:
		logout(request)
		return redirect('/')

@login_required(login_url='/')
def companyCrud(request):
	
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

@login_required(login_url='/')
def userCrud(request):
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

@login_required(login_url='/')	
def dimensionValueCrud(request):
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


@login_required(login_url='/')
def dimensionCrud(request):
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

@login_required(login_url='/')
def uploadFile(request):
	email = request.user.email
	user_obj = User.objects.get(email=email)
	context_dict_1 = getData(user_obj)
	role = Role.objects.filter(id=UserRole.objects.get(user_id=user_obj.id).role_id_id)
	if request.method == 'POST':
		form = UploadFileForm(request.POST, request.FILES)
		if form.is_valid():
			upload_data.handle_uploaded_file(request.FILES['file'], user_obj)
			return render(request, 'kpi_app/uploadData.html', {'form': form, 'context_dict1': context_dict_1, 'role': role, 'success': True})
		else:
			return render(request, 'kpi_app/uploadData.html', {'form': form, 'context_dict1': context_dict_1, 'role': role, 'success': False})
	else:
		form = UploadFileForm()
	return render(request, 'kpi_app/uploadData.html', {'form': form, 'context_dict1': context_dict_1, 'role': role})





def getData(user_obj):
	company_obj = Company.objects.get(id=user_obj.company_name.id)
	dim_obj = Dimension.objects.filter(company_name_id=company_obj.id)
	'''unique_dim_value=dict()
	for d in dim_obj:
		l = list()
		for i in DimensionValue.objects.filter(dim_type_id=d.id):
			l.append(i.dim_name)
		unique_dim_value.update({d.dim_type : l})
	print(unique_dim_value)'''
	dimval_obj_level1 = DimensionValue.objects.filter(parent_id = DimensionValue.objects.get(dim_name= "root"), dim_type_id=dim_obj)
	dimval_obj_level2 = DimensionValue.objects.filter(parent_id__in = dimval_obj_level1, dim_type_id=dim_obj )
	dimval_obj_level3 = DimensionValue.objects.filter(parent_id__in = dimval_obj_level2,  dim_type_id=dim_obj)
	c1,c2,c3 = (list(),list(),list())
	for i in dimval_obj_level1:
		if i.dim_name not in c1:
			c1.append(i.dim_name)

	for i in dimval_obj_level2:
		if i.dim_name not in c2:
			c2.append(i.dim_name)

	for i in dimval_obj_level3:
		if i.dim_name not in c3:
			c3.append(i.dim_name)
	context_dict = {'filter1': company_obj.filter1_dimValue, 'filter2': company_obj.filter2_dimValue,
					 'filter3': company_obj.filter3_dimValue, 'tab3': company_obj.tab3_name,
					  'tab4': company_obj.tab4_name, 'combo1' : c1, 'combo2': c2,'combo3' : c3}
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
