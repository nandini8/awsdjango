#populate_user.py

import os, csv
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "KPI_project.settings")

import django
django.setup()

from kpi_app.models import User, Company, Attribute, AttributeValue

def populate():
	User.objects.all().delete()
	user_data = [{'id': 1, 'name': 'Nandini', 'email': 'nandini@solivarindia.com', 'company_obj':Company.objects.get(id=1)},
				{'id': 2, 'name': 'Sahil', 'email': 'sahil@solivarindia.com', 'company_obj':Company.objects.get(id=1)},
				{'id': 3, 'name': 'SahilChanchad', 'email': 'chanchadsahil@gmail.com', 'company_obj':Company.objects.get(id=3)},
				{'id': 4,'name': 'NandiniSoni', 'email': 'nandini.soni8@gmail.com', 'company_obj':Company.objects.get(id=3)},
				{'id': 5,'name': 'Venkateshtadinada', 'email': 'venkatesh@solivar.com', 'company_obj':Company.objects.get(id=3)},
				{'id': 6,'name': 'Preethi', 'email': 'preethi@solivarindia.com', 'company_obj':Company.objects.get(id=3)},
				{'id': 7,'name': 'Sahil', 'email': 'chanchadsahil7@gmail.com', 'company_obj':Company.objects.get(id=4)},
				{'id': 8,'name': 'NandiniS', 'email': 'nandini.soni845@gmail.com', 'company_obj':Company.objects.get(id=3)},
				{'id': 9,'name': 'Keerthi', 'email': 'keerthikrishnacp@gmail.com', 'company_obj':Company.objects.get(id=3)},
				{'id': 10,'name': 'Vinuthna', 'email': 'chetanavinuthna@gmail.com', 'company_obj':Company.objects.get(id=3)},
				{'id': 11,'name': 'Alekhya', 'email': 'ganugapatisaialekhya@gmail.com', 'company_obj':Company.objects.get(id=3)},
				{'id': 12,'name': 'Ajay', 'email': 'g.ajaykumar3684@gmail.com', 'company_obj':Company.objects.get(id=3)},
				{'id': 13,'name': 'Sravya', 'email': 'sravyamalla203@gmail.com', 'company_obj':Company.objects.get(id=3)},
				{'id': 14,'name': 'Vennela', 'email': 'vennela.gonuguntla@gmail.com', 'company_obj':Company.objects.get(id=3)},
				{'id': 15,'name': 'Nikhitha Goli', 'email': 'nikhithagolinikki86@gmail.com', 'company_obj':Company.objects.get(id=3)},
				]
		    

	with open('data/pythonStudents.csv', 'r') as csvfile:
		students = csv.DictReader(csvfile)
		#u = User.objects.get_or_create(user_name="Venkateshtadinada", company_name=Company.objects.get(id=3), email="venkatesh@solivar.com")[0]
		s=0
		for row in students:
			print(row)
			s +=1
			print(s)
			u = User.objects.get_or_create(user_name=row['Name'], company_name=Company.objects.get(id=3), email=row['Email Address'])[0]


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

def populateRocheUsers():
	with open('data/RocheUsers.csv', 'r') as csvfile:
		students = csv.DictReader(csvfile)
		#u = User.objects.get_or_create(user_name="Venkateshtadinada", company_name=Company.objects.get(id=3), email="venkatesh@solivar.com")[0]
		s=0
		for row in students:
			print(row)
			s +=1
			print(s)
			u = User.objects.get_or_create(user_name=row['Name'], company_name=Company.objects.get(id=4), email=row['Email Address'])[0]

if __name__ == '__main__':
	print('Starting script')
	populate()
	#populatePythonclassUser()
	populateRocheUsers()
