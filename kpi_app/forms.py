#forms.py

from django import forms
from kpi_app.models import Company, User, DimensionValue, Dimension

class CompanyForm(forms.ModelForm):
	class Meta:
		model = Company
		fields = '__all__'
		

class UserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = '__all__'

class DimensionValueForm(forms.ModelForm):
	class Meta:
		model = DimensionValue
		fields = '__all__'

class DimensionForm(forms.ModelForm):
	class Meta:
		model = Dimension
		fields = '__all__'

class UploadFileForm(forms.Form):
	file = forms.FileField()