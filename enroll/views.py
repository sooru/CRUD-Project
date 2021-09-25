from django.shortcuts import redirect, render
from .forms import Registrations
from .models import User
from django.http import HttpResponseRedirect
def home(request):
    return render(request,'enroll/home.html')

def base(request):
    if(request.method=='POST'):
        fm=Registrations(request.POST)
        if(fm.is_valid()):
            fm.save()
            return HttpResponseRedirect('/')
            # data=User.objects.all()
    fm=Registrations()
    data=User.objects.all()
    return render(request,'enroll/base.html',{'form':fm,'data':data})

def delete(request,myid):
    # reg=User(id=myid)
    reg=User.objects.get(pk=myid)
    reg.delete()
    return HttpResponseRedirect('/')

def edit(request,myid):
    pi=User.objects.get(pk=myid)
    if(request.method=='POST'):
        fm=Registrations(request.POST,instance=pi)
        if(fm.is_valid()):
            fm.save()
            fm=Registrations()

    else:
        fm=Registrations(instance=pi)
    data=User.objects.all()
    return render(request,'enroll/update.html',{'form':fm,'data':data})
