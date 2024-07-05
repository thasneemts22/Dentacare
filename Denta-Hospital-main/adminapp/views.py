from django.shortcuts import redirect, render

from Dental_app.models import Doctor_reg
from django.contrib import messages
from django.contrib.auth.models import User

from adminapp.models import Service
from userapp.models import Appointment

# Create your views here.
def adminindex(request):
    return render(request,'admin/index.html')


def doctorlist(request):
    shop = Doctor_reg.objects.filter(user__last_name='0')

    return render(request,'admin/doctor_list.html',{'shop':shop})

def approved_doctor(request):
    shop = Doctor_reg.objects.filter(user__last_name='1')

    return render(request,'admin/approved_doctor.html',{'shop':shop})


def approve(request,id):
    user = User.objects.get(pk=id)
    user.last_name='1'
    user.save()
    messages.success(request, 'Approved')

    return redirect('doctorlist')

def reject(request,id):
    user = User.objects.get(pk=id)
    user.last_name='0'
    user.is_active='0'
    user.save()
    messages.success(request, 'Rejected')

    return redirect('doctorlist')


def booking(request):
    book = Appointment.objects.all()

    return render(request,'admin/booking.html',{'book':book})


def book_approve(request,id):
    us = Appointment.objects.get(pk=id)
    us.status='approve'
    us.save()
    messages.success(request, 'Approved')

    return redirect('booking')

def book_reject(request,id):
    us = Appointment.objects.get(pk=id)
    us.status='reject'
    us.save()
    messages.success(request, 'Rejected')

    return redirect('booking')


def paid_booking(request):
    book = Appointment.objects.filter(payment='paid')

    return render(request,'admin/paid_booking.html',{'book':book})


def Assign_time(request,id):
    if request.method == 'POST':
        time_period = request.POST['time_period']
        boo=Appointment.objects.get(id=id)
        boo.time_period=time_period
        boo.time_status='added'
    
        boo.save()
        return redirect('paid_booking')
    return render(request,'admin/assign_time.html')



def add_service(request):
    if request.method == 'POST':
        ser = request.POST['ser']
        dels = request.POST['details']

        boo=Service()
        boo.service_name=ser
        boo.details=dels
    
        boo.save()
        messages.success(request, 'Added')

        return redirect('add_service')
    return render(request,'admin/add_service.html')