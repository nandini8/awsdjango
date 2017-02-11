#reports.py
from kpi_app import views
from django.http import HttpResponse
from django.db.models import Max, Sum
from django.db import connection

from kpi_app.models import Company, Attribute, AttributeValue, MetricData, DimensionValue


def filter(request):
	filter1_option = request.POST['filter1']
	filter2_option = request.POST['filter2']
	filter3_option = request.POST['filter3']
	return (filter1_option, filter2_option, filter3_option)

def getreports(user_obj, request):
	filter1_option, filter2_option, filter3_option = filter(request)
	company_obj = Company.objects.get(id=user_obj.company_name.id)
	attr_obj = Attribute.objects.filter(company_name_id=company_obj)[0]
	attrv_obj = AttributeValue.objects.filter(attr_type_id = attr_obj)

	if filter1_option == 'all':
				MetricData_obj = MetricData.objects.raw('select * from kpi_app_metricdata where date_associated = (select max(date_associated) from kpi_app_metricdata) and company_name_id = ' + str(company_obj.id))
	else:
		dimv_obj = DimensionValue.objects.get(dim_name = filter1_option)
		MetricData_obj = MetricData.objects.raw('select id, attr_1_id, numerator from kpi_app_metricdata where date_associated = (select max(date_associated) from kpi_app_metricdata) and company_name_id = ' + str(company_obj.id) +' and dim_1_id = "' + str(dimv_obj.id) + '";')

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
				get_attendance(name)
				temp_dv = DimensionValue.objects.get(id=y.dim_1_id)
				if temp_dv and int(y.numerator) > 0 :
					scores[temp_dv.dim_name]= int(y.numerator)
				else:
					m_obj = MetricData.objects.filter(attr_1_id = temp_av.id, dim_1_id = temp_dv.id).aggregate(Max('numerator'))
					scores[temp_dv.dim_name] = int(m_obj['numerator__max'])
		report_data.append(scores)
		
	headers = [ 'Name', 'Attendance','Hackerrank Algorithm Score',
					'Hackerrank Python Score',
					'Hackerrank Data Structure Score',
					'Project Euler - Number of problems solved',
					'Rosalind Info - Number of problems solved'
					]
	return(report_data, headers)

def get_attendance(name):
	#attendance = MetricData.objects.filter(dim_1_id = 384).values('attr_1_id').annotate(total =Sum('numerator'))
	#attendance = MetricData.objects.raw('select sum(numerator)from kpi_app_metricdata where dim_1_id = 384 group by attr_1_id')
	c = connection.cursor()
	c.execute('select sum(numerator), attr_1_id from kpi_app_metricdata where dim_1_id = 384 group by attr_1_id;')
	rows = c.fetchall()
	print(rows)