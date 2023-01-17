from django.contrib import admin
from .models import Doctor,Patient,blog,Appointment,Room,lab,staff,PatientDischargeDetails,medicalprogramms


# Register your models here.
@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display=('user','user_id','first_name','last_name','profile_pic','education')

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
      list_display=('id','user','mobile','address','profile_pic')

@admin.register(blog)
class blogAdmin(admin.ModelAdmin):
    list_display=('user',)

@admin.register(staff)
class staffAdmin(admin.ModelAdmin):
      list_display=('user','salry','staff_type')


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
      list_display=('patientId','room_no','room_type','room_amount','status')
      
@admin.register(PatientDischargeDetails)
class PatientDischargeDetailsAdmin(admin.ModelAdmin):
      list_display=('patientId','doctorId','room_Id','Lab_Id','medicineCost','total','OtherCharge')

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
     list_display=('patientId','doctorId','description','appointmentDate','status')


@admin.register(lab)
class labAdmin(admin.ModelAdmin):
    list_display=('patientId','doctorId','lab_no','lab_test','amount')

@admin.register(medicalprogramms)
class medicalprogrammsAdmin(admin.ModelAdmin):
    list_display=('patientId','programname','programdescription','amount')
