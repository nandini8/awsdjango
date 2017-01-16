import csv
from kpi_app.models import Company, Dimension, DimensionValue, Attribute, AttributeValue
def handle_uploaded_file(f, user_obj):	
	company_obj = Company.objects.get(id=user_obj.company_name.id)
	#print(company_obj)
	with open('templates/kpi_app/a.csv', 'wb') as destination:
		for chunk in f.chunks():
			destination.write(chunk)
	with open('templates/kpi_app/a.csv', 'r') as destination:
		x = csv.DictReader(destination)
		dim1_obj = Dimension.objects.get_or_create(dim_type= company_obj.filter1_dimValue, company_name = company_obj)[0]
		dim2_obj = Dimension.objects.get_or_create(dim_type= company_obj.filter2_dimValue, company_name = company_obj)[0]
		attr1_obj = Attribute.objects.get_or_create(attr_type = company_obj.tab3_name, company_name=company_obj)[0]
		#dim3_obj = Dimension.objects.get_or_create(dim_type= company_obj.filter3_dimValue, company_name = company_obj)
		print(type(dim1_obj))
		for row in x:
			dimValue1_obj = DimensionValue.objects.get_or_create(dim_type_id = dim1_obj, dim_name = row[company_obj.filter1_dimValue], level=1 )
			dimValue2_obj = DimensionValue.objects.get_or_create(dim_type_id = dim2_obj, dim_name = row[company_obj.filter2_dimValue], level=1 )
			attrValue1_obj = AttributeValue.objects.get_or_create(attr_type_id = attr1_obj, attr_name = row[company_obj.tab3_name])