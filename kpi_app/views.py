
from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.views import login
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import logout as auth_logout
from kpi_app.models import *
from django.core.exceptions import ObjectDoesNotExist
from kpi_app.forms import CompanyForm, UserForm, DimensionValueForm, DimensionForm
from django.core.context_processors import csrf
from .forms import UploadFileForm
from django.contrib.auth.decorators import login_required
import csv, json
from kpi_app import upload_data , reports
from django.db.models import Max, Min



# Create your views here.

def login_page(request):
	if request.user.is_authenticated():
		logout(request)
	return render(request, "kpi_app/login.html")

@login_required(login_url='/')	
def home(request):
	email = request.user.email
	user_obj = User.objects.get(email=email)
	company_obj = Company.objects.get(id = user_obj.company_name.id)
	role = Role.objects.filter(id=UserRole.objects.get(user_id=user_obj.id).role_id_id)
	context_dict_1 = getData(user_obj)
	if company_obj.company_name == 'Xaviers':
		pagePath = 'kpi_app/home.html'
	elif company_obj.company_name == 'Python Class':
		pagePath = 'kpi_app/home.html'
	elif company_obj.company_name == 'Roche':
		pagePath = 'kpi_app/Rochehome.html'
	if request.method == 'POST':
		report_dict = reports.getreports(user_obj, company_obj,request)
	else:
		try:
			if user_obj:
				#context_dict_1 = getData(user_obj)
				report_dict = reports.getreports(user_obj, company_obj, request)
				#report_dict = reports.getreportsBeforeApply(user_obj,request)
				return render(request,pagePath, {'context_dict1' : context_dict_1, 'role': role, 'report_dict': report_dict[0], 'headers': report_dict[1]})
		except Exception as ex:
		    template = "An exception of type {0} occurred. Arguments:\n{1!r}"
		    message = template.format(type(ex).__name__, ex.args)
		    print (message)
	return render(request,pagePath, {'context_dict1' : context_dict_1, 'role': role, 'report_dict': report_dict[0], 'headers': report_dict[1]})

def logout(request):
	auth_logout(request)
	return redirect('/')


@login_required(login_url='/')	
def tab3(request):
	email = request.user.email
	user_obj = User.objects.get(email=email)
	company_obj = user_obj.company_name
	role = Role.objects.filter(id=UserRole.objects.get(user_id=user_obj.id).role_id_id)
	if company_obj.company_name == 'Xaviers':
		context_dict1 = getData(user_obj)
		if request.method == 'POST':
			report_dict, header_dict = reports.getreports(user_obj, request)
			report_data = json.dumps(report_dict)
			header_data = json.dumps(header_dict)
		else:
			try:
				if user_obj:
					report_dict, header_dict = reports.getreports(user_obj, request)
					report_data = json.dumps(report_dict)
					header_data = json.dumps(header_dict)
					return render(request,"kpi_app/Xtab3.html", {'context_dict1' : context_dict1, 'role': role, 'report_dict':report_data, 'header_dict': header_data })
			except ObjectDoesNotExist:
				logout(request)
				return redirect('/')
		
	elif company_obj.company_name == 'Python Class':
		context_dict1 = getData(user_obj)
		if request.method == 'POST':
			report_dict, header_dict = reports.getreports(user_obj, request)
			getavg = json.dumps(reports.get_avg(user_obj,request))
			report_data = json.dumps(report_dict)
			header_data = json.dumps(header_dict)
			#context_dict_1 = getData(user_obj)
			#print(getavg)
		else:
			#email = request.user.email
			#user_obj = User.objects.get(email=email)
			#role = Role.objects.filter(id=UserRole.objects.get(user_id=user_obj.id).role_id_id)
			try:
				if user_obj:
					#context_dict_1 = getData(user_obj)
					#report_dict = reports.getreports(user_obj, request)
					report_dict, header_dict = reports.getreportsBeforeApply(user_obj,request)
					getavg = json.dumps(reports.get_avg(user_obj,request))
					report_data = json.dumps(report_dict)
					header_data = json.dumps(header_dict)
					return render(request,"kpi_app/tab3.html", {'context_dict1' : context_dict1, 'role': role, 'reports': report_data, 'headers': header_data, 'average' : getavg})
			except ObjectDoesNotExist:
				logout(request)
				return redirect('/')
		
	if company_obj.company_name == 'Xaviers':
		return render(request,"kpi_app/Xtab3.html", {'context_dict1': context_dict1, 'role':role,'report_dict':report_data, 'header_dict': header_data })
	elif company_obj.company_name == 'Python Class':
		return render(request,"kpi_app/tab3.html", {'context_dict1': context_dict1, 'role':role, 'reports': attendance_dict, 'reports_chart':attendance_data}) 



