from django.db import models
from django.conf import settings

# Create your models here.

class Company(models.Model):
	company_name = models.CharField(max_length=50)
	company_logo = models.ImageField(upload_to = settings.MEDIA_URL+'/kpi_app')

	def __str__(self):
		return self.company_name

class User(models.Model):
	user_name = models.CharField(max_length=25)
	company_name = models.ForeignKey(Company)
	email = models.EmailField(max_length=50)

	def __str__(self):
		return self.user_name


class Metric(models.Model):
	metric_name = models.CharField(max_length=50)
	metric_type = models.CharField(max_length=10)
	company_name = models.ForeignKey(Company)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	row_status = models.IntegerField(blank=False)

	def __str__(self):
		return self.metric_name

class Dimension(models.Model):
	dim_type = models.CharField(max_length=50)
	company_name = models.ForeignKey(Company)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.dim_type

class DimensionValue(models.Model):
	dim_type_id = models.ForeignKey(Dimension)
	dim_name = models.CharField(max_length=50)
	parent = models.ForeignKey('self', null=True)
	level = models.IntegerField(blank=False)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.dim_name
	

class MetricData(models.Model):
	dim_1 = models.ForeignKey(DimensionValue, related_name = 'dim_1')
	#dim_2 = models.ForeignKey(DimensionValue, related_name = 'dim_2')
	#dim_3 = models.ForeignKey(DimensionValue, related_name = 'dim_3')
	attr_1 = models.CharField(max_length=50)
	attr_2 = models.CharField(max_length=50)
	attr_3 = models.CharField(max_length=50)
	date_associated = models.DateField()
	metric_id = models.ForeignKey(Metric)
	numerator = models.IntegerField()
	denominator = models.IntegerField()
	company_name = models.ForeignKey(Company)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	row_status = models.IntegerField(blank=False, default=True)
	loaded_by = models.CharField(max_length=50)

	def __str__(self):
		return self.attr_1





