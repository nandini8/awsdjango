#populate_metricdata.py

import os, django, csv, datetime, random, quickstart
from django.utils import timezone
from collections import Counter
from itertools import chain, groupby
import copy
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'KPI_project.settings' )
django.setup()

from kpi_app.models import *

def populate():
	MetricData.objects.all().delete()
	subjects_list, students_list = list(), list()
	x = list()
	company_obj = Company.objects.get(id=1)
	attr_obj = Attribute.objects.get(id=1)
	attr_1 = AttributeValue.objects.filter(attr_type_id=attr_obj.id)
	#print(attr_1[0])
	#exam_types = {'type of exam': [month for even sem, month for odd sem, minimum marks, maximum marks]}
	exam_types = {attr_1[0]: [2, 8, 15, 40], attr_1[1]: [4, 10, 25, 60], attr_1[2]: [6, 12, 35, 100]}
	semester = {'Sem I': 2014, 'Sem II': 2014, 'Sem III': 2015, 'Sem IV': 2015, 'Sem V': 2016, 'Sem VI': 2016}
	#for x in exam_types:
	#	print(x)

	attr_obj = Attribute.objects.get(id=2)
	students_list = AttributeValue.objects.filter(attr_type_id=attr_obj.id)
	#print(students_list[0])


	metric_obj = Metric.objects.get_or_create(id=2,metric_name='marks', metric_type='ratio', company_name=Company.objects.get(company_name='Xaviers'))[0]
	metric_obj = Metric.objects.get(id=2)

	bca_obj = DimensionValue.objects.filter(dim_name='BCA')[0]
	semesters = DimensionValue.objects.filter(parent=bca_obj)
	sem_index = 0

	for sem in semesters:
		print(sem.dim_name)
		exam_year = semester[sem.dim_name]
		print(exam_year)
		subjects = DimensionValue.objects.filter(parent=sem)
		sem_index += 1
		exam_day = 0

		for subject in subjects:
			print("\t", subject.dim_name)
			exam_day += 1

			for exam_type in exam_types.keys():
				exam_month = exam_types[exam_type][sem_index % 2]
				#print(exam_month)
				exam_date = datetime.date(exam_year, exam_month, exam_day)
				print("\t\t", exam_type, exam_date)
				min1 = exam_types[exam_type][2]
				print(min1)
				max1 = exam_types[exam_type][3]
				print(max1)


				for student in students_list:
					print("\t\t\t", student)
					num = random.randrange(min1, max1)
					
					m = MetricData.objects.get_or_create(dim_1=bca_obj, dim_2=sem, dim_3=subject, attr_1=student,
						attr_2= exam_type,
						date_associated=exam_date, metric_id=metric_obj,
						numerator=num, denominator=max1, company_name=company_obj)[0]
					m.save()
					print(student," created")


