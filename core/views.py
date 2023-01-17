from django.shortcuts import render,redirect
from .form import userregister,DoctorUserForm,PatientUserForm,updatedoctorForm,updatePatientForm,appointmentForm,CommentForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate
from django.views import View
from django.conf import settings
from .models import Doctor,Patient,blog,Appointment,PatientDischargeDetails,lab,Room,medicalprogramms
from django.http import HttpResponse,JsonResponse
from django.core.mail import BadHeaderError, send_mail
import math, random
from django.db.models import Q

#for pdf gerator impiort.
import io
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse

# Create your views here.
def index(request):   
   context={}
   doc=Doctor.objects.all()
   labs=lab.objects.all()
   blo =blog.objects.all()
   programss=medicalprogramms.objects.all()
   context['programss']=programss
   context['doc']=doc
   context['labs']=labs
   context['blo']=blo
   return render(request,'core/base.html',context)

def adminpanel(request):   
   context={}
   return render(request,'core/adminpanel.html',context)

def Doctors(request):   
   context={}
   doc=Doctor.objects.all()
   context['doc']=doc
   return render(request,'core/doctor.html',context)

def Doctors_update(request,id):   
   context={}
   form=updatedoctorForm()
   uer=Doctor.objects.get(id=id)
   print(uer)
   if request.method == "POST":
      form=updatedoctorForm(request.POST,request.FILES,instance=uer)
      if form.is_valid():
         form.save()
         messages.success(request,'update ho gi')
         return redirect('doctor')
      else:
          print(form.errors)  
   context['form']=form
   return render(request,'core/update_profile.html',context)

def Doctors_delete(request):   
   id=request.GET['prod_id']
   print(id)
   doc=Doctor.objects.get(id=id)
   doc.delete()
   return render(request,'core/doctor.html')

def Patients(request):   
   context={}
   pac=Patient.objects.all()
   context['pac']=pac
   return render(request,'core/patient.html',context)

def Patient_update(request,id):   
   context={}
   form=updatePatientForm()  
   uer=Patient.objects.get(id=id)
   if request.method == "POST":
      form=updatePatientForm(request.POST,request.FILES,instance=uer)
      if form.is_valid():
         form.save()
         messages.success(request,'update ho gi')
         return redirect('patient')
      else:
          print(form.errors)  
   context['form']=form
   return render(request,'core/update_patient.html',context)

def Patient_delete(request):   
   id=request.GET['prod_id']
   print(id)
   doc=Patient.objects.get(id=id)
   doc.delete()
   return render(request,'core/patient.html')

def Rooms(request):   
   context={}
   rom=Room.objects.all()
   context['rom']=rom
   return render(request,'core/room.html',context)

def add_room(request):   
   context={}
   rom=Room.objects.all()
   context['rom']=rom
   return render(request,'core/room.html',context)

def room_delete(request):   
   id=request.GET['prod_id']
   print(id)
   doc=Room.objects.get(id=id)
   doc.delete()
   return render(request,'core/room.html')

def Labs(request):   
   context={}
   lac=lab.objects.all()
   context['lac']=lac
   return render(request,'core/labs.html',context)

def lab_delete(request):   
   id=request.GET['prod_id']
   print(id)
   doc=lab.objects.get(id=id)
   doc.delete()
   return render(request,'core/labs.html')



def blogs(request,id=None):
   context={}
   blo=blog.objects.all()
   context['blo']=blo
   if id:
      blo_detail=blog.objects.get(id=id)
      context['blo_detail']=blo_detail
      return render(request,'core/detail.html',context)
   else:
      return render(request,'core/blog.html',context)

def Pricing(request):
   context={}
   programss=medicalprogramms.objects.all()
   context['programss']=programss
   return render(request,'core/pricing.html',context)


