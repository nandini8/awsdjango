from django.contrib import admin
from kpi_app.models import *
# Register your models here.

class CompanyAdmin(admin.ModelAdmin):
	def has_delete_permission(self, request, obj=None):
		return False
class UserAdmin(admin.ModelAdmin):
	def has_delete_permission(self, request, obj=None):
		return False
class MetricAdmin(admin.ModelAdmin):
	def has_delete_permission(self, request, obj=None):
		return False
class DimensionAdmin(admin.ModelAdmin):
	def has_delete_permission(self, request, obj=None):
		return False
class DimensionValueAdmin(admin.ModelAdmin):
	def has_delete_permission(self, request, obj=None):
		return False
class AttributeAdmin(admin.ModelAdmin):
	def has_delete_permission(self, request, obj=None):
		return False
class AttributeValueAdmin(admin.ModelAdmin):
	def has_delete_permission(self, request, obj=None):
		return False
class RoleAdmin(admin.ModelAdmin):
	def has_delete_permission(self, request, obj=None):
		return False
class UserRoleAdmin(admin.ModelAdmin):
	list_display = ('user_id', 'role_id')
	def has_delete_permission(self, request, obj=None):
		return False
class PrivilegeAdmin(admin.ModelAdmin):
	def has_delete_permission(self, request, obj=None):
		return False
class RolePrivilegeAdmin(admin.ModelAdmin):
	list_display = ('role_id', 'privilege_id')
	def has_delete_permission(self, request, obj=None):
		return False


admin.site.register(Company, CompanyAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Metric, MetricAdmin)
#admin.site.register(Dimension, DimensionAdmin)
#admin.site.register(DimensionValue, DimensionValueAdmin)
#admin.site.register(Attribute, AttributeAdmin)
#admin.site.register(AttributeValue, AttributeValueAdmin)
admin.site.register(Role, RoleAdmin)
admin.site.register(UserRole, UserRoleAdmin)
admin.site.register(Privilege, PrivilegeAdmin)
admin.site.register(RolePrivilege, RolePrivilegeAdmin)