def populate_pythonClass():
	metric_obj = Metric.objects.get_or_create(id=1,metric_name='Score', metric_type='count', company_name=Company.objects.get(company_name='Python Class'))[0]

	company_obj = Company.objects.get(company_name='Python class')
	dim_obj = Dimension.objects.get(company_name=company_obj)
	dim1_obj = DimensionValue.objects.filter(dim_type_id=dim_obj, level=1)
	attr1_obj = Attribute.objects.get(company_name=company_obj)
	attr1_values = AttributeValue.objects.filter(attr_type_id=attr1_obj)
	with open('names.csv', 'r') as csvfile:
		records_from_file = csv.DictReader(csvfile)
		records = list(records_from_file)
		for row in records:
			if '/' in row['Date for Saturday class']:
					row['Date for Saturday class'] = datetime.datetime.strptime(row['Date for Saturday class'], '%m/%d/%Y')
			else:
				date = row['Date for Saturday class'].replace('th', "")
				row['Date for Saturday class'] = datetime.datetime.strptime(date, '%b %d %Y')

		sortedRecords =  sorted(records, key=lambda k: [k['Email Address'], k['Date for Saturday class'] ])
		number_of_days = sorted(set(record['Date for Saturday class'] for record in sortedRecords))

		list_to_be_entered = list()
		for key, group in groupby(sortedRecords, lambda x: x['Email Address']):
			individual_student = [x for x in group]
			number_of_days_entered = sorted(set(record['Date for Saturday class'] for record in individual_student))
			if len(individual_student) < len(number_of_days):
				missing_days = sorted(set(number_of_days).difference(set(number_of_days_entered)))
				#print(missing_days)
				for i in missing_days:
					rec = copy.copy(individual_student[-1])
					rec['Date for Saturday class'] = i
					rec['Did you attend the class?'] = 'No'
					individual_student.append(rec)
				#print(individual_student[-1]['Date for Saturday class'])
			print(individual_student)
			list_to_be_entered.append(individual_student)

		for rows in list_to_be_entered:
			for row in rows:
				attrv_obj = AttributeValue.objects.get(attr_name = row['Email Address'])
				for x in dim1_obj:
					if x.dim_name == 'Attendance':
						if row['Did you attend the class?'] == "Yes" :
							metric_data_obj = MetricData.objects.get_or_create(dim_1=x, attr_1=attrv_obj, metric_id=metric_obj, company_name=company_obj, date_associated=row['Date for Saturday class'], numerator=1)[0]
							print(attrv_obj,x.dim_name)
						else:
							metric_data_obj = MetricData.objects.get_or_create(dim_1=x, attr_1=attrv_obj, metric_id=metric_obj, company_name=company_obj, date_associated=row['Date for Saturday class'], numerator=0)[0]
							print(attrv_obj,x.dim_name)
					else:
						metric_data_obj = MetricData.objects.get_or_create(dim_1=x, attr_1=attrv_obj, metric_id=metric_obj, company_name=company_obj, date_associated=row['Date for Saturday class'], numerator=row[x.dim_name])[0]
						print(attrv_obj,x.dim_name)
	#print(type(Attribute.objects.get(company_name=company_obj)))
	#print(attr1_values)
	'''values = quickstart.main()
	for x in values:
		for y in dim1_obj:
			for z in attr1_values:
				if x[1] == z.attr_name:
					num=0
					print(num)
					if '/' in x[3]:
						date_obj = datetime.datetime.strptime(x[3], '%m/%d/%Y')
					else:
						date = x[3].replace('th', "")
						date_obj = datetime.datetime.strptime(date, '%b %d %Y')
					print(date_obj)
					if y.dim_name == 'Hackerrank Algorithm Score':
						num = x[7]
					elif y.dim_name == 'Hackerrank Python Score':
						num = x[8]
					elif y.dim_name == 'Hackerrank Data Structure Score':
						num = x[9]
					elif y.dim_name == 'Project Euler - Number of problems solved':
						num = x[10]
					elif y.dim_name == 'Rosalind Info - Number of problems solved':
						num = x[11]
					#metric_data_obj = MetricData.objects.get_or_create(dim_1=y, attr_1=z, metric_id=metric_obj, company_name=company_obj, date_associated=x[3], numerator=num)[0]
					metric_data_obj = MetricData.objects.get_or_create(dim_1=y, attr_1=z, metric_id=metric_obj, company_name=company_obj, date_associated=date_obj, numerator=num)[0]
					#print(metric_data_obj)
	Metric.objects.all().delete()
	metric_obj = Metric.objects.get_or_create(id=1,metric_name='Score', metric_type='count', company_name=Company.objects.get(company_name='Python Class'))[0]
	company_obj = Company.objects.get(company_name = 'Python Class')
	dim_obj = Dimension.objects.get(company_name=company_obj)
	dim1_obj = DimensionValue.objects.filter(dim_type_id=dim_obj, level=1)'''
	

		#for x in list_to_be_entered:
			#for y in x:
				#print(y["Email Address"], y["Date for Saturday class"])
			#print(len(x))

		#print(number_of_days)
		#print(number_of_records_entered, number_of_days)
		#for records in sortedRecords:
			#if records['Date for Saturday class'] in number_of_days:
				#print(records['Email Address'])
			#print(record, number_of_records_entered[record])
			#my_item = next((item for item in sortedRecords if item['Email Address'] == record and item['Date for Saturday class'] == max(number_of_days)), None)


		

			

if __name__ == '__main__':
	print("Starting to populate data")
	populate()
	#populate_pythonClass()
