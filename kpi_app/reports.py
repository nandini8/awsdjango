#reports.py
#from kpi_app import views
from django.http import HttpResponse
from django.db.models import Max, Sum
from django.db import connection
from kpi_app.models import *
from django.db.models import Q

def filter(request):

	filter1_option = request.POST['filter1']
	filter2_option = request.POST['filter2']
	filter3_option = request.POST['filter3']
	filter4_option = request.POST['filter4']
	filter5_option = request.POST['filter5']

	dimv_obj_list = DimensionValue.objects.filter(Q(dim_name = filter1_option) | Q(dim_name = filter2_option) | Q(dim_name = filter3_option))
	dimv_obj_dict = {'dim_1': '', 'dim_2':'', 'dim_3':'', 'year': filter4_option, 'month': filter5_option}
	for obj in dimv_obj_list:
		if obj.level == 1:
			dimv_obj_dict['dim_1'] = str(obj.id)
		elif obj.level == 2:
			dimv_obj_dict['dim_2'] = str(obj.id)
		else:
			dimv_obj_dict['dim_3'] = str(obj.id)

	return(dimv_obj_dict)
	#return (filter1_option, filter2_option, filter3_option, filter4_option, filter5_option)

def getreports(user_obj, request):
	dimv_obj_dict = filter(request)
	#print(dimv_obj_dict)
	company_obj = Company.objects.get(id=user_obj.company_name.id)
	#print(company_obj)
	attr_obj = Attribute.objects.filter(company_name_id=company_obj)[0]
	attrv_obj = AttributeValue.objects.filter(attr_type_id = attr_obj)

	#if filter1_option == 'all':
				#MetricData_obj = MetricData.objects.raw('select id, attr_1_id, numerator from kpi_app_metricdata where date_associated = (select max(date_associated) from kpi_app_metricdata) and company_name_id = ' + str(company_obj.id))
	#else:
		#dimv_obj = DimensionValue.objects.get(dim_name = filter1_option)
		#MetricData_obj = MetricData.objects.raw('select id, attr_1_id, numerator from kpi_app_metricdata where month(date_associated) = if("'+ filter5_option +'", "'+filter5_option+'", month(date_associated)) and company_name_id = ' + str(company_obj.id) +' and dim_1_id = "' + str(dimv_obj.id) + '"; ')


	#General query not completed yet
	str1 = 'select id, attr_1_id, numerator from kpi_app_metricdata where month(date_associated) = if("'+ dimv_obj_dict['month'] +'", "'+dimv_obj_dict['month']+'", month(date_associated)) and dim_1_id = if("'+ dimv_obj_dict['dim_1'] +'", "'+dimv_obj_dict['dim_1']+'", dim_1_id) or dim_2_id = if("'+ dimv_obj_dict['dim_2'] +'", "'+dimv_obj_dict['dim_2']+'", dim_2_id) or dim_3_id = if("'+ dimv_obj_dict['dim_3'] +'", "'+dimv_obj_dict['dim_3']+'", dim_3_id)'
	#print(str1)
	MetricData_obj = MetricData.objects.raw(str1)

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
				#print(attendance)
				temp_dv = DimensionValue.objects.get(id=y.dim_1_id)
				if temp_dv.dim_name == 'Attendance': # and int(y.numerator) > 0 :
					attendance = get_attendance(temp_av, dimv_obj_dict['month'])
					scores[temp_dv.dim_name]= int(attendance)
				else:
					#scores['Attendance'] = int(attendance)
					#print(scores['Name'],scores['Attendance'])
					scores[temp_dv.dim_name]= int(y.numerator)
					#m_obj = MetricData.objects.filter(attr_1_id = temp_av.id, dim_1_id = temp_dv.id).aggregate(Max('numerator'))
					#scores[temp_dv.dim_name] = int(m_obj['numerator__max'])
		report_data.append(scores)
	#print(report_data)
		
	headers = [ 'Name', 'Attendance','Hackerrank Algorithm Score',
					'Hackerrank Python Score',
					'Hackerrank Data Structure Score',
					'Project Euler - Number of problems solved',
					'Rosalind Info - Number of problems solved'
					]
	return report_data, headers


def getreportsBeforeApply(user_obj,request):
	company_obj = Company.objects.get(id=user_obj.company_name.id)
	#print(company_obj)
	attr_obj = Attribute.objects.filter(company_name_id=company_obj)[0]
	attrv_obj = AttributeValue.objects.filter(attr_type_id = attr_obj)

	str1 = "select id, attr_1_id, numerator from kpi_app_metricdata where company_name_id = " + str(company_obj.id)
	#print(str1)
	MetricData_obj = MetricData.objects.raw(str1)
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
				#print(attendance)
				temp_dv = DimensionValue.objects.get(id=y.dim_1_id)
				if temp_dv.dim_name == 'Attendance': # and int(y.numerator) > 0 :
					attendance = get_attendance(temp_av, "")
					scores[temp_dv.dim_name]= int(attendance)
				else:
					#scores['Attendance'] = int(attendance)
					#print(scores['Name'],scores['Attendance'])
					scores[temp_dv.dim_name]= int(y.numerator)
					#m_obj = MetricData.objects.filter(attr_1_id = temp_av.id, dim_1_id = temp_dv.id).aggregate(Max('numerator'))
					#scores[temp_dv.dim_name] = int(m_obj['numerator__max'])
		report_data.append(scores)
	#print(report_data)
		
	headers = [ 'Name', 'Attendance','Hackerrank Algorithm Score',
					'Hackerrank Python Score',
					'Hackerrank Data Structure Score',
					'Project Euler - Number of problems solved',
					'Rosalind Info - Number of problems solved'
					]
	return report_data, headers

def get_attendance(temp_av, month):
	str1 = 'select sum(numerator) from kpi_app_metricdata where dim_1_id in (select id from kpi_app_dimensionvalue where dim_name = "Attendance" ) and attr_1_id = ' + str(temp_av.id) + ' and month(date_associated) = if("'+ month +'", "'+ month +'", month(date_associated))'
	#print(str1)
	str2 = 'select count(distinct(date_associated)) from kpi_app_metricdata'
	b = connection.cursor()
	b.execute(str2)
	max_date = b.fetchone()[0]
	c = connection.cursor()
	c.execute(str1)
	rows = c.fetchone()[0]
	#print(rows)
	return rows * 100 / max_date

def get_avg(user_obj,request):
	company_obj = Company.objects.get(id=user_obj.company_name.id)
	dim_obj = Dimension.objects.filter(company_name_id=company_obj.id)
	dimv_obj = DimensionValue.objects.filter(dim_type_id=dim_obj)
	c = connection.cursor()
	l = dict()
	for x in dimv_obj:
		c.execute('select avg(numerator) from kpi_app_metricdata where date_associated = (select max(date_associated) from kpi_app_metricdata) and dim_1_id= ' + str(x.id))
		rows = c.fetchone()[0]
		#print(round(int(rows)),x.dim_name)
		l.update({x.dim_name:round(int(rows))})
	return(l)