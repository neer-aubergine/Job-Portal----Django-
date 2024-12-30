from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.jobs_list , name='jobs'),
    path('create_job/', views.job_create , name='create_job'),
    path('<int:job_id>/edit/', views.job_edit , name='job_edit'),
    path('<int:job_id>/delete/', views.job_delete , name='job_delete'),
   
]