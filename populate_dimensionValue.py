#populate_user.py

import os, csv
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'KPI_project.settings')

import django
django.setup()

from kpi_app.models import Dimension, DimensionValue, Company
def populate():
	DimensionValue.objects.all().delete()

	company_obj = Company.objects.get(company_name='xaviers')
	dim_obj = Dimension.objects.get_or_create(dim_type='Subject', company_name=company_obj)[0]
	print(dim_obj)
	dim_value_obj = DimensionValue.objects.get_or_create(id=1, dim_type_id=dim_obj, dim_name='Root', parent=None, level=0)[0]
	print(dim_value_obj)


	with open('data/dimensionvalue.csv', 'r') as csvfile:
		dimension = csv.DictReader(csvfile)
		for row in dimension:
			print(row)
			dim_value_obj = DimensionValue(id=row['DimId'])
			dim_value_obj.dim_type_id = dim_obj
			dim_value_obj.dim_name = row['DimName']
			dim_value_obj.parent = DimensionValue.objects.get(id=row['ParentId'])
			dim_value_obj.level = row['Level']

			dim_value_obj.save()

if __name__== '__main__':
	print("Populating dimension values")
	populate()
