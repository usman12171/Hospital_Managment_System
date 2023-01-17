from django.forms import ModelForm
from django import forms
from .models import Doctor,Patient,Appointment,Comment
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField,UserChangeForm
from django.utils.translation import gettext ,gettext_lazy as _

class userregister(UserCreationForm):
    password1=forms.CharField(label="Password",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(label="Confirm Password",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    email=forms.EmailField(label="Email",widget=forms.EmailInput(attrs={'class':'form-control','name':'email'}))
    class Meta:
     model = User
     fields = ['username','email','password1','password2']
     widgets = {'username':forms.TextInput(attrs={'class':'form-control'})}

    def clean_email(self):
      email = self.cleaned_data['email']
      try:
        user = User.objects.get(email = email)
      except Exception as e:
        return email
      raise forms.ValidationError(f"The {user.email} mail is already exists/taken")
class DoctorUserForm(forms.ModelForm):
    class Meta:
        model=Doctor
        fields=['address','mobile','department','profile_pic']
        widgets = {
        'password': forms.PasswordInput()
        }
class PatientUserForm(forms.ModelForm):
    class Meta:
        model=Patient
        fields=['address','mobile','patient_type','profile_pic']
        widgets = {
        'password': forms.PasswordInput()
        }
class updatedoctorForm(forms.ModelForm):
    class Meta:
        model=Doctor
        fields=['first_name','last_name','address','mobile','education','profile_pic']
        widgets = {
        'password': forms.PasswordInput()
        }

class updatePatientForm(forms.ModelForm):
    class Meta:
        model=Patient
        fields=['address','mobile','profile_pic','patient_file']
        widgets = {'address':forms.TextInput(attrs={'class':'form-control bg-white border-0'}),
                  'mobile':forms.NumberInput(attrs={'class':'form-control bg-white border-0'}),
                  'profile_pic':forms.FileInput(attrs={'class':'form-control bg-white border-0'}),
        }

class appointmentForm(forms.ModelForm):
    class Meta:
        model=Appointment
        fields=['description']
        widgets = {'Appointment':forms.TextInput(attrs={'class':'form-control bg-white border-0'})
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['title','content']
        

class loginform(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'}))
    password = forms.CharField(label=_('password'),strip=False,
    widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))