class doctorregister(View):
   def get(self,request):
      context={}
      form = userregister()
      form2=DoctorUserForm()
      context['form']=form
      context['form2']=form2
      return render(request, 'core/register.html',context)
   def post(self,request):
    context={}
    if request.method == "POST":
       form=userregister(request.POST)
       form2=DoctorUserForm(request.POST,request.FILES)
       if form.is_valid() and form2.is_valid():
            post_email=form.cleaned_data['email']  
            if User.objects.filter(email=post_email).exists():
               messages.success(request,'erroe')
            else:
               user=form.save() 
               doctor=form2.save(commit=False)
               doctor.user=user
               doctor=form2.save() 
               messages.success(request,'register succesfully')
               return redirect('index')
    context['form']=form
    context['form2']=form2
    context['messages']=messages
    return render(request,'core/register.html',context)

class patientregister(View):
   def get(self,request):
      context={}
      form = userregister()
      form2=PatientUserForm()
      context['form']=form
      context['form2']=form2
      return render(request, 'core/register.html',context)
   def post(self,request):
    context={}
    if request.method == "POST":
       form=userregister(request.POST)
       form2=PatientUserForm(request.POST,request.FILES)
       if form.is_valid() and form2.is_valid():
            post_email=form.cleaned_data['email']  
            if User.objects.filter(email=post_email).exists():
               messages.success(request,'erroe')
            else:
               user=form.save() 
               doctor=form2.save(commit=False)
               doctor.user=user
               doctor=form2.save() 
               messages.success(request,'register succesfully')
    context['form']=form
    context['form2']=form2
    context['messages']=messages
    return render(request,'core/register.html',context)

   
def updates_profile(request):
   context={}
   form=updatedoctorForm()
   curent=request.user.id
   obj=User.objects.get(id=curent)
   uer=Doctor.objects.get(user_id=obj)
   if request.method == "POST":
      form=updatedoctorForm(request.POST,request.FILES,instance=uer)
      if form.is_valid():
         form.save()
         messages.success(request,'update ho gi')
      else:
          print(form.errors)  
   context['form']=form
   return render(request,'core/update_profile.html',context)
       
def doctor(request):
   context={}
   doc=Doctor.objects.all()
   context['doc']=doc
   return render(request,'core/team.html',context)
   
def appointment(request,id=None):
   context={}
   doc=Doctor.objects.all() 
   if request.user.is_authenticated: 
    if id:
      objs=Doctor.objects.get(user_id=id) 
      context['objs']=objs
      form=updatePatientForm() 
      form2=appointmentForm()
      curent=request.user.id
      obj=User.objects.get(id=curent)
      uer=Patient.objects.get(user_id=obj)
      if request.method == "POST":
         form=updatePatientForm(request.POST,request.FILES,instance=uer)
         form2=appointmentForm(request.POST)
      if form.is_valid() and form2.is_valid():
         alps=form2.cleaned_data['description']
         form.save()
         user=request.user.id
         userpr=Patient.objects.get(user_id=user)
         pro=Doctor.objects.get(user_id=id)
         max=Appointment.objects.all()
         max=Appointment.objects.filter(Q(patientId=userpr) & Q(doctorId=pro)) 
         if not max:
               appoint=Appointment(patientId=uer,doctorId=objs,description=alps)
               appoint.save()
               messages.success(request,'update ho gi')
         else:
             messages.success(request,'alredy appoiont')
      else:
         print(form.errors) 
         context['form']=form
         context['form2']=form2
    else:
         context['doc']=doc
         return render(request,'core/appointment.html',context) 
   else:
      context['doc']=doc
   return render(request,'core/appointment.html',context) 

def appointmentaccept(request):
   id=request.GET['prod_id']
   obj=Appointment.objects.get(patientId=id)
   print(obj.status)
   obj.status = True
   ab=Appointment(id=obj.id,patientId=obj.patientId,doctorId=obj.doctorId,status=obj.status)
   ab.save()
   dis=PatientDischargeDetails(patientId=obj.patientId,doctorId=obj.doctorId,medicineCost=0,OtherCharge=obj.doctorId.doctorFee,total=obj.doctorId.doctorFee)
   dis.save()
   return JsonResponse({'value':'appointment done'})
   
   print(obj.status)
   return render(request,'core/appointment.html')

