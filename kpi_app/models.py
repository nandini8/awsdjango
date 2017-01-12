from django.db import models
from django.conf import settings

# Create your models here.

class Company(models.Model):
	company_name = models.CharField(max_length=50)
	company_logo = models.ImageField(upload_to = 'kpi_app', default=None)
	tab3_name = models.CharField(max_length=15)
	tab4_name = models.CharField(max_length=15)
	filter1_dimValue = models.CharField(max_length=20)
	filter2_dimValue = models.CharField(max_length=20)
	filter3_dimValue = models.CharField(max_length=20)

	class Meta():
		verbose_name_plural = 'Companies'

	def __str__(self):
		return self.company_name

class User(models.Model):
	user_name = models.CharField(max_length=25)
	company_name = models.ForeignKey(Company)
	email = models.EmailField(max_length=50)
	user_role = models.CharField(max_length=50, default="Company User")	#The other values are "Company Admin" and "System Admin"

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
	

class Attribute(models.Model):
	attr_type = models.CharField(max_length=50)
	company_name = models.ForeignKey(Company)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.attr_type

class AttributeValue(models.Model):
	attr_type_id = models.ForeignKey(Attribute)
	attr_name = models.CharField(max_length=50)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.attr_name

class Role(models.Model):
	company_name = models.ForeignKey(Company)
	role_name = models.CharField(max_length=20)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.role_name

class Privilege(models.Model):
	company_name = models.ForeignKey(Company)
	privilege_name = models.CharField(max_length=20)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.privilege_name

class UserRole(models.Model):
	user_id = models.ForeignKey(User, related_name='user_id')
	role_id = models.ForeignKey(Role, related_name='role_id')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.user_id

class RolePrivilege(models.Model):
	role_id = models.ForeignKey(Role, related_name='Role_id')
	privilege_id = models.ForeignKey(User, related_name='privilege_id')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.role_id




class MetricData(models.Model):
	dim_1 = models.ForeignKey(DimensionValue, related_name = 'dim_1')
	#dim_2 = models.ForeignKey(DimensionValue, related_name = 'dim_2',default=None)
	#dim_3 = models.ForeignKey(DimensionValue, related_name = 'dim_3',default=None)
	attr_1 = models.ForeignKey(AttributeValue, related_name = 'attr_1')
	attr_2 = models.ForeignKey(AttributeValue, related_name = 'attr_2')
	#attr_3 = models.ForeignKey(AttributeValue, related_name = 'attr_3',default=None)
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
		return self.attr_1.attr_name
