#populate_roles.py

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "KPI_project.settings")

import django
django.setup()

from kpi_app.models import Company, Role, User, UserRole, Privilege, RolePrivilege

def populate_role():
	Role.objects.all().delete()
	company_obj = Company.objects.get(id=1)
	role_data = [{'id': 1, 'name': 'admin', 'company_obj':Company.objects.get(id=1)},
				{'id': 2, 'name': 'data_loader', 'company_obj':Company.objects.get(id=1)},
				{'id': 3, 'name': 'kpi_analyzer', 'company_obj':Company.objects.get(id=1)},
				{'id': 4, 'name': 'adminP', 'company_obj':Company.objects.get(id=3)},
				{'id': 5, 'name': 'data_loaderP', 'company_obj':Company.objects.get(id=3)},
				{'id': 6, 'name': 'kpi_analyzerP', 'company_obj':Company.objects.get(id=3)},
				]
	for x in role_data:
		u = Role.objects.get_or_create(id = x['id'], role_name=x['name'], company_name=x['company_obj'])
	
def populate_user_role():
	UserRole.objects.all().delete()
	user_obj = User.objects.filter(company_name=Company.objects.get(company_name='Python Class'))
	for x in user_obj:
		u = UserRole.objects.get_or_create(user_id=x, role_id=Role.objects.get(id=6))
		print(u)
	'''user_role_data = [
						{'id': 1, 'user_id': User.objects.get(id=1), 'role_id':Role.objects.get(id=1) },
						{'id': 2, 'user_id': User.objects.get(id=2), 'role_id':Role.objects.get(id=1) },
						{'id': 3, 'user_id': User.objects.get(id=3), 'role_id':Role.objects.get(id=4) },
						{'id': 4, 'user_id': User.objects.get(id=4), 'role_id':Role.objects.get(id=4) }
					]

	for x in user_role_data:
		u = UserRole.objects.get_or_create(id = x['id'], user_id=x['user_id'], role_id=x['role_id'])'''


def populate_privileges():
	Privilege.objects.all().delete()
	company_obj = Company.objects.get(id=1)
	privilege_data = [{'id': 1, 'name': 'add_user', 'company_obj':Company.objects.get(id=1)},
				{'id': 2, 'name': 'update_user', 'company_obj':Company.objects.get(id=1)},
				{'id': 3, 'name': 'delete_user', 'company_obj':Company.objects.get(id=1)},
				{'id': 4, 'name': 'add_role', 'company_obj':Company.objects.get(id=1)},
				{'id': 5, 'name': 'delete_role', 'company_obj':Company.objects.get(id=1)},
				{'id': 6, 'name': 'update_role', 'company_obj':Company.objects.get(id=1)},
				{'id': 7, 'name': 'add_privilege', 'company_obj':Company.objects.get(id=1)},
				{'id': 8, 'name': 'update_privilege', 'company_obj':Company.objects.get(id=1)},
				{'id': 9, 'name': 'delete_privilege', 'company_obj':Company.objects.get(id=1)},
				{'id': 10, 'name': 'add_data', 'company_obj':Company.objects.get(id=1)},
				{'id': 11, 'name': 'update_data', 'company_obj':Company.objects.get(id=1)},
				{'id': 12, 'name': 'view_data', 'company_obj':Company.objects.get(id=1)},
				{'id': 13, 'name': 'update_company_setup', 'company_obj':Company.objects.get(id=1)},
				{'id': 14, 'name': 'view_report', 'company_obj':Company.objects.get(id=1)},
				]
	for x in privilege_data:
		u = Privilege.objects.get_or_create(id = x['id'], privilege_name=x['name'], company_name=x['company_obj'])[0]

def populate_role_privilege():
	RolePrivilege.objects.all().delete()
	role_privilege_data = [
						{'id': 1, 'role_id': Role.objects.get(id=1), 'privilege_id':Privilege.objects.get(id=1)},
						{'id': 2, 'role_id': Role.objects.get(id=1), 'privilege_id':Privilege.objects.get(id=2)},
						{'id': 3, 'role_id': Role.objects.get(id=1), 'privilege_id':Privilege.objects.get(id=3)},
						{'id': 4, 'role_id': Role.objects.get(id=1), 'privilege_id':Privilege.objects.get(id=4)},
						{'id': 5, 'role_id': Role.objects.get(id=1), 'privilege_id':Privilege.objects.get(id=5)},
						{'id': 6, 'role_id': Role.objects.get(id=1), 'privilege_id':Privilege.objects.get(id=6)},
						{'id': 7, 'role_id': Role.objects.get(id=1), 'privilege_id':Privilege.objects.get(id=7)},
						{'id': 8, 'role_id': Role.objects.get(id=1), 'privilege_id':Privilege.objects.get(id=8)},
						{'id': 9, 'role_id': Role.objects.get(id=1), 'privilege_id':Privilege.objects.get(id=9)},
						{'id': 10, 'role_id': Role.objects.get(id=1), 'privilege_id':Privilege.objects.get(id=12)},
						{'id': 11, 'role_id': Role.objects.get(id=1), 'privilege_id':Privilege.objects.get(id=13)},
						{'id': 12, 'role_id': Role.objects.get(id=1), 'privilege_id':Privilege.objects.get(id=14)},

						{'id': 13, 'role_id': Role.objects.get(id=2), 'privilege_id':Privilege.objects.get(id=10)},
						{'id': 14, 'role_id': Role.objects.get(id=2), 'privilege_id':Privilege.objects.get(id=11)},
						{'id': 15, 'role_id': Role.objects.get(id=2), 'privilege_id':Privilege.objects.get(id=12)},
						{'id': 16, 'role_id': Role.objects.get(id=2), 'privilege_id':Privilege.objects.get(id=14)},

						{'id': 17, 'role_id': Role.objects.get(id=3), 'privilege_id':Privilege.objects.get(id=14)},
					]

	for x in role_privilege_data:
		u = RolePrivilege.objects.get_or_create(id = x['id'], role_id=x['role_id'], privilege_id=x['privilege_id'])

if __name__ == '__main__':
	print('Starting script')
	populate_role()
	populate_user_role()
	#populate_privileges()
	#populate_role_privilege()