@login_required(login_url='/')
def tab4(request):
	email = request.user.email
	user_obj = User.objects.get(email=email)
	company_obj = user_obj.company_name
	role = Role.objects.filter(id=UserRole.objects.get(user_id=user_obj.id).role_id_id)
	if company_obj.company_name == 'Xaviers':
		context_dict1 = getData(user_obj)
		if request.method == 'POST':
			report_dict, header_dict = reports.getreports(user_obj, request)
			report_data = json.dumps(report_dict)
			header_data = json.dumps(header_dict)
		else:
			try:
				if user_obj:
					report_dict, header_dict = reports.getreports(user_obj, request)
					report_data = json.dumps(report_dict)
					header_data = json.dumps(header_dict)
					return render(request,"kpi_app/Xtab4.html", {'context_dict1' : context_dict1, 'role': role, 'report_dict':report_data, 'header_dict': header_data })
			except ObjectDoesNotExist:
				logout(request)
				return redirect('/')
		
	elif company_obj.company_name == 'Python Class':
		context_dict1 = getData(user_obj)
		if request.method == 'POST':
			report_dict, header_dict = reports.getreports(user_obj, request)
			attendance_dict, header_data = list(), list()
			for attendance in report_dict:
				attendance_dict.append({'Name':attendance['Name'], 'Attendance':attendance['Attendance']})
			attendance_data = json.dumps(attendance_dict)

		else:
			try:
				if user_obj:
					report_dict, header_dict = reports.getreportsBeforeApply(user_obj,request)
					attendance_dict, header_data = list(), list()
					for attendance in report_dict:
						attendance_dict.append({'Name':attendance['Name'], 'Attendance':attendance['Attendance']})
					attendance_data = json.dumps(attendance_dict)
					return render(request,"kpi_app/tab4.html", {'context_dict1' : context_dict1, 'role': role, 'reports': attendance_dict, 'reports_chart':attendance_data})
			except ObjectDoesNotExist:
				logout(request)
				return redirect('/')
	if company_obj.company_name == 'Xaviers':
		return render(request,"kpi_app/Xtab4.html", {'context_dict1': context_dict1, 'role':role,'report_dict':report_data, 'header_dict': header_data })
	elif company_obj.company_name == 'Python Class':
		return render(request,"kpi_app/tab4.html", {'context_dict1': context_dict1, 'role':role, 'reports': attendance_dict, 'reports_chart':attendance_data}) 


@login_required(login_url='/')	
def charts(request):
	email = request.user.email
	user_obj = User.objects.get(email=email)
	company_obj = user_obj.company_name
	role = Role.objects.filter(id=UserRole.objects.get(user_id=user_obj.id).role_id_id)
	if company_obj.company_name == 'Xaviers':
		pagePath = 'kpi_app/Xtab1.html'
	elif company_obj.company_name == 'Python Class':
		pagePath = 'kpi_app/charts.html'
	elif company_obj.company_name == 'Roche':
		pagePath = 'kpi_app/Rochecharts.html'
	if company_obj.company_name == 'Xaviers':
		context_dict1 = getData(user_obj)
		if request.method == 'POST':
			report_dict, header_dict = reports.getreports(user_obj, company_obj, request)
			report_data = json.dumps(report_dict)
			header_data = json.dumps(header_dict)
		else:
			try:
				if user_obj:
					report_dict, header_dict = reports.getreports(user_obj,company_obj ,request)
					report_data = json.dumps(report_dict)
					header_data = json.dumps(header_dict)
					print(report_data)
					return render(request,pagePath, {'context_dict1' : context_dict1, 'role': role, 'report_dict':report_data, 'header_dict': header_data })
			except ObjectDoesNotExist:
				logout(request)
				return redirect('/')
	elif company_obj.company_name == 'Python Class':
		context_dict1=getData(user_obj)
		if request.method == 'POST':
			report_dict = reports.getreports(user_obj, company_obj, request)
			report_data = json.dumps(report_dict[0])
			header_data = json.dumps(report_dict[1])
		else:
			try:
				if user_obj:
					report_dict = reports.getreportsBeforeApply(user_obj,request)
					report_data = json.dumps(report_dict[0])
					header_data = json.dumps(report_dict[1])
					return render(request,pagePath, {'context_dict1': context_dict1, 'role':role, 'reports': report_data, 'headers': header_data})
			except ObjectDoesNotExist:
				logout(request)
				return redirect('/')
	elif company_obj.company_name == 'Roche':
		context_dict1 = getData(user_obj)
		if request.method == 'POST':
			report_dict, header_dict = reports.getreports(user_obj,company_obj, request)
			report_data = json.dumps(report_dict)
			header_data = json.dumps(header_dict)
			print("working")			
		else:
			try:
				if user_obj:
					report_dict, header_dict = reports.getreports(user_obj,company_obj ,request)
					report_data = json.dumps(report_dict)
					header_data = json.dumps(header_dict)
					return render(request,pagePath, {'context_dict1' : context_dict1, 'role': role, 'reports':report_data, 'headers': header_data })
			except ObjectDoesNotExist:
				logout(request)
				return redirect('/')
	return render(request,pagePath, {'context_dict1': context_dict1, 'role':role, 'reports': report_data, 'headers': header_data})



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
	dimval_obj_level1 = DimensionValue.objects.filter(parent_id = DimensionValue.objects.get(dim_name= "root"), dim_type_id=dim_obj)
	dimval_obj_level2 = DimensionValue.objects.filter(parent_id__in = dimval_obj_level1, dim_type_id=dim_obj )
	dimval_obj_level3 = DimensionValue.objects.filter(parent_id__in = dimval_obj_level2,  dim_type_id=dim_obj)
	MetricData_date_obj = MetricData.objects.filter(company_name = company_obj).aggregate(Max('date_associated'))
	MetricData_date_obj1 = MetricData.objects.filter(company_name = company_obj).aggregate(Min('date_associated'))
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

	max_date = MetricData_date_obj['date_associated__max']
	min_date = MetricData_date_obj1['date_associated__min']
	print(max_date, min_date)
	context_dict = {'filter1': company_obj.filter1_dimValue, 'filter2': company_obj.filter2_dimValue,
					 'filter3': company_obj.filter3_dimValue, 'tab3': company_obj.tab3_name,
					  'tab4': company_obj.tab4_name, 'combo1' : c1, 'combo2': c2, 'combo3' : c3, 'years': range(min_date.year, max_date.year+1), 'months' : range(1,13) }
	return context_dict





