from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import render,redirect

from Dental_app.models import Doctor_reg, UserType, user_reg
from django.contrib.auth.models import User

from userapp.models import Appointment, Prescription

# Create your views here.
def index(request):
    return render(request,'index.html')


def loginview(request):
    if request.method == 'POST':

        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=email, password=password)

        if user is not None:
            login(request, user)
            if user.last_name =='1':
                if user.is_superuser:
                    return redirect('admin')
                elif UserType.objects.get(user_id=user.id).type =="user":
                    return redirect('user')
                elif UserType.objects.get(user_id=user.id).type =="doctor":
                    return redirect('doctor')  
               
            else:
                return render(request, 'login.html', {'message': " User Account Not Authenticated"})


        else:
            return render(request, 'login.html', {'message': "Invalid Username or Password"})
    
    return render(request,'login.html')




def Doctor_Register(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        phone_number = request.POST['mob']
        quali = request.POST['quali']
        dob = request.POST['dob']

        exp = request.POST['exp']
        if User.objects.filter(email=email):
            return render(request, 'doctor_reg.html', {'message': "already added the email"})

        else:
            user = User.objects._create_user(username=email, password=password, email=email, first_name=name,
                                                 is_staff='0', last_name='0')
            user.save()
            st = Doctor_reg()
            st.user = user
            st.dob= dob
            st.phone_number=phone_number
            st.qualification=quali
            st.exp=exp
            st.save()
            usertype = UserType()
            usertype.user = user
            usertype.type ="doctor"
            usertype.save()
            return render(request, 'doctor_reg.html', {'message': "successfully added"})
    return render(request,'doctor_reg.html')

def reg(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        phone_number = request.POST['mob']
        dob = request.POST['dob']

        address = request.POST['place']
        if User.objects.filter(email=email):
            return render(request, 'patient_reg.html', {'message': "already added the email"})

        else:
            user = User.objects._create_user(username=email, password=password, email=email, first_name=name,
                                                 is_staff='0', last_name='1')
            user.save()
            stu = user_reg()
            stu.user = user
            stu.address= address
            stu.phone_number=phone_number
            stu.dob= dob

            stu.save()
            usertype = UserType()
            usertype.user = user
            usertype.type = "user"
            usertype.save()
            return render(request, 'patient_reg.html', {'message': "successfully added"})
    return render(request,'patient_reg.html')

def doctorindex(request):
    return render(request,'doctor/index.html')



def app_booking(request):
    use=Doctor_reg.objects.get(user_id=request.user.id)
    boo=Appointment.objects.filter(doctor_id=use.id,time_status='added',status='paid')
    return render(request,'doctor/view_booking.html',{'boo':boo})



def prescription(request,id):
    use=Doctor_reg.objects.get(user_id=request.user.id)
    boo=Appointment.objects.get(id=id)
    boo.status='pre_added'
    boo.save()
    user=boo.user_id
    if request.method == 'POST':
        pre = request.POST['pre']
        yy=Prescription()
        yy.doctor_id=use.id
        yy.user_id=user
        yy.prescription=pre
        yy.appointment_id=id      
        yy.save()
        return redirect('doctor')
    return render(request,'doctor/prescription.html')



