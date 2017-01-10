#populate_roles.py

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "KPI_project.settings")

import django
django.setup()

from kpi_app.models import Company, Role, User, UserRole

def populate_role():
	Role.objects.all().delete()
	company_obj = Company.objects.get(id=1)
	role_data = [{'id': 1, 'name': 'admin', 'company_obj':Company.objects.get(id=1)},
				{'id': 2, 'name': 'data_loader', 'company_obj':Company.objects.get(id=1)},
				{'id': 3, 'name': 'kpi_analyzer', 'company_obj':Company.objects.get(id=1)},
				]
	for x in role_data:
		u = Role.objects.get_or_create(id = x['id'], role_name=x['name'], company_name=x['company_obj'])
	
def populate_user_role():
	UserRole.objects.all().delete()
	user_role_data = [
						{'id': 1, 'user_id': User.objects.get(id=1), 'role_id':Role.objects.get(id=2) },
						{'id': 2, 'user_id': User.objects.get(id=2), 'role_id':Role.objects.get(id=1) }
					]

	for x in user_role_data:
		u = UserRole.objects.get_or_create(id = x['id'], user_id=x['user_id'], role_id=x['role_id'])



if __name__ == '__main__':
	print('Starting script')
	populate_role()
	populate_user_role()