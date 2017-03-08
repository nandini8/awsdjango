#populate_company.py
import os, sys
print(sys.path)
os.chdir('/home/nandini/django_project/KPI/serene-reef-39478/KPI_project')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'KPI_project.settings')

import django
django.setup()

#from django.core.wsgi import get_wsgi_application
#application = get_wsgi_application()

from kpi_app.models import Company

def populate():
	company_data = [{'company_name': 'xaviers', 'tab3':'semester', 'tab4': 'subject'},
					{'company_name': 'abc', 'tab3': 'x', 'tab4': 'y'}]

	for x in company_data:
		company_obj = Company.objects.get_or_create(company_name=x['company_name'])
		company_obj.tab3 = x['tab3']
		company_obj.tab4 = x['tab4']

		company_obj.save()

		print(company_obj)

if __name__ == '__main__':
	print("Populating company data")
	populate()