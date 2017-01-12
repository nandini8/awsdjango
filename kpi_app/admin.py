from django.contrib import admin

# Register your models here.
from kpi_app.models import *

admin.site.register(Company)
admin.site.register(User)
admin.site.register(Metric)
admin.site.register(Dimension)
admin.site.register(DimensionValue)
admin.site.register(Attribute)
admin.site.register(AttributeValue)
admin.site.register(Role)
admin.site.register(UserRole)
admin.site.register(Privilege)
admin.site.register(RolePrivilege)


