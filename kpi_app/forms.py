#forms.py

from django import forms
from kpi_app.models import Company

class CompanyForm(forms.ModelForm):
	class Meta:
		model = Company
		fields = '__all__'
		