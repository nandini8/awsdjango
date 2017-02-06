#context_processors.py
from django.conf import settings
from kpi_app.models import *
def report(request):
	l = []
	print(l)
	records = {'Name': "" ,'Attendance': 0,'Hackerrank Algorithm Score':0,
				'Hackerrank Python Score':0,
				'Hackerrank Data Structure Score':0,
				'Project Euler - Number of problems solved':0,
				'Rosalind Info - Number of problems solved':0
				}
	user_obj = User.objects.get(user_name = request.user)
	company_obj = Company.objects.get(id=user_obj.company_name.id)
	dim_obj = Dimension.objects.get(company_name_id=company_obj.id)
	attr_obj = Attribute.objects.get(company_name_id=company_obj)
	attrv_obj = AttributeValue.objects.filter(attr_type_id = attr_obj)
	dimv_obj = DimensionValue.objects.filter(dim_type_id=dim_obj)
	context = {'company' : company_obj, 'dimension' : dim_obj, 'attribute' : attr_obj}
	MetricData_obj = MetricData.objects.raw('select * from kpi_app_metricdata where date_associated = (select max(date_associated) from kpi_app_metricdata) and company_name_id=' + str(company_obj.id))
	for attr in attrv_obj:
		for dim in dimv_obj:
			for obj in MetricData_obj:
				if attr.id == obj.attr_1_id:
					if dim.id == obj.dim_1_id:
						print(dim.id, obj.dim_1_id)
						records[dim.dim_name] = obj.numerator
						records['Name'] = attr
						records['Attendance'] = 0
		print(records)
		l.append(records)
		print(len(l))
		#print(l)
	return {'list': l}