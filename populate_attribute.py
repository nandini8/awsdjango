import os, csv
import quickstart
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "KPI_project.settings")

import django
django.setup()

from kpi_app.models import Company, Attribute, AttributeValue, Metric

def populate_attribute():
	Attribute.objects.all().delete()
	company_obj = Company.objects.get(id=3)
	attribute_data = [{'id': 1, 'attr_type': 'exam_type', 'company_obj':Company.objects.get(id=1)},
				{'id': 2, 'attr_type': 'student', 'company_obj':Company.objects.get(id=1)},
				{'id': 3, 'attr_type': 'students', 'company_obj':Company.objects.get(id=3)},
				]
	for x in attribute_data:
		u = Attribute.objects.get_or_create(id = x['id'], attr_type=x['attr_type'], company_name=x['company_obj'])

def populate_attributeValue():
	#AttributeValue.objects.all().delete()
	attr_value_data = [
						{'id': 31, 'attr_type_id': Attribute.objects.get(id=1), 'attr_name': 'Oral'},
						{'id': 32, 'attr_type_id': Attribute.objects.get(id=1), 'attr_name': 'Practical'},
						{'id': 33, 'attr_type_id': Attribute.objects.get(id=1), 'attr_name': 'Written'},
					]

	attr_obj = Attribute.objects.get(id=2)
	with open('data/Students.csv', 'r') as csvfile:
		students = csv.DictReader(csvfile)
		for row in students:
			print(row)
			attr_value_obj = AttributeValue(id=row['Num'])
			attr_value_obj.attr_type_id = attr_obj
			attr_value_obj.attr_name = row['StudentName']

			attr_value_obj.save()

	for x in attr_value_data:
		u = AttributeValue.objects.get_or_create(id = x['id'], attr_type_id=x['attr_type_id'], attr_name=x['attr_name'])

	'''attribute1 = ['Hackerrank Algorithm Score','Hackerrank Python Score','Hackerrank Data Structure Score','Project Euler - Number of problems solved','Rosalind Info - Number of problems solved']
	attr_obj = Attribute.objects.get(id=3) 
	for x in attribute1:
		u = AttributeValue.objects.get_or_create(attr_type_id=attr_obj, attr_name=x)
	values = quickstart.main()

	attr_obj = Attribute.objects.get(id=3)
	l = list()
	for x in values:
		l.append(x[1])
	s = set(l)

	for x in s:
		AttributeValue.objects.create(attr_type_id=attr_obj, attr_name=x)
		print(x)'''

	attr_obj = Attribute.objects.get(id=3)
	with open('data/pythonStudents.csv', 'r') as csvfile:
		students = csv.DictReader(csvfile)
		for row in students:
			print(row)
			attr_value_obj = AttributeValue()
			attr_value_obj.attr_type_id = attr_obj
			attr_value_obj.attr_name = row['Email Address']
			attr_value_obj.save()
			
if __name__ == '__main__':
	print('Starting script')
	populate_attribute()
	populate_attributeValue()