'''def getreports(user_obj):
	company_obj = Company.objects.get(id=user_obj.company_name.id)
	attr_obj = Attribute.objects.filter(company_name_id=company_obj)[0]
	attrv_obj = AttributeValue.objects.filter(attr_type_id = attr_obj)
	MetricData_obj = MetricData.objects.raw('select * from kpi_app_metricdata where date_associated = (select max(date_associated) from kpi_app_metricdata) and company_name_id = ' + str(company_obj.id))
	report_data = list()
	for x in attrv_obj:
		scores = dict()
		scores.update({ 'Name': "", 'Attendance': 0,'Hackerrank Algorithm Score':0,
					'Hackerrank Python Score':0,
					'Hackerrank Data Structure Score':0,
					'Project Euler - Number of problems solved':0,
					'Rosalind Info - Number of problems solved':0
					})
		name = x.attr_name
		for y in MetricData_obj:
			temp_av = AttributeValue.objects.get(attr_name = y.attr_1)
			if temp_av.attr_name == name:
				scores['Name'] = name
				temp_dv = DimensionValue.objects.get(id=y.dim_1_id)
				if temp_dv and int(y.numerator) > 0 :
					scores[temp_dv.dim_name]= int(y.numerator)
				else:
					m_obj = MetricData.objects.filter(attr_1_id = temp_av.id, dim_1_id = temp_dv.id).aggregate(Max('numerator'))
					scores[temp_dv.dim_name] = int(m_obj['numerator__max'])
		report_data.append(scores)
	#for z in report_data:
		#print(z)
	headers = [ 'Name', 'Attendance','Hackerrank Algorithm Score',
					'Hackerrank Python Score',
					'Hackerrank Data Structure Score',
					'Project Euler - Number of problems solved',
					'Rosalind Info - Number of problems solved'
					]
	return(report_data, headers)'''


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

'''@login_required(login_url='/')
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
'''
'''@login_required(login_url='/')	
def tab3(request):
	email = request.user.email
	user_obj = User.objects.get(email=email)
	role = Role.objects.filter(id=UserRole.objects.get(user_id=user_obj.id).role_id_id)
	#report_dict = reports.getreports(user_obj, request)
	#getavg = reports.get_avg(user_obj,request)
	context_dict1 = getData(user_obj)
	if request.method == 'POST':
		report_dict, header_dict = reports.getreports(user_obj, request)
		getavg = json.dumps(reports.get_avg(user_obj,request))
		report_data = json.dumps(report_dict)
		header_data = json.dumps(header_dict)
		#context_dict_1 = getData(user_obj)
		#print(getavg)
	else:
		#email = request.user.email
		#user_obj = User.objects.get(email=email)
		#role = Role.objects.filter(id=UserRole.objects.get(user_id=user_obj.id).role_id_id)
		try:
			if user_obj:
				#context_dict_1 = getData(user_obj)
				#report_dict = reports.getreports(user_obj, request)
				report_dict, header_dict = reports.getreportsBeforeApply(user_obj,request)
				getavg = json.dumps(reports.get_avg(user_obj,request))
				report_data = json.dumps(report_dict)
				header_data = json.dumps(header_dict)
				return render(request,"kpi_app/tab3.html", {'context_dict1' : context_dict1, 'role': role, 'reports': report_data, 'headers': header_data, 'average' : getavg})
		except ObjectDoesNotExist:
			logout(request)
			return redirect('/')
	return render(request,"kpi_app/tab3.html", {'context_dict1': context_dict1, 'role':role, 'reports': report_data, 'headers': header_data, 'average' : getavg})
'''
