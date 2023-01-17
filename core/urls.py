from django.conf import settings
from django.urls import path
from . import views
from .form import loginform
import random
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index,name='index'),
    path('admin_panel',views.adminpanel,name='admin_panel'),
    path('doctor',views.Doctors,name='doctor'),
    path('doctor',views.Doctors_update,name='doctor'),
    path('updatedoctor/<int:id>/',views.Doctors_update,name='updatedoctor'),
    path('deletdoctor/',views.Doctors_delete,name='deletdoctor'),
    path('patient',views.Patients,name='patient'),
    path('updatepatient/<int:id>/',views.Patient_update,name='updatepatient'),
    path('deletpatient/',views.Patient_delete,name='deletpatient'),
    path('rooms',views.Rooms,name='rooms'),
    path('deletroom/',views.room_delete,name='deletroom'),
    path('patientRooms',views.patientRooms,name='patientRooms'),
    path('patientRooms/<int:id>/',views.patientRooms,name='patientRooms'),
    path('labs',views.Labs,name='labs'),
    path('pricing',views.Pricing,name='pricing'),
    path('deletlab/',views.lab_delete,name='deletlab'),
    path('discharge',views.discahsrgedetails,name='discharge'),
    path('downloadbill/<int:id>',views.downloadbill,name='downloadbill'),
    path('commentform',views.comment,name='commentform'),
    path('signup',views.doctorregister.as_view(),name='signup'),
    path('signuppatient',views.patientregister.as_view(),name='signuppatient'),
    path('updateprofile',views.updates_profile,name='updateprofile'),
    path('doctorteam',views.doctor,name='doctorteam'),
    path('appointment/',views.appointment,name='appointment'),
    path('appointment/<int:id>/',views.appointment,name='appointment'),
    path('showappointment/',views.showappointment,name='showappointment'),
    path('appointmentaccept/',views.appointmentaccept,name='appointmentaccept'),
    path('blogs/',views.blogs,name='blogs'),
    path('blogs/<int:id>',views.blogs,name='blogs'),
    path('login',auth_views.LoginView.as_view(template_name='core/login.html',authentication_form=loginform,next_page='index'),name='login'),
    path('logout',auth_views.LogoutView.as_view(next_page='index'),name='logout')
    ]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)