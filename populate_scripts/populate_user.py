#populate_user.py

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "KPI_project.settings")

import django
django.setup()

from kpi_app.models import User, Company

def populate():
	#company_obj = Company.objects.get(id=1)
	user_data = [{'name': 'Nandini', 'email': 'nandini@solivarindia.com'},
				{'name': 'Sahil', 'email': 'sahil@solivarindia.com'}]

	print(x['name'])

	#for x in user_data:
	#	u = User.objects.get_or_create(name=x['name'])

if __name__ == '__main__':
	print('Starting script')
	populate()

