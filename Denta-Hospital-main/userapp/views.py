from django.http import HttpResponse
from django.shortcuts import redirect, render

from Dental_app.models import Doctor_reg, user_reg
from adminapp.models import Service
from userapp.models import Appointment, Prescription
from django.contrib import messages

# Create your views here.
def userindex(request):
    return render(request,'user/index.html')

from datetime import datetime

def book_appointment(request):
    doc = Doctor_reg.objects.filter(user__last_name='1')
    if request.method == 'POST':
        doctor = request.POST['doctor']
        date= request.POST['date']
        current_date = datetime.strptime(date, '%Y-%m-%d').date()
        last_generated = Appointment.objects.filter(generated_at=current_date).order_by('-number').first()
        if last_generated:
            last_number = int(last_generated.number[-3:])  # Extract the last 4 digits
            new_number = last_number + 1
            number = f'{new_number:03d}'
        else:
            number = f'001'       
        us= user_reg.objects.get(user_id=request.user.id)
        reg = Appointment()
        reg.user_id = us.id
        reg.doctor_id=doctor
        reg.status = 'added'
        reg.payment = 'notpaid'
        reg.time_status ='notassigned'

        reg.generated_at=current_date
        reg.number=number
        reg.save()
        return redirect('booking_statussss')
    return render(request,'user/appointment.html',{'doc':doc})


def booking_statussss(request):
    use=user_reg.objects.get(user_id=request.user.id)
    boo=Appointment.objects.filter(user_id=use.id)
    return render(request,'user/view_booking.html',{'boo':boo})

from django.views.generic import TemplateView

def paymentview(request,id):
    if request.method == 'POST':
        bo=Appointment.objects.get(id=id)
        bo.payment='paid'
        bo.status='paid'
        bo.save()
        messages.success(request, 'paid')

        return redirect('booking_statussss')
    return render(request,'user/payment.html')

    
def view_service(request):
    ss=Service.objects.all()
    return render(request,'user/view_service.html',{'boo':ss})

    
def view_prescription(request):
    use=user_reg.objects.get(user_id=request.user.id)

    pp=Prescription.objects.filter(user_id=use.id)
    return render(request,'user/view_prescription.html',{'boo':pp})

from django.template.loader import get_template
from xhtml2pdf import pisa
def pdf_receipt(request,id):
    # Retrieve data from your model
    se = Appointment.objects.get(id=id)

    # Specify the path to your template
    template_path = 'user/re.html'

    # Define the context to pass to the template
    context = {'service': Appointment}

    # Create a Django response object and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'

    # Find the template and render it
    template = get_template(template_path)
    html = template.render(context)

    # Create a PDF
    pisa_status = pisa.CreatePDF(
        html, dest=response)

    # If there was an error creating the PDF, display a message
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')

    return response

    

    



    