def showappointment(request):
   context={ }
   if request.user.is_superuser:
      uer=Appointment.objects.all()
      context['uer']=uer
      return render(request,'core/appointment.html',context)
   else:
      curent=request.user.id
      obj=Doctor.objects.get(user_id=curent)
      print(obj)
      uer=Appointment.objects.filter(doctorId=obj)
      context['uer']=uer
   return render(request,'core/appointment.html',context) 
   

def patientRooms(request,id=None):
   context={
   }
   if id:
      curent=id
      advanceuser=request.user.is_superuser 
      context['advanceuser']=advanceuser
      print(curent)
   else:
      curent=request.user.id
   obj=User.objects.get(id=curent)
   uer=Patient.objects.get(user_id=obj)
   dich=PatientDischargeDetails.objects.get(patientId=uer)
   ap=Appointment.objects.get(patientId=uer)
   rooms=Room.objects.filter(patientId=uer) 
   Lbas=lab.objects.filter(patientId=uer)
   programm=medicalprogramms.objects.filter(patientId=uer)
   print(Lbas)  
   print('jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj',rooms)
   if rooms or Lbas:
      for room in rooms:
            print('jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj',room.room_amount)
            dich=PatientDischargeDetails.objects.get(patientId=uer)  
            totals=ap.doctorId.doctorFee + room.room_amount
            dis=PatientDischargeDetails(id=dich.id,patientId=uer,doctorId=ap.doctorId,room_Id=room,medicineCost=0,OtherCharge=room.room_amount,total=totals)
            dis.save()
            dich=PatientDischargeDetails.objects.get(patientId=uer)
      for la in Lbas:
          if not rooms:
            dis=PatientDischargeDetails(id=dich.id,patientId=uer,doctorId=ap.doctorId,Lab_Id=la,medicineCost=0,OtherCharge=la.amount,total=la.amount+ap.doctorId.doctorFee)
            dis.save()
            dich=PatientDischargeDetails.objects.get(patientId=uer)
            context['dich']=dich
            context['programm']=programm
            return render(request,'core/patientdetails.html',context)
          else:
            totalse=ap.doctorId.doctorFee + room.room_amount+la.amount
            dis=PatientDischargeDetails(id=dich.id,patientId=uer,doctorId=ap.doctorId,room_Id=room,Lab_Id=la,medicineCost=0,OtherCharge=room.room_amount+la.amount,total=totalse)
            dis.save()
            dich=PatientDischargeDetails.objects.get(patientId=uer)
      dich=PatientDischargeDetails.objects.get(patientId=uer)
      context['dich']=dich
      context['programm']=programm
      return render(request,'core/patientdetails.html',context)
      
        
   else:
      dis=PatientDischargeDetails(id=dich.id,patientId=uer,doctorId=ap.doctorId,medicineCost=0,OtherCharge=ap.doctorId.doctorFee,total=ap.doctorId.doctorFee)
      dis.save()
      dich=PatientDischargeDetails.objects.get(patientId=uer)
      context['dich']=dich
      return render(request,'core/patientdetails.html',context) 
   
   

def discahsrgedetails(request):
   context={
   }
   if  request.user.is_superuser:
      discharg=PatientDischargeDetails.objects.all()
      context['discharg']=discharg
   return render(request,'core/patientdetails.html',context) 


def render_to_pdf(template_src, context_dict):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = io.BytesIO()
    pdf = pisa.pisaDocument(io.BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return


def downloadbill(request,id=None):
   if id:
      dischar=PatientDischargeDetails.objects.get(patientId=id)
      print(dischar)
      dict={
        'patientName':dischar.patientId.user.username,
        'DoctorName':dischar.doctorId.user.username,
        'DoctorFee':dischar.doctorId.doctorFee,
        'Medicancost':dischar.medicineCost,
        'Total':dischar.total,
        'payemnt':'done',
      }
   return render_to_pdf('core/downloadbill.html',dict)
  

def comment(request):
   context={}
   form=CommentForm()  
   uer=User.objects.get(id=request.user.id)
   if request.method == "POST":
      form=CommentForm(request.POST,request.FILES,instance=uer)
      if form.is_valid():
         form.save()
         messages.success(request,'update ho gi')
         return redirect('patient')
      else:
          print(form.errors)  
   context['form']=form
   return render(request,'core/detail.html',context)


