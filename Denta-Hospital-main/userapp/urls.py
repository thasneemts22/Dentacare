from django.urls import path
from userapp import views


urlpatterns = [
    path('user',views.userindex,name='user'),
 
    path('book_appointment',views.book_appointment,name='book_appointment'),
    path('booking_statussss',views.booking_statussss,name='booking_statussss'),
    path('paymentview/<int:id>',views.paymentview,name='paymentview'),
    path('view_service',views.view_service,name='view_service'),
    path('view_prescription',views.view_prescription,name='view_prescription'),
    path('pdf_receipt/<int:id>',views.pdf_receipt, name='pdf_receipt'),

]