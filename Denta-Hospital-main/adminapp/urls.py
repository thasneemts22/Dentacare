

from django.urls import path

from adminapp import views


urlpatterns = [
    path('admin',views.adminindex,name='admin'),
    path('doctorlist',views.doctorlist,name='doctorlist'),
    path('approved_doctor',views.approved_doctor,name='approved_doctor'),
    path('booking',views.booking,name='booking'),
    path('add_service',views.add_service,name='add_service'),

    path('approve/<int:id>',views.approve,name='approve'),
    path('reject/<int:id>',views.reject,name='reject'),
    path('book_approve/<int:id>',views.book_approve,name='book_approve'),
    path('book_reject/<int:id>',views.book_reject,name='book_reject'),
    path('paid_booking',views.paid_booking,name='paid_booking'),
    path('Assign_time/<int:id>',views.Assign_time,name='Assign_time'),


]