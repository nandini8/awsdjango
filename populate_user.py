#populate_user.py

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "KPI_project.settings")

import django
django.setup()

from kpi_app.models import User, Company, Attribute, AttributeValue

def populate():
	#sUser.objects.all().delete()
	user_data = [{'id': 1, 'name': 'Nandini', 'email': 'nandini@solivarindia.com', 'company_obj':Company.objects.get(id=1)},
				{'id': 2, 'name': 'Sahil', 'email': 'sahil@solivarindia.com', 'company_obj':Company.objects.get(id=1)},
				{'id': 3, 'name': 'SahilChanchad', 'email': 'chanchadsahil@gmail.com', 'company_obj':Company.objects.get(id=3)},
				{'id': 4,'name': 'NandiniSoni', 'email': 'nandini.soni8@gmail.com', 'company_obj':Company.objects.get(id=3)},
				{'id': 5,'name': 'Venkateshtadinada', 'email': 'venkatesh@solivar.com', 'company_obj':Company.objects.get(id=3)},
				{'id': 6,'name': 'Preethi', 'email': 'preethi@solivarindia.com', 'company_obj':Company.objects.get(id=3)},
				{'id': 7,'name': 'Sahil', 'email': 'chanchadsahil7@gmail.com', 'company_obj':Company.objects.get(id=4)},
				]
	for x in user_data:
		print(x)
		u = User.objects.get_or_create(id = x['id'], user_name=x['name'], company_name=x['company_obj'], email=x['email'])[0]

def populatePythonclassUser():
	company_obj = Company.objects.get(company_name='Python Class')
	attr_obj = Attribute.objects.get(company_name=company_obj)
	attrv_obj = AttributeValue.objects.filter(attr_type_id= attr_obj) 
	for x in attrv_obj:
		name = x.attr_name.split('@')[0]
		u = User.objects.get_or_create(user_name=name, company_name=company_obj, email=x.attr_name)[0]
		#print(u)
	u = User.objects.get_or_create(user_name='Venkatesh', company_name=company_obj, email='venkatesh@solivar.com')[0]
	#print(u)

	
if __name__ == '__main__':
	print('Starting script')
	populate()
	#populatePythonclassUser()preethi@solivarindia.com
