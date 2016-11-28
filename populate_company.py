#populate_company.py

import os, sys
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'KPI_project.settings')

import django
django.setup()


from kpi_app.models import Company

def populate():
	company_data = [{'id': 1, 'company_name': 'xaviers', 'tab3':'Semester', 'tab4': 'Subject'},
					{'id': 2, 'company_name': 'abc', 'tab3': 'x', 'tab4': 'y'}]

	Company.objects.all().delete()

	
	for x in company_data:
		print(x['tab3'], x['tab4'])
		company_obj = Company.objects.get_or_create(id= x['id'], company_name=x['company_name'])[0]
		company_obj.tab3_name = x['tab3']
		company_obj.tab4_name = x['tab4']


		company_obj.save()

		print(company_obj)

if __name__ == '__main__':
	print("Populating company data")
	populate()