from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from testapp.forms import signup_forms
from django.http import HttpResponseRedirect
from testapp.models import monday_model1,column_model1
from testapp.forms import mondayupdate_forms,columninsert_forms
# Create your views here.
def home_view(request):
    return render(request,'home.html')

@login_required
def timetable_view1(request):
    monday=monday_model1.objects.all()
    columninsert=column_model1.objects.all()
    dict={'monday':monday,'columninsert':columninsert}
    return render(request,'timetable1.html',dict)

def thank_view(request):
    return render(request,'thank.html')

def signup_view(request):
    form=signup_forms()
    if request.method=="POST":
        form=signup_forms(request.POST)
        user=form.save()
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request,'signup.html',{'form':form})

def update_view(request,id):
    update=monday_model1.objects.get(id=id)
    
    if request.method=='POST':
        form=mondayupdate_forms(request.POST,instance=update)
        if form.is_valid():
            form.save()
        return redirect('/timetable1') 

    return render(request,'update.html',{'update':update})

def insert_view(request):
    form=mondayupdate_forms()
    
    if request.method=='POST':
        form=mondayupdate_forms(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/timetable1')
    return render(request,'insert.html',{'form':form})

def columninsert_views(request):
    form=columninsert_forms()
    
    if request.method=='POST':
        form=columninsert_forms(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/timetable1')
    return render(request,'columninsert.html',{'form':form})

def delete_view(request,id):
    delete=monday_model1.objects.get(id=id)
    delete.delete()
    return redirect('/timetable1')
