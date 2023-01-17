from django.db import models
from django.contrib.auth.models import User



departments=(
    ('Cardiologist','Cardiologist'),
('Dermatologists','Dermatologists'),
('Emergency Medicine Specialists','Emergency Medicine Specialists'),
('Allergists/Immunologists','Allergists/Immunologists'),
('Anesthesiologists','Anesthesiologists'),
('Colon and Rectal Surgeons','Colon and Rectal Surgeons'),
)
class Doctor(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=20,null=True)
    last_name=models.CharField(max_length=20,null=True)
    profile_pic= models.ImageField(upload_to='profile_pic/DoctorProfilePic/',null=True,blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=True)
    education=models.CharField(max_length=20,null=True)
    doctorFee=models.PositiveIntegerField(null=True)
    department= models.CharField(max_length=50,choices=departments,default='Cardiologist')
    otp=models.PositiveIntegerField(null=True)
    status=models.BooleanField(default=False)

   

patient=(
    ('InPatient','InPatient'),
('OutPatient','OutPatient'),
)

class Patient(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to='profile_pic/PatientProfilePic/',null=True,blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=True)
    symptoms = models.CharField(max_length=100,null=True)
    patient_file=models.FileField(upload_to='uploads/file')
    prescription=models.CharField(max_length=100,null=True)
    patient_type=models.CharField(max_length=50,choices=patient,default='InPatient')
    admitDate=models.DateField(auto_now=True)
    releaseDate=models.DateField(auto_now=True)
    otp=models.PositiveIntegerField(null=True)
    status=models.BooleanField(default=False)
    def __str__(self):
        return str(self.id)
 


class Appointment(models.Model):
    patientId=models.ForeignKey(Patient,on_delete=models.CASCADE)
    doctorId=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    appointmentDate=models.DateField(auto_now=True)
    description=models.TextField(max_length=500,null=True)
    status=models.BooleanField(default=False)


room_type =(
    ('Private_room','Private_room'),
    ('PrivatePlus_room','PrivatePlus_room'),
    ('Executive_room','Executive_room'),
)
class Room(models.Model):
    patientId=models.ForeignKey(Patient,on_delete=models.CASCADE,null=True,blank=True)
    room_no=models.CharField(max_length=100)
    room_image=models.ImageField(upload_to='room_pic/roomPic/',null=True,blank=True)
    room_type=models.CharField(max_length=50,choices=room_type,default='Private_room')
    status=models.BooleanField(default=False)
    room_amount=models.IntegerField()
    def __str__(self):
        return str(self.id)


staffs_type =(
    ('Doctor','Doctor'),
    ('Nurse','Nurse'),
    ('Ward_boy','Ward_boy'),
    ('Reciptionaciest','Reciptionaciest'),
    ('Data_entry operator','Data_entry operator'),
) 
class staff(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    salry=models.IntegerField()
    staff_type=models.CharField(max_length=50,choices=staffs_type,default='Doctor')

class Comment(models.Model):
    title = models.CharField(max_length=255,null=True,blank=True)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments', related_query_name='comment')
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    rate=models.IntegerField(default=1)

class blog(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    comment=models.ForeignKey(Comment,on_delete=models.CASCADE,null=True,blank=True)
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    blog_image=models.ImageField(upload_to='blog_pic/blogPic/',null=True,blank=True)
    blog_description=models.TextField(null=True)
    doc_advcie=models.TextField()
    diet=models.CharField(max_length=250)
    deises_name=models.CharField(max_length=250)

Test_type =(
    ('Blood test','Blood test'),
    ('Urine test','Urine test'),
    ('Xray','Xray'),
    ('tumor test','tumor test'),
    ('Biochemstry test','Biochemstry test'),
) 
class lab(models.Model):
    patientId=models.ForeignKey(Patient,on_delete=models.CASCADE,null=True,blank=True)
    doctorId=models.ForeignKey(Doctor,on_delete=models.CASCADE,null=True,blank=True)
    lab_no=models.PositiveBigIntegerField(null=True)
    lab_image=models.ImageField(upload_to='lab/labtest/',null=True,blank=True)
    lab_test=models.CharField(max_length=50,choices=Test_type,default='Blood test')
    test_description=models.TextField(null=True,blank=True)
    amount=models.IntegerField()

class medicalprogramms(models.Model):
    patientId=patientId=models.ForeignKey(Patient,on_delete=models.CASCADE,null=True,blank=True)
    programname=models.CharField(max_length=250)
    programnimage=models.ImageField(upload_to='program/programimg/',null=True,blank=True)
    programdescription=models.TextField()
    amount=models.IntegerField()

class PatientDischargeDetails(models.Model):
    patientId=models.ForeignKey(Patient,on_delete=models.CASCADE)
    doctorId=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    room_Id=models.ForeignKey(Room,on_delete=models.CASCADE,null=True,blank=True)
    Lab_Id=models.ForeignKey(lab,on_delete=models.CASCADE,null=True,blank=True)
    daySpent=models.PositiveIntegerField(null=True,blank=True)
    medicineCost=models.PositiveIntegerField(null=False)
    OtherCharge=models.PositiveIntegerField(null=False)
    total=models.PositiveIntegerField(null=False)




