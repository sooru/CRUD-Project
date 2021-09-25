from django import forms
from django.forms import widgets
from enroll.models import User
def string(value):
    if(value[0]!='s'):
        raise forms.ValidationError('Name should start with s')
class Registrations(forms.ModelForm):
    class Meta:
        model=User
        fields=['name','email','password']
        # labels={'name':'Enter Name','email':'Enter Email','password':'Enter Password'}
        error_messages={
            'name':{'required':'Enter Your Name'},
            'email':{'required':'Enter your Email'},
            'password':{'required':'Enter your Password'}
        }
        widgets={
            'name':forms.TextInput(attrs={'placeholder':'Enter your Name'}),
            'email':forms.EmailInput(attrs={'placeholder':'Enter your Email'}),
            'password':forms.PasswordInput(attrs={'placeholder':'Enter your Password'}),

        }
        
