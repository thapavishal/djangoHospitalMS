from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index, name='home'),
    path('about/', views.About, name='about'),
    path('contact/', views.Contact, name='contact'),
    path('admin_login/', views.Login, name='login'),
    path('admin_logout/', views.Logout, name='logout'),
    path('view_doctor/', views.View_doctor, name='view_doctor'),
    path('add_doctor/', views.Add_doctor, name='add_doctor'),
    path('delete_doctor(?P<int:pid>)', views.Delete_doctor, name='delete_doctor'),
    path('view_patient/', views.View_patient, name='view_patient'),
    path('add_patient/', views.Add_patient, name='add_patient'),
    path('delete_patient(?P<int:pid>)',
         views.Delete_patient, name='delete_patient'),
    path('view_appointment/', views.View_appointment, name='view_appointment'),
    path('add_appointment/', views.Add_appointment, name='add_appointment'),
    path('delete_appointment(?P<int:pid>)',
         views.Delete_appointment, name='delete_appointment'),
]
