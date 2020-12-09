"""CSI3450_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', views.index, name='index'),
    path('mydb/', views.dashboard, name='dashboard'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', LoginView.as_view(template_name='mydb/login.html'), name="Login"),
    path('Confirm', views.Confirm, name='Confirm'),
    

    path('employee/', views.employee, name='employee'),
    path('employee_creation/', views.employee_creation, name='employee_creation'),
    path('emp_conf', views.emp_conf, name='emp_conf'),
    path('emp_delete', views.emp_delete, name='emp_delete'),
    path('emp_edit', views.emp_edit, name='emp_edit'),
    path('emp_edit_conf', views.emp_edit_conf, name='emp_edit_conf'),

    path('grant_creation/', views.grant_creation, name='grant_creation'),
    path('grant_conf', views.grant_conf, name='grant_conf'),
    path('grant_delete', views.grant_delete, name='grant_delete'),
    path('grant_edit_conf', views.grant_edit_conf, name='grant_edit_conf'),
    path('grant_edit', views.grant_edit, name='grant_edit'),

    path('grantee_home', views.grantee_home, name='grantee_home'),
    path('grantee_delete', views.grantee_delete, name='grantee_delete'),
    path('grantee_edit_conf', views.grantee_edit_conf, name='grantee_edit_conf'),
    path('grantee_edit', views.grantee_edit, name='grantee_edit'),

    path('Auditor_home', views.Auditor_home, name='Auditor_home'),
    path('auditor_creation/', views.auditor_creation, name='auditor_creation'),
    path('auditor_conf', views.auditor_conf, name='auditor_conf'),
    path('auditor_delete', views.auditor_delete, name='auditor_delete'),
    path('auditor_edit_conf', views.auditor_edit_conf, name='auditor_edit_conf'),
    path('auditor_edit', views.auditor_edit, name='auditor_edit'),

    path('manager_home', views.manager_home, name='manager_home'),
    path('manager_conf', views.manager_conf, name='manager_conf'),
    path('manager_delete', views.manager_delete, name='manager_delete'),
    path('manager_edit_conf', views.manager_edit_conf, name='manager_edit_conf'),
    path('manager_edit', views.manager_edit, name='manager_edit'),
    path('manager_creation/', views.manager_creation, name='manager_creation'),
    

    path('organization_home', views.organization_home, name='organization_home'),
    path('organization_conf', views.organization_conf, name='organization_conf'),
    path('organization_delete', views.organization_delete, name='organization_delete'),
    path('organization_edit_conf', views.organization_edit_conf, name='organization_edit_conf'),
    path('organization_edit', views.organization_edit, name='organization_edit'),
    path('organization_creation/', views.organization_creation, name='organization_creation'),


    path('status_home', views.status_home, name='status_home'),
    path('status_delete', views.status_delete, name='status_delete'),
    path('status_edit_conf', views.status_edit_conf, name='status_edit_conf'),
    path('status_edit', views.status_edit, name='status_edit'),
    
    
    
]