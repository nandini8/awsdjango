"""KPI_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from kpi_app import views

urlpatterns = [
	url(r'^home/', views.home, name="home"),
    url(r'^tab3/', views.tab3, name="tab3"),
        url(r'^tab4/', views.tab4, name="tab4"),
	url(r'^charts/', views.charts, name="charts"),
    url(r'upload-data/', views.uploadFile, name='uploadDataCrud'), 
    #url(r'^company/', views.companyCrud, name="company"),
    #url(r'^user/', views.userCrud, name='user'),
    #url(r'dimension/', views.dimensionCrud, name="dimension"),
    #url(r'dimensionValue/', views.dimensionValueCrud, name="dimensionValue"),
]
