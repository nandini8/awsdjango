#populate_company.py

import os, sys
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'KPI_project.settings')

import django
django.setup()


from kpi_app.models import Company

def populate():
	company_data = [{'id': 1, 'company_name': 'Xaviers', 'tab3':'Semester', 'tab4': 'Subject', 'filter1': 'Degree', 'filter2': 'Semester', 'filter3': 'Subject'},
					{'id': 3, 'company_name': 'Python Class', 'tab3':'Student', 'tab4': 'Attendance', 'filter1': 'Problems', 'filter2': 'NA', 'filter3': 'NA'}
					]

	Company.objects.all().delete()

	
	for x in company_data:
		print(x['tab3'], x['tab4'])
		company_obj = Company.objects.get_or_create(id= x['id'], company_name=x['company_name'])[0]
		company_obj.tab3_name = x['tab3']
		company_obj.tab4_name = x['tab4']
		company_obj.filter1_dimValue = x['filter1']
		company_obj.filter2_dimValue = x['filter2']
		company_obj.filter3_dimValue = x['filter3']


		company_obj.save()

		print(company_obj)

if __name__ == '__main__':
	print("Populating company data")
	populate()